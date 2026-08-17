# Changelog

Every released version of the printable document, newest first. Old
versions are never removed, replaced, or quietly corrected, because
someone recovering from a sheet printed years ago needs the version
they are actually holding to mean what it meant when they filled it in.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and versions follow [Semantic Versioning](https://semver.org/). The
document is not software, so the three numbers are read like this:

- **MAJOR** - a filled-in sheet from an earlier version now reads
  differently. The same marks on paper mean something else. Anyone
  holding an older sheet must read it against the version printed on
  it, never the current one.
- **MINOR** - fields added, removed, renamed, or moved. An older sheet
  still reads correctly, but the two versions are not the same form.
- **PATCH** - typo fixes, wording that does not change what belongs in
  a field, and pure layout adjustments.

Only the document is versioned. The site and the guide are not, and
they always describe the current document.

## [1.2] - 2026-08-17

- Download: <https://keybackup.org/keybackup-v1.2.html>
- SHA256: `15b0b2c02c3b79da09ac0901e7bd66851e68f342ee73b5d7f52877d7fa9cd151`

A filled-in v1.1 set needs no attention. Every field that existed in
v1.1 still means what it meant. v1.2 is a shorter, less wordy document
that leans on [the guide](https://keybackup.org/guide/) for the
explanations, and spends the space it saves on room to write.

### Added

- Sheet 3 records a digital copy of the passphrase, if you keep one:
  where it is, the password or key that opens it, and a notes area. A
  passphrase on its own cannot spend, so a copy in a password manager is
  a different risk from a copy of the seed words. What loses funds is a
  copy nobody can find.
- Sheet 4 records where the owner's own instructions live, with the same
  three fields. Whatever you wrote about your wallets, your heirs, or
  your reasoning belongs somewhere a stranger holding this sheet can
  actually reach it.

### Changed

- The explanatory text is cut back to what you need in your hand. v1.1
  explained its own reasoning on the page. v1.2 keeps the instructions
  you have to follow to fill a sheet in correctly, and the warnings a
  stranger needs during a recovery, and moves the rest to the guide.
  Nothing was lost: everything trimmed off the sheets is covered there.
- Every footer now points at the guide, replacing "never photograph,
  never type into any device, never share". That warning moved to the
  header of Sheets 1, 2 and 3, which are the sheets it applies to.
  Sheet 4 still carries it in full as a numbered instruction.
- Much more room to write, paid for by the text that came off. v1.1
  gave a write-in line about 4mm of clearance above it, which is not
  enough for an address or a long name. Sheet 1's five sections now get
  around 8mm and the name-and-contact blocks around 9mm. The seed boxes
  on Sheet 2 and the passphrase boxes on Sheet 3 grew with them.
- Contact details are three fields, not two, everywhere they appear.
  Sheet 1's "who holds Sheet 3" and Sheet 3's "who holds the seed words"
  now ask for a name, an email and a telephone number, the way Sheet 4's
  contact block already did.
- The master fingerprint on Sheet 3 is always filled in. v1.1 asked for
  it only if the sheet was held separately. It costs nothing to write,
  it cannot move funds, and it is what keeps a passphrase sheet matched
  to its wallet when you hold sets for more than one.

### Removed

- "How to reach them" on Sheets 1 and 3, replaced by the email and
  telephone fields above.
- The optional hint field on Sheet 3. A hint that means nothing to a
  stranger and still means something to you in twenty years is close to
  impossible to write, and a hint that fails either test is a liability.
- The "last thing" note on Sheet 4. Steel backups and two buildings are
  advice for the owner, not for the stranger this sheet is addressed to.
  It is still in the guide.

## [1.1] - 2026-08-13

- Download: <https://keybackup.org/keybackup-v1.1.html>
- SHA256: `9361e76fcc6a0a3183bf06b71933e84b0f4f32b1c717d2b23fc9c32a0446dc2f`

A filled-in v1.0 set still recovers a wallet, but read it with v1.0 in
hand rather than v1.1. The passphrase sheet is the one place the two
versions read differently, noted under Changed below.

By the rule stated at the top of this file that difference is a MAJOR
change, and v1.1 should have been v2.0. It was released as v1.1 and
stays released as v1.1, because the number printed on a sheet is how
someone finds the right version to read it against, and renumbering it
afterwards would break exactly the thing versioning is here to protect.

### Added

- The master fingerprint appears on Sheet 2 as well as Sheet 1, since
  sheets get separated. It carries a tick for whether it is the
  fingerprint for the seed plus its passphrase, or for the seed alone,
  in which case Sheet 3 is unused and can be discarded.
- A ninth box per seed word. The longest word on the BIP39 English list
  is eight letters, so v1.0 had no room for a slip. The spare box
  supports the new correction rule: a letter written wrong gets its box
  filled in solid with black ink, and the writing carries on in the next
  box. The same rule applies to the passphrase sheet.
- Sheets 2 and 3 record which case was used. BIP39 words are always
  lowercase whatever you write, so capitals there are purely a
  legibility choice, but a reader should not have to guess.
- Sheet 1 records a device number alongside the serial number.
- A second handwriting-key block on Sheet 4. One is lowercase and one is
  capitals, because the character pairs that get confused are not the
  same in each.

### Changed

- **The passphrase now runs together with no spaces.** v1.0 separated
  the words with single spaces and left a box empty for each one. On
  paper an empty box is ambiguous: it could be a space, or it could be
  where the passphrase ended, and a space at either end is invisible
  entirely. Removing spaces removes the whole failure mode and costs
  nothing in strength. **This is the change that reads a v1.0 sheet
  differently**: on a v1.0 passphrase sheet, an empty box still means a
  space.
- Renamed to **Bitcoin Key Backup Record**. It records a key, not only a
  seed.
- Passphrase guidance rewritten. True randomness, and a length that
  depends on the list: at least 7 words from the BIP39 English wordlist,
  6 from the EFF long wordlist, or 5 from the whole English dictionary.
  Mixed case is allowed. v1.0 asked for four lowercase BIP39 words,
  which is too short.
- Sheet 4 asks for one contact with name, email and telephone, rather
  than two contacts with no fixed fields.
- Sheet 4 gave up vertical room to fit the second handwriting block:
  tighter step spacing and five test-log rows per column instead of six.

### Fixed

- v1.0 claimed the sheets were lowercase only, which was never true.
  Capitals were always allowed.
- Dropped "the BIP39 25th word" from the passphrase sheet. It is a
  common nickname but not what a passphrase actually is.

## [1.0] - 2026-08-10

- Download: <https://keybackup.org/keybackup-v1.0.html>
- SHA256: `cb007de4b673c29958d3e4a0726e7f51682889fd365b15d6a824eaf041fbccab`

First release. Four sheets: key identity and the multisig index, seed
words, passphrase, and instructions with a handwriting key and recovery
test log.

[1.2]: https://keybackup.org/keybackup-v1.2.html
[1.1]: https://keybackup.org/keybackup-v1.1.html
[1.0]: https://keybackup.org/keybackup-v1.0.html
