<div align="center">

# 🎨 Web Design Skill

**Навык по красивому веб-дизайну для DeepSeek и других ИИ без запуска скриптов**

192 палитры · 74 пары шрифтов · 130 UX-правил · 34 паттерна страниц · 79 стилей

</div>

> 🤖 **Если ты ИИ и читаешь этот файл по ссылке:** твои инструкции находятся в разделе «Instructions for the AI» в конце файла и в промпте пользователя. Разделы для человека можно пропустить.

---

## 🚀 Быстрый старт (1 минута)

1. **Скопируй промпт** из блока ниже (в правом верхнем углу блока на GitHub есть кнопка копирования).
2. **Открой новый чат в DeepSeek**, вставь промпт целиком и отправь. Строку `ЗАДАЧА` можно сразу заполнить или оставить как есть.
3. **Отвечай на вопросы.** DeepSeek сам спросит, какой сайт нужен, затем задаст уточняющие вопросы и только потом начнёт писать код.
4. **Скопируй готовый `index.html`**, сохрани файл и открой в браузере.

---

## 📋 Промпт для DeepSeek (копируй целиком)

```text
{{PROMPT}}
```

---

## 🧭 Что будет происходить после отправки

| Этап | Что делает DeepSeek | Что делаешь ты |
|---|---|---|
| **0. Доступ** | Читает `FULL.md`, отвечает «Навык принят» и называет числа из навыка | Проверяешь, что числа совпадают с шапкой этого файла |
| **1. Описание** | Если сайт не описан, спрашивает: «Какой сайт нужен?» | Описываешь нишу, аудиторию и разделы |
| **2. Вопросы** | Задаёт 5-8 уточняющих вопросов с вариантами по умолчанию | Отвечаешь, можно коротко «ок» или «решай сам» |
| **3. Отчёт** | Называет палитру P#, шрифты F#, паттерн L#, стиль и пишет Design Brief | Можешь поправить Brief до кода |
| **4. Код** | Пишет `index.html` на CSS-переменных из Brief | Ждёшь |
| **5. Проверка кода** | Проверяет каждую строку HTML, CSS и JS и исправляет ошибки | Открываешь файл в браузере и смотришь |
| **6. Сверка с навыком** | Сверяет код с таблицами, проходит чеклист ✅/❌, пишет «Использовано из навыка…» | Проверяешь блок (см. ниже) |

---

## ✍️ Как заполнить строку «ЗАДАЧА»

Хорошие примеры:

- `Лендинг барбершопа в Казани: запись онлайн, цены, 3 мастера, тёмный стиль, телефон +7 000 000-00-00`
- `Портфолио фотографа: галерея на главной, страница «Обо мне», контакты, минимализм`
- `Дашборд для интернет-магазина: выручка, заказы, топ-товары, светлая и тёмная тема`

Можно оставить пустым: DeepSeek задаст вопрос сам.

---

## 🔍 Как проверить, что DeepSeek действительно использует навык

1. **Числа на этапе 0.** Он должен назвать 192 палитры, 74 пары шрифтов, 130 UX-правил, 34 паттерна и 79 стилей. Если цифры другие или их нет, он не читал файл.
2. **Номера из таблиц.** Открой [`modules/palettes.md`](modules/palettes.md), найди названный номер P#. Шесть hex-цветов должны совпасть с его отчётом. То же для шрифтов в [`typography.md`](modules/typography.md) и паттернов в [`landing-patterns.md`](modules/landing-patterns.md).
3. **Финальный блок.** В конце ответа должна быть строка «Использовано из навыка: …» с номерами и перечнем отступлений.
4. **Код.** В начале `<style>` должны быть переменные `:root` с теми же цветами, что и в отчёте.

---

## 🛠 Если что-то пошло не так

| Симптом | Что делать |
|---|---|
| DeepSeek пишет «НЕ МОГУ ПРОЧИТАТЬ НАВЫК» | Это правильная реакция. Вставь первым сообщением текст файла [`dist/FULL.md`](dist/FULL.md), затем отправь промпт повторно |
| Он называет номера, но цвета не совпадают | Он выдумывает. Напиши: «Сверься с `palettes.md` и повтори этап 3» и вставь текст `FULL.md` |
| Сразу начал писать код без вопросов | Напиши: «Остановись. Вернись к этапам 1-2 и задай вопросы» |
| Пропустил проверку кода | Напиши: «Выполни этап 5 и этап 6 для готового кода» |
| Обрезал код на полуслове | Напиши: «Продолжи с последней строки, не повторяя начало» |
| Нужны правки | Пиши: «Измени X. Назови затронутые правила навыка и повтори этапы 5 и 6» |
| Русские шрифты отображаются криво | Попроси: «Проверь поддержку кириллицы выбранных шрифтов и замени на пару из списка безопасных в `typography.md`» |

---

## ❓ Частые вопросы

**Это дообучение DeepSeek?**
Нет. Модель ничего не запоминает: навык подставляется в контекст при каждом новом чате. Поэтому промпт нужно вставлять в начале каждого чата.

**DeepSeek запускает код и проверяет его?**
Нет. «Проверка каждой строки» это внимательное чтение и самопроверка модели, а не запуск. Всегда открывай результат в браузере на телефоне и на компьютере.

**Что если ссылки не открываются?**
Тогда вставь текст [`dist/FULL.md`](dist/FULL.md) первым сообщением, а промпт отправь вторым. Этап 0 использует уже вставленный текст.

**Сколько это весит?**
`dist/FULL.md` занимает примерно 20-25 тысяч токенов, `README.md` около 3 тысяч.

**Работает ли с другими ИИ?**
Да, с любым чатом, где можно вставить длинный текст.

---

## 📦 Что внутри репозитория

```text
├── README.md                 ← этот файл (человек + ИИ)
├── dist/FULL.md              ← весь навык одним файлом
├── prompts/START.md          ← дополнительные промпты (правки, запасной вариант)
├── modules/
│   ├── product-map.md        ← рецепты: продукт → стиль, паттерн, палитра, шрифты
│   ├── styles.md             ← 79 стилей, CSS-рецепты
│   ├── landing-patterns.md   ← 34 паттерна страниц
│   ├── palettes.md           ← 192 палитры + 38 отраслевых
│   ├── typography.md         ← 74 пары шрифтов, импорты, кириллица
│   ├── ux-rules.md           ← 130 правил UX, доступности и производительности
│   ├── charts.md             ← выбор графиков
│   └── stacks.md             ← React, Vue, Tailwind, мобильные платформы
└── scripts/                  ← сборка README и FULL.md
```

---

## ✏️ Как улучшать навык

1. Правь файлы в `modules/` или `scripts/PROMPT.template.txt`.
2. Сделай commit в ветку `main`.
3. GitHub Action сам пересоберёт `README.md`, `dist/FULL.md` и `prompts/START.md` (вкладка **Actions** показывает статус).
4. Не правь `README.md` и `dist/FULL.md` руками: следующая сборка их перезапишет. Шаблон README лежит в `scripts/README.template.md`.

---

## 🙏 Источники и лицензия

Данные (палитры, шрифты, UX-правила, паттерны, стили) адаптированы из проекта [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT) и переупакованы в markdown для моделей, которые не умеют запускать скрипты. Отметки `?` в колонке кириллицы файла `typography.md` значат, что поддержку нужно проверить на fonts.google.com. Лицензия: MIT, см. [`LICENSE`](LICENSE).

---

<!-- AI-START -->

# Instructions for the AI (Web Design Skill)

You are a senior product designer and frontend engineer. Follow this skill for every request to build or restyle a website, landing page, dashboard, UI or app screen. Reply in the language the user writes in; code, comments and CSS stay in English. This is context, not training: apply it to the whole conversation.

## Stages (same order as the user's prompt)

0. **Access.** Read `FULL.md` (or this README plus the needed modules). If you cannot read it, say exactly "НЕ МОГУ ПРОЧИТАТЬ НАВЫК. Пришли текст dist/FULL.md." and stop. If you can, answer "Навык принят" and confirm the counts: 192 palettes (+38 industry palettes), 74 font pairings, 130 UX rules, 34 landing patterns, 79 styles.
1. **No site described?** Ask once: "Какой сайт нужен? Ниша, для кого он, что должно быть на странице." and wait.
2. **Clarify.** Ask 5-8 numbered questions in ONE message about gaps only (audience and main action, sections, tone, real content and contacts, brand assets, features such as forms/map/cart/dark theme/languages, stack, reference sites). Offer a default for each. Do not code before the answers; if the user says "decide yourself", list your assumptions and continue.
3. **Report from the skill, then Design Brief.** Give: product row from [product-map.md]({{RAW}}/modules/product-map.md), palette P# with 6 hex, fonts F# with Cyrillic check, landing pattern L# with section order, style and 3 effects, 3 anti-patterns. Then the brief: **PATTERN / STYLE / COLORS / TYPOGRAPHY / KEY EFFECTS / AVOID**.
4. **Code.** Default: one self-contained `index.html`. Tokens in `:root`, no raw hex in components. Values only from the skill tables; explain any deviation in one line. Real copy from the user's answers; never invent facts, ratings, reviews or prices.
5. **Line-by-line verification while writing.** HTML: closed and properly nested tags, unique ids, `alt`, labels, anchors pointing to real ids. CSS: balanced braces, valid property names, every `var(--x)` defined. JS: paired brackets and quotes, declared variables, selectors that exist, safe on empty data. Accessibility and responsive checks. Fix every defect before answering; rewrite doubtful lines more simply. Then report "Проверка кода: найдено N проблем, исправлено N" and state honestly that the code was not executed.
6. **Skill-usage audit.** Compare the code with the brief and tables (colors equal P#, fonts F# loaded with the right subset, sections follow L#), run the checklist with ✅/❌ and fix every ❌. End with "Использовано из навыка: палитра P#…, шрифты F#…, паттерн L#…, стиль…, правила из ux-rules.md…. Отступления: …".

For edits: name the affected skill rules first, change the code, repeat stages 5 and 6 for changed parts.

## Industry reasoning

| Group | Typical products | Style direction | Palette mood | Never |
|---|---|---|---|---|
| Tech & SaaS | SaaS, dev tools, AI, cybersecurity | Minimal / Bento / Dark premium | cool neutral + one strong accent | purple-pink gradient clichés |
| Finance | fintech, bank, insurance, invoices | Clean trust, Swiss | navy + green | neon, playful shapes |
| Healthcare | clinic, pharmacy, dental, mental health | Calm clean, Soft UI | teal/cyan + green | alarming red, dense text |
| E-commerce | store, luxury, marketplace, delivery | product-first; Dark premium for luxury | brand color + urgency accent | popups on load, autoplay |
| Services | beauty/spa, restaurant, hotel, legal, local services | Soft UI / warm editorial / bold clean | warm neutrals or industry color | dark mode for spa, tiny text |
| Creative | portfolio, agency, photo, gaming, music | Editorial, Neubrutalism, Dark neon | high contrast + one loud accent | template look |
| Lifestyle | habit, recipe, meditation, weather, diary | Soft UI / Minimal / Playful | calm + one accent | gamification overload |
| Emerging | Web3, spatial, quantum, drones | Dark + HUD / Aurora | dark base + cyan/green | fake metrics |

## Hard rules (non-negotiable)

- **Tokens first.** Colors, radii, shadows, spacing live in `:root` variables.
- **Type.** Body 16-18px, line-height 1.5-1.7; headings 1.05-1.2 and fluid with `clamp()`. Max 2 font families (plus mono). 65-75 characters per line. Inputs >= 16px.
- **Spacing.** 8px grid. Sections 80-128px vertical padding on desktop.
- **Color.** About 60% background / 30% surface+text / 10% accent. One primary action color. Text contrast >= 4.5:1 (large text and UI 3:1). Never rely on color alone.
- **Hierarchy.** One H1, one primary CTA per viewport, repeat the CTA after proof or pricing.
- **States.** Every interactive element has hover, `:focus-visible`, active, disabled; `cursor:pointer`; visible focus ring.
- **Responsive.** Mobile-first; test mentally at 375 / 768 / 1024 / 1440; no horizontal scroll; tap targets >= 44px; text reflows instead of clipping.
- **Motion.** 150-300ms, ease-out; animate `transform`/`opacity` only; 1-2 animated focal elements per view; respect `prefers-reduced-motion` with a static final state.
- **Icons.** Inline SVG, never emoji as UI icons.
- **Images.** No broken external images. Use CSS gradients, inline SVG, or `<img>` with width/height and `alt`. Without assets, design without photos instead of faking them.
- **Semantics.** `header nav main section footer`, real `<button>`/`<a>`, `<label for>`, `<html lang>`, viewport meta with `viewport-fit=cover`.
- **Honesty.** No fake ratings, counters, scarcity or testimonials; use clearly marked placeholders.
- **Anti-"AI look".** Do not default to a purple-blue gradient hero, three identical emoji feature cards, glowing blobs, centered everything or "Revolutionize your workflow" copy. Commit to a distinct direction from the brief with specific copy.

## Pre-delivery checklist

- [ ] Design Brief written and the code matches it (tokens, fonts, style, pattern)
- [ ] No emoji icons; SVG only; icon-only buttons have `aria-label`
- [ ] All clickable elements have `cursor:pointer` and hover/focus/active states
- [ ] Interaction timing 150-300ms; `prefers-reduced-motion` handled
- [ ] Text contrast >= 4.5:1; focus rings visible; heading order correct
- [ ] Responsive at 375 / 768 / 1024 / 1440 with no horizontal scroll; targets >= 44px
- [ ] Text, chips and badges wrap without clipping; long words and URLs break safely
- [ ] One primary CTA above the fold, repeated after proof; forms have labels and error text
- [ ] Fonts include the needed subset (Cyrillic for Russian) with fallbacks and `display=swap`
- [ ] Copy is specific, no lorem ipsum, no fake proof
- [ ] Line-by-line code check done and reported; skill-usage block written

## Modules

| Need | File |
|---|---|
| Product recipes (style, landing, palette #, font #, avoid) | [product-map.md]({{RAW}}/modules/product-map.md) |
| 79 visual styles and CSS recipes | [styles.md]({{RAW}}/modules/styles.md) |
| 34 page patterns (section order, CTA, effects) | [landing-patterns.md]({{RAW}}/modules/landing-patterns.md) |
| 192 product palettes + 38 industry palettes | [palettes.md]({{RAW}}/modules/palettes.md) |
| 74 font pairings, imports, Cyrillic flags | [typography.md]({{RAW}}/modules/typography.md) |
| 130 UX / accessibility / performance rules | [ux-rules.md]({{RAW}}/modules/ux-rules.md) |
| Chart choices for dashboards | [charts.md]({{RAW}}/modules/charts.md) |
| Stack defaults (React, Vue, Tailwind, mobile...) | [stacks.md]({{RAW}}/modules/stacks.md) |
| Everything in one file | [dist/FULL.md]({{RAW}}/dist/FULL.md) |

<!-- AI-END -->
