# Pocket Home

Landing page for **Pocket Home** — a design + build studio in Chennai working on compact plots.
A single static page: no build step, no framework, no dependencies.

## Viewing it

Open `index.html` in any browser. That's it.

To serve it locally instead:

```bash
python -m http.server 8000
```

Then visit <http://localhost:8000>.

## What's here

```
index.html          the whole page — markup, inlined CSS, and ~120 lines of vanilla JS
img/                35 optimised JPEGs (project covers + full renders + hero)
tools/inline.py     bundles index.html + img/ into one self-contained file
```

Images come in two forms, following the studio's own convention:

- `*-c.jpg` — a clean 4:5 **cover** crop used in the project grid
- `*-f.jpg` — the **full** render, shown in the lightbox

## A single-file build

For emailing the page or opening it with no folder alongside it:

```bash
python tools/inline.py
```

This writes `pocket-home-standalone.html` (~10 MB) with every image embedded as a
data URI. Google Fonts is the only remaining network request; without it the page
falls back to system fonts.

## Design

| | |
|---|---|
| Background | white, with `#F6F6F7` alternating panels |
| Text | near-black `#0A0A0B` |
| Accent | raspberry `#C42056` |
| Type | Inter, with Instrument Serif italic for pull-words |
| Logo | Apple system stack (SF Pro on Apple devices, Inter elsewhere) |

Colours and type are CSS custom properties defined in one `:root` block near the top
of the `<style>` element, so re-theming is a handful of edits.

## Sections

Hero → About → How we think → Why now (Chennai) → The method → How we're different →
Selected works (15 projects) → Book a consultation → Footer

Interactions, all vanilla JS:

- scroll reveal via `IntersectionObserver`
- project lightbox — click a card; arrow keys or dots to move between images, `Esc` to close
- booking form — plot-size and stage chips, submitting opens WhatsApp pre-filled

## Before this goes live

- [x] ~~Replace the placeholder WhatsApp number.~~ Enquiries now go to **+91 96001 56838**
      (`https://wa.me/919600156838` in `index.html`).
- [ ] Point the Instagram link at the actual profile (currently `instagram.com`).
- [ ] Confirm every plot area and BHK count in the project grid.
