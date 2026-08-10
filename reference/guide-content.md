# How to use the Key Backup Record

This document is four printed sheets that record one Bitcoin key — the seed words, the passphrase, and the handful of details that make them usable years from now by someone who may not be you.

It takes about twenty minutes to fill in properly. Read this page first.

---

## Before you start

**Understand what these sheets do and do not cover.**

For a single-signature wallet, the seed words on Sheet 2 are enough to recover your funds. Everything else on the sheets makes recovery faster and less error-prone, but the seed is the thing.

For a multisig wallet, the seed words on their own recover **nothing**. You also need the wallet descriptor — the record of how many keys there are, what the quorum is, and every co-signer's xpub. Without it, you can hold every seed in the quorum and still be unable to reconstruct the wallet or find your own coins.

This is the most common way multisig funds are lost. People back up three seeds beautifully and never write down the descriptor.

So there are two documents, with opposite handling rules:

| | Key Backup Record | Wallet Configuration Record |
|---|---|---|
| One per | key | wallet |
| Secret? | yes — treat as bearer cash | no |
| Copies | as few as you can manage | as many as you like |
| Losing it | loses one key | loses the whole wallet |

Keep at least one copy of the configuration record somewhere that holds **no seed words**. That single rule is what makes a multisig survivable.

---

## What you need

- A printer, printing at actual size
- A pen with **archival pigment ink**. Not pencil, which smudges and fades. Not gel or rollerball, which run when wet. Not a thermal-printed anything.
- The device or software holding the key
- Twenty uninterrupted minutes, offline, somewhere you're not overlooked

Print on the heaviest plain paper your printer takes. Avoid glossy stock — ink sits on the surface and smears.

---

## Print settings

Set your print dialog to **100% / Actual Size**. Not "Fit to page", not "Shrink to fit". Browsers default to scaling, and a scaled sheet has boxes too small to write in.

Sheet 1 carries a calibration ruler. After printing, measure it. If the line is not 100mm, the page was scaled — change the setting and reprint. Don't trust the on-screen preview; the ruler is the ground truth.

Choose the paper size that matches your printer's tray. A4 gives marginally larger boxes; Letter is otherwise identical.

**Print Sheet 4 once for every person who will hold any part of this backup.** It contains no secrets, and whoever ends up holding only Sheet 3 needs the handwriting key and the warnings just as much as you do.

---

## Filling in the sheets

### Sheet 1 — Key identity

**Master fingerprint.** Eight hexadecimal characters that identify this key. Your device shows it during setup, and wallet software shows it whenever you import the key.

If you use a passphrase, load the passphrase first and record the fingerprint the device shows **with the passphrase applied**. This matters twice over: it's the value that appears in your wallet descriptor, and it's how a future recoverer confirms they've entered the passphrase correctly.

Hex uses only `0-9` and `a-f`. There is never an `o`, `l`, `s`, `g` or `z` — so a circle is always zero, and a bare vertical stroke is always the digit one.

**Key origin.** Which device or software created the key, and what version. Firmware matters more than it looks: some vendors have had derivation quirks in specific versions, and a future recoverer benefits from knowing what produced this key.

**If the entropy was imported**, say where the key came from and what else has ever held it. Treat this as mandatory rather than optional. An imported key's security is capped by the weakest environment it has ever touched — a phone wallet from 2017, a paper backup someone once photographed, an exchange that generated it for you. Nothing else records this, and it becomes unknowable later. If the honest answer is uncomfortable, that's a signal to move the funds to a fresh key rather than to document the problem.

**Multisig table.** Leave it blank for single-signature wallets.

The derivation path belongs to each *wallet*, not to the key. The same device used in a single-sig and two multisigs uses three different paths. Fill in one row per wallet.

The descriptor checksum is the eight characters after the `#` at the very end of the descriptor:

```
wsh(sortedmulti(2,[...]))#tjg09x5t
```

It uses a restricted character set that never contains `b`, `i`, `o` or the digit `1`. So when you read it back: a circle is always zero, a bare vertical stroke is always `l`, and a shape like `b` is always `6`.

The checksum verifies a descriptor you already have. It cannot reconstruct one — eight characters is enough to catch a transcription error, nowhere near enough to recover the descriptor itself. The configuration record is still what rebuilds the wallet.

### Sheet 2 — Seed words

Write in capitals if it helps legibility, and don't join letters up.

**Fill in the word numbers.** Each BIP39 word has a position from 1 to 2048, and your wallet software will show them. This is the highest-value field on the sheet. Handwriting degrades, ink fades, and `flight` and `fight` look identical after fifteen years in a drawer — but `#712` doesn't.

Strike through every unused row. A sheet with twelve words and twelve blanks is ambiguous; a sheet with twelve words and twelve struck-out rows is not.

If you make a mistake, **start a fresh sheet and destroy the old one.** Do not cross out and rewrite. A corrected seed sheet is exactly the artifact that causes a failed recovery at the worst possible moment.

Two facts that will help you later. Only the first four letters of each word are needed to identify it uniquely. And the final word encodes a checksum, so a single mistyped word is almost always rejected outright by wallet software — a phrase that "almost works" means a transcription error, not lost funds.

### Sheet 3 — Passphrase

Leave this sheet blank and destroy it if you don't use a passphrase.

**Choosing one.** Use four or more words from the BIP39 English wordlist, all lowercase, separated by single spaces. Nothing else — no capitals, no punctuation, no accented letters, no emoji, and never a space at the start or end.

This isn't fussiness. Accented and unusual characters are normalised differently by different wallets, so the same passphrase can open different wallets depending on the software. A trailing space is invisible on paper and unguessable. Each is a way to lose funds while believing the backup is fine.

Write one character per box, leaving a box empty for each space.

**Where this sheet lives is the real decision.**

For a *single-signature* wallet, storing Sheet 3 beside Sheet 2 cancels the passphrase out entirely — anyone who finds the pair has everything. Splitting them is the whole point of having a passphrase.

For *multisig*, keeping them together is usually correct. One compromised key still can't spend anything, and the far greater risk is that you or your heir never recovers the passphrase at all.

**If you split them**, complete the bottom block: copy the master fingerprint across, and name the person holding the seed words. Sheet 1 has the mirror field for their contact details. Held by two people, the halves work like a 2-of-2 lock — neither can move funds alone.

Understand the trade you're making. A 2-of-2 split converts a theft risk into a loss risk. There's no threshold to fall back on: if either half is destroyed, everything is gone.

### Sheet 4 — Instructions and testing

This sheet is not secret. Print it for every holder, and **give it to your heir now** — not on your death. Someone reading "never type these words into a website" for the first time during a bereavement is already at risk.

**Fill in the handwriting key while you're still the person who can read your own writing.** It takes one minute. Every character on these sheets is a lowercase letter or a digit, and this row is what tells a future reader whether the mark you made was a zero or an `o`, a `1` or an `l`.

---

## Storing them

Paper is the starting point, not the destination. Transfer the seed words to **stamped or punched stainless steel**, which survives fire and flood. Keep the paper as the record of everything the steel can't hold — the fingerprint, the paths, the instructions.

Keep copies in at least two separate buildings. A single location is a single fire.

Don't laminate. It traps moisture against the paper, and you can't add to a sealed sheet later — you'll want to, when you complete the test log or add a wallet.

Use a tamper-evident bag and sign across the seal, so you can tell whether a sheet has been read.

Some practical notes on locations: a bank safe deposit box is secure but may be sealed on your death, exactly when your heir needs it. A home safe is accessible but is the first place a burglar looks. Most people end up using both, splitting differently.

---

## Testing your backup

An untested backup is a guess.

Restore the seed onto a spare device or into offline wallet software, confirm it produces the same master fingerprint written on Sheet 1, then wipe the test device. Record it in the log on Sheet 4.

Repeat every year or two, and after every house move — moves are when backups get separated from the people who know what they are.

If you use a passphrase, test the seed *and* passphrase together. Testing only the seed proves nothing about the half you're most likely to get wrong.

---

## Things that lose funds

**Photographing the sheets.** The most common failure by a wide margin. Phone photos sync to cloud storage automatically, and cloud storage gets breached. This includes photographing them "just temporarily".

**Typing the words into anything.** No legitimate service, wallet, exchange or support agent ever needs your seed words. Everyone who asks is stealing from you, without exception — including anyone who contacts you offering to help recover a wallet.

**Backing up the seed but not the descriptor.** Covered above, and worth repeating: for multisig, this is the one that gets people.

**Storing the passphrase with the seed in a single-sig wallet.** It makes the passphrase decorative.

**Never testing.** You find out your backup is wrong at the exact moment you can no longer fix it.

---

## Recovering

If you're reading this because you need to recover a wallet: there is no emergency. Funds don't expire. Rushing is how people lose money at this stage.

Read Sheet 4 first, in full. Then find out whether Sheet 1 lists a multisig wallet — if so, locate the wallet configuration record before you do anything else.

If you need help, ask a Bitcoin professional you've verified independently: a firm with a real address and a reputation, never someone who contacted you. Show them Sheet 4 and nothing else. A trustworthy helper will never need to see or hold your seed words.

---

## Contributing

This is an open-source project and contributions are welcome. Translations are the most valuable — BIP39 has wordlists in ten languages, and each one needs a version of this sheet.

Every released version stays permanently downloadable. If you're recovering from an older sheet, you need that version's exact wording and layout, not the current one.
