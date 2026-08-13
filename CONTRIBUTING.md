# Contributing

Corrections, translations, and improvements are all welcome. This
document is meant to be forked and adapted, so if it does not fit how
you hold your keys, change it.

## Translations are the highest-value contribution

BIP39 has official wordlists in ten languages: English, Japanese,
Korean, Spanish, Simplified Chinese, Traditional Chinese, French,
Italian, Czech, and Portuguese. Someone whose seed was generated in
Japanese cannot safely use an English sheet, and a sheet in a language
the person recovering cannot read is close to worthless. Each wordlist
needs its own sheet.

A translation is not just the prose. Check all of these:

- **The handwriting key on sheet 4.** It lists the character pairs that
  get confused by a reader of that language and script. The English
  sheet pairs `0/o`, `1/l`, `2/z`, `5/s`, `6/b`, `9/g`, `u/v`, `n/m`.
  These are wrong for other scripts and need rethinking rather than
  translating, along with the spoken names beside each glyph.
- **The box counts on sheet 2.** Eight boxes per word fits the English
  wordlist. Other languages need a different count, and the note that
  the first four letters identify a word does not hold for every
  wordlist.
- **The passphrase advice on sheet 3.** The warning about accented
  letters and normalisation matters more, not less, in languages that
  use them.
- **Line lengths.** Several lines are pre-broken to fit the page width.
  A longer translation will overflow, so re-check the layout.

Say plainly which wordlist and which script your sheet is for. Where
you were unsure, say so in the pull request rather than guessing.

## Changes to the printed document

The document is `public/keybackup-v*.html`. It is a single
self-contained file: inline CSS only, no imports, no webfonts, no
JavaScript, no network requests of any kind. It must render correctly
opened from `file://` on a machine with no internet connection. Never
let the build process touch it.

**Any change to the document must be re-verified against both page
sizes.** The layout flows in document order, so adding a single field
pushes everything after it down, and the sheet that fit yesterday may
spill onto a second page today. Before opening a pull request, confirm
that A4 and Letter both still render as **four clean pages**, with
nothing overflowing the footer and nothing clipped at the edges.

To check, print to PDF from headless Chrome at both sizes. The Letter
variant is the same file with `class="letter"` on the `<body>`, which
switches the `@page` size. Confirm the output is exactly four pages in
both cases, then look at every page. Letter is 18mm shorter than A4 and
is always the one that fails first, so a change that fits A4 is not
evidence of anything.

Sheets 1, 2 and 4 are the tight ones. As of v1.1 they have roughly 6mm,
5mm and 4mm of spare room on Letter respectively, so there is very
little room to spend. Sheet 3 has around 30mm. A change that needs more
room than a sheet has means finding it elsewhere on that sheet, not
letting the sheet grow.

## Versioning

The version string lives in exactly one place in the document source
and propagates from there to the header and all four sheet footers. Do
not add a second copy.

**Any change that alters the meaning of a field requires a version
bump.** Renaming a field, changing what belongs in it, reordering the
sheets, changing how many boxes a value gets: all of these change how a
filled-in sheet should be read. Someone may be recovering from a sheet
printed years ago, and they need the version they actually hold to mean
what it meant when they filled it in.

**Every released version stays downloadable permanently.** Old versions
are never removed, replaced, or quietly corrected. If v1.0 contains a
mistake, fix it in v1.1 and leave v1.0 exactly where it is, because
someone is holding a printed copy of it.

Typo fixes, wording that does not change a field's meaning, and pure
layout adjustments do not need a bump.

A version bump touches four things, and all four must move together:

- a new `public/keybackup-v<version>.html`, with `--version` updated
  inside it
- `DOC_VERSION` in `src/site.js`, which drives the site header and the
  download link
- the README download links, the "what changed" notes, and the SHA256
  block
- `README.md` checksums are taken from the files themselves, so
  recompute them last, after the document is final:
  `shasum -a 256 public/keybackup-v*.html`

The old document file stays exactly as it is. Never edit a released
version to match the new one.

## The site

The site is Vite plus Tailwind v4. Three hard constraints:

- Tailwind v4 only, wired up through `@tailwindcss/vite`. No React, no
  other CSS frameworks, no component libraries.
- No analytics, trackers, cookies, or third-party requests anywhere. A
  page about paper backups has no business phoning home. Fonts are
  self-hosted through `@fontsource-variable/*`, and icons are inlined
  from `@phosphor-icons/core` in `src/icons.js`. Never link a CDN.
- Never commit generated PDFs. They are release artifacts only.

Design tokens live in the `@theme` block at the top of `src/style.css`.
Layout is done with utility classes; the guide's running prose is styled
by element inside `.doc`, so paragraphs stay readable in the markup.

### Palette

```
--ocean-deep:   #2364aa
--white:        #ffffff
--shadow-grey:  #262322
--coral-glow:   #ef8354
--grey-olive:   #8a897c
```

The site is one light theme throughout, and every foreground on
background pair in use passes WCAG AA. Three rules keep it that way:

- **Ocean is the only accent.** Links, primary buttons, emphasis rules,
  focus rings. It is 6.0:1 against white in both directions.
- **Coral means danger and nothing else, and only ever sits on an ink
  surface**, where it is 6.0:1. Coral on white is 2.6:1 and fails every
  contrast threshold, so it is never text or a mark on a light
  background.
- **The supplied grey-olive is 3.5:1 on white** and fails AA at body
  size. Use the `--color-muted` token, which is a darkened version at
  5.7:1, rather than the raw colour.

Ink panels, such as the failure-modes block in the guide, are components
rather than sections that flip the theme. Nothing on the site inverts to
a dark mode.

### Sheet images

The pictures on the site are the real document, not a mock-up.
`npm run sheets` renders each sheet of the current document to
`public/sheets/` with Playwright. Re-run it whenever the document
version changes, and commit the PNGs.

## Licence

Contributions are accepted under the licence covering the files you
touch: [CC0 1.0](LICENSE-DOCUMENT) for the printable document,
[MIT](LICENSE) for the site and tooling.

In practice this means translations and document changes are placed in
the public domain, which is deliberate. A recovery sheet has to be
freely copyable by anyone, forever, with no notice attached.
