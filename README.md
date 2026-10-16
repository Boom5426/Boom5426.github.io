# 李波 Bo Li: [Academic Homepage](https://boom5426.github.io/)

Source for <https://boom5426.github.io>. Built with Jekyll and served by GitHub Pages.

## Editing

The site has an English page and a Chinese page that share their data-heavy sections:

| File | What it controls |
| :--- | :--- |
| [`_pages/about.md`](_pages/about.md) | English page (`/`): hero, research, education, honors, patents, service |
| [`_pages/zh.md`](_pages/zh.md) | Chinese page (`/zh/`): the same sections, translated |
| [`_data/news.yml`](_data/news.yml) | News for both pages: one entry per item with `en` and `zh` text; `earlier: true` folds it |
| [`_includes/publications.md`](_includes/publications.md) | Selected publications for both pages (Chinese labels and summaries via `lang="zh"`) |
| [`_includes/software.md`](_includes/software.md) | Software table for both pages |
| [`_data/bibtex.yml`](_data/bibtex.yml) | BibTeX behind each paper's copy button, keyed by the button's `data-key` |
| [`_config.yml`](_config.yml) | Site title, SEO description, sidebar profile (`bio`/`bio_zh`, `location`/`location_zh`), social links |

Other things worth knowing:

- [`_data/navigation.yml`](_data/navigation.yml): the top nav (`main` for English, `main_zh` for Chinese).
  Section headings set their anchor explicitly, e.g. `## ...News {#news}`, so renaming a heading
  does not break the nav. Each page keeps one `<h1>`, the visually hidden name at the top.
- Icons are inline SVG: `{% include icon.html name="envelope" %}` reads
  [`_data/icons.yml`](_data/icons.yml) (Font Awesome Free 5 paths). No icon font is loaded; to add an
  icon, copy its `viewBox` and path from the Font Awesome SVG named in that file's header.
- [`assets/js/site.js`](assets/js/site.js): all page behaviour, no jQuery (overflow nav menu, image
  lightbox, new-tab external links, collapsible author lists on phones, BibTeX copy).
- [`files/CV_Bo_Li.pdf`](files/): the CV served at `/files/CV_Bo_Li.pdf`. Replace the file to update it.
- [`images/`](images/): teaser images for the publication entries.
- [`assets/css/homepage.css`](assets/css/homepage.css): hero, publication cards, icons, lightbox,
  and their dark and mobile styles. Loaded after `main.css`, so it overrides it.

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
The homepage no longer displays these numbers; the citation count and h-index are kept in a committed snapshot,
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

The page follows the reader's system setting through `@media (prefers-color-scheme: dark)` blocks at
the end of [`assets/css/main.scss`](assets/css/main.scss) and
[`assets/css/homepage.css`](assets/css/homepage.css). They only override colors. Any new component
needs its dark colors added there; the institution logo strip, for example, keeps a light
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
