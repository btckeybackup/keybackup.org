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

## The two-document concept

The backup is deliberately split in two, because the two halves have
completely different security properties and belong in different
places.

**Key Backup Record**, one per key, **secret**. The four printed
sheets in this repository. They hold the seed words and the passphrase.
Anyone holding sheets 2 and 3 together can move the funds, so these are
handled like bearer cash: written by hand, never photographed, never
typed into any device, stored in a safe or a deposit box. You fill in
one set per key, so a 2-of-3 multisig means three sets, usually held by
three different people or in three different places.

**Wallet Configuration Record**, one per wallet, **not secret**, copy
freely. This holds the descriptor and every co-signer's xpub: the
information that says how the keys combine into a wallet. It cannot
move funds on its own and it reveals no private key. Its only real risk
is a privacy one, since an xpub exposes a wallet's transaction history
to whoever holds it.

The asymmetry is the point. The secret half must be scarce and hidden,
which makes it easy to lose. The non-secret half must be abundant,
because losing it is what actually strands multisig funds. Keep at
least one copy of the configuration record somewhere that holds no seed
words at all, so that the copy most likely to survive is the one that
is safe to leave lying around.

The configuration record is not yet in this repository. It is the next
document to be written.

## Download

The current document is **v1.0**.

- <https://keybackup.org/keybackup-v1.0.html>

It is a single self-contained HTML file. Open it in any browser and
print it. It has no scripts, no webfonts, and makes no network
requests, so it works offline from a local file, and works the same in
ten years as it does today. Print at 100% or Actual Size, never Fit to
Page. Sheet 1 carries a 100mm ruler so you can confirm your printer did
not scale the page.

Every released version stays downloadable permanently. Someone
recovering from a v1.0 sheet needs v1.0 semantics, so old versions are
never removed or quietly changed.

## Verifying the download

The document is what you are trusting your coins to, so check that the
file you received is the file that was published. Compare its SHA256
against the value published with the release:

```
# macOS
shasum -a 256 keybackup-v1.0.html

# Linux
sha256sum keybackup-v1.0.html
```

Expected for v1.0:

```
d1810df4f9ebf94610ee02e4b9c61b5b6257b2f6c276acf6ab7311c0e875edf8
```

If the value does not match, do not use the file.

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
```

The site is Vite plus Pico CSS, with no framework.

The printable document at `public/keybackup-v1.0.html` is deliberately
not part of the build. Files in `public/` are copied byte for byte,
which is what keeps the document self-contained. Nothing bundles it,
nothing minifies it, and nothing may add an external reference to it.

## Licence

Two licences, because the repository holds two different kinds of thing.

**The printable document is public domain.** `public/keybackup-v*.html`
and `reference/keyrecord.py` are released under
[CC0 1.0 Universal](LICENSE-DOCUMENT): copy it, print it, sell it,
translate it, fork it, no permission or attribution needed. A backup
sheet should never have to carry a legal notice into a safe deposit
box.

**Everything else is [MIT](LICENSE).** The site source, build config
and tooling. Standard permissive terms, attribution required.

## Contributing

Contributions are welcome, translations most of all. See
[CONTRIBUTING.md](CONTRIBUTING.md).
