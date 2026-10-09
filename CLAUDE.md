# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

GitHub Pages builds with Ruby 3.3. The `github-pages` gem does not support Ruby 4, and macOS's system Ruby (2.6) is too old, so use Homebrew's `ruby@3.3`:

```bash
export PATH=/opt/homebrew/opt/ruby@3.3/bin:$PATH
bundle install                          # gems install to vendor/bundle
bundle exec jekyll serve --drafts       # http://localhost:4000, includes _drafts/
```

Restart `jekyll serve` after editing `_config.yml`, because it isn't reloaded automatically.

## Architecture Overview

GitHub Pages runs Jekyll on every push to `master` (custom domain via `CNAME`).

**Hand-written pages**: `index.html` (Work), `about.html` and `photography.html` have no front matter, so Jekyll copies them through untouched. Each one is self-contained with inline CSS and JS. Shared styles such as fonts, colours, nav and view transitions are duplicated in each page and in `_layouts/base.html`, so update all four when you change shared UI. The nav links also need updating in all four places (the blog's nav is `_includes/nav.html`).

**Blog** (`/blog`):
- `_posts/YYYY-MM-DD-slug.md` - Published at `/blog/slug/` and use the `post` layout by default
- `_drafts/` - Unpublished posts (shown locally with `--drafts`)
- `blog/index.html` - Post list
- `_layouts/base.html` - Blog page shell and all blog CSS
- `_layouts/post.html` - Single post template
- `_includes/` - Shared blog partials such as the nav and reading time
- RSS is generated at `/blog/feed.xml` by `jekyll-feed`
- `README.md` has the post-writing guide

**Assets**: `images/` (thumbnails, favicon, about photo), `images/photos/` (full-size photos opened in the lightbox via `data-full`), `images/photos/thumbs/` (grid thumbnails) and `fonts/` (self-hosted Baskervville; EB Garamond comes from Google Fonts).

**Photo EXIF**: each grid `<img>` in `photography.html` carries `data-camera`, `data-lens`, `data-exposure`, `data-aperture` and `data-iso`, which the photo viewer shows. Generate these with `python3 scripts/update-photo-exif.py` (needs `exiftool`) instead of writing them by hand. See README "Adding a photo".

**UI convention**: images scale up slightly on hover with `transition: transform 0.3s ease`, matching the Work page icons (`1.08` at 50px). Scale larger images by less so the growth stays subtle: `1.03` for the photo grid and `1.015` for full-width images.
