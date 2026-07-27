"""Fetch Google Scholar profile stats and write them to ./results.

Run by .github/workflows/google_scholar_crawler.yaml. The output is force-pushed
to the `google-scholar-stats` branch and read by the homepage at load time.

Google throttles scraping from shared CI addresses, so this can fail. It is
meant to fail loudly: a stale branch is better than a silently wrong number,
and the homepage already renders a static fallback when the fetch does not
return.
"""

import json
import os
import sys
from datetime import datetime, timezone

from scholarly import scholarly

RESULTS_DIR = "results"

scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
if not scholar_id:
    sys.exit("GOOGLE_SCHOLAR_ID is not set; refusing to guess a profile.")

author = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])

author["updated"] = datetime.now(timezone.utc).isoformat()
author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}

print(f"{author['name']}: {author['citedby']} citations, h-index {author.get('hindex')}")

os.makedirs(RESULTS_DIR, exist_ok=True)

with open(os.path.join(RESULTS_DIR, "gs_data.json"), "w", encoding="utf-8") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open(os.path.join(RESULTS_DIR, "gs_data_shieldsio.json"), "w", encoding="utf-8") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
