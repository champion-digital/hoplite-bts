# hoplite-bts

Live prototype of the redesigned **Behind the Shield**, Hoplite's weekly freight brief.

**Live:** https://champion-digital.github.io/hoplite-bts/

This is a design prototype for review, not the production site. It is a plain static site (HTML, CSS, a few lines of JavaScript) served by GitHub Pages from the `main` branch.

## Pages

| Page | File | What it shows |
|---|---|---|
| Home | `index.html` | Logo, latest edition (Week 48), three recent editions |
| All editions | `editions.html` | All 30 editions, grouped by month |
| Edition | `edition.html` | A full edition, using Week 47 as the sample |

The layout follows the Figma designs at 1440 (desktop) and 390 (phone) and scales between them.

## What is not real yet

- **Every edition link opens the Week 47 sample.** Only that edition is built.
- **The sign-up form is not connected.** It shows a note and sends nothing.
- **Week 48 borrows a photo.** Each edition will need its own.
- Search engines are asked not to index the site (`noindex`, `robots.txt`).

## Editing

The three `.html` files are generated. Change the content or markup in `build.py`, then run:

```bash
python3 build.py
```

Styles are in `assets/css/styles.css`, the menu and form script in `assets/js/site.js`, images and logos in `assets/img/`. Commit and push to `main`; GitHub Pages updates in about a minute.

To look at it locally:

```bash
python3 -m http.server 4173
```

Then open http://localhost:4173.
