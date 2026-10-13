#!/usr/bin/env python3
"""Refresh the static Google Scholar counts shown in the homepage hero.

Run this from your own machine: Google Scholar blocks requests from GitHub
Actions runners, so the counts cannot be refreshed in CI.
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

PROFILE_ID = 'y1myk_IAAAAJ'


def main():
    path = Path(__file__).resolve().parents[1] / '_data' / 'scholar_stats.json'
    profile = 'https://scholar.google.com/citations?user=' + PROFILE_ID + '&hl=en'
    request = Request(profile, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/140.0 Safari/537.36',
        'Accept-Language': 'en',
    })

    # Write only after the page parses cleanly; failures preserve the last good snapshot.
    try:
        with urlopen(request, timeout=20) as response:
            html = response.read().decode('utf-8', 'replace')
        # The stats table lists Citations, h-index, i10-index; each row is (All, Since 20xx).
        cells = [int(n) for n in re.findall(r'class="gsc_rsb_std">(\d+)<', html)]
        if len(cells) != 6:
            raise ValueError('expected 6 stats cells, found %d (blocked or layout changed)' % len(cells))
    except Exception as exc:
        raise SystemExit('Scholar refresh failed; existing snapshot preserved: ' + str(exc))
    updated = {
        'updated_at': datetime.now(timezone.utc).date().isoformat(),
        'profile_url': profile,
        'citations': cells[0],
        'h_index': cells[2],
        'i10_index': cells[4],
    }
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(updated, indent=2) + '\n')
    temporary.replace(path)
    print('Google Scholar: %d citations, h-index %d, i10-index %d.'
          % (updated['citations'], updated['h_index'], updated['i10_index']))


if __name__ == '__main__':
    main()
