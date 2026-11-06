# Web Design Skill for LLMs

> **Instruction for the AI reading this file:** from now on you are a senior product designer and frontend engineer. Follow this skill whenever the user asks you to build or restyle a website, landing page, dashboard, UI, or app screen. Reply in the language the user writes in. Code, comments and CSS stay in English.

This is context, not training. Apply it to every design task in this conversation. If you can open links, read the modules below on demand; if you cannot, this README is enough for a good result.

## Workflow (always, in this order)

1. **Understand.** Ask at most 2 questions, only if critical (product, audience). Otherwise assume and state assumptions in one line.
2. **Classify the product** with [product-map.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/product-map.md): it gives style, landing pattern (L#), palette (P#), fonts (F#) and anti-patterns. No row fits? Use the nearest of the 192 types in [palettes.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/palettes.md).
3. **Write a Design Brief BEFORE any code**, exactly in this shape:
   - **PATTERN:** name + section order (from landing-patterns.md) + CTA placement
   - **STYLE:** one name + 3-4 keywords + performance/accessibility note
   - **COLORS:** primary, secondary, CTA, background, text, border (hex)
   - **TYPOGRAPHY:** heading / body + Google Fonts link (check the Cyrillic subset for Russian)
   - **KEY EFFECTS:** 2-3 concrete interactions
   - **AVOID:** 3 anti-patterns for this industry
4. **Build** with CSS variables (design tokens) from the brief. Default deliverable: one self-contained `index.html` (HTML + CSS + minimal JS). Use another stack only if the user names it (see [stacks.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/stacks.md)).
5. **Self-check** against the checklist below, fix problems silently, then deliver.
6. **Deliver:** short brief + code + one line on how to tweak tokens. For multi-page work keep a `MASTER` brief (global tokens) and per-page overrides, and re-read it before each page.

## Industry reasoning (how to choose)

| Group | Typical products | Style direction | Palette mood | Never |
|---|---|---|---|---|
| Tech & SaaS | SaaS, dev tools, AI, cybersecurity | Minimal / Bento / Dark premium | cool neutral + one strong accent | purple-pink gradient clichés |
| Finance | fintech, bank, insurance, invoices | Clean trust, Swiss | navy + green | neon, playful shapes |
| Healthcare | clinic, pharmacy, dental, mental health | Calm clean, Soft UI | teal/cyan + green | alarming red, dense text |
| E-commerce | store, luxury, marketplace, delivery | product-first, Dark premium for luxury | brand color + urgency accent | popups on load, autoplay |
| Services | beauty/spa, restaurant, hotel, legal, local services | Soft UI / warm editorial / bold clean | warm neutrals or industry color | dark mode for spa, tiny text |
| Creative | portfolio, agency, photo, gaming, music | Editorial, Neubrutalism, Dark neon | high contrast + one loud accent | template look |
| Lifestyle | habit, recipe, meditation, weather, diary | Soft UI / Minimal / Playful | calm + one accent | gamification overload |
| Emerging | Web3, spatial, quantum, drones | Dark + HUD / Aurora | dark base + cyan/green | fake metrics |

## Hard rules (non-negotiable)

- **Tokens first.** Colors, radii, shadows, spacing live in `:root` variables. No raw hex inside components.
- **Type.** Body 16-18px, line-height 1.5-1.7; headings 1.05-1.2 and fluid with `clamp()`. Max 2 font families (plus mono). 65-75 characters per line. Inputs >= 16px.
- **Spacing.** 8px grid. Sections 80-128px vertical padding on desktop. Whitespace beats decoration.
- **Color.** About 60% background / 30% surface+text / 10% accent. One primary action color. Text contrast >= 4.5:1 (large text and UI 3:1). Never rely on color alone.
- **Hierarchy.** One H1, one primary CTA per viewport, repeat the CTA after proof or pricing.
- **States.** Every interactive element has hover, `:focus-visible`, active, disabled; `cursor:pointer`; visible focus ring.
- **Responsive.** Mobile-first; mentally test 375 / 768 / 1024 / 1440; no horizontal scroll; tap targets >= 44px; text reflows instead of clipping.
- **Motion.** 150-300ms, ease-out; animate `transform`/`opacity` only; max 1-2 animated focal elements per view; respect `prefers-reduced-motion` with a static final state.
- **Icons.** Inline SVG (Lucide/Heroicons style), never emoji as UI icons.
- **Images.** No broken external images. Use CSS gradients, inline SVG, or `<img>` with width/height and `alt`. Without supplied assets, design without photos instead of faking them.
- **Semantics.** `header nav main section footer`, real `<button>`/`<a>`, `<label for>`, `<html lang>`, viewport meta with `viewport-fit=cover`.
- **Honesty.** No fake ratings, counters, scarcity or testimonials; use clearly marked placeholders.
- **Anti-"AI look".** Do not default to: purple-blue gradient hero, three identical emoji feature cards, glowing blobs, centered everything, "Revolutionize your workflow" copy. Commit to a distinct direction from the brief and write real, specific copy.

## Pre-delivery checklist

- [ ] Design Brief written and the code matches it (tokens, fonts, style, pattern)
- [ ] No emoji icons; SVG only; icon-only buttons have `aria-label`
- [ ] All clickable elements have `cursor:pointer` and hover/focus/active states
- [ ] Interaction timing 150-300ms; `prefers-reduced-motion` handled
- [ ] Light mode text contrast >= 4.5:1; focus rings visible; heading order correct
- [ ] Responsive at 375 / 768 / 1024 / 1440 with no horizontal scroll; targets >= 44px
- [ ] Text, chips and badges wrap without clipping; long words and URLs break safely
- [ ] One primary CTA above the fold, repeated after proof; forms have labels and error text
- [ ] Fonts include the needed subset (Cyrillic for Russian) with fallbacks and `display=swap`
- [ ] Copy is specific, no lorem ipsum, no fake proof

## Modules

| Need | File |
|---|---|
| Product recipes (style, landing, palette #, font #, avoid) | [product-map.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/product-map.md) |
| 79 visual styles and CSS recipes | [styles.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/styles.md) |
| 34 page patterns (section order, CTA, effects) | [landing-patterns.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/landing-patterns.md) |
| 192 product palettes + 38 industry palettes | [palettes.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/palettes.md) |
| 74 font pairings, imports, Cyrillic flags | [typography.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/typography.md) |
| 130 UX / accessibility / performance rules | [ux-rules.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/ux-rules.md) |
| Chart choices for dashboards | [charts.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/charts.md) |
| Stack defaults (React, Vue, Tailwind, mobile...) | [stacks.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/modules/stacks.md) |
| Starter prompts for the user (not needed by the model) | [prompts/START.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/prompts/START.md) |
| **Everything in one file** | [dist/FULL.md](https://raw.githubusercontent.com/mintlygit/DeepSeek-UI-UX/main/dist/FULL.md) |


---

# Product recipes: product -> style, landing pattern, palette #, font #

IDs refer to: landing-patterns.md (L#), palettes.md (P#), typography.md (F#). If no row fits, use the nearest product in palettes.md (192 types) and choose style by risk and mood.

| Product | Style (primary + secondary) | Landing L# | Palette P# | Fonts F# | Avoid |
|---|---|---|---|---|---|
| SaaS / B2B | Minimalism + Bento, Glass accents | 1, 28, 8 | 1, 2 | 2, 13, 60 | purple-pink gradients, vague slogans |
| Micro-SaaS / indie tool | Neubrutalism or Flat | 4, 3 | 2 | 3, 20, 53 | long pages |
| Developer tool / API / IDE | Dark Mode First + Minimal | 3, 34 | 81, 163 | 9, 42, 62 | light-gray text on white |
| AI / chatbot product | AI-Native + Aurora (one glow) | 30, 3 | 18 | 3, 70, 60 | robot clip-art, rainbow gradients |
| Fintech / crypto / DeFi | Dark Premium + Glass | 33, 34 | 14, 19 | 36, 31, 70 | scam-style neon overload |
| Banking / insurance / legal | Clean trust + Swiss | 33, 25 | 42, 41, 40 | 31, 16, 29 | AI purple/pink gradients, neon, playful shapes |
| Healthcare / clinic / dental / telemedicine | Soft UI Evolution + Accessible | 2, 32 | 58, 60, 190, 8 | 30, 16, 48 | red-heavy UI, dense walls of text |
| Mental health / meditation | Soft UI + Minimal/Zen | 4, 2 | 22, 98 | 8, 19 | harsh animation, neon |
| Spa / beauty / wellness | Soft UI Evolution | 32, 2 | 32 | 1, 12, 8 | bright neon, dark mode, harsh animation |
| Restaurant / cafe / bakery | Warm editorial | 32, 1 | 34, 63 | 33, 8, 10 | cold blues, tiny menu text |
| Hotel / travel / airline | Editorial + Soft UI | 9, 32, 22 | 38, 37, 65 | 12, 50, 1 | cluttered booking forms |
| Luxury / jewelry / fashion | Dark Premium + Editorial | 32, 26 | 4, 33 | 12, 50, 59 | bright colors, discount banners |
| E-commerce store | Clean product-first + Bento | 22, 19 | 3 | 40, 2 | popups on load, autoplay |
| Marketplace / classifieds / directory | Clean + dense filters | 22 | 48, 171, 165 | 2, 5 | hiding search |
| Portfolio / designer | Editorial or Neubrutalism / Brutalism | 26, 10 | 11, 88 | 44, 18, 57 | template look, equal tiles |
| Photographer / artist / museum | Minimal dark / Editorial Grid | 26 | 53, 76 | 44, 35, 4 | heavy chrome around work |
| Creative / marketing agency | Neubrutalism + Typography-Led | 10, 26 | 10, 69 | 7, 18, 53 | stock team photos |
| Blog / magazine / news | Editorial Grid | 23, 16 | 67, 66 | 14, 35, 4 | crowded sidebars |
| Education / courses / LMS / language | Playful rounded or Clean | 8, 31 | 43, 179, 78, 9 | 6, 45, 40 | low-contrast pastels |
| Kids product / kids learning | Claymorphism + Playful | 32, 15 | 152, 56 | 45, 71, 19 | thin fonts, dark UI |
| Gaming / esports | Dark neon (controlled) / Cyberpunk | 17, 20 | 12, 125 | 37, 36, 69 | neon on all text |
| Music / podcast / streaming | Dark + Bold editorial | 15, 20 | 45, 27, 46 | 43, 63 | unreadable overlays |
| Fitness / sport / gym | Bold, high contrast, Dark | 8, 21 | 35, 140, 75 | 49, 57 | pastel low-energy |
| Real estate | Clean + map/search | 22, 32 | 36 | 32, 2 | clutter, tiny photos |
| Local service / repair / barbershop | Bold clean, sticky call button | 2, 4 | 55, 31 | 2, 7 | no visible phone/booking |
| Wedding / event / invitation | Soft editorial | 18 | 39 | 46, 1, 12 | busy backgrounds |
| Conference / webinar | Clean + Trust | 18, 24 | 172 | 2, 16 | fake scarcity |
| Non-profit / charity / church | Warm editorial / Storytelling | 10, 1 | 44, 74, 170 | 8, 14 | guilt imagery |
| Dashboard / analytics / admin | Data Dense or Clean (dark option) | n/a | 7, 6, 101 | 5, 42, 60 | decorative charts, 3D |
| Mobile app landing | Minimal or Glass + device mockup | 15 | 1, 92 | 2, 13, 64 | fake store ratings |
| Link-in-bio / personal hub | Minimal / Editorial | 4 | 132, 11 | 5, 18 | walls of text |
| Newsletter | Editorial minimal | 23 | 72 | 14, 5 | popups |
| Docs / knowledge base / wiki / changelog | Minimal Swiss | 16 | 30, 167, 169 | 5, 9 | animation for its own sake |
| Status page / feature flags / RPA | Operational Monitor | 34 | 166, 176, 188 | 42, 62 | decorative motion |
| Crypto / NFT / Web3 | Dark Premium + HUD accents | 33, 34 | 19, 14 | 36, 70, 69 | fake yields, scammy glow |
| Cybersecurity | HUD / Dark Terminal | 34, 25 | 80 | 51, 69 | consumer cuteness |
| Space / aerospace / quantum | Dark + Kinetic Typography | 17 | 83, 85 | 56, 36 | cartoonish |
| Automotive / dealership | Dark Premium + Motion | 29, 9 | 52 | 56, 12 | clutter |
| Agriculture / eco / climate | Organic Biophilic + Clean | 1, 10 | 50, 90 | 8, 40 | greenwash clichés |
| Construction / industrial / logistics | Flat bold | 33, 2 | 51, 49 | 49, 2 | consumer pastels |
| Food delivery / grocery | Playful consumer | 15, 22 | 95, 106 | 40, 6 | long forms |
| Dating / social / community | Playful + Vibrant | 20 | 15, 28, 71 | 2, 6 | dark patterns |
| Productivity / notes / habit / calendar apps | Minimal + Soft | 15, 3 | 16, 93, 94, 110 | 13, 5 | gamification overload |
| Resume / invoice / document tools | Clean trust | 3, 8 | 186, 105, 175 | 5, 16 | ornate effects |
| Open-source project | Dark minimal + Bento | 3, 28 | 181 | 9, 5 | corporate stock imagery |

## Industry anti-patterns (quick reference)
- Banking/insurance/legal/government: no neon, no AI purple/pink gradients, no playful illustration, restrained motion.
- Healthcare: no alarming red as primary, no dense text walls, large readable type, calm colors.
- Luxury: no bright colors, no discount banners, big imagery, slow reveals.
- Kids: no thin type, no low-contrast pastels, big radius and targets.
- Crypto/gaming: dark base is fine; glow only on primary action, never on body text.
- Spa/wellness: no harsh animation, no dark mode default.
- Everyone: no emoji as icons, no lorem ipsum, no fake social proof counters.


---

# Visual styles: 79 searchable (50 active), condensed

Pick ONE primary style per project (optionally one secondary). Use tokens. Performance: ⚡ excellent / ⚠ good / ❌ heavy. Accessibility: AAA / AA / ⚠ limited.

## A. General styles (names)
Minimalism & Swiss, Neumorphism, Glassmorphism, Brutalism, 3D & Hyperrealism, Vibrant & Block-based, Dark Mode (OLED), Accessible & Ethical, Claymorphism, Aurora UI, Retro-Futurism, Flat Design, Skeuomorphism, Liquid Glass, Motion-Driven, Micro-interactions, Inclusive Design, Zero Interface, Soft UI Evolution, Neubrutalism, Bento Box Grid, Y2K Aesthetic, Cyberpunk UI, Organic Biophilic, AI-Native UI, Memphis Design, Vaporwave, Dimensional Layering, Exaggerated Minimalism, Kinetic Typography, Parallax Storytelling, Swiss Modernism 2.0, HUD / Sci-Fi FUI, Pixel Art, Spatial UI (visionOS), E-Ink / Paper, Gen Z Chaos / Maximalism, Biomimetic / Organic 2.0, Anti-Polish / Raw, Tactile Digital / Deformable UI, Nature Distilled, Interactive Cursor Design, Voice-First Multimodal, 3D Product Preview, Gradient Mesh / Aurora Evolved, Editorial Grid / Magazine, Chromatic Aberration / RGB Split, Vintage Analog / Retro Film. Also: Material Design 3, Fluent 2, Shopify Polaris, Adobe Spectrum, Liquid Glass (Apple material).

## B. Detailed recipes
| Style | Signature effects (CSS) | Best for | Avoid for |
|---|---|---|---|
| Minimalism / Swiss | grid 12-16 cols, white space, `border-radius:0`, no shadows, sans-serif, single accent, ⚡ AAA | enterprise, SaaS, docs, dashboards | creative/playful brands |
| Swiss Modernism 2.0 | strict grid with column rules, Helvetica/Inter, red #E02424 only accent, type as layout, ⚡ | editorial, agencies, cultural institutions | consumer apps, kids |
| Neumorphism | `box-shadow:-5px -5px 15px rgba(255,255,255,.8), 5px 5px 15px rgba(0,0,0,.1)`, radius 12-16px, pastel mono, ⚠ low contrast | wellness, minimal controls, smart home | data-heavy, accessibility-critical |
| Glassmorphism | `backdrop-filter:blur(15px)`, `rgba(255,255,255,.15)` bg, 1px `rgba(255,255,255,.2)` border, vibrant backdrop, ⚠ | modern SaaS overlays, AI, media | text-heavy, low-end devices |
| Glassmorphism Dark | blur 24px on #0A0A0A, card `rgba(255,255,255,.05)`, neon border at 30% | gaming, media players, AI dark surfaces | long body text |
| Brutalism | `border-radius:0`, no transitions, system/mono fonts, 700+ weight, 2-4px borders, primary colors, ⚡ AAA | portfolios, art, counter-culture | corporate, regulated, healthcare |
| Neubrutalism | 2-3px dark border, hard offset shadow `4px 4px 0 #111`, flat saturated fills, hover color flip | indie SaaS, creative tools, Gen Z | enterprise, finance |
| Flat Design 2.0 | single subtle shadow, vibrant palette, geometric icons, 8pt grid | productivity, docs, dev tools | luxury, entertainment |
| Claymorphism | radius 30-50px, inner highlight + outer soft shadow, pastel, 3-4px borders | kids, lifestyle, gifting | enterprise, precision tools |
| Soft UI Evolution | multi-layer soft shadows, 12-24px radius, calm, better contrast than neumorphism | wellness, beauty, hotels, health | high-density dashboards |
| Dark Mode First | bg #0A0A0A-#121212, surfaces #1C1C1E/#2C2C2E/#3A3A3C, text #F5F5F5, accents desaturated 20%, ⚡ | dev tools, media, gaming | clinical settings, bright kiosks |
| Dark Premium | #0A0A0A canvas, gold #D4AF37/#B8860B or silver accent, display serif 80-120px, 120-200px section rhythm | luxury SaaS, membership, watches, whiskey | mass-market apps |
| AI-Native | gradient mesh bg (3-5 stops), glow border, mono/geometric sans, particles optional ❌ | AI products, dev platforms | traditional enterprise, healthcare |
| Aurora / Gradient Mesh | 4-6 stop mesh at 40-70% opacity, no hard borders, type on gradient | AI landings, creative hero | form-heavy flows, data apps |
| Bento Grid | CSS grid with named areas, cards 1x1 to 3x2, gap 8-16px, radius 12-24px | landing features, dashboards home, portfolios | long-form reading, checkout |
| Editorial Grid | overlapping text/image, headlines 80-120px, serif display, column rules | media, publishing, portfolios | SaaS apps, dashboards |
| Typography-Led | display type 100-200px, tight leading .9-1.1, inverted type color | agencies, foundries, artists | functional apps, e-com |
| Monochromatic Minimal | one hue, lightness 5-97%, no accent | portfolios, luxury identity | multi-action apps, e-com CTA |
| Minimal / Zen | 70%+ whitespace, one accent, thin serif/geometric sans, paper texture 5% | wellness, meditation, authors | feature-dense apps |
| Vaporwave / Retrowave | pink-cyan gradient #FF00FF to #00FFFF, grid lines, scanlines, glow ❌ | gaming, music, nostalgia | finance, healthcare, gov |
| HUD / Sci-Fi FUI | black bg, green/cyan on black, 1px rules, mono, corner brackets ❌ | cybersecurity, aerospace, game UI | consumer products |
| Skeuomorphism 2.0 | material textures, specular highlights, press depth ⚠ | instruments, hardware companion apps | modern SaaS |
| Memphis Revival | geometric patterns, primary color blocking, controlled chaos | Gen Z, playful e-com, campaigns | enterprise, finance |
| Material Design 3 | tonal surfaces from seed color, state layers 8/12/16%, elevation by color | Android-first, Google ecosystem | luxury, editorial |
| Data Dense | 12-13px table text, 4-8px row padding, no cards, tooltips over labels | trading, ops centers, medical records | consumer, mobile |
| Executive Dashboard | KPI numbers 48-64px, 3-state status colors, sparklines, max 6 KPIs | C-suite, board packs | ops monitoring, exploration |
| Operational Monitor | live status dots, rolling mono log, alert banner, incident timeline, dark | DevOps, NOC, on-call | executive reporting |
| Data Storytelling | finding as header, chart below, annotations, 640-720px column | insight reports, journalism | self-serve exploration |
| Conversion-First | CTA above fold, social proof within 2 scrolls, sticky mobile CTA, benefits over features | lead-gen, trials, launches | editorial, docs |
| Story-Scroll | IntersectionObserver fades, chapters, progress indicator, full-bleed imagery | brand launches, annual reports | high-conversion pages |
| Trust-Builder | logo strip, real-photo testimonials, SOC2/ISO badges, security copy near forms | B2B SaaS, fintech onboarding | consumer social, dev tools |
| Playful Consumer | radius 24-32px, emoji in headings, confetti on success, spring bounce | consumer apps, food delivery | enterprise, finance, health |

## C. Dashboard styles (BI)
Data-Dense, Heat Map, Executive, Real-Time Monitoring, Drill-Down, Comparative, Predictive (forecast + confidence intervals), User Behavior (funnels, flows), Financial (P&L, budget), Sales Intelligence (pipeline), Grid/Matrix (sticky headers, zebra), Graph/Network (force layout), Geospatial (map-first), Timeline-First, Comparison View, Mobile Analytics (horizontal bars, bottom sheets, 48px targets).

## D. Selection rules
- Performance ⚡: Minimalism, Flat, Brutalism, Accessible, Dark OLED. ❌ heavy: 3D/WebGL, Liquid Glass, Motion-Driven, Skeuomorphism.
- Accessibility AAA: Minimalism, Accessible & Ethical, Inclusive, Brutalism. Limited: Neumorphism, 3D, Skeuomorphism, Liquid Glass.
- Match style to risk: regulated/trust products (finance, health, legal, gov) use Clean trust, Swiss, Minimalism, Flat; never neon, vaporwave, memphis, AI purple/pink gradients.
- Conflicting pairs to avoid: glassmorphism on flat white; neumorphism + dense data; brutalism + banking.


---

# Landing / page patterns: 34

Format: id | pattern | section order | CTA | color | effects | rule. Pick by goal and product type.

1. **Hero + Features + CTA**: Hero (headline/image) > value prop > 3-5 key features > CTA > footer. CTA: sticky in hero + bottom. Hero brand/vibrant, cards #FAFAFA, CTA contrasting. FX: hero parallax, card hover lift, CTA glow. Rule: deep CTA placement; CTA label text 4.5:1 on button; parallax off under reduced motion.
2. **Hero + Testimonials + CTA**: Hero > problem > solution > testimonials carousel > CTA. CTA after social proof. Quotes italic muted #666. Rule: verified testimonials with photo, name, role; carousel needs prev/next + pause, stops on focus/hover/reduced motion, announces position.
3. **Product Demo + Features**: Hero > product video/mockup (center) > feature breakdown > optional comparison > CTA. Rule: demo only if it explains value better than static media; captions, transcript, visible play/pause, non-video fallback; no autoplay under reduced motion.
4. **Minimal Single Column**: headline > short description > up to 3 benefit bullets > one large CTA > footer. Lots of whitespace, no nav clutter, mobile-first.
5. **Funnel (3-step)**: Hero > step 1 problem > step 2 solution > step 3 action, mini-CTA per step. Progress indicator, progressive disclosure.
6. **Comparison Table + CTA**: Hero > problem > comparison table (you vs competitors) > optional pricing > CTA below table. Highlight your row; mention free trial.
7. **Lead Magnet + Form**: benefit headline > magnet preview (ebook/checklist) > minimal form > submit CTA. Ask only what is needed; show progress on submit.
8. **Pricing Page + CTA**: pricing headline > plan cards > feature table > FAQ > final CTA; sticky CTA in nav. Highlight the plan for the target audience; show real annual savings; FAQ handles objections.
9. **Video-First Hero**: video background > feature overlay > benefits > CTA. Overlay strong enough for text contrast; captions, visible pause, static poster under reduced motion; pause when offscreen.
10. **Scroll-Triggered Storytelling**: hook > chapter 1 problem > chapter 2 journey > chapter 3 solution > climax CTA; mini-CTA per chapter. Understandable without scroll effects; progress indicator; complete DOM reading order; simplify on mobile.
11. **AI Personalization Landing**: dynamic hero > relevant features > tailored testimonials > smart CTA. Needs consent-aware analytics and fallback for new users.
12. **Waitlist / Coming Soon**: hero with countdown > teaser > email capture > social proof. Form above fold + sticky; no fabricated scarcity; show waitlist count only if verified and dated; static deadline as text.
13. **Comparison Table Focus**: problem hero > comparison matrix > feature deep-dive > winner CTA. Be factual; your column highlighted; sticky header.
14. **Pricing-Focused Landing**: value hero > 3 pricing cards > feature comparison > FAQ > final CTA. Popular plan highlighted; free grey, enterprise dark; transparent totals.
15. **App Store Style**: hero with device mockup > screenshot carousel > feature icons > reviews/ratings > download CTAs (App Store + Google Play) throughout. Real screenshots and verified ratings only; buttons as well as swipe; stop auto-rotation on focus/reduced motion.
16. **FAQ / Documentation**: hero with search bar > popular categories > FAQ accordion > contact CTA. High readability, search autocomplete, helpful-feedback buttons, escalation path.
17. **Immersive / Interactive**: full-screen interactive element > guided tour > benefits > CTA after completion; skip option. Provide skip, keyboard, reduced-motion and non-3D fallback.
18. **Event / Conference**: hero (date, place, countdown) > speakers > agenda > sponsors > Register CTA (sticky + after speakers + bottom). Early-bird deadline as text; static final state for countdown.
19. **Product Review / Ratings**: hero with aggregate rating > rating breakdown > reviews > buy CTA. Verified purchases badge, filters, respond to negatives.
20. **Community / Forum**: value prop > popular topics > active members > Join CTA. Counts only if verified and dated; pause controls for live feeds.
21. **Before-After Transformation**: problem state > slider comparison > how it works > results CTA. Arrow buttons + keyboard steps (no drag-only); real metrics.
22. **Marketplace / Directory**: search-focused hero > categories > featured listings > trust/safety > "become a seller/host" CTA. Search is the primary CTA; carousels with prev/next + pause.
23. **Newsletter / Content First**: value prop + inline form > recent issues > subscriber count (only if verified) > author. Minimal, paper-like background, link a sample issue.
24. **Webinar Registration**: topic + timer + form > what you'll learn > speaker > bonuses > form again. State time + timezone as text; claim limited seats only if verified; pause for tickers.
25. **Enterprise Gateway**: mission/video hero > solutions by industry > by role > client logos > Contact Sales (+ Login secondary). Navy/grey, path selection "I am a...", pause for rotating logos.
26. **Portfolio Grid**: name/role > masonry project grid > about > contact. Neutral bg so work shines; filter by category; fast loading; hover overlay + lightbox.
27. **Horizontal Scroll Journey**: vertical intro > horizontal track > detail reveal > vertical footer. Keep a normal vertical navigation path; disable scroll-jacking under reduced motion.
28. **Bento Grid Showcase**: hero > bento grid of features > detail cards > specs > CTA. Cards #F5F5F7 or glass, hover scale 1.02; usable without hover; stack on mobile.
29. **Interactive 3D Configurator**: configurator hero > synced feature highlight > price/specs > purchase. Buttons + keyboard for rotate/zoom, 2D/spec fallback.
30. **AI-Driven Dynamic Landing**: prompt/input hero > generated result preview > how it works > value prop. "Show, don't tell", low-friction start; disable typing/shimmer under reduced motion.
31. **Feature-Rich Showcase**: hero > 4-6 feature cards > use cases/benefits > social proof/logos > CTA. One message per card; repeat CTA.
32. **Hero-Centric Design**: full-bleed hero > single value strip > key proof > primary CTA. One CTA; keep a cue to next content; static hero under reduced motion.
33. **Trust & Authority + Conversion**: mission/credibility hero > proof (logos, certs, stats) > solution > CTA path. Contact Sales/Get Quote; security badges, case studies, transparent pricing.
34. **Real-Time / Operations Landing**: hero with live preview/status > key metrics > how it works > CTA (trial/contact). Label "live" only if backed by a current source; show update time; pause controls.

## Section rules (all patterns)
- One idea and one heading per section; alternate dense and airy sections.
- Proof (numbers, logos, quotes) near every CTA; no fake counters, ratings or urgency.
- Footer has navigation, legal, contact.
- Motion must have a static final state under `prefers-reduced-motion`.


---

# Palettes: 192 product types (hex)

How to use: find the closest product row, take its colors, then shift hue ±10-15° or tweak lightness so the brand is not generic. `CTA` is the accent for the main action button. Dark rows have a dark Bg.
Derive the rest: card = #FFF on light bg or bg lightened 4-6% on dark; muted = bg tinted; border = see Bg family (light: ~#E2E8F0 tint, dark: rgb(255 255 255 / .08-.15)); destructive = #DC2626 (light) / #EF4444 (dark); text on a colored button must reach 4.5:1 (white or #0F172A). Always verify contrast.

| # | Product | Primary | Secondary | CTA | Bg | Text |
|---|---|---|---|---|---|---|
| 1 | SaaS (general) | #2563EB | #3B82F6 | #EA580C | #F8FAFC | #1E293B |
| 2 | Micro SaaS | #6366F1 | #818CF8 | #059669 | #F5F3FF | #1E1B4B |
| 3 | E-commerce | #059669 | #10B981 | #EA580C | #ECFDF5 | #064E3B |
| 4 | E-commerce luxury | #1C1917 | #44403C | #A16207 | #FAFAF9 | #0C0A09 |
| 5 | B2B service | #0F172A | #334155 | #0369A1 | #F8FAFC | #020617 |
| 6 | Financial dashboard (dark) | #0F172A | #1E293B | #22C55E | #020617 | #F8FAFC |
| 7 | Analytics dashboard | #1E40AF | #3B82F6 | #D97706 | #F8FAFC | #1E3A8A |
| 8 | Healthcare app | #0891B2 | #22D3EE | #059669 | #ECFEFF | #164E63 |
| 9 | Educational app | #4F46E5 | #818CF8 | #EA580C | #EEF2FF | #1E1B4B |
| 10 | Creative agency | #EC4899 | #F472B6 | #0891B2 | #FDF2F8 | #831843 |
| 11 | Portfolio / personal | #18181B | #3F3F46 | #2563EB | #FAFAFA | #09090B |
| 12 | Gaming (dark) | #7C3AED | #A78BFA | #F43F5E | #0F0F23 | #E2E8F0 |
| 13 | Government / public service | #0F172A | #334155 | #0369A1 | #F8FAFC | #020617 |
| 14 | Fintech / crypto (dark) | #F59E0B | #FBBF24 | #8B5CF6 | #0F172A | #F8FAFC |
| 15 | Social media app | #E11D48 | #FB7185 | #2563EB | #FFF1F2 | #881337 |
| 16 | Productivity tool | #0D9488 | #14B8A6 | #EA580C | #F0FDFA | #134E4A |
| 17 | Design system / components | #4F46E5 | #6366F1 | #EA580C | #EEF2FF | #312E81 |
| 18 | AI / chatbot platform | #7C3AED | #A78BFA | #0891B2 | #FAF5FF | #1E1B4B |
| 19 | NFT / Web3 (dark) | #8B5CF6 | #A78BFA | #FBBF24 | #0F0F23 | #F8FAFC |
| 20 | Creator economy | #EC4899 | #F472B6 | #EA580C | #FDF2F8 | #831843 |
| 21 | Remote work / collaboration | #6366F1 | #818CF8 | #059669 | #F5F3FF | #312E81 |
| 22 | Mental health app | #8B5CF6 | #C4B5FD | #059669 | #FAF5FF | #4C1D95 |
| 23 | Pet tech | #F97316 | #FB923C | #2563EB | #FFF7ED | #9A3412 |
| 24 | Smart home / IoT (dark) | #1E293B | #334155 | #22C55E | #0F172A | #F8FAFC |
| 25 | EV / charging | #0891B2 | #22D3EE | #16A34A | #ECFEFF | #164E63 |
| 26 | Subscription box | #D946EF | #E879F9 | #EA580C | #FDF4FF | #86198F |
| 27 | Podcast (dark) | #1E1B4B | #312E81 | #F97316 | #0F0F23 | #F8FAFC |
| 28 | Dating app | #E11D48 | #FB7185 | #EA580C | #FFF1F2 | #881337 |
| 29 | Micro-credentials / badges | #0369A1 | #0EA5E9 | #A16207 | #F0F9FF | #0C4A6E |
| 30 | Knowledge base / docs | #475569 | #64748B | #2563EB | #F8FAFC | #1E293B |
| 31 | Hyperlocal services | #059669 | #10B981 | #EA580C | #ECFDF5 | #064E3B |
| 32 | Beauty / spa / wellness | #EC4899 | #F9A8D4 | #8B5CF6 | #FDF2F8 | #831843 |
| 33 | Luxury / premium brand | #1C1917 | #44403C | #A16207 | #FAFAF9 | #0C0A09 |
| 34 | Restaurant / food service | #DC2626 | #F87171 | #A16207 | #FEF2F2 | #450A0A |
| 35 | Fitness / gym (dark) | #F97316 | #FB923C | #22C55E | #1F2937 | #F8FAFC |
| 36 | Real estate / property | #0F766E | #14B8A6 | #0369A1 | #F0FDFA | #134E4A |
| 37 | Travel / tourism | #0EA5E9 | #38BDF8 | #EA580C | #F0F9FF | #0C4A6E |
| 38 | Hotel / hospitality | #1E3A8A | #3B82F6 | #A16207 | #F8FAFC | #1E40AF |
| 39 | Wedding / event planning | #DB2777 | #F472B6 | #A16207 | #FDF2F8 | #831843 |
| 40 | Legal services | #1E3A8A | #1E40AF | #B45309 | #F8FAFC | #0F172A |
| 41 | Insurance | #0369A1 | #0EA5E9 | #16A34A | #F0F9FF | #0C4A6E |
| 42 | Banking / traditional finance | #0F172A | #1E3A8A | #A16207 | #F8FAFC | #020617 |
| 43 | Online course / e-learning | #0D9488 | #2DD4BF | #EA580C | #F0FDFA | #134E4A |
| 44 | Non-profit / charity | #0891B2 | #22D3EE | #EA580C | #ECFEFF | #164E63 |
| 45 | Music streaming (dark) | #1E1B4B | #4338CA | #22C55E | #0F0F23 | #F8FAFC |
| 46 | Video streaming / OTT (dark) | #0F0F23 | #1E1B4B | #E11D48 | #000000 | #F8FAFC |
| 47 | Job board / recruitment | #0369A1 | #0EA5E9 | #16A34A | #F0F9FF | #0C4A6E |
| 48 | Marketplace (P2P) | #7C3AED | #A78BFA | #16A34A | #FAF5FF | #4C1D95 |
| 49 | Logistics / delivery | #2563EB | #3B82F6 | #EA580C | #EFF6FF | #1E40AF |
| 50 | Agriculture / farm tech | #15803D | #22C55E | #A16207 | #F0FDF4 | #14532D |
| 51 | Construction / architecture | #64748B | #94A3B8 | #EA580C | #F8FAFC | #334155 |
| 52 | Automotive / dealership | #1E293B | #334155 | #DC2626 | #F8FAFC | #0F172A |
| 53 | Photography studio (dark) | #18181B | #27272A | #F8FAFC | #000000 | #FAFAFA |
| 54 | Coworking space | #F59E0B | #FBBF24 | #2563EB | #FFFBEB | #78350F |
| 55 | Home services (plumber, electrician) | #1E40AF | #3B82F6 | #EA580C | #EFF6FF | #1E3A8A |
| 56 | Childcare / daycare | #F472B6 | #FBCFE8 | #16A34A | #FDF2F8 | #9D174D |
| 57 | Senior care | #0369A1 | #38BDF8 | #16A34A | #F0F9FF | #0C4A6E |
| 58 | Medical clinic | #0891B2 | #22D3EE | #16A34A | #F0FDFA | #134E4A |
| 59 | Pharmacy | #15803D | #22C55E | #0369A1 | #F0FDF4 | #14532D |
| 60 | Dental practice | #0EA5E9 | #38BDF8 | #0EA5E9 | #F0F9FF | #0C4A6E |
| 61 | Veterinary clinic | #0D9488 | #14B8A6 | #EA580C | #F0FDFA | #134E4A |
| 62 | Florist / plant shop | #15803D | #22C55E | #EC4899 | #F0FDF4 | #14532D |
| 63 | Bakery / cafe | #92400E | #B45309 | #92400E | #FEF3C7 | #78350F |
| 64 | Brewery / winery | #7C2D12 | #B91C1C | #A16207 | #FEF2F2 | #450A0A |
| 65 | Airline | #1E3A8A | #3B82F6 | #EA580C | #EFF6FF | #1E40AF |
| 66 | News / media | #DC2626 | #EF4444 | #1E40AF | #FEF2F2 | #450A0A |
| 67 | Magazine / blog | #18181B | #3F3F46 | #EC4899 | #FAFAFA | #09090B |
| 68 | Freelancer platform | #6366F1 | #818CF8 | #16A34A | #EEF2FF | #312E81 |
| 69 | Marketing agency | #EC4899 | #F472B6 | #0891B2 | #FDF2F8 | #831843 |
| 70 | Event management | #7C3AED | #A78BFA | #EA580C | #FAF5FF | #4C1D95 |
| 71 | Membership / community | #7C3AED | #A78BFA | #16A34A | #FAF5FF | #4C1D95 |
| 72 | Newsletter platform | #0369A1 | #0EA5E9 | #EA580C | #F0F9FF | #0C4A6E |
| 73 | Digital products / downloads | #6366F1 | #818CF8 | #16A34A | #EEF2FF | #312E81 |
| 74 | Church / religious org | #7C3AED | #A78BFA | #A16207 | #FAF5FF | #4C1D95 |
| 75 | Sports team / club | #DC2626 | #EF4444 | #DC2626 | #FEF2F2 | #7F1D1D |
| 76 | Museum / gallery | #18181B | #27272A | #18181B | #FAFAFA | #09090B |
| 77 | Theater / cinema (dark) | #1E1B4B | #312E81 | #CA8A04 | #0F0F23 | #F8FAFC |
| 78 | Language learning | #4F46E5 | #818CF8 | #16A34A | #EEF2FF | #312E81 |
| 79 | Coding bootcamp (dark) | #0F172A | #1E293B | #22C55E | #020617 | #F8FAFC |
| 80 | Cybersecurity (dark) | #00FF41 | #0D0D0D | #FF3333 | #000000 | #E0E0E0 |
| 81 | Developer tool / IDE (dark) | #1E293B | #334155 | #22C55E | #0F172A | #F8FAFC |
| 82 | Biotech / life sciences | #0EA5E9 | #0284C7 | #059669 | #F0F9FF | #0C4A6E |
| 83 | Space tech / aerospace (dark) | #F8FAFC | #94A3B8 | #3B82F6 | #0B0B10 | #F8FAFC |
| 84 | Architecture / interior | #171717 | #404040 | #A16207 | #FFFFFF | #171717 |
| 85 | Quantum computing (dark) | #00FFFF | #7B61FF | #FF00FF | #050510 | #E0E0FF |
| 86 | Biohacking / longevity | #FF4D4D | #4D94FF | #059669 | #F5F5F7 | #1C1C1E |
| 87 | Drone fleet manager (dark) | #00FF41 | #008F11 | #FF3333 | #0D1117 | #E6EDF3 |
| 88 | Generative art platform | #18181B | #3F3F46 | #EC4899 | #FAFAFA | #09090B |
| 89 | Spatial computing app | #FFFFFF | #E5E5E5 | #FFFFFF | #888888 | #000000 |
| 90 | Sustainable energy / climate | #059669 | #10B981 | #059669 | #ECFDF5 | #064E3B |
| 91 | Personal finance tracker (dark) | #1E40AF | #3B82F6 | #059669 | #0F172A | #FFFFFF |
| 92 | Chat / messaging app | #2563EB | #6366F1 | #059669 | #FFFFFF | #0F172A |
| 93 | Notes / writing app | #78716C | #A8A29E | #D97706 | #FFFBEB | #0F172A |
| 94 | Habit tracker | #D97706 | #F59E0B | #059669 | #FFFBEB | #0F172A |
| 95 | Food delivery | #EA580C | #F97316 | #2563EB | #FFF7ED | #0F172A |
| 96 | Ride hailing (dark) | #1E293B | #334155 | #2563EB | #0F172A | #FFFFFF |
| 97 | Recipe / cooking app | #9A3412 | #C2410C | #059669 | #FFFBEB | #0F172A |
| 98 | Meditation / mindfulness | #7C3AED | #8B5CF6 | #059669 | #FAF5FF | #0F172A |
| 99 | Weather app | #0284C7 | #0EA5E9 | #F59E0B | #F0F9FF | #0F172A |
| 100 | Diary / journal | #92400E | #A16207 | #6366F1 | #FFFBEB | #0F172A |
| 101 | CRM / client management | #2563EB | #3B82F6 | #059669 | #F8FAFC | #0F172A |
| 102 | Inventory / stock | #334155 | #475569 | #059669 | #F8FAFC | #0F172A |
| 103 | Flashcards / study | #7C3AED | #8B5CF6 | #059669 | #FAF5FF | #0F172A |
| 104 | Booking / appointment | #0284C7 | #0EA5E9 | #059669 | #F0F9FF | #0F172A |
| 105 | Invoice / billing | #1E3A5F | #2563EB | #059669 | #F8FAFC | #0F172A |
| 106 | Grocery / shopping list | #059669 | #10B981 | #D97706 | #ECFDF5 | #0F172A |
| 107 | Timer / pomodoro (dark) | #DC2626 | #EF4444 | #059669 | #0F172A | #FFFFFF |
| 108 | Parenting / baby tracker | #EC4899 | #F472B6 | #0284C7 | #FDF2F8 | #0F172A |
| 109 | Scanner / document manager | #1E293B | #334155 | #2563EB | #F8FAFC | #0F172A |
| 110 | Calendar / scheduling | #2563EB | #3B82F6 | #059669 | #F8FAFC | #0F172A |
| 111 | Password manager (dark) | #1E3A5F | #334155 | #059669 | #0F172A | #FFFFFF |
| 112 | Expense splitter | #059669 | #10B981 | #DC2626 | #F8FAFC | #0F172A |
| 113 | Voice recorder / memo | #DC2626 | #EF4444 | #2563EB | #FFFFFF | #0F172A |
| 114 | Bookmark / read-later | #D97706 | #F59E0B | #2563EB | #FFFBEB | #0F172A |
| 115 | Translator | #2563EB | #0891B2 | #EA580C | #F8FAFC | #0F172A |
| 116 | Calculator / converter (dark) | #EA580C | #F97316 | #2563EB | #1C1917 | #FFFFFF |
| 117 | Alarm / world clock (dark) | #D97706 | #F59E0B | #6366F1 | #0F172A | #FFFFFF |
| 118 | File manager / transfer | #2563EB | #3B82F6 | #D97706 | #F8FAFC | #0F172A |
| 119 | Email client | #2563EB | #3B82F6 | #DC2626 | #FFFFFF | #0F172A |
| 120 | Casual puzzle game | #EC4899 | #8B5CF6 | #F59E0B | #FDF2F8 | #0F172A |
| 121 | Trivia / quiz game | #2563EB | #7C3AED | #F59E0B | #EFF6FF | #0F172A |
| 122 | Card / board game (dark) | #15803D | #166534 | #D97706 | #0F172A | #FFFFFF |
| 123 | Idle / clicker game | #D97706 | #F59E0B | #7C3AED | #FFFBEB | #0F172A |
| 124 | Word / crossword game | #15803D | #059669 | #D97706 | #FFFFFF | #0F172A |
| 125 | Arcade / retro game (dark) | #DC2626 | #2563EB | #22C55E | #0F172A | #FFFFFF |
| 126 | Photo editor (dark) | #7C3AED | #6366F1 | #0891B2 | #0F172A | #FFFFFF |
| 127 | Short video editor (dark) | #EC4899 | #DB2777 | #2563EB | #0F172A | #FFFFFF |
| 128 | Drawing canvas (dark) | #7C3AED | #8B5CF6 | #0891B2 | #1C1917 | #FFFFFF |
| 129 | Beat maker (dark) | #7C3AED | #6366F1 | #22C55E | #0F172A | #FFFFFF |
| 130 | Meme / sticker maker | #EC4899 | #F59E0B | #2563EB | #FFFFFF | #0F172A |
| 131 | AI photo / avatar generator | #7C3AED | #6366F1 | #EC4899 | #FAF5FF | #0F172A |
| 132 | Link-in-bio builder | #2563EB | #7C3AED | #EC4899 | #FFFFFF | #0F172A |
| 133 | Wardrobe / outfit planner | #BE185D | #EC4899 | #D97706 | #FDF2F8 | #0F172A |
| 134 | Plant care tracker | #15803D | #059669 | #D97706 | #F0FDF4 | #0F172A |
| 135 | Book / reading tracker | #78716C | #92400E | #D97706 | #FFFBEB | #0F172A |
| 136 | Couple / relationship app | #BE185D | #EC4899 | #DC2626 | #FDF2F8 | #0F172A |
| 137 | Family calendar / chores | #2563EB | #059669 | #D97706 | #F8FAFC | #0F172A |
| 138 | Mood tracker | #7C3AED | #6366F1 | #D97706 | #FAF5FF | #0F172A |
| 139 | Gift / wishlist | #DC2626 | #D97706 | #EC4899 | #FFF1F2 | #0F172A |
| 140 | Running / cycling GPS (dark) | #EA580C | #F97316 | #059669 | #0F172A | #FFFFFF |
| 141 | Yoga / stretching | #6B7280 | #78716C | #0891B2 | #F5F5F0 | #0F172A |
| 142 | Sleep tracker (dark) | #4338CA | #6366F1 | #7C3AED | #0F172A | #FFFFFF |
| 143 | Calorie / nutrition | #059669 | #10B981 | #EA580C | #ECFDF5 | #0F172A |
| 144 | Period / cycle tracker | #BE185D | #EC4899 | #7C3AED | #FDF2F8 | #0F172A |
| 145 | Medication reminder | #0284C7 | #0891B2 | #DC2626 | #F0F9FF | #0F172A |
| 146 | Water / hydration | #0284C7 | #06B6D4 | #0891B2 | #F0F9FF | #0F172A |
| 147 | Fasting timer (dark) | #6366F1 | #4338CA | #059669 | #0F172A | #FFFFFF |
| 148 | Anonymous community (dark) | #475569 | #334155 | #0891B2 | #0F172A | #FFFFFF |
| 149 | Local events / discovery | #EA580C | #F97316 | #2563EB | #FFF7ED | #0F172A |
| 150 | Study together / virtual coworking | #2563EB | #3B82F6 | #059669 | #F8FAFC | #0F172A |
| 151 | Coding challenge (dark) | #22C55E | #059669 | #D97706 | #0F172A | #FFFFFF |
| 152 | Kids learning (ABC, math) | #2563EB | #F59E0B | #EC4899 | #EFF6FF | #0F172A |
| 153 | Music instrument learning | #DC2626 | #9A3412 | #D97706 | #FFFBEB | #0F172A |
| 154 | Parking finder | #2563EB | #059669 | #DC2626 | #F0F9FF | #0F172A |
| 155 | Public transit guide | #2563EB | #0891B2 | #EA580C | #F8FAFC | #0F172A |
| 156 | Road trip planner | #EA580C | #0891B2 | #D97706 | #FFF7ED | #0F172A |
| 157 | VPN / privacy tool (dark) | #1E3A5F | #334155 | #22C55E | #0F172A | #FFFFFF |
| 158 | Emergency SOS / safety | #DC2626 | #EF4444 | #2563EB | #FFF1F2 | #0F172A |
| 159 | Wallpaper / theme app | #7C3AED | #EC4899 | #2563EB | #FAF5FF | #0F172A |
| 160 | White noise / ambient (dark) | #475569 | #334155 | #4338CA | #0F172A | #FFFFFF |
| 161 | Home decoration / interior | #78716C | #A8A29E | #D97706 | #FAF5F2 | #0F172A |
| 162 | Academic journal | #1E3A5F | #334155 | #B45309 | #F8FAFC | #0F172A |
| 163 | API developer portal (dark) | #0F172A | #1E293B | #22C55E | #020617 | #F8FAFC |
| 164 | Forum / discussion board | #475569 | #64748B | #2563EB | #F8FAFC | #1E293B |
| 165 | Directory / listing site | #059669 | #10B981 | #D97706 | #ECFDF5 | #064E3B |
| 166 | Status page / incidents | #16A34A | #22C55E | #DC2626 | #F0FDF4 | #14532D |
| 167 | Wiki / encyclopedia | #1E3A8A | #3B82F6 | #7C3AED | #F8FAFC | #1E40AF |
| 168 | Auction platform (dark) | #0F172A | #1E293B | #16A34A | #020617 | #F8FAFC |
| 169 | Changelog / release notes | #475569 | #64748B | #059669 | #F8FAFC | #1E293B |
| 170 | Citizen science | #15803D | #22C55E | #D97706 | #F0FDF4 | #14532D |
| 171 | Classifieds / buy-sell | #2563EB | #3B82F6 | #16A34A | #EFF6FF | #1E40AF |
| 172 | Conference / symposium | #1E3A5F | #2563EB | #A16207 | #F8FAFC | #0F172A |
| 173 | Crowdfunding | #D97706 | #F59E0B | #16A34A | #FFFBEB | #0F172A |
| 174 | Digital signage / kiosk (dark) | #0F172A | #1E293B | #EF4444 | #020617 | #F8FAFC |
| 175 | E-signature / document workflow | #1E3A5F | #2563EB | #16A34A | #F8FAFC | #0F172A |
| 176 | Feature flags / config (dark) | #0F172A | #1E293B | #16A34A | #020617 | #F8FAFC |
| 177 | Government portal / civic services | #1E40AF | #3B82F6 | #16A34A | #EFF6FF | #1E3A8A |
| 178 | Grant / funding portal | #1E3A5F | #2563EB | #16A34A | #F8FAFC | #0F172A |
| 179 | LMS | #0D9488 | #2DD4BF | #D97706 | #F0FDFA | #134E4A |
| 180 | No-code / low-code builder | #7C3AED | #A78BFA | #EC4899 | #FAF5FF | #4C1D95 |
| 181 | Open source project landing (dark) | #0F172A | #1E293B | #A16207 | #020617 | #F8FAFC |
| 182 | Patient portal / health records | #0284C7 | #0891B2 | #16A34A | #F0F9FF | #0C4A6E |
| 183 | Patent / IP database | #475569 | #64748B | #A16207 | #F8FAFC | #1E293B |
| 184 | Q&A community | #2563EB | #0891B2 | #D97706 | #F8FAFC | #0F172A |
| 185 | Research lab / university dept | #1E3A5F | #2563EB | #A16207 | #F8FAFC | #0F172A |
| 186 | Resume / CV builder | #1E3A5F | #2563EB | #16A34A | #F8FAFC | #0F172A |
| 187 | Review platform | #F59E0B | #FBBF24 | #16A34A | #FFFBEB | #0F172A |
| 188 | RPA / automation dashboard (dark) | #0F172A | #1E293B | #16A34A | #020617 | #F8FAFC |
| 189 | Survey / form builder | #0D9488 | #2DD4BF | #D97706 | #F0FDFA | #134E4A |
| 190 | Telemedicine | #0891B2 | #22D3EE | #16A34A | #F0FDFA | #134E4A |
| 191 | Testimonial / social-proof widget | #7C3AED | #A78BFA | #F59E0B | #FAF5FF | #4C1D95 |
| 192 | Ticketing / box office (dark) | #0F172A | #1E293B | #16A34A | #020617 | #F8FAFC |

## Industry vertical palettes (full roles, light mode baselines)
Use when a product spans verticals: anchor on the main revenue vertical, borrow the accent from the second. Format: Primary / Secondary / Accent / Bg / Foreground / Border / Destructive.

| Vertical | Primary | Secondary | Accent | Bg | Fg | Border | Why |
|---|---|---|---|---|---|---|---|
| Fintech / banking | #1A56DB | #0E9F6E | #F05252 | #F9FAFB | #111928 | #E5E7EB | navy trust, green for positive states |
| Healthcare / medical | #0E9F6E | #1A56DB | #FF8A4C | #F9FAFB | #111928 | #E5E7EB | clinical green, no alarming red as primary |
| SaaS / B2B tools | #6875F5 | #0E9F6E | #F05252 | #FFFFFF | #111928 | #E5E7EB | periwinkle: calm, not boring blue |
| E-commerce / retail | #D97706 | #1A56DB | #E02424 | #FFFFFF | #111928 | #E5E7EB | amber urgency, blue for payment trust |
| Gaming / entertainment (dark) | #7E3AF2 | #FF8A4C | #F05252 | #111928 | #F9FAFB | #4B5563 | deep violet on near-black |
| Social / community | #3F83F8 | #0E9F6E | #F05252 | #FFFFFF | #111928 | #E5E7EB | friendly blue, green for online |
| Developer tools | #0F172A | #6875F5 | #22D3EE | #F8FAFC | #0F172A | #CBD5E1 | near-black precision, cyan pop |
| EdTech / learning | #FF8A4C | #6875F5 | #0E9F6E | #FFFBEB | #111928 | #FDE68A | warm amber, energizing |
| Legal / compliance | #1E3A5F | #374151 | #B45309 | #F9FAFB | #111928 | #D1D5DB | gravity, no bright colors |
| HR / people ops | #7E3AF2 | #FF8A4C | #0E9F6E | #FAF5FF | #111928 | #E9D5FF | authority + empathy |
| Real estate | #065F46 | #1A56DB | #B45309 | #F9FAFB | #111928 | #E5E7EB | forest green, avoid cliché red |
| Travel / hospitality | #1A56DB | #0E9F6E | #FF8A4C | #EFF6FF | #111928 | #BFDBFE | sky blue + warm accent |
| Food / delivery | #D97706 | #E02424 | #0E9F6E | #FFFBEB | #111928 | #FDE68A | appetite amber |
| Fitness / wellness | #047857 | #1A56DB | #F05252 | #F0FDF4 | #111928 | #BBF7D0 | vital green |
| Non-profit / NGO | #065F46 | #D97706 | #1A56DB | #F9FAFB | #111928 | #E5E7EB | earthy, not corporate |
| Government / civic | #1E3A5F | #374151 | #D97706 | #F9FAFB | #111928 | #D1D5DB | navy by convention |
| Luxury / fashion | #111928 | #374151 | #B45309 | #FFFFFF | #111928 | #E5E7EB | minimum color, maximum status |
| Media / publishing | #111928 | #E02424 | #D97706 | #FFFFFF | #111928 | #E5E7EB | ink on paper + editorial red |
| Analytics / BI | #1A56DB | #0E9F6E | #FF8A4C | #F9FAFB | #111928 | #E5E7EB | data is the hero |
| AI / ML platform (dark) | #4F46E5 | #7E3AF2 | #22D3EE | #0F172A | #F8FAFC | #475569 | indigo on dark, cyan for streaming |
| Cybersecurity (dark) | #1E3A5F | #0E9F6E | #22D3EE | #0A0A0A | #F8FAFC | #374151 | monitoring-room look |
| Logistics | #D97706 | #1A56DB | #0E9F6E | #FFFBEB | #111928 | #FDE68A | high-vis signage |
| Insurance | #1E3A5F | #0E9F6E | #D97706 | #F9FAFB | #111928 | #D1D5DB | protection, stability |
| Automotive | #111928 | #374151 | #E02424 | #F9FAFB | #111928 | #D1D5DB | matte dark + performance red |
| Agriculture | #065F46 | #D97706 | #1A56DB | #F0FDF4 | #111928 | #A7F3D0 | fields, harvest, water |
| CleanTech | #047857 | #1A56DB | #D97706 | #F0FDF4 | #111928 | #BBF7D0 | rich emerald, avoid greenwash |
| Pharma | #1E3A5F | #0E9F6E | #FF8A4C | #F9FAFB | #111928 | #D1D5DB | clinical authority; red only for severe events |
| Architecture / AEC | #374151 | #D97706 | #1A56DB | #F9FAFB | #111928 | #E5E7EB | concrete, wood, blueprint |
| Interior design | #92400E | #065F46 | #1E3A5F | #FFFBEB | #111928 | #FDE68A | terracotta, linen, plants |
| Music / audio (dark) | #111928 | #7E3AF2 | #F05252 | #0A0A0A | #F9FAFB | #4B5563 | dark-first medium |
| Photography / video (dark) | #111928 | #374151 | #FF8A4C | #0A0A0A | #F9FAFB | #4B5563 | UI must disappear |
| Crypto / Web3 (dark) | #4F46E5 | #0E9F6E | #F59E0B | #0F172A | #F8FAFC | #475569 | crypto-native dark |
| Marketing / AdTech | #D97706 | #E02424 | #7E3AF2 | #FFFFFF | #111928 | #FDE68A | campaign energy |
| Customer support | #0E9F6E | #3F83F8 | #FF8A4C | #F9FAFB | #111928 | #E5E7EB | resolution green |
| Telemedicine | #1A56DB | #0E9F6E | #FF8A4C | #EFF6FF | #111928 | #BFDBFE | photographs well on video calls |
| Smart home / IoT | #1E3A5F | #0E9F6E | #F59E0B | #F9FAFB | #111928 | #E5E7EB | functional, never decorative |
| Manufacturing | #374151 | #D97706 | #1A56DB | #F9FAFB | #111928 | #D1D5DB | steel + safety amber |
| Construction | #D97706 | #374151 | #1A56DB | #FFFBEB | #111928 | #FDE68A | hi-vis site signage |

Dark-mode rule: bg #0A0A0A-#1C1917 family, text #F5F5F5, desaturate accents ~20%, elevate with lighter surfaces.

## Token template
```css
:root{
  --bg:#F8FAFC; --surface:#fff; --text:#1E293B; --muted:#64748B;
  --primary:#2563EB; --secondary:#3B82F6; --cta:#EA580C; --border:#E2E8F0;
  --success:#16A34A; --warning:#D97706; --danger:#DC2626;
  --radius:14px; --shadow:0 10px 30px rgb(15 23 42 / .08); --ease:cubic-bezier(.2,.7,.2,1);
}
```


---

# Font pairings: 74 (Google Fonts)

Cyr column: yes = Cyrillic subset exists on Google Fonts, no = Latin only, ? = verify on fonts.google.com before using for Russian text. For Russian sites safe picks: Inter, Manrope, Onest, Montserrat, Playfair Display, Cormorant Garamond, Lora, Nunito, Rubik, Roboto, Fira Sans, IBM Plex Sans, JetBrains Mono, Source Sans 3, Source Serif 4, Oswald, Unbounded.

| # | Name | Heading | Body | Mood | Best for | Cyr (H/B) |
|---|---|---|---|---|---|---|
| 1 | Classic Elegant | Playfair Display | Inter | elegant, luxury, editorial | luxury, fashion, spa, magazines | yes/yes |
| 2 | Modern Professional | Poppins | Open Sans | modern, corporate, friendly | SaaS, corporate, startups | no/yes |
| 3 | Tech Startup | Space Grotesk | DM Sans | tech, bold, futuristic | tech, AI, dev tools | no/no |
| 4 | Editorial Classic | Cormorant Garamond | Libre Baskerville | literary, refined | publishing, blogs, news | yes/no |
| 5 | Minimal Swiss | Inter | Inter | neutral, functional | dashboards, docs, enterprise | yes/yes |
| 6 | Playful Creative | Fredoka | Nunito | playful, warm | kids, education, games | ?/yes |
| 7 | Bold Statement | Bebas Neue | Source Sans 3 | impactful, headlines | marketing, agencies, sports | no/yes |
| 8 | Wellness Calm | Lora | Raleway | calm, natural, organic | health, spa, yoga | yes/yes |
| 9 | Developer Mono | JetBrains Mono | IBM Plex Sans | code, precise | dev tools, docs, CLI | yes/yes |
| 10 | Retro Vintage | Abril Fatface | Merriweather | retro, dramatic | breweries, restaurants, posters | no/yes |
| 11 | Geometric Modern | Outfit | Work Sans | geometric, balanced | portfolios, agencies | no/no |
| 12 | Luxury Serif | Cormorant | Montserrat | luxury, refined | fashion, jewelry, luxury e-com | yes/yes |
| 13 | Friendly SaaS | Plus Jakarta Sans | Plus Jakarta Sans | friendly, clean | SaaS, B2B, productivity | ?/? |
| 14 | News Editorial | Newsreader | Roboto | trustworthy, readable | news, journalism | no/yes |
| 15 | Handwritten Charm | Caveat | Quicksand | personal, casual | blogs, invitations, lifestyle | yes/? |
| 16 | Corporate Trust | Lexend | Source Sans 3 | accessible, professional | enterprise, government, health | yes/yes |
| 17 | Brutalist Raw | Space Mono | Space Mono | raw, stark | brutalist, dev portfolios | no/no |
| 18 | Fashion Forward | Syne | Manrope | avant-garde, edgy | fashion, galleries, studios | no/yes |
| 19 | Soft Rounded | Varela Round | Nunito Sans | soft, gentle | kids, pets, soft UI | no/yes |
| 20 | Premium DM Sans | DM Sans | DM Sans | premium, versatile | premium brands, SaaS | no/no |
| 21 | Vietnamese Friendly | Be Vietnam Pro | Noto Sans | multilingual | Vietnamese, international | no/yes |
| 22 | Japanese Elegant | Noto Serif JP | Noto Sans JP | traditional + modern | Japanese sites | n/a |
| 23 | Korean Modern | Noto Sans KR | Noto Sans KR | clean | Korean sites | n/a |
| 24 | Chinese Traditional | Noto Serif TC | Noto Sans TC | elegant, cultural | TC sites | n/a |
| 25 | Chinese Simplified | Noto Sans SC | Noto Sans SC | modern | SC sites | n/a |
| 26 | Arabic Elegant | Noto Naskh Arabic | Noto Sans Arabic | RTL, traditional | Arabic sites | n/a |
| 27 | Thai Modern | Noto Sans Thai | Noto Sans Thai | readable | Thai sites | n/a |
| 28 | Hebrew Modern | Noto Sans Hebrew | Noto Sans Hebrew | RTL, clean | Hebrew sites | n/a |
| 29 | Legal Professional | EB Garamond | Lato | formal, authoritative | law, contracts, government | yes/no |
| 30 | Medical Clean | Figtree | Noto Sans | accessible, trustworthy | clinics, pharma, health apps | no/yes |
| 31 | Financial Trust | IBM Plex Sans | IBM Plex Sans | serious, banking | banks, fintech, insurance | yes/yes |
| 32 | Real Estate Luxury | Cinzel | Josefin Sans | elegant, premium | real estate, architecture | ?/no |
| 33 | Restaurant Menu | Playfair Display SC | Karla | culinary, elegant | restaurants, cafes | ?/? |
| 34 | Art Deco | Poiret One | Didact Gothic | 1920s, decorative | luxury hotels, events | yes/yes |
| 35 | Magazine Style | Libre Bodoni | Public Sans | editorial, print | magazines, publications | no/no |
| 36 | Crypto / Web3 | Orbitron | Exo 2 | futuristic, digital | crypto, NFT, blockchain | no/yes |
| 37 | Gaming Bold | Russo One | Chakra Petch | action, esports | gaming, esports | yes/no |
| 38 | Indie / Craft | Amatic SC | Cabin | handmade, artisan | craft brands, organic | yes/no |
| 39 | Startup Bold | Outfit | Rubik | bold, confident | startups, launches | no/yes |
| 40 | E-commerce Clean | Rubik | Nunito Sans | clean, retail | online stores | yes/yes |
| 41 | Academic / Research | Crimson Pro | Atkinson Hyperlegible | scholarly, accessible | universities, journals | no/no |
| 42 | Dashboard Data | Fira Code | Fira Sans | precise, technical | dashboards, analytics | yes/yes |
| 43 | Music / Entertainment | Righteous | Poppins | energetic, fun | music, festivals | no/no |
| 44 | Minimalist Portfolio | Space Grotesk | Archivo | minimal, artistic | design portfolios | no/no |
| 45 | Kids / Education | Baloo 2 | Comic Neue | colorful, learning | kids apps, edu games | no/no |
| 46 | Wedding / Romance | Great Vibes | Cormorant Infant | script, feminine | weddings, invitations | yes/yes |
| 47 | Science / Tech | Exo | Roboto Mono | research, data | science, tech docs | ?/yes |
| 48 | Accessibility First | Atkinson Hyperlegible | Atkinson Hyperlegible | WCAG, dyslexia-friendly | gov, health, inclusive | no/no |
| 49 | Sports / Fitness | Barlow Condensed | Barlow | athletic, condensed | gyms, sports | no/no |
| 50 | Luxury Minimalist | Bodoni Moda | Jost | high-end, refined | fashion, premium | no/yes |
| 51 | Tech / HUD Mono | Share Tech Mono | Fira Code | sci-fi, precise | cybersecurity, sci-fi UI | no/yes |
| 52 | Pixel Retro | Press Start 2P | VT323 | 8-bit, arcade | pixel games, retro | yes/? |
| 53 | Neubrutalist Bold | Lexend Mega | Public Sans | loud, quirky | Gen Z brands, bold marketing | no/no |
| 54 | Academic / Archival | EB Garamond | Crimson Text | old-school, serious | university, archives | yes/no |
| 55 | Spatial Clear | Inter | Inter | legible on glass | spatial, glassmorphism | yes/yes |
| 56 | Kinetic Motion | Syncopate | Space Mono | wide, speed | festivals, automotive | no/no |
| 57 | Gen Z Brutal | Anton | Epilogue | shouty, meme | streetwear, viral campaigns | no/no |
| 58 | Bauhaus Geometric | Outfit | Outfit | geometric, uppercase posters | design-forward brands | no/no |
| 59 | Monochrome Editorial | Playfair Display + Source Serif 4 | JetBrains Mono for labels | austere, luxury, no sans | fashion, editorial, e-readers | yes |
| 60 | Dark Cinema | Inter | Inter | precise, premium | dev tools, trading, AI dashboards | yes/yes |
| 61 | SaaS Boutique | Calistoga | Inter (+ JetBrains Mono labels) | warm, bold | B2B SaaS, fintech | no/yes |
| 62 | Terminal CLI | JetBrains Mono | JetBrains Mono | hacker, matrix | dev tools, Web3, ARG | yes/yes |
| 63 | Kinetic Brutalism | Space Grotesk | Space Grotesk | uppercase, oversized | music, sports, drops | no/no |
| 64 | Flat Mobile | Inter | Inter | flat, bold weights | cross-platform apps | yes/yes |
| 65 | Material You | Roboto | Roboto | MD3, tonal | Android, enterprise | yes/yes |
| 66 | Neo Brutalism Mobile | Space Grotesk 700 | Space Grotesk 700 | pop, loud | creative tools, youth e-com | no/no |
| 67 | Bold Typography | Inter 600-800 (+ Playfair italic quotes) | Inter / JetBrains Mono | poster, type-as-hero | brand flagships, events | yes |
| 68 | Academia | Cormorant Garamond + Cinzel labels | Crimson Pro | library, parchment | reading tools, RPG, portfolios | yes/no |
| 69 | Cyberpunk | Orbitron | JetBrains Mono | neon, HUD | gaming, crypto | no/yes |
| 70 | Web3 DeFi | Space Grotesk | Inter (+ JetBrains Mono data) | precise, dark | DeFi, wallets, NFT | no/yes |
| 71 | Claymorphism | Nunito 800-900 | DM Sans | bubbly, tactile | kids, teen, gamified fintech | yes/no |
| 72 | Enterprise SaaS | Plus Jakarta Sans | Plus Jakarta Sans | approachable, legible | B2B, admin, onboarding | ?/? |
| 73 | Sketch Hand-Drawn | Kalam | Patrick Hand | imperfect, paper | journals, picture-books | no/no |
| 74 | Neumorphism | Plus Jakarta Sans | Plus Jakarta Sans | soft, ceramic | smart home, minimal tools | ?/? |

## Import pattern
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@400;500;600&display=swap&subset=cyrillic" rel="stylesheet">
```
Format: `family=Name+With+Plus:wght@400;600;700`, one `family=` per font, `display=swap`. Load only used weights. Always give a fallback stack (`serif`, `system-ui, sans-serif`, `ui-monospace`).

## Rules
- Contrast in style: serif + sans, display + neutral. Never two similar fonts.
- Display fonts (Bebas Neue, Abril Fatface, Poiret One, Press Start 2P, Amatic SC, Great Vibes, Caveat) are for big headlines or accents only, not body text.
- Mono for data, labels, code; uppercase labels with +1 to +2px letter-spacing.
- Body 16-18px, line-height 1.5-1.7, 65-75ch. Minimum 16px inputs (prevents iOS zoom).
- Fluid scale: `--step-0: clamp(1rem,.95rem+.25vw,1.125rem)` ... `--step-4: clamp(2.8rem,1.8rem+4.5vw,5.5rem)`; `h1{line-height:1.05;letter-spacing:-.02em;text-wrap:balance}`.
- Balanced wrapping (`text-wrap: balance`) is progressive enhancement: layouts must survive natural wrapping, long words, other locales and zoom.


---

# UX, accessibility and interaction rules (130 guidelines, condensed)

Severity: H = must, M = should, L = nice. Each line: rule. Avoid: anti-pattern.

## Navigation
- [M] Anchor links scroll smoothly: `html{scroll-behavior:smooth}`. Avoid: jumps.
- [M] Sticky nav must not cover content: body padding or `scroll-padding-top` = nav height.
- [M] Mark the active item (color/underline + `aria-current`).
- [H] Never break the back button: use `history.pushState` for views, not `location.replace`.
- [M] URL reflects state (hash or query) so views can be shared.
- [L] Breadcrumbs only for 3+ levels of depth.
- [M] Navbar state change at 50-100px scroll, transition 0.3-0.4s `cubic-bezier(.4,0,.2,1)`; shrink header ~80px to 56px with explicit heights.
- [M] Auto-hide on scroll down / show on scroll up: `transform:translateY(-100%)`, 80px threshold, `requestAnimationFrame` throttle. Avoid `display:none` toggles.
- [M] Mobile menu animates (`max-height`+`opacity` or transform), not instant display toggle.
- [M] Page transitions: View Transitions API as progressive enhancement (`if (document.startViewTransition)`), name shared elements with `view-transition-name`.

## Animation
- [H] Animate 1-2 key elements per view. Avoid: everything moving.
- [M] 150-300ms for micro-interactions, <500ms for UI. Avoid: 1000ms.
- [H] Respect `prefers-reduced-motion` (`animation-duration:.01ms!important` fallback); every animation has a static final state.
- [H] Loading feedback for async (skeleton/spinner). Avoid: blank/frozen UI.
- [H] Never rely on hover alone (touch has no hover): primary actions work on click/tap.
- [M] Infinite animation only for loaders. Avoid: bouncing icons.
- [M] Animate `transform` and `opacity`, not width/height/top/left.
- [L] ease-out for entering, ease-in for exiting. Avoid: linear.
- [M] Scroll-linked effects via CSS `animation-timeline: scroll()/view()` over JS scroll listeners; fall back gracefully.
- [H] Parallax/scroll-jacking causes nausea: disable under reduced motion.
- [M] Rapid interactions may cancel animation but final state, focus and content must remain correct.

## Layout
- [H] z-index scale (10 dropdown, 20 sticky, 30 modal, 40 toast, 50 tooltip). Avoid: `z-index:99999`.
- [M] Test that `overflow:hidden` is not clipping content; understand stacking contexts.
- [M] Fixed elements account for safe areas and each other.
- [H] Reserve space for async content: `aspect-ratio`, width/height on images, skeletons. Avoid: layout shift.
- [M] `min-height:100dvh` instead of `100vh` on mobile.
- [M] Text container max 65-75ch (`max-w-prose`).
- [M] Essential text must reflow without clipping at narrow widths, zoom and text scaling; long URLs/identifiers wrap; chips/tags wrap or use an operable `+n`; badges not color-only; truncated labels keep an accessible full value.

## Touch and mobile
- [H] Targets >= 44x44px (WCAG 2.2 AA minimum 24x24px). Avoid: 24px icon buttons on touch.
- [M] 8px gaps between targets.
- [M] Avoid horizontal-swipe conflicts with system gestures; use platform-native gestures.
- [M] `touch-action:manipulation` removes tap delay.
- [L] `overscroll-behavior:contain` where pull-to-refresh is unwanted; haptics sparingly.
- [H] Primary actions in the thumb zone (bottom of screen, bottom nav, FAB).

## Interaction states
- [H] Visible `:focus-visible` ring on all interactive elements (2px, offset 2px). Avoid: `outline:none` without replacement.
- [M] Hover: cursor + subtle change; active: pressed feedback (`active:scale-95`); disabled: reduced opacity + `cursor:not-allowed`.
- [H] Loading buttons: disable and show spinner during async; prevent double submit.
- [H] Errors near the field with `aria-invalid`, `aria-describedby`, `role="alert"`; success feedback via toast/check.
- [H] Confirm destructive actions (alertdialog with Cancel / Delete) or offer undo.
- [M] Buttons use verbs ("Book a table"), not "Submit".

## Accessibility
- [H] Text contrast >= 4.5:1 (large text/UI 3:1). Avoid: gray-400 on white.
- [H] Do not convey meaning by color alone: add icon/text.
- [H] Images: meaningful `alt`; decorative `alt=""`; icon-only buttons need `aria-label`; decorative SVG `aria-hidden`.
- [M] Sequential headings h1-h6, one h1. Semantic HTML (`nav main article`), not div soup.
- [H] All functionality via keyboard; tab order matches visual order; no clickable `<div>`.
- [H] Labels via `<label for>`; errors announced with `aria-live`/`role=alert`.
- [M] Skip link on nav-heavy pages.
- [H] Drag-only interactions need a single-pointer alternative (buttons, arrows).
- [H] Respect motion sensitivity.

## Forms
- [H] Visible labels above/beside inputs; placeholder is not a label.
- [M] Error under each field; validate on blur; mark required (`*` or "(required)").
- [M] Correct `type` (email, tel, number, url), `autocomplete`, `inputmode` on mobile.
- [M] Password show/hide toggle; inputs look interactive (border/background).
- [H] Submit shows loading then success/error state.

## Responsive
- [M] Mobile-first; test 320/375/414/768/1024/1440.
- [H] Touch-sized targets on mobile; body text >= 16px; inputs >= 16px (no iOS zoom).
- [H] `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`.
- [H] No horizontal scroll; images `max-width:100%; height:auto`; tables in `overflow-x:auto` wrappers or card layout.

## Typography
- [M] Line-height 1.5-1.75; 65-75 characters per line; modular scale (12/14/16/18/24/32); fallback font similar to webfont; clear heading vs body difference.

## Performance
- [H] Responsive images (`srcset`, WebP/AVIF, correct size); `loading="lazy"` below fold.
- [M] `font-display:swap`; third-party scripts `async/defer`; split code by route; monitor bundle; inline critical CSS; cache headers.
- [M] Blur-up image placeholders; skeleton shimmer matching content layout.
- [M] No autoplay heavy video (click-to-play, preload none); compress 3D/image assets.

## Feedback and content
- [H] Spinner/skeleton for operations >300ms. [M] Empty states explain + give an action; error recovery gives next step; progress steps ("Step 2 of 4"); toasts auto-dismiss 3-5s.
- [M] Truncate with ellipsis + expand; [L] relative or locale dates, formatted numbers, realistic placeholder data (no lorem ipsum).
- [M] Onboarding is skippable. Search: autocomplete, helpful "no results" with suggestions. Bulk actions for lists [L].

## AI and chat interfaces
- [H] Label AI-generated content; never present AI as a human. [M] Stream responses token by token; show confidence when relevant; progressive disclosure for advanced AI options; expectation-setting copy (what it can/cannot do); retry + alternatives on error; graceful non-AI fallback; thumbs up/down or regenerate [L].
- [H] Chat threads: distinct bubbles for user vs assistant; `aria-label` for who spoke.
- [H] Voice UI needs visual fallback (multimodal).

## Dashboards
- [H] KPI hierarchy: most important metric largest, top-left. [H] Chart by data story (line trend, bar comparison, donut 2-4 parts only). [M] Persist filters in URL/localStorage. [M] Real-time presence: show collaborators' cursors/avatars.

## Spatial / sustainability
- Gaze hover and depth (visionOS): respond to look before pinch; glass material + z-offset. Sustainability: avoid autoplay video, compress assets.


---

# Chart choices (dashboards and data pages)

| Data story | Best chart | Notes |
|---|---|---|
| Trend over time | Line / area | smooth lines for continuous series; max 5 series; label axes and units |
| Compare categories | Bar (horizontal for long labels, vertical for time) | sort bars; start at zero |
| Part of whole (2-4 parts) | Donut / stacked bar | more than 4 parts: use bar |
| Distribution | Histogram / box plot | show median and outliers |
| Correlation | Scatter / bubble | trend line, tooltips |
| Funnel / conversion | Funnel or stepped bars | show drop-off % per step |
| Progress to goal | Progress bar / gauge (sparingly) | include target value as text |
| Geographic | Choropleth / dot map | legend with scale; sequential color |
| Matrix / density | Heatmap | sequential single hue; don't rely on color alone |
| Flow / hierarchy | Sankey / treemap | only when relationships matter |
| KPI snapshot | Big number + sparkline + delta | 48-64px number; up/down icon, not only color |
| Exact values | Table with sort and filter | right-align numbers, tabular-nums |

Rules: max 5-6 colors (colorblind-safe; use `#2563EB, #F97316, #16A34A, #7C3AED, #64748B`), direct labels beat legends, tooltips on hover AND tap, text alternative or data table for screen readers, no 3D, no dual axes unless clearly labeled, empty/loading/error state for every chart. Libraries: Chart.js or inline SVG for simple, D3 for custom, ECharts for dense dashboards.


---

# Stack defaults

If the user names no stack, deliver one self-contained `index.html` (HTML + CSS variables + minimal vanilla JS; Tailwind via CDN only if asked). Otherwise follow these defaults.

- **HTML + Tailwind**: mobile-first utilities (`md:` `lg:`), `max-w-6xl mx-auto px-4`, design tokens via CSS variables or Tailwind theme, `focus-visible:ring-2`, `motion-safe:`/`motion-reduce:` variants, `min-h-dvh`.
- **React / Next.js**: function components, tokens in CSS variables or Tailwind theme, `next/image` with width/height and `priority` for hero only, `next/font` for fonts, server components by default, `Link viewTransition` optional, no `useEffect` for data that can be fetched on the server.
- **Vue / Nuxt**: `<script setup>`, composables for shared state, `NuxtImg`, scoped CSS with variables; Nuxt UI for components.
- **Svelte / SvelteKit**: runes or stores, `transition:` directives respect reduced motion, scoped styles.
- **Astro**: ship zero JS by default, islands (`client:visible`) only for interactive parts.
- **shadcn/ui**: use its tokens (`--background`, `--foreground`, `--primary`, `--ring`, `--radius`), compose variants, keep Radix accessibility.
- **Angular / Laravel (Blade, Livewire)**: component templates with semantic HTML, server-side validation messages shown next to fields.
- **Mobile (SwiftUI, Jetpack Compose, React Native, Flutter)**: follow platform guidelines (HIG / Material 3), 44pt/48dp targets, Dynamic Type and font scaling, safe areas, system dark mode, native gestures, haptics sparingly.
- **Three.js**: lazy-load, cap pixel ratio, pause when offscreen, always provide a non-3D fallback and reduced-motion state.
- **Desktop (WPF, WinUI 3, JavaFX, Avalonia)**: density-appropriate tables, keyboard shortcuts, high-contrast themes, resource dictionaries / CSS for tokens.
