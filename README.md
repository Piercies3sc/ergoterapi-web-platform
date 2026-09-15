# Occupational Therapy Web Platform

A bilingual multi-page website for presenting occupational therapy fields, exercises, certificates, and related media content. The Turkish and English pages share a responsive layout and client-side interactions.

[View the site](https://hazalpural.netlify.app/)

## Features

- Turkish and English versions of nine pages
- Responsive desktop and mobile navigation
- Client-side search for therapy-area cards on the home page
- FAQ accordion, scroll-to-top control, and highlighted content cards
- Image certificate modal and local video playback modal
- Lazy loading on page images
- Shared CSS, JavaScript, and Tailwind theme configuration
- Direct email, social profile, and WhatsApp contact links

## Structure

```text
.
├── index.html and topic pages     # Turkish content
├── en/                            # English page versions
├── assets/css/style.css           # Shared styles
├── assets/js/main.js              # Shared interactions
├── assets/js/tailwind-config.js   # Shared Tailwind theme values
├── assets/images/certs/           # Certificate images
├── *.jpg, *.png, *.mp4            # Page images and local videos
└── *.py                           # Small maintenance scripts
```

`update_html.py` keeps repeated navigation, footer, modal, and script sections consistent across the Turkish and English pages. `prepare_en.py` was used to create an initial English page set and adjust relative asset paths. `prepare_redesign.py` is a small inspection helper that extracts selected content from the Turkish topic pages.

These scripts edit or inspect the static HTML files; there is no server-side application or automated build pipeline.

## Tech Stack

| Area | Technology |
| --- | --- |
| Pages and styling | HTML, CSS, Tailwind CSS (CDN) |
| Interactions | Vanilla JavaScript |
| Maintenance scripts | Python 3 standard library |
| Icons and fonts | Font Awesome, Google Fonts |
| Hosting | Netlify |

## Run Locally

No package installation or build step is required. Start a local static server from the repository root:

```bash
python3 -m http.server 8080
```

Open <http://localhost:8080>. The English home page is available at <http://localhost:8080/en/>.

## What I Practiced

- Organizing a bilingual static website across multiple pages
- Reusing styles and interface behavior across related pages
- Implementing search, modals, accordions, and responsive navigation with JavaScript
- Managing relative links and media paths in nested language folders
- Using small Python scripts to reduce repetitive HTML updates

## Current Limitations

- Shared page sections are stored in generated HTML as well as in the maintenance script, so updates must be applied carefully.
- Tailwind CSS, Font Awesome, and Google Fonts are loaded from third-party CDNs.
- The site has no automated HTML validation or link-checking workflow.
- Contact details and certificate images included in the pages are public repository content.
