# keybackup

An open-source printable paper backup for Bitcoin wallets, and a small
static site explaining how to use it.

Most Bitcoin backups fail the same way. People back up the seed phrase
and stop there. But a seed phrase on its own is often not enough to
find the coins again: recovery also needs the wallet configuration, the
derivation path, the script type, the passphrase if one was set, and
for multisig, every other co-signer's extended public key. That
information usually lives only inside the wallet software, so when the
laptop dies or the app is discontinued, it is gone.

keybackup gives that information a fixed place to live, on paper, in a
format a stranger can follow.

## What these sheets cover

keybackup backs up **keys**. One set of four sheets per key, holding
the seed words, the passphrase, and the details that make them usable
years later. Anyone holding sheets 2 and 3 together can move the funds,
so a filled-in set is handled like bearer cash: written by hand, never
photographed, never typed into any device.

For a **single-signature** wallet that is the whole job. The seed words
on Sheet 2 recover your funds and you need nothing else.

## Multisig needs a second backup, and keybackup does not supply it

For a **multisig** wallet, the seed words alone recover **nothing**. You
also need the wallet descriptor: the record of the quorum, the
derivation paths, and every co-signer's xpub. You can hold every seed in
the quorum, and without the descriptor still be unable to rebuild the
wallet or find your own coins. This is the most common way multisig
funds are lost.

That descriptor backup is yours to create and hold. These sheets are
not it. Sheet 1 has a table for recording *which* multisig wallets a key
belongs to, but that table is an index, so a future recoverer knows what
to go looking for. It does not rebuild anything. The eight-character
checksum field catches a transcription error in a descriptor you already
have; it cannot reconstruct one.

**The recommended form is a BC-UR2 QR code of the wallet descriptor,
printed on paper.** BC-UR2 is a Blockchain Commons encoding that Bitcoin
wallets and signing devices already understand, so the descriptor gets
scanned back in rather than retyped. A descriptor is a long run of xpubs
full of confusable characters, and copying it by hand is exactly the
transcription risk these sheets exist to remove. Print the plain
descriptor text beside the QR as a fallback, in case nothing to hand can
scan that format years from now.

### Store it *with* the key backups, not away from them

Keep a copy alongside the paper backup of **every** signing key in the
wallet.

This is safe, and the reason is worth understanding. The descriptor
cannot spend anything on its own. Nor can the descriptor plus a single
key: spending needs as many keys as your quorum requires, and those live
in separate places. So putting the descriptor next to one key backup
adds no ability to steal that was not already there. Separating them, on
the other hand, creates exactly the gap that strands multisig funds,
because the descriptor is the piece most likely to be missing when
someone finally needs it.

The rule holds because your quorum is more than one signature. A 1-of-N
policy is the exception: there, one key plus the descriptor is enough to
spend, so treat the pair as you would a single-sig seed.

Someone who had already gathered enough of your keys to meet the quorum
would of course find the descriptor sitting beside them. That is true,
and it is still not a reason to separate them. If an attacker holds two
of your three keys you have already lost, and withholding the descriptor
buys a short delay against an adversary who has won, at the price of a
recovery failure that is far more likely to actually happen.

Extra copies cost you nothing in spendability. They do cost privacy: an
xpub reveals a wallet's whole transaction history to whoever holds it.

| | These four sheets | Your descriptor backup |
|---|---|---|
| Needed for | every key | multisig only |
| Supplied by keybackup | yes | no, you create it |
| One per | key | wallet |
| Secret | yes, treat as bearer cash | no private keys, but reveals history |
| Copies | as few as you can manage | one with each key's backup |
| Losing it | loses one key | loses the whole wallet |

## Download

The current document is **v1.2**.

- <https://keybackup.org/keybackup-v1.2.html>

It is a single self-contained HTML file. Open it in any browser and
print it. It has no scripts, no webfonts, and makes no network
requests, so it works offline from a local file, and works the same in
ten years as it does today. Print at 100% or Actual Size, never Fit to
Page. Sheet 1 carries a 100mm ruler so you can confirm your printer did
not scale the page.

Every released version stays downloadable permanently, because someone
recovering from a v1.0 sheet needs v1.0 semantics. Old versions are
never removed or quietly changed. [CHANGELOG.md](CHANGELOG.md) lists
every release, what changed in it, and where to download it.

### What changed in v1.2

v1.2 is a shorter, less wordy document that leans on
[the guide](https://keybackup.org/guide/) for the explanations and
spends the space it saves on room to write. A filled-in v1.1 set needs
no attention: every field that existed in v1.1 still means what it
meant.

See [CHANGELOG.md](CHANGELOG.md) for the full list, and for every
earlier release.

## Verifying the download

The document is what you are trusting your coins to, so check that the
file you received is the file that was published. Compare its SHA256
against the value published with the release:

```
# macOS
shasum -a 256 keybackup-v1.2.html

# Linux
sha256sum keybackup-v1.2.html
```

Expected for v1.2:

```
15b0b2c02c3b79da09ac0901e7bd66851e68f342ee73b5d7f52877d7fa9cd151
```

If the value does not match, do not use the file. Checksums for earlier
releases are published with each release in [CHANGELOG.md](CHANGELOG.md).

This is a check against a corrupted or tampered download, not a proof
of origin. Anyone who could replace the file could also replace a
checksum printed next to it, so treat a match as a sanity check rather
than a guarantee.

## Building locally

Requires Node 20 or newer.

```
npm install
npm run dev      # local dev server
npm run build    # static site into dist/
npm run preview  # serve the built site
npm run sheets   # re-render the sheet images from the current document
```

The site is Vite plus Tailwind v4, with no framework. Fonts are
self-hosted and icons are inlined, so the site makes no third-party
requests either.

The printable documents at `public/keybackup-v*.html` are deliberately
not part of the build. Files in `public/` are copied byte for byte,
which is what keeps the document self-contained. Nothing bundles it,
nothing minifies it, and nothing may add an external reference to it.

The published checksums are taken from those files directly, so any
edit to a document means recomputing the value in this README and in
the changelog:

```
shasum -a 256 public/keybackup-v*.html
```

## Licence

Two licences, because the repository holds two different kinds of thing.

**The printable document is public domain.** `public/keybackup-v*.html`
is released under [CC0 1.0 Universal](LICENSE-DOCUMENT): copy it, print
it, translate it, adapt it, fork it, no permission or attribution
needed. A backup sheet should never have to carry a legal notice into a
safe deposit box.

**Everything else is [MIT](LICENSE).** The site source, build config
and tooling. Standard permissive terms, attribution required.

## Contributing

Contributions are welcome, translations most of all. See
[CONTRIBUTING.md](CONTRIBUTING.md).
