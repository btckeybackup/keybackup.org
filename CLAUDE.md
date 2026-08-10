# keybackup

Open-source printable Bitcoin key backup template. Static site + a
self-contained printable HTML document.

## Hard constraints
- Pico CSS only. No Tailwind (its Preflight reset destroys Pico's
  semantic styling). No React, no other CSS frameworks.
- No analytics, trackers, cookies, or third-party requests anywhere.
- `public/keybackup-v*.html` must be fully self-contained: inline CSS
  and JS, no imports, no webfonts, no network requests. It must work
  offline from a local file. Never let Vite process or bundle it.
- Never commit generated PDFs. They are release artifacts only.
- Do not add Co-Authored-By trailers to commits.

## Palette
--saffron: #ff9500  --ink: #031926  --snow: #fffbff
--dim-grey: #727072  --grey-olive: #808f87

Accessibility: saffron on snow is 2.2:1 and FAILS WCAG AA. Never use it
as text on light backgrounds. On ink it is 8.1:1 — use it for text on
dark, for button fills with ink-coloured text, and for accents only.

## Versioning
Document version lives in one place and propagates to the header, all
four sheet footers, and the filename. Every released version stays
downloadable forever — someone recovering from a v1.0 sheet needs v1.0
semantics.