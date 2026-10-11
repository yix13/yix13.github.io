# Yonggang Li — academic homepage

English academic website for https://yix13.github.io, based on al-folio v0.14.6.

## Edit content

- `_pages/about.md`: biography, research themes, and contact.
- `_pages/research.md`: project summaries. No publication claims or non-public paper links are added.
- `_pages/cv.md`: short web CV.
- `assets/img/portrait.jpg`: original supplied photograph, shown in a compact frame with CSS.
- `_sass/_personal.scss`: colors, spacing, and portrait dimensions (220 × 248 px desktop, 140 × 158 px mobile).

## Local preview

With Ruby 3.4 and Bundler installed:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open http://127.0.0.1:4000. For production checks:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
```

## GitHub Pages

The workflow builds and checks pull requests without publishing them. After merging,
it deploys the production site using GitHub Pages Actions. In the repository's
Settings → Pages → Build and deployment, select **GitHub Actions** as the source.

The existing master branch and Git history preserve the former site.

## Editorial notes

The CV is the source of truth for dates and experience. The website omits unconfirmed
publication venues/statuses, does not invent a Scholar account, and introduces
unpublished work as research projects. The personal CV PDF is not published or offered for download.
See `THIRD_PARTY.md` for theme attribution.
