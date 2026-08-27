# -*- coding: utf-8 -*-
"""
Nova Solar Solutions - static site generator.

Renders the shared chrome (head, header, footer) around per-page content so
every page stays consistent. Output is plain static HTML in this folder.

    python build.py
"""
import os, re, io

SITE = "https://www.novasolarsolutions.com.au"
BRAND = "Nova Solar Solutions"
PHONE_DISPLAY = "1300 668 275"
PHONE_HREF = "1300668275"
EMAIL = "info@novasolarsolutions.com.au"
ADDRESS_LINES = ["Suite 12, 45 Dandenong Road", "Clayton VIC 3168"]
ABN = "12 345 678 901"

# --------------------------------------------------------------------------
# Icons (inline stroke SVG, 24x24)
# --------------------------------------------------------------------------
def _svg(paths, fill=False):
    attrs = ('fill="currentColor" stroke="none"' if fill else
             'fill="none" stroke="currentColor" stroke-width="1.9" '
             'stroke-linecap="round" stroke-linejoin="round"')
    return ('<svg viewBox="0 0 24 24" %s aria-hidden="true" focusable="false">%s</svg>'
            % (attrs, paths))

ICONS = {
 "sun": _svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
 "home": _svg('<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.8V20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9.8"/><path d="M9.5 21v-6h5v6"/>'),
 "building": _svg('<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2"/><path d="M10 21v-3h4v3"/>'),
 "battery": _svg('<rect x="2" y="7" width="16" height="10" rx="2.5"/><path d="M22 10.5v3"/><path d="M10.5 9.5 8 12.5h3.5L9 15.5"/>'),
 "wrench": _svg('<path d="M14.7 6.3a4.5 4.5 0 0 0 5.9 5.9l-8.4 8.4a2.1 2.1 0 0 1-3-3z"/><path d="M14.7 6.3 17.5 3.5"/>'),
 "monitor": _svg('<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8M12 17v4"/><path d="M6.5 12.5 9.5 9l2.5 2.5L16 7"/>'),
 "check": _svg('<circle cx="12" cy="12" r="9.2"/><path d="M8 12.3l2.7 2.7L16 9.6"/>'),
 "arrow": _svg('<path d="M4 12h15"/><path d="M13 6l6 6-6 6"/>'),
 "phone": _svg('<path d="M21 16.9v2.6a2 2 0 0 1-2.2 2 19.6 19.6 0 0 1-8.5-3 19.3 19.3 0 0 1-6-6 19.6 19.6 0 0 1-3-8.6A2 2 0 0 1 3.3 2H6a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L7.1 9.8a16 16 0 0 0 6 6l1.2-1.1a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7A2 2 0 0 1 21 16.9z"/>'),
 "mail": _svg('<rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="m3 6.5 9 6.5 9-6.5"/>'),
 "pin": _svg('<path d="M20 10.4c0 5.4-8 12.1-8 12.1s-8-6.7-8-12.1a8 8 0 1 1 16 0z"/><circle cx="12" cy="10.2" r="2.9"/>'),
 "clock": _svg('<circle cx="12" cy="12" r="9.2"/><path d="M12 6.9V12l3.3 2"/>'),
 "shield": _svg('<path d="M12 22s8-3.4 8-9.4V5.6L12 2.4 4 5.6v7c0 6 8 9.4 8 9.4z"/><path d="M8.7 12.2l2.3 2.3 4.3-4.6"/>'),
 "award": _svg('<circle cx="12" cy="9" r="6"/><path d="M8.5 14.2 7 22l5-2.6L17 22l-1.5-7.8"/>'),
 "star": _svg('<path d="m12 2.6 2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.5 6.1 20.6l1.2-6.5L2.5 9.5l6.6-.9z"/>', fill=True),
 "plus": _svg('<path d="M12 5v14M5 12h14"/>'),
 "zap": _svg('<path d="M13.5 2 4 13.5h6.5L10 22l9.5-11.5H13z"/>'),
 "users": _svg('<circle cx="9" cy="8" r="3.6"/><path d="M2.5 20.5a6.5 6.5 0 0 1 13 0"/><path d="M16.5 4.8a3.6 3.6 0 0 1 0 6.5M18 14.6a6.5 6.5 0 0 1 3.5 5.9"/>'),
 "leaf": _svg('<path d="M4 20c0-9 5-15 16-16 0 11-5.5 16-11 16a5 5 0 0 1-5-5z"/><path d="M9 15c2-3.5 5-6 9-8"/>'),
 "dollar": _svg('<path d="M12 2.5v19"/><path d="M16.5 6.6H9.8a3.1 3.1 0 0 0 0 6.2h4.4a3.1 3.1 0 0 1 0 6.2H7"/>'),
 "doc": _svg('<path d="M14 2.5H6.5a1.5 1.5 0 0 0-1.5 1.5v16a1.5 1.5 0 0 0 1.5 1.5h11a1.5 1.5 0 0 0 1.5-1.5V7.5z"/><path d="M14 2.5v5h5"/><path d="M8.5 13h7M8.5 17h5"/>'),
 "facebook": _svg('<path d="M14.5 8.5V6.8c0-.8.3-1.3 1.4-1.3h1.6V2.6c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.2v1.8H8.5v3h2.6V21h3.4v-9.5h2.6l.4-3z"/>', fill=True),
 "instagram": _svg('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/>'),
 "linkedin": _svg('<path d="M4.8 8.9h3.3V21H4.8zM6.4 2.9a1.9 1.9 0 1 1 0 3.9 1.9 1.9 0 0 1 0-3.9zM10.6 8.9h3.2v1.7c.6-1 1.8-1.9 3.6-1.9 2.8 0 4 1.7 4 4.9V21h-3.3v-6.4c0-1.6-.6-2.5-1.9-2.5-1.1 0-1.9.7-2.2 1.7-.1.3-.1.7-.1 1.1V21h-3.3z"/>', fill=True),
}
def ico(name): return ICONS[name]

# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------
NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("residential-solar.html", "Residential"),
    ("commercial-solar.html", "Commercial"),
    ("contact.html", "Contact"),
]

# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------
def head(page):
    canonical = SITE + "/" + ("" if page["slug"] == "index" else page["slug"] + ".html")
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.className+=" js";</script>
<title>{page['title']}</title>
<meta name="description" content="{page['desc']}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0A2545">
<meta name="robots" content="index,follow">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{page['title']}">
<meta property="og:description" content="{page['desc']}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/logo-mark.png">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Manrope:wght@400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">

<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"LocalBusiness",
  "@id":"{SITE}/#business",
  "name":"{BRAND}",
  "url":"{SITE}",
  "image":"{SITE}/assets/logo-mark.png",
  "logo":"{SITE}/assets/logo.png",
  "telephone":"+61{PHONE_HREF[1:]}",
  "email":"{EMAIL}",
  "priceRange":"$$",
  "address":{{"@type":"PostalAddress","streetAddress":"{ADDRESS_LINES[0]}","addressLocality":"Clayton","addressRegion":"VIC","postalCode":"3168","addressCountry":"AU"}},
  "areaServed":[{{"@type":"State","name":"Victoria"}},{{"@type":"City","name":"Melbourne"}}],
  "openingHoursSpecification":[
    {{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:30"}},
    {{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"14:00"}}
  ]
}}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(page):
    """Homepage-only header. The menu names are shown for design completeness but
    are inert <span>s - there are no other pages to link to yet. When the rest of
    the site goes live, turn these back into <a href> links."""
    links = "".join(
        '<li><span class="nav__link%s"%s>%s</span></li>' % (
            " is-active" if label == "Home" else "",
            ' aria-current="page"' if label == "Home" else ' aria-disabled="true"',
            label)
        for href, label in NAV)
    return f"""<header class="site-header">
  <div class="topbar">
    <div class="wrap topbar__in">
      <ul class="topbar__list">
        <li>{ico('pin')}<span>Servicing Greater Melbourne &amp; regional Victoria</span></li>
        <li>{ico('clock')}<span>Mon&ndash;Fri 8:00am&ndash;5:30pm &middot; Sat 9:00am&ndash;2:00pm</span></li>
      </ul>
      <ul class="topbar__list">
        <li>{ico('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ico('phone')}<a href="tel:{PHONE_HREF}"><strong>{PHONE_DISPLAY}</strong></a></li>
      </ul>
    </div>
  </div>

  <div class="wrap">
    <nav class="nav" aria-label="Main">
      <a class="brand" href="#main" aria-label="{BRAND}">
        <img class="brand__img" src="assets/logo.png" alt="{BRAND}" width="230" height="80">
      </a>

      <ul class="nav__menu nav__menu--inert">{links}</ul>

      <div class="nav__cta">
        <a class="btn btn--ghost" href="tel:{PHONE_HREF}">{ico('phone')}<span>{PHONE_DISPLAY}</span></a>
        <a class="btn btn--primary" href="#quote">Free Quote</a>
        <button class="nav__toggle" type="button" aria-expanded="false" aria-label="Toggle navigation menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>
  </div>
</header>
"""


def footer():
    """Homepage-only footer. Column names are shown but inert - see header()."""
    nav_names = "".join('<li><span class="footer__name">%s</span></li>' % l for h, l in NAV[1:5])
    svc_names = "".join('<li><span class="footer__name">%s</span></li>' % l for l in [
        "Residential Solar", "Commercial Solar", "Battery Storage",
        "Maintenance &amp; Repairs", "Rebates &amp; Incentives"])
    legal_names = "".join('<li><span class="footer__name">%s</span></li>' % l for l in [
        "Privacy Policy", "Terms of Service", "Contact"])
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="brand footer__brand" href="#main" aria-label="{BRAND}">
          <img class="brand__img brand__img--footer" src="assets/logo-light.png" alt="{BRAND}" width="230" height="80">
        </a>
        <p class="footer__about">Victorian solar specialists designing, installing and maintaining rooftop solar and battery systems for homes and businesses across the state.</p>
        <div class="accred">
          <span>CEC Approved Retailer</span><span>SAA Accredited Installers</span><span>Solar Victoria Authorised</span>
        </div>
      </div>

      <div>
        <h4>Explore</h4>
        <ul class="footer__list">{nav_names}</ul>
      </div>

      <div>
        <h4>Services</h4>
        <ul class="footer__list">{svc_names}</ul>
      </div>

      <div>
        <h4>Get in touch</h4>
        <ul class="footer__contact">
          <li>{ico('phone')}<span><b><a href="tel:{PHONE_HREF}">{PHONE_DISPLAY}</a></b>Mon&ndash;Fri 8:00am&ndash;5:30pm</span></li>
          <li>{ico('mail')}<span><b><a href="mailto:{EMAIL}">{EMAIL}</a></b>We reply within one business day</span></li>
          <li>{ico('pin')}<span><b>{ADDRESS_LINES[0]}</b>{ADDRESS_LINES[1]}</span></li>
        </ul>
      </div>
    </div>

    <div class="footer__bar">
      <p>&copy; <span data-year>2026</span> {BRAND}. ABN {ABN}. All rights reserved.</p>
      <ul>{legal_names}</ul>
    </div>
  </div>
</footer>

<a class="btn btn--primary fab" href="tel:{PHONE_HREF}">{ico('phone')}<span>Call now</span></a>

<script src="js/main.js" defer></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# Reusable blocks
# --------------------------------------------------------------------------
def page_hero(h1, intro, crumbs, bg="assets/images/solar-farm.jpg"):
    items = "".join(
        '<li%s>%s</li>' % (
            ' aria-current="page"' if href is None else "",
            label if href is None else '<a href="%s">%s</a>' % (href, label))
        for label, href in crumbs)
    return f"""<section class="phero">
  <div class="phero__bg"><img src="{bg}" alt="" aria-hidden="true"></div>
  <div class="wrap phero__in">
    <ul class="crumb">{items}</ul>
    <h1>{h1}</h1>
    <p>{intro}</p>
  </div>
</section>
"""

def cta_band(title, text, primary=("#quote", "Get my free quote"), secondary=True):
    sec = ('<a class="btn btn--lg btn--outline-light" href="tel:%s">%s<span>%s</span></a>'
           % (PHONE_HREF, ico('phone'), PHONE_DISPLAY)) if secondary else ""
    return f"""<section class="section section--flush-top">
  <div class="wrap">
    <div class="cta-band reveal">
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="btn-row btn-row--center">
        <a class="btn btn--lg btn--primary" href="{primary[0]}">{primary[1]}{ico('arrow')}</a>
        {sec}
      </div>
    </div>
  </div>
</section>
"""

def quote_form(compact=False, form_id="quoteForm"):
    """Lead capture form. compact=True drops the message field."""
    message = "" if compact else """
      <div class="field">
        <label for="%s-msg">Anything else we should know?</label>
        <textarea class="textarea" id="%s-msg" name="message" placeholder="Roof type, current bill, battery interest, timing..."></textarea>
      </div>""" % (form_id, form_id)
    return f"""<form class="quote-form" id="{form_id}" data-validate novalidate>
  <div class="field-row">
    <div class="field">
      <label for="{form_id}-name">Full name <span class="req">*</span></label>
      <input class="input" id="{form_id}-name" name="name" type="text" required placeholder="Jane Whitmore" autocomplete="name">
      <span class="err-text"></span>
    </div>
    <div class="field">
      <label for="{form_id}-phone">Phone <span class="req">*</span></label>
      <input class="input" id="{form_id}-phone" name="phone" type="tel" required placeholder="0412 345 678" autocomplete="tel">
      <span class="err-text"></span>
    </div>
  </div>
  <div class="field-row">
    <div class="field">
      <label for="{form_id}-email">Email <span class="req">*</span></label>
      <input class="input" id="{form_id}-email" name="email" type="email" required placeholder="jane@example.com.au" autocomplete="email">
      <span class="err-text"></span>
    </div>
    <div class="field">
      <label for="{form_id}-post">Postcode <span class="req">*</span></label>
      <input class="input" id="{form_id}-post" name="postcode" type="text" required placeholder="3168" inputmode="numeric" autocomplete="postal-code">
      <span class="err-text"></span>
    </div>
  </div>
  <div class="field">
    <label for="{form_id}-type">What are you after?</label>
    <select class="select" id="{form_id}-type" name="interest">
      <option value="residential">Home solar system</option>
      <option value="battery">Home battery</option>
      <option value="solar-battery">Solar and battery together</option>
      <option value="commercial">Commercial solar</option>
      <option value="service">Service, repair or upgrade</option>
      <option value="unsure">Not sure yet &ndash; need advice</option>
    </select>
  </div>{message}
  <button class="btn btn--primary btn--block btn--lg" type="submit">Request my free quote</button>
  <div class="form-msg" role="status" aria-live="polite"></div>
  <p class="form-note">No obligation and no door-knocking. We use your details only to prepare your quote &ndash; your details are never shared.</p>
</form>"""

def faq(items, heading="Frequently asked questions", intro=None, soft=True):
    rows = []
    for i, (q, a) in enumerate(items):
        rows.append(f"""<div class="acc__item">
      <h3 style="margin:0">
        <button class="acc__btn" type="button" aria-expanded="false" aria-controls="faq-{i}" id="faqb-{i}">
          <span>{q}</span>{ico('plus')}
        </button>
      </h3>
      <div class="acc__panel" id="faq-{i}" role="region" aria-labelledby="faqb-{i}">
        <div class="acc__inner">{a}</div>
      </div>
    </div>""")
    intro_html = f"<p>{intro}</p>" if intro else ""
    schema_items = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (_json(q), _json(re.sub("<[^>]+>", "", a)))
        for q, a in items)
    return f"""<section class="section{' section--soft' if soft else ''}">
  <div class="wrap wrap-narrow">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Good to know</span>
      <h2>{heading}</h2>
      {intro_html}
    </div>
    <div class="acc reveal">{''.join(rows)}</div>
  </div>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{schema_items}]}}
  </script>
</section>
"""

def _json(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").replace("&amp;", "&").replace("&ndash;", "-").replace("&nbsp;", " ").strip() + '"'

# --------------------------------------------------------------------------
# Render
# --------------------------------------------------------------------------
def render(page):
    html = head(page) + header(page) + '<main id="main">\n' + page["body"] + "\n</main>\n" + footer()
    out = page["slug"] + ".html"
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return out, len(html)

def main():
    import pages
    # Homepage only until the client signs off; flip to False to build every page.
    ONLY_HOME = True
    pages_to_build = [p for p in pages.PAGES if p["slug"] == "index"] if ONLY_HOME else pages.PAGES
    built = [render(page) for page in pages_to_build]
    for name, size in built:
        print("  %-26s %6.1f KB" % (name, size / 1024))
    print("\n%d pages built." % len(built))

if __name__ == "__main__":
    main()
