#!/usr/bin/env python3
"""Refresh the static star counts before a site build, without browser API calls."""

import json
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


def main():
    path = Path(__file__).resolve().parents[1] / '_data' / 'github_stars.json'
    previous = json.loads(path.read_text())
    headers = {
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'Bo-Li-homepage-stats',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token

    def fetch(repo):
        request = Request('https://api.github.com/repos/' + repo, headers=headers)
        with urlopen(request, timeout=20) as response:
            data = json.load(response)
        stars = data.get('stargazers_count')
        if not isinstance(stars, int) or stars < 0:
            raise ValueError('Missing valid star count for ' + repo)
        return repo, {'stars': stars, 'url': data['html_url']}

    # Write only after every request succeeds; failures preserve the last good cache.
    try:
        with ThreadPoolExecutor(max_workers=4) as pool:
            repositories = dict(pool.map(fetch, previous['repositories']))
    except Exception as exc:
        raise SystemExit('Star refresh failed; existing cache preserved: ' + str(exc))
    updated = {
        'updated_at': datetime.now(timezone.utc).date().isoformat(),
        'repositories': repositories,
    }
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(updated, indent=2) + '\n')
    temporary.replace(path)
    print('Refreshed star counts for', len(repositories), 'repositories.')


if __name__ == '__main__':
    main()
