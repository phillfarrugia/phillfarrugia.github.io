# phillfarrugia.com

The main pages (`index.html`, `about.html`, `photography.html`) are plain HTML. The blog at `/blog` is built by Jekyll, which GitHub Pages runs automatically on every push.

## Writing a post

1. Create `_posts/YYYY-MM-DD-my-post-title.md`. The part after the date becomes the URL: `/blog/my-post-title/`.
2. Add front matter at the top, then write in Markdown:

   ```yaml
   ---
   title: My post title
   description: One sentence for the blog list, link previews and RSS.
   image: /images/blog/cover.jpg   # optional, used for link previews
   ---
   ```

3. Commit and push to `master`. GitHub Pages rebuilds the site in a minute or two.

**Tips**

- **Excerpt:** with no `description`, the blog list shows the text above `<!--more-->`.
- **Images:** put them in `images/blog/` and use `![Alt text](/images/blog/file.jpg)`. An italic line directly after an image becomes its caption.
- **Code:** use fenced blocks with a language, e.g. ```` ```swift ````.
- **Drafts:** keep unfinished posts in `_drafts/` (no date in the filename). They aren't published.
- **RSS:** generated at `/blog/feed.xml`.

## Previewing locally (optional)

```sh
bundle install
bundle exec jekyll serve --drafts
```

Then open http://localhost:4000. The `Gemfile` uses the `github-pages` gem, so what you see matches what gets published.
