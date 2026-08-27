# -*- coding: utf-8 -*-
"""Page content for the Nova Solar Solutions site."""
from build import (ico, page_hero, cta_band, quote_form, faq,
                   PHONE_DISPLAY, PHONE_HREF, EMAIL, ADDRESS_LINES, BRAND)

IMG = "assets/images/"

# ==========================================================================
# HOME
# ==========================================================================
HOME = """
<section class="hero">
  <div class="hero__bg"><img src="%(img)shero-home.jpg" alt="" aria-hidden="true" fetchpriority="high"></div>
  <div class="wrap hero__in">
    <div class="hero__grid">
      <div class="hero__copy">
        <span class="eyebrow">Solar &amp; battery specialists &middot; Victoria</span>
        <h1>Turn your roof into the cheapest power station <em>you'll ever own</em></h1>
        <ul class="hero__badges">
          <li>%(check)s Accredited installers, never subcontracted blind</li>
          <li>%(check)s Rebate paperwork handled for you</li>
          <li>%(check)s Real people answering the phone after handover</li>
        </ul>
        <div class="btn-row">
          <a class="btn btn--lg btn--primary" href="#quote">Get my free quote %(arrow)s</a>
          <a class="btn btn--lg btn--outline-light" href="#services">See what we do</a>
        </div>
      </div>

      <div class="quote-card reveal" id="quote">
        <h3>Find out what your roof is worth</h3>
        <p class="quote-card__note">A short form, then a proper conversation. No pushy sales scripts.</p>
        %(form)s
      </div>
    </div>
  </div>
</section>

<section class="trust">
  <div class="wrap">
    <div class="trust__grid">
      <div class="trust__item"><div class="trust__ico">%(shield)s</div><div><div class="trust__t">Clean Energy Council approved</div><div class="trust__s">Retailer signatory &amp; accredited installers</div></div></div>
      <div class="trust__item"><div class="trust__ico">%(dollar)s</div><div><div class="trust__t">Rebates applied upfront</div><div class="trust__s">We do the forms, you pay the discounted price</div></div></div>
      <div class="trust__item"><div class="trust__ico">%(award)s</div><div><div class="trust__t">Workmanship warranty</div><div class="trust__s">10 years on installation and mounting</div></div></div>
      <div class="trust__item"><div class="trust__ico">%(users)s</div><div><div class="trust__t">Local Victorian team</div><div class="trust__s">Melbourne based, servicing the whole state</div></div></div>
    </div>
  </div>
</section>

<section class="section" id="services">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">What we do</span>
      <h2>Three ways we lower your energy bill</h2>
      <p>Every property is different. We start with your bill and your roof, then recommend the smallest system that does the job properly &mdash; not the biggest one we can sell you.</p>
    </div>

    <div class="grid g-3">
      <article class="scard reveal">
        <div class="scard__img"><img src="%(img)sresidential-roof.jpg" alt="Rooftop solar panels installed on a home" loading="lazy"></div>
        <div class="scard__body">
          <h3>Residential solar</h3>
          <p>Rooftop systems from 6.6kW upwards, engineered around your daily usage pattern, roof pitch and shading &mdash; so you actually use what you generate.</p>
          <ul class="ticks" style="margin-bottom:18px">
            <li>%(check)s Tier&nbsp;1 panels with 25&ndash;30 year performance warranties</li>
            <li>%(check)s Single and three-phase inverter options</li>
            <li>%(check)s Solar Victoria rebate handled end to end</li>
          </ul>
        </div>
      </article>

      <article class="scard reveal" data-delay="90">
        <div class="scard__img"><img src="%(img)sbattery-storage.jpg" alt="Home battery storage unit" loading="lazy"></div>
        <div class="scard__body">
          <h3>Battery storage</h3>
          <p>Store the sunshine you generate during the day and spend it at night, when grid power costs the most. Blackout backup available on supported models.</p>
          <ul class="ticks" style="margin-bottom:18px">
            <li>%(check)s Federal battery discount applied at quote stage</li>
            <li>%(check)s Sized to your evening load, not a sales target</li>
            <li>%(check)s Retrofit to most existing solar systems</li>
          </ul>
        </div>
      </article>

      <article class="scard reveal" data-delay="180">
        <div class="scard__img"><img src="%(img)scommercial-solar.jpg" alt="Commercial solar installation on a business rooftop" loading="lazy"></div>
        <div class="scard__body">
          <h3>Commercial solar</h3>
          <p>From 20kW warehouse arrays to 100kW+ installations. We model your load profile against generation so the payback case is honest before you commit.</p>
          <ul class="ticks" style="margin-bottom:18px">
            <li>%(check)s Written payback and cash-flow modelling</li>
            <li>%(check)s Weekend and after-hours installation</li>
            <li>%(check)s Grid application and metering managed</li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="split split--equal">
      <div class="split__media reveal">
        <div class="media"><img src="%(img)sinstaller-team.jpg" alt="Nova Solar installers fitting panels to a roof" loading="lazy">
          <div class="media-badge"><div><div class="media-badge__n">10&nbsp;yr</div><div class="media-badge__l">Workmanship<br>warranty</div></div></div>
        </div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Why Nova</span>
        <h2>The quote you get is the job we do</h2>
        <p class="lead">Solar has a reputation problem in Victoria, and most of it comes down to three things: systems sold too big, installs rushed by crews who never come back, and rebate promises that quietly evaporate.</p>
        <p>We built Nova around fixing those three things. Your quote lists the exact panel and inverter model, the exact rebate figures you qualify for, and the name of the accredited installer who will be on your roof.</p>
        <ul class="ticks mt-3">
          <li>%(check)s <strong>No phantom discounts.</strong> We show the full price, then the rebate deducted &mdash; not an inflated price with a "special offer" applied.</li>
          <li>%(check)s <strong>Site assessed before you sign.</strong> We check switchboard capacity, roof condition and shading first, so there are no variation invoices later.</li>
          <li>%(check)s <strong>One team, start to finish.</strong> Design, install, grid paperwork and aftercare all sit with us.</li>
          <li>%(check)s <strong>Monitoring set up on handover day.</strong> You leave knowing how to read your own generation data.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">By the numbers</span>
      <h2>Built on completed installs, not promises</h2>
    </div>
    <div class="stats reveal">
      <div class="stat"><div class="stat__n"><span data-count="2400" data-suffix="+">0</span></div><div class="stat__l">Systems installed across Victoria</div></div>
      <div class="stat"><div class="stat__n"><span data-count="18.6" data-decimals="1" data-suffix=" MW">0</span></div><div class="stat__l">Total capacity commissioned</div></div>
      <div class="stat"><div class="stat__n"><span data-count="4.9" data-decimals="1">0</span></div><div class="stat__l">Average customer rating</div></div>
      <div class="stat"><div class="stat__n"><span data-count="12" data-suffix=" yrs">0</span></div><div class="stat__l">Operating in the Victorian market</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">How it works</span>
      <h2>From first call to first export &mdash; four steps</h2>
      <p>Most residential jobs run about three to five weeks end to end, with the install itself taking a single day.</p>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="step__n">1</div><h4>Bill review &amp; roof check</h4><p>Send us a recent bill. We pull satellite imagery of your roof, model shading across the year and size a system to your actual usage.</p></div>
      <div class="step"><div class="step__n">2</div><h4>Fixed written quote</h4><p>You get named equipment, generation estimates, every rebate you qualify for and a fixed price. Ask us anything before you sign.</p></div>
      <div class="step"><div class="step__n">3</div><h4>Approvals &amp; install</h4><p>We lodge the grid connection and rebate paperwork, then our accredited crew installs &mdash; usually in one day, tidy site guaranteed.</p></div>
      <div class="step"><div class="step__n">4</div><h4>Switch on &amp; aftercare</h4><p>We commission, test, walk you through your monitoring app, and stay reachable for servicing and warranty for the life of the system.</p></div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Popular configurations</span>
      <h2>A starting point, not a fixed menu</h2>
      <p>These are the setups Victorian households ask for most often. Your final design depends on your roof, your switchboard and how much power you use after dark.</p>
    </div>
    <div class="grid g-3">
      <div class="pkg reveal">
        <div class="pkg__size">6.6 kW</div>
        <p class="pkg__for">Couples and smaller households, modest evening usage</p>
        <ul class="pkg__spec">
          <li><span>Panels</span><span>16 &times; 440W tier&nbsp;1</span></li>
          <li><span>Inverter</span><span>5kW single phase</span></li>
          <li><span>Roof area</span><span>~30 m&sup2;</span></li>
          <li><span>Typical output</span><span>~24 kWh/day avg</span></li>
        </ul>
        <p class="pkg__out">Best suited to homes using <b>under 20 kWh a day</b> with someone home during daylight hours.</p>
        <a class="btn btn--ghost btn--block" href="#quote">Price this system</a>
      </div>

      <div class="pkg pkg--featured reveal" data-delay="90">
        <span class="pkg__tag">Most requested</span>
        <div class="pkg__size">10 kW</div>
        <p class="pkg__for">Family homes with ducted heating or cooling</p>
        <ul class="pkg__spec">
          <li><span>Panels</span><span>24 &times; 440W tier&nbsp;1</span></li>
          <li><span>Inverter</span><span>8&ndash;10kW single or three phase</span></li>
          <li><span>Roof area</span><span>~45 m&sup2;</span></li>
          <li><span>Typical output</span><span>~37 kWh/day avg</span></li>
        </ul>
        <p class="pkg__out">Pairs well with a battery later &mdash; we leave the system <b>battery ready</b> at no extra cost.</p>
        <a class="btn btn--primary btn--block" href="#quote">Price this system</a>
      </div>

      <div class="pkg reveal" data-delay="180">
        <div class="pkg__size">10 kW + battery</div>
        <p class="pkg__for">Households wanting evening independence</p>
        <ul class="pkg__spec">
          <li><span>Panels</span><span>24 &times; 440W tier&nbsp;1</span></li>
          <li><span>Battery</span><span>10&ndash;13.5 kWh usable</span></li>
          <li><span>Backup</span><span>Optional essential circuits</span></li>
          <li><span>Typical output</span><span>~37 kWh/day avg</span></li>
        </ul>
        <p class="pkg__out">Eligible for the <b>federal battery discount</b> on top of your solar rebate.</p>
        <a class="btn btn--ghost btn--block" href="#quote">Price this system</a>
      </div>
    </div>
    <p class="center mt-3" style="font-size:.9rem;color:var(--muted)">Output figures are annual daily averages modelled for Melbourne conditions on an unshaded north-facing roof. Your site will differ &mdash; we model yours specifically before quoting.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--rev split--equal">
      <div class="split__media reveal">
        <div class="media"><img class="focus-right" src="%(img)ssolar-homes-program.jpg" alt="Solar consultants reviewing a Victorian solar installation" loading="lazy"></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Rebates &amp; incentives</span>
        <h2>Victorian and federal support, stacked properly</h2>
        <p class="lead">Between state and federal programs there is real money on the table &mdash; but only if the paperwork is lodged correctly and on time. That is our job, not yours.</p>
        <ul class="ticks mt-3">
          <li>%(check)s <strong>Solar Homes Program (Victoria).</strong> Rebates of up to $1,400 on eligible solar PV for owner-occupiers, applied as a point-of-sale discount, plus an optional interest-free loan.</li>
          <li>%(check)s <strong>Small-scale Renewable Energy Scheme (federal).</strong> STCs discount your system cost upfront &mdash; we assign them so you never handle a certificate.</li>
          <li>%(check)s <strong>Cheaper Home Batteries Program (federal).</strong> A substantial per-kWh discount on eligible battery installs, tapering each year until the scheme ends.</li>
        </ul>
        <div class="callout mt-3">
          <strong>Eligibility changes regularly</strong>
          Income thresholds, rebate values and battery rates are reviewed by government periodically. We confirm exactly what you qualify for &mdash; in writing &mdash; before you commit to anything.
        </div>
        <div class="btn-row mt-3">
          <a class="btn btn--navy" href="#quote">Check what you qualify for %(arrow)s</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Customer feedback</span>
      <h2>What Victorian homeowners tell us</h2>
    </div>
    <div class="grid g-3">
      <div class="quote reveal">
        <div class="quote__stars">%(stars)s</div>
        <p class="quote__text">"I'd had three quotes and every one recommended a different size. Nova was the only company that asked to see my actual bills before proposing anything. They talked me <em>down</em> from what I thought I needed and explained exactly why. Install day was spotless."</p>
        <div class="quote__who"><div class="quote__av">RM</div><div><div class="quote__nm">Rebecca M.</div><div class="quote__loc">Glen Waverley, VIC</div></div></div>
      </div>
      <div class="quote reveal" data-delay="90">
        <div class="quote__stars">%(stars)s</div>
        <p class="quote__text">"We run a small fabrication workshop and our daytime load is enormous. Nova modelled it properly against our meter data instead of guessing. Two years on, the numbers have landed within a few percent of what they projected."</p>
        <div class="quote__who"><div class="quote__av">DT</div><div><div class="quote__nm">Daniel T.</div><div class="quote__loc">Dandenong South, VIC</div></div></div>
      </div>
      <div class="quote reveal" data-delay="180">
        <div class="quote__stars">%(stars)s</div>
        <p class="quote__text">"What sold me was that they answered the phone eighteen months after the install, when an inverter fault code came up. Sorted under warranty within the week. That is rarer than it should be in this industry."</p>
        <div class="quote__who"><div class="quote__av">PS</div><div><div class="quote__nm">Priya S.</div><div class="quote__loc">Point Cook, VIC</div></div></div>
      </div>
    </div>
  </div>
</section>
"""

HOME_FAQ = [
 ("How much does a solar system actually cost in Victoria?",
  "After the federal STC discount and the Victorian Solar Homes rebate, a quality 6.6kW system typically lands in the low-to-mid thousands, and a 10kW system somewhat above that. The honest answer is that it depends on your roof type, how many storeys, whether your switchboard needs upgrading and which equipment you choose. We quote a fixed price after a site assessment &mdash; no estimates that shift later."),
 ("How long until the system pays for itself?",
  "For most Victorian households with a well-sized system, payback typically falls somewhere in the three-to-six year range. The biggest variable is how much of your generation you use yourself rather than exporting, since feed-in tariffs are far lower than what you pay to buy power. We model this specifically for your household rather than quoting an industry average."),
 ("Do I need a battery, or should I start with panels?",
  "For many households, panels first is the sensible sequence &mdash; you capture the savings immediately and can add storage later. A battery makes the strongest case if you use a lot of power after sunset, want blackout protection, or have already maximised your roof. We design every solar system battery ready so adding one later is straightforward rather than a rewire."),
 ("What happens if my roof needs work first?",
  "We assess roof condition during the site inspection. If tiles are brittle, sheeting is corroded or the structure needs attention, we will tell you before you sign rather than discovering it on install day. It is far cheaper to address roofing before panels go on than to remove an array later."),
 ("Will solar still generate through a Melbourne winter?",
  "Yes, though output drops. A Melbourne system typically produces roughly a third less in June and July than its annual daily average, and more on clear cold days than overcast warm ones &mdash; panels actually run more efficiently at lower temperatures. Our modelling uses month-by-month figures, so the annual number we quote already accounts for winter."),
 ("Are you the ones doing the install, or do you subcontract?",
  "Installations are carried out by accredited installers working to our standards, and we name the accredited person on your quote. We do not hand jobs to whichever crew is cheapest that week, and the same company you signed with is the one you call for warranty and servicing."),
]

# ==========================================================================
# ABOUT
# ==========================================================================
ABOUT = """
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Our story</span>
        <h2>Started by people who were tired of fixing other companies' work</h2>
        <p class="lead">Nova Solar Solutions began because too many Victorian households were being sold systems that did not suit their homes, by companies that disappeared the moment the invoice cleared.</p>
        <p>Our founders spent years in electrical contracting, and a growing share of that work was remediation &mdash; undersized cabling, arrays pointed the wrong way, inverters mounted in full afternoon sun, rebate paperwork never lodged. The pattern was always the same: a system sold fast by someone who never saw the roof.</p>
        <p>So we built the company we wished those customers had called first. Every job starts with a site assessment. Every quote names the actual equipment. Every install is done by accredited people who answer the phone afterwards. It is not a complicated proposition &mdash; it is just rarer than it should be.</p>
        <div class="btn-row mt-3">
          <a class="btn btn--primary" href="#quote">Talk to our team %(arrow)s</a>
          <a class="btn btn--ghost" href="services.html">What we install</a>
        </div>
      </div>
      <div class="split__media reveal">
        <div class="media"><img src="%(img)sengineer-inspect.jpg" alt="Technician inspecting a solar installation" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">What we stand for</span>
      <h2>Four commitments we hold ourselves to</h2>
      <p>These are the standards we measure our own work against &mdash; and the ones you should hold any solar company to.</p>
    </div>
    <div class="grid g-4">
      <div class="card reveal"><div class="card__ico">%(doc)s</div><h3>Right-sized, always</h3><p>We would rather sell you a smaller system that pays for itself than a larger one that exports power at a poor feed-in rate. Sizing follows your usage data.</p></div>
      <div class="card reveal" data-delay="80"><div class="card__ico">%(shield)s</div><h3>Quality over margin</h3><p>We install equipment we are willing to warrant for a decade. If a cheaper component would not survive a Victorian summer on a dark roof, we do not stock it.</p></div>
      <div class="card reveal" data-delay="160"><div class="card__ico">%(users)s</div><h3>Straight answers</h3><p>If solar is a poor fit for your roof, your shading or your usage pattern, we will say so. A no from us costs less than a bad install.</p></div>
      <div class="card reveal" data-delay="240"><div class="card__ico">%(wrench)s</div><h3>Here afterwards</h3><p>Handover is the start of the relationship, not the end. Servicing, fault finding and warranty claims stay with us for the life of the system.</p></div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="split split--equal">
      <div class="split__media reveal">
        <div class="media"><img src="%(img)sinstaller-team.jpg" alt="Installation crew at work" loading="lazy"></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Accreditation</span>
        <h2>Credentials that actually matter</h2>
        <p>Solar accreditation in Australia is a patchwork of acronyms, and not all of them mean much. These are the ones that determine whether your rebate is valid and your warranty is enforceable.</p>
        <ul class="ticks mt-3">
          <li>%(check)s <strong>Clean Energy Council Approved Retailer.</strong> A signatory to the industry code of conduct governing sales practice, contracts and complaint handling.</li>
          <li>%(check)s <strong>SAA-accredited installers.</strong> Required for your system to qualify for STCs and state rebates &mdash; an unaccredited install voids both.</li>
          <li>%(check)s <strong>Solar Victoria authorised.</strong> Allows us to lodge Solar Homes Program rebates directly on your behalf.</li>
          <li>%(check)s <strong>Licensed electrical contractors.</strong> All grid-connected work certified under Victorian electrical safety requirements.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Where we work</span>
      <h2>Servicing Victoria, based in Melbourne</h2>
      <p>Our crews work across the metropolitan area and out into regional Victoria. If you are outside these areas, call us anyway &mdash; we will tell you honestly whether we can service you well.</p>
    </div>
    <div class="grid g-4 reveal">
      <div class="card"><h3 style="font-size:1.1rem">Inner &amp; eastern Melbourne</h3><p>Richmond, Hawthorn, Box Hill, Glen Waverley, Doncaster, Ringwood, Croydon and surrounds.</p></div>
      <div class="card"><h3 style="font-size:1.1rem">Southern &amp; bayside</h3><p>Brighton, Cheltenham, Clayton, Dandenong, Frankston, Mornington Peninsula.</p></div>
      <div class="card"><h3 style="font-size:1.1rem">Northern &amp; western</h3><p>Preston, Coburg, Craigieburn, Sunshine, Werribee, Point Cook, Melton.</p></div>
      <div class="card"><h3 style="font-size:1.1rem">Regional Victoria</h3><p>Geelong, Ballarat, Bendigo, Shepparton and the Latrobe Valley by arrangement.</p></div>
    </div>
  </div>
</section>
"""

# ==========================================================================
# SERVICES
# ==========================================================================
SERVICES = """
<section class="section">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Our services</span>
      <h2>Everything from first design to year-ten service call</h2>
      <p>We are a single point of accountability across the whole life of your system &mdash; design, supply, installation, compliance, monitoring and maintenance.</p>
    </div>

    <div class="grid g-3">
      <article class="scard reveal">
        <div class="scard__img"><img src="%(img)sresidential-roof.jpg" alt="Residential rooftop solar" loading="lazy"></div>
        <div class="scard__body">
          <h3>Residential solar</h3>
          <p>Grid-connected rooftop systems for houses, townhouses and units, designed around your household's real consumption pattern.</p>
        </div>
      </article>
      <article class="scard reveal" data-delay="80">
        <div class="scard__img"><img src="%(img)scommercial-solar.jpg" alt="Commercial solar array" loading="lazy"></div>
        <div class="scard__body">
          <h3>Commercial solar</h3>
          <p>20kW to 100kW+ systems for warehouses, workshops, retail and agriculture, with financial modelling built from your interval data.</p>
        </div>
      </article>
      <article class="scard reveal" data-delay="160">
        <div class="scard__img"><img src="%(img)sbattery-storage.jpg" alt="Battery storage system" loading="lazy"></div>
        <div class="scard__body">
          <h3>Battery storage</h3>
          <p>New installs and retrofits to existing solar, sized against your evening load, with optional blackout backup circuits.</p>
        </div>
      </article>
    </div>

    <div class="grid g-3 mt-4">
      <div class="card reveal"><div class="card__ico">%(wrench)s</div><h3>Servicing &amp; repairs</h3><p>Fault diagnosis, inverter replacement, isolator and DC cabling remediation, and warranty claim handling &mdash; including on systems we did not install.</p></div>
      <div class="card reveal" data-delay="80"><div class="card__ico">%(zap)s</div><h3>System upgrades</h3><p>Adding panels to an existing array, replacing an ageing inverter, or expanding capacity when you add an EV charger or a heat pump.</p></div>
      <div class="card reveal" data-delay="160"><div class="card__ico">%(monitor)s</div><h3>Monitoring &amp; performance</h3><p>Consumption monitoring set up properly at handover, plus annual performance reviews so underperformance gets caught early rather than at year five.</p></div>
      <div class="card reveal"><div class="card__ico">%(doc)s</div><h3>Grid applications</h3><p>Pre-approval, connection agreements, export limit negotiation and metering reconfiguration with your distributor, all handled by us.</p></div>
      <div class="card reveal" data-delay="80"><div class="card__ico">%(dollar)s</div><h3>Rebate management</h3><p>Eligibility checks, Solar Victoria applications, STC assignment and the interest-free loan process &mdash; prepared and lodged on your behalf.</p></div>
      <div class="card reveal" data-delay="160"><div class="card__ico">%(leaf)s</div><h3>Pre-purchase advice</h3><p>Buying a property with an existing system? We will inspect it and tell you what it is worth, what it will cost to maintain, and what needs replacing.</p></div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Equipment</span>
      <h2>What we install, and why</h2>
      <p>We are not tied to a single manufacturer. Equipment is selected per site &mdash; but everything we quote meets these baselines.</p>
    </div>
    <div class="table-wrap reveal">
      <table>
        <caption class="sr-only">Equipment standards used by Nova Solar Solutions</caption>
        <thead><tr><th scope="col">Component</th><th scope="col">Our minimum standard</th><th scope="col">Typical warranty</th></tr></thead>
        <tbody>
          <tr><td><strong>Solar panels</strong></td><td>Tier&nbsp;1 monocrystalline, CEC-approved, 440W+ per module</td><td>25&ndash;30 yr performance, 15&ndash;25 yr product</td></tr>
          <tr><td><strong>Inverters</strong></td><td>CEC-listed string or hybrid, with consumption monitoring</td><td>10 yr standard, extendable</td></tr>
          <tr><td><strong>Batteries</strong></td><td>LiFePO&#8324; chemistry, CEC-approved, modular where possible</td><td>10 yr or throughput-based</td></tr>
          <tr><td><strong>Mounting</strong></td><td>Australian-certified rail, wind-region rated for the site</td><td>10&ndash;20 yr structural</td></tr>
          <tr><td><strong>Installation</strong></td><td>SAA-accredited installer, licensed electrical contractor</td><td>10 yr Nova workmanship</td></tr>
        </tbody>
      </table>
    </div>
    <p class="center mt-3" style="font-size:.9rem;color:var(--muted)">Specific makes and models are named on your written quote before you sign. Warranty terms are the manufacturer's and are provided in full with your documentation.</p>
  </div>
</section>
"""

# ==========================================================================
# RESIDENTIAL
# ==========================================================================
RESIDENTIAL = """
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Home solar</span>
        <h2>Sized to your household, not to a price list</h2>
        <p class="lead">The single most common mistake in residential solar is buying the wrong size. Too small and you keep paying peak rates; too large and you export cheaply to the grid at a fraction of what you pay to buy it back.</p>
        <p>We start with twelve months of your consumption data where we can get it, and your bills where we cannot. That tells us not just how much power you use, but <em>when</em> &mdash; which is the number that actually determines the right system.</p>
        <ul class="ticks mt-3">
          <li>%(check)s Shading modelled across all four seasons, not just midday summer</li>
          <li>%(check)s Roof pitch, orientation and available area measured, not estimated</li>
          <li>%(check)s Switchboard and main-switch capacity checked before quoting</li>
          <li>%(check)s Every design left battery ready at no additional cost</li>
        </ul>
      </div>
      <div class="split__media reveal">
        <div class="media"><img src="%(img)sresidential-roof.jpg" alt="Modern Victorian home with rooftop solar" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Choosing a size</span>
      <h2>Which system suits which household</h2>
      <p>A rough guide based on daily consumption. Your quote will refine this against your actual usage curve.</p>
    </div>
    <div class="table-wrap reveal">
      <table>
        <caption class="sr-only">Residential system sizing guide</caption>
        <thead><tr><th scope="col">System size</th><th scope="col">Suits daily usage</th><th scope="col">Roughly</th><th scope="col">Roof area needed</th></tr></thead>
        <tbody>
          <tr><td><strong>6.6 kW</strong></td><td>Up to 20 kWh/day</td><td>1&ndash;3 people, gas heating, modest cooling</td><td>~30 m&sup2;</td></tr>
          <tr><td><strong>8.8 kW</strong></td><td>20&ndash;28 kWh/day</td><td>Family home, reverse-cycle cooling</td><td>~40 m&sup2;</td></tr>
          <tr><td><strong>10 kW</strong></td><td>28&ndash;40 kWh/day</td><td>Larger family, ducted climate control, pool</td><td>~45 m&sup2;</td></tr>
          <tr><td><strong>13.3 kW</strong></td><td>40 kWh+/day</td><td>All-electric home, EV charging, heat pump</td><td>~60 m&sup2;</td></tr>
        </tbody>
      </table>
    </div>
    <div class="callout callout--eco mt-3">
      <strong>Going all-electric?</strong>
      If you are planning to replace gas heating or hot water, or add an EV charger in the next few years, tell us at quote stage. Sizing for tomorrow's load rather than today's usually costs far less than expanding an array later.
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media reveal">
        <div class="media"><img src="%(img)sinverter.jpg" alt="Solar inverter installation" loading="lazy"></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Install day</span>
        <h2>What actually happens on your roof</h2>
        <p>Most residential installs are completed in a single day. Here is the sequence, so nothing on the day is a surprise.</p>
        <ul class="ticks mt-3">
          <li>%(check)s <strong>Arrival and setup.</strong> Crew arrives between 7:30 and 8:30am, sets up fall protection and lays down protection for your driveway and garden beds.</li>
          <li>%(check)s <strong>Mounting and rail.</strong> Roof penetrations sealed to manufacturer specification &mdash; this is where cheap installs fail, and where leaks come from years later.</li>
          <li>%(check)s <strong>Panels and DC.</strong> Modules mounted, DC cabling run in conduit and correctly labelled to Australian standards.</li>
          <li>%(check)s <strong>Inverter and switchboard.</strong> Inverter mounted out of direct afternoon sun, isolators fitted, switchboard connected. Power is off for roughly one to two hours.</li>
          <li>%(check)s <strong>Test and handover.</strong> System commissioned and tested, monitoring configured on your phone, compliance certificate issued, site left clean.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

# ==========================================================================
# COMMERCIAL
# ==========================================================================
COMMERCIAL = """
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Commercial solar</span>
        <h2>A business case built from your meter data, not a brochure</h2>
        <p class="lead">Commercial solar either stacks up financially or it does not, and the difference comes down to how well generation lines up with your actual load. We model that properly before either of us commits.</p>
        <p>We request your interval data from your retailer &mdash; typically 15 or 30 minute readings across twelve months &mdash; and overlay modelled generation onto it. That produces a genuine self-consumption figure, which drives everything: system size, payback period and whether storage makes sense.</p>
        <ul class="ticks mt-3">
          <li>%(check)s Written payback, IRR and cash-flow projections</li>
          <li>%(check)s Structural assessment of roof loading before design is finalised</li>
          <li>%(check)s Export limits negotiated with your distributor where needed</li>
          <li>%(check)s Installation scheduled around your trading hours</li>
        </ul>
        <div class="btn-row mt-3">
          <a class="btn btn--primary" href="#quote">Request a feasibility assessment %(arrow)s</a>
        </div>
      </div>
      <div class="split__media reveal">
        <div class="media"><img src="%(img)scommercial-solar.jpg" alt="Commercial rooftop solar installation" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Sectors</span>
      <h2>Where commercial solar performs best</h2>
      <p>Businesses that consume most of their power during daylight hours see the strongest returns, because self-consumed energy is worth far more than exported energy.</p>
    </div>
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">%(building)s</div><h3>Warehousing &amp; logistics</h3><p>Large unshaded roof areas and steady daytime load from lighting, materials handling and refrigeration. Often the strongest payback case we model.</p></div>
      <div class="card reveal" data-delay="80"><div class="card__ico">%(wrench)s</div><h3>Manufacturing &amp; workshops</h3><p>High daytime demand from machinery and compressed air. Systems here frequently reach self-consumption rates above 80 percent.</p></div>
      <div class="card reveal" data-delay="160"><div class="card__ico">%(users)s</div><h3>Retail &amp; hospitality</h3><p>Trading-hours load from refrigeration, cooking and climate control, with roof space often shared across a strata arrangement we can help navigate.</p></div>
      <div class="card reveal"><div class="card__ico">%(leaf)s</div><h3>Agriculture &amp; horticulture</h3><p>Irrigation pumping, cool rooms and shed load, with generous roof and ground-mount options across the Victorian regions.</p></div>
      <div class="card reveal" data-delay="80"><div class="card__ico">%(home)s</div><h3>Aged care &amp; community</h3><p>Consistent round-the-clock demand where solar plus storage can meaningfully reduce exposure to peak tariffs.</p></div>
      <div class="card reveal" data-delay="160"><div class="card__ico">%(monitor)s</div><h3>Offices &amp; professional</h3><p>Predictable weekday load profiles from HVAC and equipment, making generation modelling unusually accurate.</p></div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Process</span>
      <h2>How a commercial project runs</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="step__n">1</div><h4>Data &amp; feasibility</h4><p>We obtain your interval data, model generation against it and produce a written feasibility summary. No cost, no obligation.</p></div>
      <div class="step"><div class="step__n">2</div><h4>Design &amp; approvals</h4><p>Structural assessment, electrical design, distributor pre-approval and export limit negotiation.</p></div>
      <div class="step"><div class="step__n">3</div><h4>Installation</h4><p>Staged around your operations, with safety documentation, inductions and traffic management as the site requires.</p></div>
      <div class="step"><div class="step__n">4</div><h4>Commission &amp; monitor</h4><p>Testing, compliance certification, monitoring portal setup and scheduled maintenance under an ongoing service agreement.</p></div>
    </div>
  </div>
</section>
"""

# ==========================================================================
# BATTERY
# ==========================================================================
BATTERY = """
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Battery storage</span>
        <h2>Use your own power after the sun goes down</h2>
        <p class="lead">Without storage, most Victorian households export a large share of what they generate during the day, then buy power back at night for several times the feed-in rate. A battery closes that gap.</p>
        <p>Whether it closes it profitably depends on your evening consumption, your tariff structure and the battery's usable capacity. We model the arbitrage honestly &mdash; and if the numbers do not work for your household yet, we will tell you.</p>
        <ul class="ticks mt-3">
          <li>%(check)s Sized against your genuine after-dark load</li>
          <li>%(check)s Federal battery discount applied at quote stage</li>
          <li>%(check)s Optional backup circuits for blackout protection</li>
          <li>%(check)s Retrofits to most existing solar systems</li>
        </ul>
      </div>
      <div class="split__media reveal">
        <div class="media"><img src="%(img)sbattery-storage.jpg" alt="Home battery storage system" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Sizing</span>
      <h2>How much storage do you actually need?</h2>
      <p>The useful question is not "how big a battery can I afford" but "how much power do I use between sunset and sunrise".</p>
    </div>
    <div class="table-wrap reveal">
      <table>
        <caption class="sr-only">Battery sizing guide</caption>
        <thead><tr><th scope="col">Usable capacity</th><th scope="col">Covers roughly</th><th scope="col">Best for</th></tr></thead>
        <tbody>
          <tr><td><strong>5&ndash;7 kWh</strong></td><td>Evening lighting, cooking, entertainment</td><td>Smaller households wanting to shave peak-rate usage</td></tr>
          <tr><td><strong>10&ndash;13.5 kWh</strong></td><td>A typical family's overnight load</td><td>The most common residential choice in Victoria</td></tr>
          <tr><td><strong>15&ndash;20 kWh</strong></td><td>Overnight load plus climate control or EV top-up</td><td>All-electric homes, larger families</td></tr>
          <tr><td><strong>20 kWh+</strong></td><td>Extended autonomy or partial off-grid</td><td>Rural properties, unreliable supply, high resilience needs</td></tr>
        </tbody>
      </table>
    </div>
    <div class="callout mt-3">
      <strong>Usable vs nominal capacity</strong>
      Manufacturers quote both, and they are not the same number. A battery advertised at 13.5 kWh may deliver noticeably less in practice once depth-of-discharge limits are applied. Our quotes state usable capacity, because that is what determines your savings.
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media reveal">
        <div class="media media--tall"><img src="%(img)sfamily-home.jpg" alt="Family home interior powered by solar and battery" loading="lazy"></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Blackout backup</span>
        <h2>What a battery does &mdash; and does not do &mdash; in an outage</h2>
        <p>This is the most misunderstood part of home storage, so it is worth being precise.</p>
        <p>A standard grid-connected battery <strong>will not</strong> power your home during a blackout unless it is specifically configured with backup capability. Without it, the system shuts down for the safety of line workers, exactly as a solar inverter does.</p>
        <p>With backup configured, a dedicated circuit &mdash; typically fridge, lighting, internet and a few power points &mdash; keeps running, and your solar can recharge the battery during the outage. Whole-home backup is possible on some systems but costs considerably more.</p>
        <ul class="ticks mt-3">
          <li>%(check)s Backup requires a compatible battery and additional switchgear</li>
          <li>%(check)s Essential circuits are chosen with you during design</li>
          <li>%(check)s Changeover is automatic, with a brief interruption on most systems</li>
          <li>%(check)s We test backup operation at commissioning, in front of you</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

BATTERY_FAQ = [
 ("How long do home batteries last?",
  "Most quality lithium batteries are warranted for around ten years, or a defined energy throughput, whichever comes first. Warranties typically guarantee the battery will still hold a stated percentage of its original capacity at end of term &mdash; commonly around 60 to 70 percent. Real-world life often exceeds the warranty period, but capacity does decline gradually throughout."),
 ("Can I add a battery to solar panels I already have?",
  "Usually yes. If you have a hybrid inverter it may be straightforward. If you have a standard string inverter, we would typically add an AC-coupled battery with its own inverter, which works with almost any existing system. We check compatibility during the site assessment before quoting."),
 ("Does a battery help if I am on a flat-rate tariff?",
  "It helps less than on a time-of-use tariff, because there is no cheap overnight rate to arbitrage against. On a flat tariff the saving comes purely from avoiding grid purchase in the evening rather than exporting cheaply. We often recommend reviewing your tariff alongside the battery decision, since the two interact significantly."),
 ("Is it safe to install a battery at home?",
  "Modern home batteries installed to Australian Standard AS/NZS 5139 are safe. That standard governs where a battery can be located &mdash; restricting installation inside habitable rooms and near exits, and setting requirements for clearances and fire separation. We assess compliant locations at your property during the site visit, and we will not install one somewhere that does not comply."),
]

# ==========================================================================
# REBATES
# ==========================================================================
REBATES = """
<section class="section">
  <div class="wrap wrap-narrow">
    <div class="reveal">
      <span class="eyebrow">Rebates &amp; incentives</span>
      <h2>What Victorian households and businesses can claim</h2>
      <p class="lead">There are three separate programs that can reduce the cost of a solar or battery installation in Victoria. They stack &mdash; but each has its own eligibility rules, and all of them change over time.</p>
      <div class="callout mt-3">
        <strong>Please read this first</strong>
        The figures below reflect the programs as they stood when this page was written. Government rebate values, income thresholds and closing dates are revised regularly. Always confirm current details with Solar Victoria and your installer before making a decision &mdash; we confirm your specific entitlement in writing on every quote.
      </div>
    </div>
  </div>
</section>

<section class="section section--soft" style="padding-top:0">
  <div class="wrap">
    <div class="grid g-3">
      <div class="card reveal">
        <div class="card__ico">%(home)s</div>
        <h3>Solar Homes Program</h3>
        <p><strong>Victorian government.</strong> A rebate of up to $1,400 towards an eligible solar PV system for owner-occupiers, applied as a point-of-sale discount so you simply pay less upfront.</p>
        <p>An optional interest-free loan of up to a matching amount is also available, repayable over four years, which lets many households install with little or no money down.</p>
        <p style="font-size:.9rem;color:var(--muted)">Eligibility depends on household income, property value, and whether the address has claimed previously. The income threshold was reduced to $150,000 per year from 1 July 2026.</p>
      </div>

      <div class="card reveal" data-delay="80">
        <div class="card__ico">%(sun)s</div>
        <h3>Small-scale Renewable Energy Scheme</h3>
        <p><strong>Federal government.</strong> Often called "the STC rebate", this is the largest single discount on most residential solar systems &mdash; frequently worth several thousand dollars.</p>
        <p>Your system generates small-scale technology certificates based on its size and location. We assign those certificates and deduct their value from your invoice, so you never handle a certificate or wait for a payment.</p>
        <p style="font-size:.9rem;color:var(--muted)">The number of certificates issued reduces each year as the scheme winds down toward its scheduled end in 2030.</p>
      </div>

      <div class="card reveal" data-delay="160">
        <div class="card__ico">%(battery)s</div>
        <h3>Cheaper Home Batteries</h3>
        <p><strong>Federal government.</strong> A per-kilowatt-hour discount on eligible battery installations, worth roughly 30 percent of typical installed cost when the program began.</p>
        <p>The rate is tiered by battery size &mdash; the first portion of capacity attracts the full rate, with larger batteries receiving a reduced rate on capacity above that.</p>
        <p style="font-size:.9rem;color:var(--muted)">The per-kWh rate steps down at scheduled intervals until the program concludes at the end of 2030, so timing affects the amount you receive.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Eligibility</span>
        <h2>Do you qualify?</h2>
        <p>The Victorian Solar Homes rebate has the most conditions attached. Broadly, an owner-occupier application is assessed against criteria along these lines:</p>
        <ul class="ticks mt-3">
          <li>%(check)s You own and live in the property</li>
          <li>%(check)s Combined household taxable income sits below the current threshold</li>
          <li>%(check)s The property value falls under the program cap</li>
          <li>%(check)s No previous solar PV rebate has been claimed at that address</li>
          <li>%(check)s The system is installed by an authorised retailer using accredited installers</li>
        </ul>
        <p class="mt-3">Rental properties are handled under a separate stream with its own rules, requiring agreement between landlord and tenant. Businesses are not eligible for Solar Homes, but do access the federal STC scheme and may claim depreciation &mdash; ask your accountant.</p>
        <div class="btn-row mt-3">
          <a class="btn btn--primary" href="#quote">Check my eligibility %(arrow)s</a>
          <a class="btn btn--ghost" href="tel:%(tel)s">Call %(phone)s</a>
        </div>
      </div>
      <div class="split__media reveal">
        <div class="media"><img src="%(img)sengineer-inspect.jpg" alt="Consultant reviewing a solar system" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>
"""

REBATES_FAQ = [
 ("Do I pay the rebate amount upfront and claim it back later?",
  "No. The Victorian Solar Homes rebate is applied as a point-of-sale discount, meaning it is deducted from your invoice and you simply pay less. The federal STC value is likewise assigned to us and deducted upfront. You should never be asked to pay full price and wait for a reimbursement."),
 ("Can I claim the solar rebate and the battery rebate together?",
  "Yes, they are separate programs administered differently &mdash; one state, one federal &mdash; and a household installing solar and a battery can generally access both, provided each program's own eligibility conditions are met. We calculate both on your quote."),
 ("What if I have already had solar installed at this address?",
  "The Solar Homes solar PV rebate is generally limited to one claim per property, so a previous claim at that address usually rules out another. However, you may still be eligible for battery incentives and for the federal STC discount on additional or replacement panels. We will check your address history before quoting."),
 ("How long does the rebate application take?",
  "Once your eligibility documents are in, approval commonly comes through within a couple of weeks, and the approval remains valid for a limited window during which the installation must be completed. We manage the timeline so nothing lapses, and we schedule your install inside the valid period."),
 ("Are interest-free loans really interest free?",
  "Yes &mdash; the Victorian loan carries no interest and no fees, repaid in instalments over four years. It is optional, and taking it does not change the rebate amount. It exists so households can install without a large upfront payment, effectively repaying from the bill savings."),
]

# ==========================================================================
# CONTACT
# ==========================================================================
CONTACT = """
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Get in touch</span>
        <h2>Let's work out what your roof can do</h2>
        <p class="lead">Send through your details and a recent electricity bill if you have one handy. We will come back within one business day with next steps &mdash; and if we are not the right fit for your property, we will say so.</p>

        <div class="grid" style="gap:18px;margin-top:30px">
          <div class="trust__item"><div class="trust__ico">%(phone)s</div><div><div class="trust__t"><a href="tel:%(tel)s">%(phone_d)s</a></div><div class="trust__s">Mon&ndash;Fri 8:00am&ndash;5:30pm &middot; Sat 9:00am&ndash;2:00pm</div></div></div>
          <div class="trust__item"><div class="trust__ico">%(mail)s</div><div><div class="trust__t"><a href="mailto:%(email)s">%(email)s</a></div><div class="trust__s">We reply within one business day</div></div></div>
          <div class="trust__item"><div class="trust__ico">%(pin)s</div><div><div class="trust__t">%(addr1)s</div><div class="trust__s">%(addr2)s &middot; by appointment</div></div></div>
        </div>

        <div class="callout mt-3">
          <strong>Existing customer needing service?</strong>
          Call us directly and mention your install address &mdash; service calls are triaged ahead of new enquiries.
        </div>
      </div>

      <div class="reveal">
        <div class="quote-card">
          <h3>Request your free quote</h3>
          <p class="quote-card__note">Takes about a minute. No obligation, and we never pass your details to third parties.</p>
          %(form)s
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">What happens next</span>
      <h2>After you hit send</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="step__n">1</div><h4>We call you</h4><p>A short conversation about your property, your usage and what you are hoping to achieve. Usually ten minutes.</p></div>
      <div class="step"><div class="step__n">2</div><h4>Desktop assessment</h4><p>We model your roof from imagery, check shading and estimate generation before anyone visits.</p></div>
      <div class="step"><div class="step__n">3</div><h4>Site visit</h4><p>We confirm roof condition, switchboard capacity and cable routes in person, so the quote is fixed rather than indicative.</p></div>
      <div class="step"><div class="step__n">4</div><h4>Written quote</h4><p>Named equipment, generation estimates, rebates itemised, fixed price. Take your time with it.</p></div>
    </div>
  </div>
</section>
"""

# ==========================================================================
# LEGAL
# ==========================================================================
PRIVACY = """
<section class="section">
  <div class="wrap wrap-narrow">
    <div class="reveal">
      <p class="lead">%(brand)s respects your privacy. This policy explains what personal information we collect, why we collect it, and what we do with it.</p>

      <h2 style="margin-top:2em">Information we collect</h2>
      <p>When you request a quote or contact us, we collect the details you provide &mdash; typically your name, phone number, email address and property postcode. To prepare an accurate quote we may also ask for your electricity bill or interval consumption data, and details about your roof, switchboard and household usage.</p>

      <h2 style="margin-top:2em">Why we collect it</h2>
      <p>We use your information to respond to your enquiry, design and price a system, arrange site visits and installation, lodge rebate and grid-connection applications on your behalf, and provide warranty and servicing afterwards. Where you have agreed to it, we may also send occasional updates about maintenance or programs relevant to your system.</p>

      <h2 style="margin-top:2em">Who we share it with</h2>
      <p>We share information only where it is necessary to deliver the service you have asked for &mdash; for example with Solar Victoria and the Clean Energy Regulator for rebate and certificate processing, with your electricity distributor for connection approval, with the accredited installer attending your property, and with equipment suppliers for warranty claims.</p>
      <p><strong>We do not sell your personal information, and we do not pass your details to third-party marketing lists or lead brokers.</strong></p>

      <h2 style="margin-top:2em">Storage and security</h2>
      <p>Your information is held in access-controlled systems and retained only as long as needed for the purposes above or as required by law &mdash; noting that rebate, electrical compliance and warranty obligations require us to keep installation records for extended periods.</p>

      <h2 style="margin-top:2em">Accessing or correcting your information</h2>
      <p>You may request access to the personal information we hold about you, ask us to correct it, or ask us to stop sending marketing communications, by emailing <a href="mailto:%(email)s">%(email)s</a> or calling %(phone_d)s. We will respond within a reasonable period.</p>

      <h2 style="margin-top:2em">Cookies</h2>
      <p>This website uses only what is necessary for the site to function. If analytics or advertising tools are added in future, this policy will be updated to say so.</p>

      <h2 style="margin-top:2em">Complaints</h2>
      <p>If you believe we have mishandled your personal information, contact us first at <a href="mailto:%(email)s">%(email)s</a>. If you are not satisfied with our response, you may refer the matter to the Office of the Australian Information Commissioner.</p>

      <div class="callout mt-4">
        <strong>Template notice</strong>
        This policy is provided as a starting point and should be reviewed by a qualified adviser before publication to confirm it reflects your actual practices and obligations under the Privacy Act 1988 (Cth).
      </div>
    </div>
  </div>
</section>
"""

TERMS = """
<section class="section">
  <div class="wrap wrap-narrow">
    <div class="reveal">
      <p class="lead">These terms govern your use of this website. Terms applying to the supply and installation of a solar or battery system are set out separately in your written quote and installation contract.</p>

      <h2 style="margin-top:2em">Website content</h2>
      <p>Information on this site is provided for general guidance. System sizes, generation figures, savings estimates, payback periods and rebate amounts are indicative only and depend on your specific property, consumption and prevailing government programs. Nothing on this site constitutes a quote or an offer to contract.</p>

      <h2 style="margin-top:2em">Rebates and government programs</h2>
      <p>Rebate values, eligibility criteria and program end dates are set by government and change from time to time. While we make reasonable efforts to keep this site current, you should confirm present details with Solar Victoria and the Clean Energy Regulator. Your entitlement is confirmed in writing on your quote.</p>

      <h2 style="margin-top:2em">Quotes and pricing</h2>
      <p>Quotes are valid for the period stated on them and are subject to a site assessment. Where a site assessment identifies conditions not reasonably apparent at quoting &mdash; such as structural defects, asbestos, or switchboard non-compliance &mdash; we will discuss any variation with you in writing before proceeding.</p>

      <h2 style="margin-top:2em">Warranties</h2>
      <p>Equipment warranties are provided by the respective manufacturers on their terms and are supplied with your handover documentation. Our workmanship warranty covers installation and mounting as stated in your contract. Nothing in these terms excludes, restricts or modifies any guarantee, right or remedy you have under the Australian Consumer Law.</p>

      <h2 style="margin-top:2em">Intellectual property</h2>
      <p>The content, branding and layout of this website are owned by %(brand)s unless otherwise indicated, and may not be reproduced without permission.</p>

      <h2 style="margin-top:2em">Liability</h2>
      <p>To the extent permitted by law, we are not liable for loss arising from reliance on general information published on this website. This does not limit our obligations under any contract you enter with us, or under the Australian Consumer Law.</p>

      <h2 style="margin-top:2em">Contact</h2>
      <p>Questions about these terms can be sent to <a href="mailto:%(email)s">%(email)s</a> or raised on %(phone_d)s.</p>

      <div class="callout mt-4">
        <strong>Template notice</strong>
        These terms are a starting point only and should be reviewed by a qualified legal adviser before publication.
      </div>
    </div>
  </div>
</section>
"""

# ==========================================================================
# Assemble
# ==========================================================================
_common = dict(
    img=IMG, check=ico('check'), arrow=ico('arrow'), shield=ico('shield'),
    dollar=ico('dollar'), award=ico('award'), users=ico('users'), doc=ico('doc'),
    wrench=ico('wrench'), zap=ico('zap'), monitor=ico('monitor'), leaf=ico('leaf'),
    building=ico('building'), home=ico('home'), sun=ico('sun'), battery=ico('battery'),
    phone=ico('phone'), mail=ico('mail'), pin=ico('pin'),
    stars=ico('star') * 5,
    tel=PHONE_HREF, phone_d=PHONE_DISPLAY, email=EMAIL,
    addr1=ADDRESS_LINES[0], addr2=ADDRESS_LINES[1], brand=BRAND,
)

def _fill(tpl, **extra):
    d = dict(_common); d.update(extra)
    return tpl % d

PAGES = [
 dict(slug="index",
      title="Nova Solar Solutions | Solar Panels &amp; Battery Storage in Victoria",
      desc="Victorian solar specialists. Right-sized rooftop solar, battery storage and commercial systems, with Solar Homes and federal rebates handled for you. Free quotes across Melbourne and regional Victoria.",
      body=_fill(HOME, form=quote_form(compact=True, form_id="heroForm"))
           + faq(HOME_FAQ, soft=False)   # white, so it reads as its own block after the soft testimonials
           + cta_band("Ready to see the numbers for your roof?",
                      "Send us a recent bill and we will model your generation, savings and rebates &mdash; at no cost and with no obligation.")),

 dict(slug="about",
      title="About Us | Nova Solar Solutions",
      desc="Nova Solar Solutions is a Melbourne-based solar and battery installer serving all of Victoria. Accredited installers, right-sized designs and aftercare that outlasts the invoice.",
      body=page_hero("Solar done properly, by people who stay reachable",
                     "We are a Victorian solar and battery company built on right-sized designs, accredited installation and a support line that still works years after handover.",
                     [("Home", "index.html"), ("About", None)],
                     bg=IMG + "installer-team.jpg")
           + _fill(ABOUT)
           + cta_band("Talk to a Victorian solar specialist",
                      "No scripts, no pressure &mdash; just a straight conversation about whether solar makes sense for your property.")),

 dict(slug="services",
      title="Our Services | Solar, Batteries &amp; Maintenance | Nova Solar Solutions",
      desc="Residential and commercial solar, battery storage, system upgrades, repairs, monitoring and rebate management across Victoria.",
      body=page_hero("Design, install, connect, maintain",
                     "One team accountable for the entire life of your system &mdash; from the first roof measurement to the year-ten service call.",
                     [("Home", "index.html"), ("Services", None)],
                     bg=IMG + "inverter.jpg")
           + _fill(SERVICES)
           + cta_band("Not sure which service you need?",
                      "Tell us about your property and we will point you to the right option &mdash; even if that turns out not to be us.")),

 dict(slug="residential-solar",
      title="Residential Solar Panels Victoria | Nova Solar Solutions",
      desc="Home solar systems from 6.6kW to 13.3kW, designed around your household's actual usage. Solar Homes rebate handled, battery-ready as standard.",
      body=page_hero("Home solar built around how you actually live",
                     "Rooftop systems sized from your real consumption data, installed by accredited people, with the rebate paperwork handled end to end.",
                     [("Home", "index.html"), ("Services", "services.html"), ("Residential Solar", None)],
                     bg=IMG + "residential-roof.jpg")
           + _fill(RESIDENTIAL)
           + cta_band("Find out what size suits your home",
                      "Send through a recent bill and we will model the right system for your roof, your usage and your budget.")),

 dict(slug="commercial-solar",
      title="Commercial Solar Systems Victoria | Nova Solar Solutions",
      desc="Commercial solar from 20kW to 100kW+ for Victorian businesses, with payback modelling built from your interval data and installation scheduled around trading hours.",
      body=page_hero("Commercial solar with a business case you can check",
                     "We model generation against your actual interval data before recommending anything, so the payback figures hold up under scrutiny.",
                     [("Home", "index.html"), ("Services", "services.html"), ("Commercial Solar", None)],
                     bg=IMG + "commercial-solar.jpg")
           + _fill(COMMERCIAL)
           + cta_band("Request a no-cost feasibility assessment",
                      "Send us twelve months of interval data and we will return modelled generation, self-consumption and payback &mdash; before you commit to anything.")),

 dict(slug="battery-storage",
      title="Home Battery Storage Victoria | Nova Solar Solutions",
      desc="Home battery installation and retrofits across Victoria. Honest sizing against your evening load, federal battery discount applied, optional blackout backup.",
      body=page_hero("Store your daytime solar, spend it after dark",
                     "Battery systems sized against your genuine evening consumption, with the federal battery discount applied and backup circuits available.",
                     [("Home", "index.html"), ("Services", "services.html"), ("Battery Storage", None)],
                     bg=IMG + "battery-storage.jpg")
           + _fill(BATTERY)
           + faq(BATTERY_FAQ, heading="Battery questions, answered plainly")
           + cta_band("Should you add a battery yet?",
                      "We will model it against your usage and tell you straight whether the numbers work for your household today.")),

 dict(slug="rebates",
      title="Solar Rebates Victoria 2026 | Solar Homes &amp; Federal Incentives",
      desc="A plain-English guide to the Victorian Solar Homes rebate, the federal STC scheme and the Cheaper Home Batteries Program, and how they stack for Victorian households.",
      body=page_hero("Solar rebates in Victoria, explained plainly",
                     "Three programs, three sets of rules, and real money involved. Here is how they work and how they combine &mdash; without the fine-print games.",
                     [("Home", "index.html"), ("Rebates", None)],
                     bg=IMG + "panel-closeup.jpg")
           + _fill(REBATES)
           + faq(REBATES_FAQ, heading="Rebate questions we hear most")
           + cta_band("Find out exactly what you qualify for",
                      "We check your eligibility against every current program and put the figures in writing on your quote.")),

 dict(slug="contact",
      title="Contact Us | Free Solar Quote | Nova Solar Solutions",
      desc="Request a free, no-obligation solar or battery quote in Victoria. Call 1300 668 275 or send an enquiry and we will respond within one business day.",
      body=page_hero("Get a free, no-obligation quote",
                     "Tell us about your property and we will come back within one business day with a clear next step.",
                     [("Home", "index.html"), ("Contact", None)],
                     bg=IMG + "solar-homes-program.jpg")
           + _fill(CONTACT, form=quote_form(form_id="contactForm"))),

 dict(slug="privacy",
      title="Privacy Policy | Nova Solar Solutions",
      desc="How Nova Solar Solutions collects, uses, stores and protects your personal information.",
      body=page_hero("Privacy Policy",
                     "What we collect, why we collect it, and what we do with it.",
                     [("Home", "index.html"), ("Privacy Policy", None)],
                     bg=IMG + "panel-closeup.jpg")
           + _fill(PRIVACY)),

 dict(slug="terms",
      title="Terms of Service | Nova Solar Solutions",
      desc="Terms governing the use of the Nova Solar Solutions website.",
      body=page_hero("Terms of Service",
                     "The terms that apply to this website and the information published on it.",
                     [("Home", "index.html"), ("Terms of Service", None)],
                     bg=IMG + "panel-closeup.jpg")
           + _fill(TERMS)),
]
