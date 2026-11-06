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
