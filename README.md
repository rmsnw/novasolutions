# Nova Solar Solutions — Website

Static marketing site for **Nova Solar Solutions**, a Victorian solar &amp; battery installer.
No frameworks, no build dependencies at runtime — plain HTML, CSS and vanilla JS.

Target domain: `https://www.novasolarsolutions.com.au`

---

## Quick start

Open `index.html` in a browser. That's it.

To preview with a local server (recommended, so paths behave exactly as they will live):

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

To deploy: upload the whole folder to any static host (Netlify, Cloudflare Pages,
cPanel, S3). There is no build step required on the server.

---

## Files

```
index.html              Homepage - the only page currently built

css/style.css           Design system: tokens, components, responsive rules
js/main.js              Accordion, scroll reveal, counters, form validation

assets/
  final-logo.png        Original supplied logo (source of truth)
  logo.png              Trimmed, transparent - used in the header
  logo-light.png        Navy recoloured to white - used in the dark footer
  logo-mark.png         Square emblem only - used for og:image / social
  favicon.ico           Multi-size icon (16-256px)
  apple-touch-icon.png  iOS home-screen icon
  images/               Photography (see Licensing below)
    CREDITS.md          Per-image licence + attribution status
    image-credits.json  Machine-readable version

build.py                Static generator: shared head/header/footer + helpers
pages.py                Copy and structure for every page (incl. unbuilt ones)
```

---

## Current status: homepage only

The site is a **single self-contained page** for client sign-off.

The navigation menu and the footer link columns **are visible** — About, Services,
Residential, Commercial, Batteries, Rebates, Contact, Privacy Policy, Terms of
Service — so the client sees the finished structure. But those names are inert
`<span>`s, not links: nothing navigates, because no other page is built yet.

Things that *do* work on the page:

* "Free Quote" / "Get my free quote" / "Price this system" → scroll to the quote
  form (`#quote`)
* "See what we do" → scrolls to the services section (`#services`)
* Phone and email (`tel:` / `mailto:`) throughout
* The mobile burger menu still opens and closes normally

Copy for the other seven pages plus Privacy and Terms is **already written** and
still lives in `pages.py` — it is just not being built.

### Homepage-only layout notes

* The hero is a **full-height banner** — `min-height: calc(100svh - header)`, with
  the two columns stretched to equal height (`.hero__grid { align-items: stretch }`).
  The background image is anchored with `object-position: center top`; adjust that
  one value if a replacement photo crops badly.
* The "four steps" section uses **connected cards** (`.step`) with amber chevrons
  between them. The chevrons are hidden below 960px, where the grid drops to two
  columns.

### Mobile behaviour

Breakpoints: **960px** (nav collapses to a burger, two-column grids stack),
**680px** (single column, tighter section padding, stats go two-up),
**430px** (header shrinks so logo + CTA + burger still fit),
**400px** (stats drop to one column).

Deliberate differences from desktop:

* The hero drops its full-height `min-height` on phones — otherwise the quote
  form is pushed far below the fold with dead space above it.
* `.split--equal` images return to normal flow and render **uncropped**, since
  there is no second column to match height with.
* Footer collapses to two columns with the brand block and contact details
  spanning full width.

Verified at 320px, 360px and 414px with no horizontal overflow.

### Re-enabling the rest of the site after approval

1. In `build.py` → `main()`, set `ONLY_HOME = False`.
2. In `build.py` → `header()`, turn the menu `<span class="nav__link">` back into
   `<a class="nav__link" href="...">` (the original loop used `NAV`), and drop the
   `nav__menu--inert` class from the `<ul>`.
3. In `build.py` → `footer()`, turn `<span class="footer__name">` back into
   `<a href="...">` for the Explore, Services and legal lists.
4. In `css/style.css`, delete the "Homepage-only build" block near the top.
5. In `pages.py`, point the CTAs back at real pages: `href="#quote"` →
   `href="contact.html"`, and re-add the `card__link` "Explore ..." links on the
   three service cards.
6. Run `python build.py`.

---

## Editing the site

There are two ways, and you should pick one and stick to it:

**A. Edit the HTML directly** (simplest). Open `index.html` and change what you
need. If you do this, **do not run `build.py` again** — it will regenerate the
HTML from `pages.py` and overwrite your edits.

**B. Edit the source and regenerate** (better if you'll make ongoing changes,
since header/footer/nav stay consistent across all pages automatically):

```bash
python build.py     # rewrites all .html files
```

Copy lives in `pages.py`. Shared chrome (head tags, header, footer, form,
FAQ, CTA band) lives in `build.py`.

Business details are constants at the top of `build.py` — change them once
and they update everywhere:

```python
PHONE_DISPLAY  = "1300 668 275"
EMAIL          = "info@novasolarsolutions.com.au"
ADDRESS_LINES  = ["Suite 12, 45 Dandenong Road", "Clayton VIC 3168"]
ABN            = "12 345 678 901"
```

---

## ⚠️ Placeholders you must replace before going live

These are invented stand-ins, not real details:

| Item | Current value | Where |
|---|---|---|
| Phone | `1300 668 275` | `build.py` → `PHONE_DISPLAY` / `PHONE_HREF` |
| Email | `info@novasolarsolutions.com.au` | `build.py` → `EMAIL` |
| Address | Suite 12, 45 Dandenong Road, Clayton | `build.py` → `ADDRESS_LINES` |
| ABN | `12 345 678 901` | `build.py` → `ABN` |
| Social links | `href="#"` | `build.py` → `footer()` |
| Stats | 2,400+ installs, 18.6 MW, 4.9 rating, 12 yrs | `pages.py` → `HOME` stats block |
| Testimonials | 3 written examples | `pages.py` → `HOME` |
| Accreditation badges | CEC / SAA / Solar Victoria | `build.py` → `footer()` |

**Do not publish the statistics, testimonials or accreditation claims until they
are true.** Claiming CEC Approved Retailer status or a review average you don't
hold is a compliance problem under Australian Consumer Law, not just a copy issue.

---

## The enquiry form

`js/main.js` validates name, Australian phone, email and Victorian postcode
client-side, then **simulates** a successful send. There is no backend.
(The form's fine-print no longer links to a Privacy Policy page, since that page
is not built yet - restore the link when it is.)

To make it actually deliver, replace the `setTimeout` block in `initForms()`
(marked with a comment) with a real POST — e.g. Formspree, Netlify Forms, or
your own endpoint. Server-side validation is still required; the client-side
rules are a convenience, not a security control.

---

## Licensing

**Logo** — supplied by you (`assets/final-logo.png`). The derived versions
(`logo.png`, `logo-light.png`, `logo-mark.png`, `favicon.ico`,
`apple-touch-icon.png`) were produced from it by background removal, trimming
and recolouring.

**Fonts** — **Bricolage Grotesque** for headings and **Manrope** for body text,
served from Google Fonts, with `"Helvetica Neue", Arial, sans-serif` as the
fallback stack. Both are SIL Open Font License, free for commercial use. They are
set once as `--font-display` and `--font-text` at the top of `css/style.css`.

**Photography** — placeholder images sourced from Wikimedia Commons and Openverse,
filtered to licences that permit commercial use. Full record in
`assets/images/CREDITS.md` (and `image-credits.json`).

> ### ⚠️ Read this before you publish
>
> The photography is **not launch-ready**, for two reasons:
>
> 1. **Four images are CC BY-SA 4.0** (`hero-home`, `commercial-solar`, `inverter`,
>    `solar-farm`). These are free to use commercially, but only if you credit the
>    author and link the licence.
> 2. **Three images could not be traced** back to a source file
>    (`family-home`, `house-modern`, `residential-roof`). Do not publish these until
>    the source is confirmed or the image is swapped out.
>
> Only `installer-team`, `engineer-inspect`, `battery-storage` and `panel-closeup`
> are unconditionally clear (public domain / CC0).

**The fix is the same in both cases: use your own photos.** Shots of your real
installations, crew and vans remove every attribution obligation and will convert
better than any stock image for a local trades business. Drop replacements into
`assets/images/` using the same filenames and nothing else needs to change.

Images are currently sized for their on-page use (1100–1600px wide, progressive
JPEG). Keep replacements around the same dimensions so the page stays light.

## Browser support

Modern evergreen browsers (Chrome, Edge, Firefox, Safari). Uses CSS custom
properties, `clamp()`, grid, `aspect-ratio` and `IntersectionObserver` — all
widely supported. Graceful fallbacks: scroll-reveal and counters render in
their final state if `IntersectionObserver` is unavailable, and
`prefers-reduced-motion` disables animation entirely.

## Accessibility

Skip link, landmark elements, labelled form fields with inline error text,
`aria-expanded` on the nav toggle and accordion, `aria-current` on the active
nav item, visible focus rings, and alt text on content images (decorative
background images are `aria-hidden`). Worth re-testing with a screen reader
after you swap in real content.

## SEO

Per-page `<title>`, meta description, canonical URL, Open Graph and Twitter
card tags. `LocalBusiness` structured data in the head of every page, plus
`FAQPage` structured data on the pages with accordions. Update the
`LocalBusiness` block in `build.py` once the real address, phone and ABN are in.

Not included: `sitemap.xml` and `robots.txt` — add them once the domain is live.
