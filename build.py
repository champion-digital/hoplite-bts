#!/usr/bin/env python3
"""Builds the three prototype pages (index, editions, edition) from the content below.

Run:  python3 build.py
Edit the content or the page functions here, never the generated .html files.
"""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://shiphoplite.com/"
CONTACT = "https://shiphoplite.com/contact-us/"
EDITION = "edition.html"          # every edition link opens the sample edition (November 16)
COUNT = 30

# (week, short date, long date, title) newest first, grouped by month
ARCHIVE = [
    ("November 2026", [
        ("48", "Nov 23", "Thanksgiving flipped the tape: rates rose even as 9% more trucks showed up."),
        ("47", "Nov 16", "Trucking's sticker price just tied its all-time record, with less freight on the road."),
        ("46", "Nov 9", "The inversion is over: spot crosses back under contract."),
        ("45", "Nov 2", "Truck rates are finally slipping. You have about two weeks to cash in.")]),
    ("October", [
        ("43", "Oct 19", "Washington just bought parking: $200M worth."),
        ("42", "Oct 12", "Six weeks to Thanksgiving: the reefer turn starts now, into the tightest base market in years."),
        ("41", "Oct 5", "Rates rose into October. Peak season has arrived.")]),
    ("September", [
        ("40", "Sep 28", "Sixteen bankruptcies in 30 days: your Q4 bid math just changed."),
        ("39", "Sep 21", "Rejections fell 9%. Rates didn't follow."),
        ("38", "Sep 14", "The first uptick since July: rejections turned, and your window is one print from closing.")]),
    ("August", [
        ("36", "Aug 31", "The blitz is over. The trucks coming back are not the ones the market parked."),
        ("35", "Aug 24", "The blitz is live: 1 in 7 trucks could park this week, and the peak already came."),
        ("34", "Aug 17", "The floor cracked: biggest van rate drop since 2008, plus new tariffs and a brake blitz."),
        ("33", "Aug 10", "The first supply-side move in two years."),
        ("32", "Aug 3", "The CH Robinson verdict is changing how freight gets moved.")]),
    ("July", [
        ("31", "Jul 27", "A $604M verdict. And four other things that moved."),
        ("30", "Jul 20", "The market moved on four fronts at once."),
        ("29", "Jul 13", "Flatbed crossed $3.00. Tonnage is down. Explain that."),
        ("28", "Jul 6", "The World Cup is moving freight. A lot of it.")]),
    ("June", [
        ("27", "Jun 29", "Don't negotiate into a holiday spike."),
        ("26", "Jun 22", "200,000 drivers are leaving. No one is replacing them."),
        ("25", "Jun 15", "Hormuz deal sends oil tumbling, but capacity holds rates at records."),
        ("24", "Jun 9", "The market has repriced. H2 planning starts now."),
        ("23", "Jun 2", "Rates hold after holiday. SCOTUS ruling tightens it.")]),
    ("May", [
        ("22", "May 25", "Happy Memorial Day. Tuesday comes fast."),
        ("21", "May 18", "The freight recession is over."),
        ("20", "May 11", "Roadcheck starts tomorrow. The market was already tight."),
        ("19", "May 4", "Three events. Twenty-one days. No room for delay.")]),
    ("April", [
        ("18", "Apr 27", "The lull was a trap. The squeeze starts now."),
        ("17", "Apr 20", "Diesel $5.61. Every lane has already changed.")]),
]
assert sum(len(r) for _, r in ARCHIVE) == COUNT
INFO = json.loads((ROOT / "data" / "editions.json").read_text(encoding="utf-8"))   # week -> tags, dek, alt
MONTHS = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June", "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}


def long_date(short):
    m, d = short.split()
    return f"{MONTHS[m]} {d}, 2026"


def tags(wk):
    return '<span class="tags">' + "".join(f'<span class="tag">{e(t)}</span>' for t in INFO[str(wk)]["tags"]) + "</span>"


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
"""


LOCKUP = """<a class="lockup" href="index.html" aria-label="Behind the Shield, from Hoplite. Home">
      <img class="wordmark" src="assets/img/hoplite-wordmark.svg" alt="Hoplite" width="642" height="147">
      <span class="rule"></span>
      <img class="bts" src="assets/img/bts-logo.svg" alt="Behind the Shield" width="165" height="61">
    </a>"""

NAV = f"""<div class="wrap nav">
    {LOCKUP}
    <nav class="nav-links" aria-label="Main">
      <a href="editions.html">All editions</a>
      <a href="{SITE}" target="_blank" rel="noopener">shiphoplite.com</a>
      <a class="btn small" href="#subscribe">Subscribe</a>
    </nav>
    <button class="menu-btn" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
  </div>"""

MENU = f"""<div class="menu" role="dialog" aria-label="Menu">
  <div class="menu-top">
    {LOCKUP}
    <button class="menu-close" type="button" aria-label="Close menu">&times;</button>
  </div>
  <nav aria-label="Menu">
    <a href="index.html">Latest edition</a>
    <a href="editions.html">All editions</a>
    <a href="{SITE}" target="_blank" rel="noopener">shiphoplite.com</a>
  </nav>
  <a class="btn" href="#subscribe">Subscribe</a>
</div>
"""

SUBSCRIBE = """<section class="subscribe deep" id="subscribe">
  <div class="wrap">
    <div class="copy">
      <h2 class="display">Get it every Monday.</h2>
      <p>What moved in freight, why it matters to your network and what to do about it. Six minutes, in your inbox.</p>
    </div>
    <div>
      <form class="form" action="#" method="post">
        <input type="email" name="email" placeholder="Work email" aria-label="Work email" required>
        <button class="btn" type="submit">Subscribe</button>
      </form>
      <p class="form-note" role="status"></p>
    </div>
  </div>
</section>
"""

CLOSING = f"""<section class="closing">
  <img src="assets/img/closing.jpg" alt="A truck on a winding road at night, city lights on the horizon" loading="lazy">
  <div class="wrap">
    <h2 class="display">Move freight with the team <em>behind the shield.</em></h2>
    <p>Van, reefer, flatbed and cross-border, with a senior operator on every account.</p>
    <a class="btn" href="{CONTACT}" target="_blank" rel="noopener">Talk to Hoplite <span aria-hidden="true">&rarr;</span></a>
  </div>
</section>
"""

FOOTER = f"""<footer class="footer deep">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <img class="wordmark" src="assets/img/hoplite-wordmark.svg" alt="Hoplite" width="642" height="147">
        <p class="tagline display">Shield to shield, every mile.</p>
      </div>
      <nav class="footer-links" aria-label="Footer">
        <a href="editions.html">All editions</a>
        <a href="#subscribe">Subscribe</a>
        <a href="{SITE}" target="_blank" rel="noopener">shiphoplite.com</a>
        <a href="{CONTACT}" target="_blank" rel="noopener">Talk to Hoplite</a>
      </nav>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Hoplite Logistics &middot; Minneapolis, MN</span>
      <span>Behind the Shield is published every Monday.</span>
    </div>
  </div>
</footer>
<script src="assets/js/site.js"></script>
</body>
</html>
"""


def meta(*parts):
    # a part may hold one {curly} phrase that is dropped on phones
    def span(p):
        a, _, rest = p.partition("{")
        b, _, c = rest.partition("}")
        return f"<span>{e(a)}" + (f'<i class="wide">{e(b)}</i>' if b else "") + f"{e(c)}</span>"
    return '<p class="meta">' + "".join(span(p) for p in parts) + "</p>"


def figure(num, cap):
    return f'<div class="figure"><p class="num display">{e(num)}</p><p class="cap">{e(cap)}</p></div>'


# ---------------------------------------------------------------- home
def home():
    cards_html = "\n".join(f"""      <a class="card" href="{EDITION}">
        <img class="photo" src="assets/img/editions/wk{wk}.jpg" alt="{e(INFO[wk]['alt'])}" loading="lazy">
        <p class="small-meta">{e(long_date(d))}</p>
        <h3 class="display">{e(t)}</h3>
        {tags(wk)}
      </a>""" for wk, d, t in ARCHIVE[0][1][1:4])
    return head("Behind the Shield. Hoplite's weekly freight brief", "What moved in freight this week, why it matters to your network and what to do about it. Six minutes, every Monday.") + MENU + f"""<header>
  {NAV}
  <div class="wrap masthead">
    <h1><img class="big-logo" src="assets/img/bts-logo.svg" alt="Behind the Shield" width="165" height="61"></h1>
    <div class="about">
      <p>What moved in freight this week, why it matters to your network and what to do about it. Six minutes, every Monday.</p>
      {meta(f"{COUNT} editions since April 2026")}
    </div>
  </div>
</header>
<main>
<section class="wrap latest">
  <a href="{EDITION}"><img class="photo" src="assets/img/wk48.jpg" alt="A crowded truck stop at night seen from above, one truck pulling out toward the highway"></a>
  <div class="latest-text">
    <div class="left">
      {meta("Latest edition", "November 23, 2026")}
      <h2 class="display"><a href="{EDITION}">Thanksgiving flipped the tape: rates rose <em>even as 9% more trucks showed up.</em></a></h2>
      {tags(48)}
    </div>
    <div class="right">
      <p>More trucks came looking for work. Less freight needed moving. Prices went up anyway. And Q3's numbers just handed you the only math that matters for your 2027 bid.</p>
      <div class="read"><a class="btn" href="{EDITION}">Read the brief <span aria-hidden="true">&rarr;</span></a><span class="small-meta">6 min read</span></div>
    </div>
  </div>
</section>
<section class="wrap recent">
  <div class="recent-inner">
    <div class="recent-head">
      <h2 class="display">Recent editions</h2>
      <a class="more" href="editions.html">All {COUNT} editions &nbsp;&rarr;</a>
    </div>
    <div class="cards">
{cards_html}
    </div>
  </div>
</section>
</main>
""" + SUBSCRIBE + CLOSING + FOOTER


# ---------------------------------------------------------------- archive
def editions():
    groups = []
    for month, rows in ARCHIVE:
        rows_html = "\n".join(f"""        <a class="row" href="{EDITION}">
          <span class="date">{e(d)}</span>
          <span class="main">
            <span class="title display">{e(t)}</span>
            <span class="reveal"><span class="reveal-inner">
              <span class="dek">{e(INFO[wk]['dek'])}</span>
              {tags(wk)}
            </span></span>
          </span>
          <span class="media"><img src="assets/img/editions/wk{wk}.jpg" alt="{e(INFO[wk]['alt'])}" loading="lazy"><span class="arrow" aria-hidden="true">&rarr;</span></span>
        </a>""" for wk, d, t in rows)
        groups.append(f"""    <section class="month">
      <h2 class="display">{e(month)}</h2>
      <div class="rows">
{rows_html}
      </div>
    </section>""")
    return head("All editions. Behind the Shield", f"Every edition of Behind the Shield, Hoplite's weekly freight brief, since April 2026. {COUNT} editions.") + MENU + f"""<header class="hero short">
  <div class="hero-photo"><img src="assets/img/overpass.jpg" alt="An interstate at night seen from an overpass, every lane streaked with light"></div>
  {NAV}
  <div class="wrap hero-text">
    <h1 class="headline display">Every edition, <em>since April 2026.</em></h1>
    {meta(f"{COUNT} editions", "A new one every Monday")}
  </div>
</header>
<main>
  <div class="wrap editions">
""" + "\n".join(groups) + """
  </div>
</main>
""" + SUBSCRIBE + CLOSING + FOOTER


# ---------------------------------------------------------------- edition (Week 47)
def edition():
    toc = [("top-story", "Contract rates tie their record"),
           ("story-2", "Turkey season is here, and reefer carriers are saying no to one load in five"),
           ("story-3", "The fleet keeps shrinking, just as the import wave that fed it rolls out"),
           ("what-to-do", "What to do this week")]
    toc_html = "\n".join(f'        <li><b>{i}</b><a href="#{a}">{e(t)}</a></li>' for i, (a, t) in enumerate(toc, 1))
    body = [
        "Quick refresher, because this is the whole story. Trucking has two prices. The spot rate is the cash price: what a truck costs today, this load, this lane. The contract rate is the yearly deal you lock in with your carriers. Spot bounces around weekly. Contract is the slow, heavy line that becomes your budget. And DAT's October print, released November 10, showed the contract line rising 4 cents to $3.28 per mile, tying the all-time record set in May 2022.",
        "Here's the part that should make you put the coffee down. In May 2022, that record made sense: everyone was shipping everything, everywhere, at once. This time? Van freight volume is down 2% year over year. Reefer is down 9. Flatbed is down 7. Prices hit a record while the amount of stuff moving went down. That only happens for one reason: the trucks are disappearing faster than the freight is. The CDL rule from March carved a hole in the driver pool, and the earliest real relief is still Q1 2027. Fewer trucks chasing less freight, and the trucks are winning.",
        "Why the urgency: it's bid season. Right now, carriers across the country are quoting your 2027 rates, and every one of them just got handed a record-tying number to point at. If you're waiting for the soft weekly spot market to drag contract prices down before you sign, understand what you're actually betting on: that demand weakness will break a price floor that demand weakness just proved it can't break. The record printed on falling volume. That was the test. The floor held.",
    ]
    actions = [
        ("Do now", "Negotiate the deal structure, not the sticker price", "Carriers will quote 2027 against the fresh $3.28 record. Counter with mechanics: rates tied to a market index, 6-month terms instead of 12, and pricing tiers that flex with your volume. A fixed rate signed against a record print is a ceiling you pay for all year."),
        ("Do now", "Tender Thanksgiving food freight this week", "With reefer carriers rejecting one in five contracted loads, late tenders get cherry-picked. Submit now, add 48–72 hours of lead time, and pre-clear a backup carrier before the holiday squeeze, not during it."),
        ("Do now", "Credit-check every carrier in your 2027 bid", "Two bankruptcies in two days and the smallest fleet since early 2022. Pull financial and authority data on every incumbent before awarding lanes. A dying carrier's cheap bid is a February service failure with your name on it."),
        ("Watch", "Watch December's DAT print for a break above $3.28", "A tie is a baseline; a break is a trend. If November contract rates print above $3.28, re-run your 2027 budget at +5% and +8% before January awards go out."),
        ("Watch", "Don't let falling imports fool your truckload budget", "November's import taper will ease port congestion and may soften weekly spot rates. It will not touch the contract floor: this record printed while volume was already falling. Budget to supply, not demand."),
    ]
    actions_html = "\n".join(f"""      <li class="action{' watch' if s == 'Watch' else ''}">
        <div class="top"><span class="numeral">{i}</span><span class="status">{s}</span></div>
        <h3>{e(t)}</h3>
        <p>{e(b)}</p>
      </li>""" for i, (s, t, b) in enumerate(actions, 1))
    numbers = [
        ("$5.35", "Diesel, a gallon", "EIA on-highway average, last on file."),
        ("$2.89", "Dry van spot, a mile", "All-in, week of November 6. Contract sits at $3.28."),
        ("14.17%", "Tender rejections (OTRI)", "October spike. Reefer and flatbed run about 21%."),
        ("5.83", "Loads per truck", "November print, against 10.93 at the summer peak."),
        ("55.6%", "ISM manufacturing (PMI)", "Last print on file. Above 50 means expansion."),
        ("+28.1%", "Freight spend, year over year", "U.S. Bank Freight Payment Index."),
    ]
    numbers_html = "\n".join(f'      <div class="number"><p class="num display">{e(n)}</p><p class="label">{e(l)}</p><p class="cap">{e(c)}</p></div>' for n, l, c in numbers)
    return head("Trucking's sticker price just tied its all-time record. Behind the Shield, November 16, 2026", "Contract van rates hit $3.28 a mile in October, matching the May 2022 record, while freight volume fell. From Hoplite's weekly freight brief.") + MENU + f"""<header class="hero">
  <div class="hero-photo"><img src="assets/img/wk47.jpg" alt="A long-nose semi truck on a snowy highway at night"></div>
  {NAV}
  <div class="wrap hero-text">
    <h1 class="headline display">Trucking's sticker price just tied its all-time record, <em>with less freight on the road.</em></h1>
    {meta("November 16, 2026", "6 min read")}
    {tags(47)}
  </div>
</header>
<main>
<div class="wrap intro">
  <p class="standfirst">Contract van rates hit $3.28/mi in October, matching the May 2022 record, while freight volume actually fell. Reefer trucks are turning down one in five loads heading into Thanksgiving, and the national fleet is the smallest it's been since early 2022. This isn't a demand story. It's a scarcity story. And it just became your 2027 budget.</p>
  <nav class="toc" aria-label="In this edition">
    <h2>In this edition</h2>
    <ol>
{toc_html}
    </ol>
  </nav>
</div>

<article class="wrap top-story" id="top-story">
  <h2 class="section display">$3.28 and nobody ordered more freight: why the record matters more than the number.</h2>
  <div class="story-cols">
    <div class="prose">
      {"".join(f"<p>{e(p)}</p>" for p in body)}
    </div>
    <div class="figures">
      {figure("$3.28 a mile", "Van contract. Up 4¢ in October, level with the May 2022 all-time record.")}
      {figure("$3.05 a mile", "Van spot, monthly all-in. Highest since February 2022, up 47% year over year.")}
      {figure("−2% year over year", "Van volume. Reefer is down 9%, flatbed 7%: a record on less freight.")}
    </div>
  </div>
  <div class="our-read">
    <div>
      <p class="line display">May 2022's record took a demand boom. This one took nothing but a shrinking fleet. <em>That's your entire 2027 budget in one sentence.</em></p>
      <p class="assessment"><b>Our read.</b> When a price record prints on shrinking volume, the floor is built out of missing trucks, and no amount of soft demand can knock it down. Carriers will anchor every 2027 quote to $3.28. Don't haggle over the number; change the deal. Rates that float with the market, shorter terms, room to flex your volumes. In a rising market, the shippers who win aren't the ones who found a cheaper price. They're the ones who refused to lock in an expensive one.</p>
    </div>
  </div>
</article>

<div class="wrap stories">
  <article class="story" id="story-2">
    <img class="photo" src="assets/img/story-silos.jpg" alt="A truck on a heartland highway at night, grain silos lit beside the road" loading="lazy">
    <h3 class="display">Turkey season is here, and reefer carriers are saying no to one load in five.</h3>
    <p class="body">Thanksgiving is the Super Bowl of refrigerated trucking, and kickoff just happened. Reefer spot rates jumped 10 cents to $3.70/mi the week of November 9 as holiday food freight hit the road. The number to watch, though, is the rejection rate: how often a carrier looks at a load it already agreed to haul under contract and says "no thanks, I can get paid more elsewhere." Reefer and flatbed rejections are both running 20–21%. One in five. California, where a huge share of holiday food originates, is leading the charge: reefer up 15 cents, dry van up 15 cents, the biggest regional jumps on the board. If you ship anything cold or grocery-adjacent: tender this week, give carriers 48–72 extra hours of notice, and line up a backup before you need one. Pay the premium once, not three times after two loads get handed back.</p>
    <div class="figures two">
      {figure("$3.70 a mile", "Reefer spot. Up 10¢ week over week, week of November 9.")}
      {figure("About 21%", "Reefer rejections: 1 in 5 loads handed back (SONAR, November 13).")}
    </div>
  </article>
  <article class="story" id="story-3">
    <img class="photo" src="assets/img/story-terminal.jpg" alt="A cross-dock terminal at night seen from above, trailers at every door" loading="lazy">
    <h3 class="display">The fleet keeps shrinking, just as the import wave that fed it rolls out.</h3>
    <p class="body">The supply side isn't stabilizing; it's still bleeding. The active truck count is now the lowest since early 2022. Over 1,000 logistics jobs were cut from late October into November, and two more carriers went down in two days: Bruin filed for liquidation November 9, X-Total filed for bankruptcy protection November 10. Meanwhile, the import surge that kept everyone busy is ending on schedule. November container volumes taper to a forecast 2.05M TEU, closing out a record 26M TEU year. Put the two lines together: freight is stepping down, but trucks are stepping down faster. That's how a record rate prints in a cooling market. One practical order of business before you award a single 2027 lane: check your carriers' financial health. The cheapest bid from a carrier that folds in February is the most expensive rate you'll buy all year.</p>
    <div class="figures two">
      {figure("Lowest since early 2022", "Active truck count. 1,021 layoffs and 2 bankruptcies, November 9–10.")}
      {figure("2.05M TEU", "November imports, tapering after a record 26M TEU year.")}
    </div>
  </article>
</div>

<section class="todo deep" id="what-to-do">
  <div class="wrap">
    <h2 class="section display">What to do this week.</h2>
    <p class="lede">Three to do now, two to watch.</p>
    <ol class="actions">
{actions_html}
    </ol>
  </div>
</section>

<section class="wrap market">
  <h2 class="section display">The market in six numbers.</h2>
  <div class="numbers">
{numbers_html}
  </div>
  <p class="sources">Sources: DAT, FreightWaves SONAR, NRF Port Tracker, U.S. Bank, EIA. Compiled by Hoplite Logistics, Minneapolis, MN.</p>
</section>
</main>
""" + SUBSCRIBE + f"""<section class="wrap previous">
  <a class="prev-card" href="{EDITION}">
    <img class="photo" src="assets/img/wk46.jpg" alt="A highway curving into the dusk" loading="lazy">
    <div>
      <p class="small-meta">Previous edition &middot; November 9, 2026</p>
      <h3 class="display">The inversion is over: spot crosses back under contract.</h3>
    </div>
  </a>
  <a class="more orange" href="editions.html">All {COUNT} editions &nbsp;&rarr;</a>
</section>
""" + CLOSING + FOOTER


for name, fn in (("index.html", home), ("editions.html", editions), ("edition.html", edition)):
    (ROOT / name).write_text(fn(), encoding="utf-8")
    print("wrote", name)
