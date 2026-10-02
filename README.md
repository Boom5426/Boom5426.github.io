# 李波 Bo Li: [Academic Homepage](https://boom5426.github.io/)

Source for <https://boom5426.github.io>. Built with Jekyll and served by GitHub Pages.

## Editing

Almost everything lives in two files:

| File | What it controls |
| :--- | :--- |
| [`_pages/about.md`](_pages/about.md) | The entire page: bio, news, publications, open source, education, experience, honors, patents, service, skills |
| [`_config.yml`](_config.yml) | Site title, tagline, SEO description, sidebar profile, social links |

Other things worth knowing:

- [`_data/navigation.yml`](_data/navigation.yml): the top nav. Anchors are the kramdown-generated
  ids of the `##` section headings in `about.md`, so renaming a heading means updating its nav entry.
  The page keeps one `<h1>`, the visually hidden name at the top, so sections are `##`.
- [`files/CV_Bo_Li.pdf`](files/): the CV served at `/files/CV_Bo_Li.pdf`. Replace the file to update it.
- [`images/`](images/): teaser images for the publication entries.
- [`assets/css/homepage.css`](assets/css/homepage.css): compact hero, evidence strip,
  publication cards, and their dark/mobile styles. Full author lists remain visible.

## GitHub star counts

The Software table renders plain text from [`_data/github_stars.json`](_data/github_stars.json).
It shows the snapshot date and links each count to GitHub for the live number. Visitors do not
load badge images or make GitHub API requests. The page no longer loads the visitor globe.

Refresh the snapshot before publishing (Python 3 standard library only):

```bash
python3 scripts/refresh_github_stars.py
```

An optional `GITHUB_TOKEN` increases the API rate limit. A failed request leaves the entire
previous snapshot intact. Commit the refreshed JSON with the website changes: the standard
GitHub Pages build uses this committed snapshot rather than running the refresh script.
For local builds, `bash scripts/build_site.sh` refreshes the counts and runs Jekyll, falling back
to the previous snapshot if the network is unavailable.

## Google Scholar citation count

The homepage shows the live total next to the "Selected Publications" intro. The number comes from
`gs_data.json` on the `google-scholar-stats` branch, which
[`.github/workflows/google_scholar_crawler.yaml`](.github/workflows/google_scholar_crawler.yaml)
refreshes daily via [`scholarly`](https://github.com/scholarly-python-package/scholarly).

The profile id defaults to the one in the workflow; override it with a repository secret named
`GOOGLE_SCHOLAR_ID` (Settings > Secrets and variables > Actions).

The branch does not exist until the workflow has succeeded once. Run it manually from the Actions
tab to create it. Until then the page simply hides the citation clause: `#gs-cit-wrap` starts with
the `hidden` attribute and `_includes/fetch_google_scholar_stats.html` only unhides it after a
successful fetch. Google throttles scraping from shared CI addresses, so runs can fail; the
workflow fails loudly rather than publishing a wrong number.

## Images

The VCDesign, PertResolve, and DrugDis cards use 800 px WebP thumbnails in
`images/publications/`; clicking a figure opens its full-size source. All six cards keep the
figure's aspect ratio within a consistent frame and declare intrinsic image dimensions.

Teaser images are served at 800 px wide, which is twice the 400 px the layout uses, as WebP with a
PNG fallback:

```html
<picture><source srcset="/images/X.webp" type="image/webp"><img src="/images/X.png" width="800" height="..."></picture>
```

Institution logos are 120 px tall, twice their 60 px display height. Keep the `width` and `height`
attributes in sync with the files: the browser uses them to reserve space before the image loads.
To add a new teaser, resize to 800 px wide, flatten onto white (a transparent background disappears
in dark mode), and export both formats.

## Dark mode

The page follows the reader's system setting through a single `@media (prefers-color-scheme: dark)`
block at the end of [`assets/css/main.scss`](assets/css/main.scss). It only overrides colors. Any new
component needs its dark colors added there; the institution logo strip, for example, keeps a light
card behind it because the logos are drawn for a white page.

## Local preview

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

Requires Ruby with development headers (`ruby-dev` / `ruby-devel`); the `github-pages` gem needs
them to build native extensions.

## Credits

Template adapted from
<a href="https://github.com/RayeRen/acad-homepage.github.io" target="_blank" rel="noopener">Yi Ren</a>.
