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
  ids of the `#` headings in `about.md`, so renaming a heading means updating its nav entry.
- [`files/CV_Bo_Li.pdf`](files/): the CV served at `/files/CV_Bo_Li.pdf`. Replace the file to update it.
- [`images/`](images/): teaser images for the publication entries.

## Google Scholar citation count

The citation number on the homepage is fetched at page load from the
`google-scholar-stats` branch, which
[`.github/workflows/google_scholar_crawler.yaml`](.github/workflows/google_scholar_crawler.yaml)
refreshes daily via [`scholarly`](https://github.com/scholarly-python-package/scholarly).

The profile id defaults to the one in the workflow; override it with a repository secret named
`GOOGLE_SCHOLAR_ID` (Settings → Secrets and variables → Actions).

Google throttles scraping from shared CI addresses, so runs can fail. That is handled by design:
the workflow fails loudly rather than publishing a wrong number, and `about.md` renders a static
fallback figure so the page never shows a blank. Run the workflow manually from the Actions tab
to check whether it currently succeeds.

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
