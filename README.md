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
The hero shows the total citation count and h-index from a committed snapshot,
[`_data/scholar_stats.json`](_data/scholar_stats.json), with a link to the profile. Google Scholar
blocks requests from GitHub Actions runners, so refresh it from your own machine before publishing:

```bash
python3 scripts/refresh_scholar_stats.py
```

A failed or blocked request leaves the previous snapshot intact. `bash scripts/build_site.sh`
runs this refresh too. The profile id is set at the top of the script.

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
