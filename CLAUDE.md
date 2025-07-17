# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development
```bash
# Install dependencies
bundle install

# Run development server (accessible at http://localhost:4000)
jekyll serve

# Build the site for production
jekyll build
```

## Architecture Overview

This is a Jekyll-based personal portfolio website using the Duet theme. Jekyll is a static site generator that converts markdown and templates into a complete website.

### Key Concepts

**Collections** - Jekyll collections are used to organize content:
- `_projects/` - Portfolio projects with front matter containing title, subtitle, date, and featured_image
- `_posts/` - Blog posts following Jekyll's naming convention (YYYY-MM-DD-title.md)
- `_pages/` - Static pages like About and Contact

**Layouts & Includes** - Templates that define page structure:
- `_layouts/` - Page templates (default, project, post, page)
- `_includes/` - Reusable components (header, footer, contact-form, socials)

**Data Files** - Configuration separated from code:
- `_data/settings.yml` - Theme customization, navigation, colors, typography
- `_config.yml` - Jekyll configuration and build settings

**Styling** - Sass-based architecture:
- `_sass/` - Modular stylesheets with component-specific styles in `_includes/`
- `css/style.scss` - Main entry point that imports all Sass partials

### Development Workflow

1. **Adding Projects**: Create markdown files in `_projects/` with required front matter (title, subtitle, date, featured_image)
2. **Blog Posts**: Add to `_posts/` following Jekyll naming convention
3. **Styling Changes**: Edit Sass files in `_sass/`, changes compile automatically
4. **Theme Settings**: Modify `_data/settings.yml` for colors, fonts, navigation
5. **Contact Form**: Uses Formspree service, configured in settings.yml

### Important Features

- **Ajax Loading**: Enabled by default for smooth page transitions (can be disabled in settings.yml)
- **Responsive Grid**: Configurable spacing and overlay opacity for portfolio items
- **Custom Domain**: Configured via CNAME file for GitHub Pages deployment
- **Syntax Highlighting**: Uses Rouge highlighter for code blocks