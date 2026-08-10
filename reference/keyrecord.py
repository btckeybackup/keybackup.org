#!/usr/bin/env python3
"""Bitcoin signing key backup record - printable blank template."""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.units import mm
from reportlab.lib.colors import black, white, HexColor

PROJECT = "seedbackup.org"
VERSION = "v1.0"

GREY = HexColor("#767676")
LIGHT = HexColor("#BFBFBF")
RULE = HexColor("#9A9A9A")
DARK = HexColor("#1A1A1A")


class Sheet:
    def __init__(self, path, pagesize):
        self.c = canvas.Canvas(path, pagesize=pagesize)
        # Lay everything out in A4 geometry, then fit that block to the real
        # page size with a single uniform scale. Letter is 18mm shorter than
        # A4, which overflowed the footer when the layout was drawn directly.
        self.W, self.H = A4
        ow, oh = pagesize
        self.k = min(ow / self.W, oh / self.H)
        self.dx = (ow - self.W * self.k) / 2.0
        self.dy = (oh - self.H * self.k) / 2.0
        self.M = 15 * mm
        self.CW = self.W - 2 * self.M
        self.c.setTitle("Bitcoin Seed Backup Record %s" % VERSION)
        self.c.setAuthor("")
        self.c.setSubject("Blank backup template - %s %s" % (PROJECT, VERSION))

    def _begin(self):
        self.c.saveState()
        self.c.translate(self.dx, self.dy)
        self.c.scale(self.k, self.k)

    # ---------- primitives ----------

    def text(self, x, y, s, size=9, font="Helvetica", color=DARK):
        self.c.setFillColor(color)
        self.c.setFont(font, size)
        self.c.drawString(x, y, s)

    def ctext(self, x, y, s, size=9, font="Helvetica", color=DARK):
        self.c.setFillColor(color)
        self.c.setFont(font, size)
        self.c.drawCentredString(x, y, s)

    def rtext(self, x, y, s, size=9, font="Helvetica", color=DARK):
        self.c.setFillColor(color)
        self.c.setFont(font, size)
        self.c.drawRightString(x, y, s)

    def wrap(self, x, y, w, s, size=8, leading=None, font="Helvetica", color=DARK):
        """Very small word-wrapper. Returns y after the last line."""
        leading = leading or size * 1.35
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        words = s.split()
        line = ""
        for word in words:
            trial = (line + " " + word).strip()
            if self.c.stringWidth(trial, font, size) <= w:
                line = trial
            else:
                self.c.drawString(x, y, line)
                y -= leading
                line = word
        if line:
            self.c.drawString(x, y, line)
            y -= leading
        return y

    def band(self, y, label, h=7.0 * mm):
        """Solid section header bar."""
        self.c.setFillColor(DARK)
        self.c.rect(self.M, y - h, self.CW, h, stroke=0, fill=1)
        self.c.setFillColor(white)
        self.c.setFont("Helvetica-Bold", 9.5)
        self.c.drawString(self.M + 2.5 * mm, y - h + 2.3 * mm, label.upper())
        return y - h - 4 * mm

    def rule(self, y, x=None, w=None, color=RULE, lw=0.5):
        x = self.M if x is None else x
        w = self.CW if w is None else w
        self.c.setStrokeColor(color)
        self.c.setLineWidth(lw)
        self.c.line(x, y, x + w, y)

    def field(self, x, y, w, label, h=8 * mm, size=7):
        """Underlined write-in field with a small caption above the line."""
        self.text(x, y + 1.2 * mm, label.upper(), size=size, color=GREY)
        self.rule(y - h + 2.5 * mm, x, w)
        return y - h

    def boxes(self, x, y, n, bw, bh, gap=0.0, lw=0.6, color=LIGHT):
        """Row of n empty boxes. y is the bottom edge."""
        self.c.setStrokeColor(color)
        self.c.setLineWidth(lw)
        for i in range(n):
            self.c.rect(x + i * (bw + gap), y, bw, bh, stroke=1, fill=0)
        return x + n * (bw + gap) - gap

    def checkbox(self, x, y, label, size=3.6 * mm, fsize=8.5, gap=1.8 * mm):
        self.c.setStrokeColor(GREY)
        self.c.setLineWidth(0.7)
        self.c.rect(x, y, size, size, stroke=1, fill=0)
        self.text(x + size + gap, y + 0.7 * mm, label, size=fsize)
        return x + size + gap + self.c.stringWidth(label, "Helvetica", fsize)

    def warnbox(self, y, lines, pad=3 * mm, size=8.2, title=None):
        """Boxed warning. lines = list of strings. Returns y below box."""
        leading = size * 1.35
        n = len(lines) + (1 if title else 0)
        h = n * leading + 2 * pad
        self.c.setStrokeColor(DARK)
        self.c.setLineWidth(1.1)
        self.c.rect(self.M, y - h, self.CW, h, stroke=1, fill=0)
        ty = y - pad - size
        if title:
            self.text(self.M + pad, ty, title, size=size + 0.3, font="Helvetica-Bold")
            ty -= leading
        for ln in lines:
            self.text(self.M + pad, ty, ln, size=size)
            ty -= leading
        return y - h - 4 * mm

    def header(self, title, subtitle, page_no, secret=True):
        self._begin()
        y = self.H - self.M
        self.c.setFillColor(DARK)
        self.c.rect(self.M, y - 13 * mm, self.CW, 13 * mm, stroke=0, fill=1)
        self.c.setFillColor(white)
        self.c.setFont("Helvetica-Bold", 13)
        self.c.drawString(self.M + 3 * mm, y - 6.2 * mm, title)
        self.c.setFont("Helvetica", 7.6)
        self.c.drawString(self.M + 3 * mm, y - 10.6 * mm, subtitle)
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawRightString(self.M + self.CW - 3 * mm, y - 6.2 * mm,
                               "SECRET" if secret else "NOT SECRET")
        self.c.setFont("Helvetica", 7.6)
        self.c.drawRightString(self.M + self.CW - 3 * mm, y - 10.6 * mm,
                               "SHEET %d OF 4" % page_no)
        return y - 13 * mm - 6 * mm

    def footer(self, note):
        self.c.setFillColor(GREY)
        self.c.setFont("Helvetica", 6.8)
        self.c.drawString(self.M, self.M - 4 * mm, "%s %s  -  %s" % (PROJECT, VERSION, note))
        self.c.drawRightString(self.M + self.CW, self.M - 4 * mm,
                               "Never photograph. Never type into any device. Never share.")

    def page(self):
        self.c.restoreState()
        self.c.showPage()

    def save(self):
        self.c.save()


# ------------------------------------------------------------------ page 1

def page_one(s):
    y = s.header("BITCOIN SEED BACKUP RECORD",
                 "%s %s   |   Complete one set of these four sheets for each key. Store as you would bearer cash."
                 % (PROJECT, VERSION), 1)

    y = s.warnbox(y, [
        "Anyone holding Sheets 2 and 3 together can move these funds. This is not a document you keep on a desk.",
        "For multisig, these sheets alone recover NOTHING. You also need a backup of the WALLET DESCRIPTOR, which",
        "keybackup does not supply. Keep a copy of it WITH this sheet - a descriptor plus one key cannot spend.",
    ], title="BEFORE YOU WRITE ANYTHING")

    # --- 1 identification
    y = s.band(y, "1. Identification")
    col = s.CW / 3.0
    s.field(s.M, y, col - 5 * mm, "Wallet / key nickname")
    s.field(s.M + col, y, col - 5 * mm, "Date created (DD / MM / YYYY)")
    s.field(s.M + 2 * col, y, col - 5 * mm, "This is copy ______ of ______")
    y -= 11 * mm

    # --- 2 device
    y = s.band(y, "2. Key origin - the device or software this key was created on")
    s.field(s.M, y, col - 5 * mm, "Make, brand or software")
    s.field(s.M + col, y, col - 5 * mm, "Model, edition or version")
    s.field(s.M + 2 * col, y, col - 5 * mm, "Serial number (if any)")
    y -= 11 * mm
    s.field(s.M, y, col - 5 * mm, "Firmware / app version at creation")
    s.field(s.M + col, y, col - 5 * mm, "Created by")
    x = s.M + 2 * col
    s.text(x, y + 1.2 * mm, "ENTROPY SOURCE", size=7, color=GREY)
    for lbl in ["Device", "Dice", "Imported"]:
        x = s.checkbox(x, y - 5 * mm, lbl, size=3.2 * mm, fsize=7.5) + 4 * mm
    y -= 10 * mm
    s.field(s.M, y, s.CW,
            "If IMPORTED, state where this key came from and what else has ever held it (old device, paper backup, exchange)")
    y -= 8 * mm
    s.text(s.M, y, "Do not record the device PIN anywhere. The seed words already override it - a PIN only helps a thief.",
           size=7, color=GREY)
    y -= 7 * mm

    # --- 3 fingerprint
    y = s.band(y, "3. Master fingerprint - the one value that identifies this key")
    s.boxes(s.M, y - 8.5 * mm, 8, 9 * mm, 9 * mm)
    s.wrap(s.M + 80 * mm, y - 1 * mm, s.CW - 80 * mm,
           "Eight hex characters, taken from the master key at m - NOT from the account xpub. If a passphrase is "
           "used, load it first and record the fingerprint shown WITH the passphrase applied. That value is also how "
           "a future recoverer confirms they have the passphrase right. Hex only: digits 0-9 and letters a-f - so a "
           "circle is always 0, a bare vertical stroke is always 1, and there is never an o, l, s, g or z.", size=7, color=GREY)
    y -= 21 * mm
    s.field(s.M, y, s.CW,
            "If this key is also used as a single-signature wallet, its derivation path (optional - standard paths are found automatically)")
    y -= 11 * mm

    # --- 4 multisig wallets
    y = s.band(y, "4. Multisig wallets this key belongs to - OPTIONAL, leave blank for single-sig")
    s.wrap(s.M, y, s.CW,
           "Fill this in only if this key co-signs a multisig. The derivation path is a property of each WALLET, not "
           "of the key: the same device in two multisigs uses two different paths. This table is a convenience index "
           "only - your descriptor backup is what actually rebuilds the wallet.", size=7.2, color=DARK)
    y -= 11 * mm

    cw = [52 * mm, 20 * mm, 48 * mm]
    fpw = 6.5 * mm
    heads = ["WALLET NAME", "QUORUM", "DERIVATION PATH", "DESCRIPTOR CHECKSUM (8 CHARACTERS)"]
    sub = ["", "e.g. 2 of 3", "", ""]
    hx = s.M
    for i, h in enumerate(heads):
        s.text(hx + 1.2 * mm, y, h, size=6.2, color=GREY)
        if sub[i]:
            s.text(hx + 1.2 * mm, y - 3 * mm, sub[i], size=5.6, color=GREY)
        hx += cw[i] if i < len(cw) else 0
    y -= 5 * mm

    rh = 9.0 * mm
    for r in range(3):
        hx = s.M
        s.c.setStrokeColor(LIGHT)
        s.c.setLineWidth(0.6)
        for w in cw:
            s.c.rect(hx, y - rh, w, rh, stroke=1, fill=0)
            hx += w
        s.boxes(hx + 1.5 * mm, y - rh + 1.4 * mm, 8, fpw, rh - 2.8 * mm)
        y -= rh
    y -= 4.5 * mm

    s.text(s.M, y, "PATH DECODER   m/48'/0'/0'/2' = multisig, native segwit   |   a second multisig on the same device usually increments the third number: m/48'/0'/1'/2'",
           size=6.8, color=GREY)
    y -= 4.2 * mm
    s.text(s.M, y, "DESCRIPTOR CHECKSUM   the eight characters after the # at the end of the descriptor:", size=6.8, color=GREY)
    s.text(s.M + 100 * mm, y, "wsh(sortedmulti(2,[...]))#tjg09x5t", size=7, font="Courier-Bold")
    y -= 4.2 * mm
    s.text(s.M, y, "It never contains b, i, o or the digit 1 - so a circle is always 0, a bare vertical stroke is always l, and a 'b' shape is always 6.",
           size=6.8, color=GREY)
    y -= 7 * mm
    s.field(s.M, y, s.CW, "Where the wallet descriptor backup is kept (keep a copy with this sheet)")
    y -= 10 * mm

    # --- 5 custody
    y = s.band(y, "5. Custody and storage")
    third = s.CW / 3.0
    s.field(s.M, y, third - 5 * mm, "Where this copy is stored")
    s.field(s.M + third, y, third - 5 * mm, "Where the other copies are stored")
    s.field(s.M + 2 * third, y, third, "Sealed by / date sealed")
    y -= 11 * mm
    half = s.CW / 2.0
    s.field(s.M, y, half - 5 * mm, "If Sheet 3 is held by someone else, who holds it")
    s.field(s.M + half, y, half, "How to reach them")

    s.footer("Sheet 1 of 4 - Key identity and wallets")
    s.page()


# ------------------------------------------------------------------ page 2

def page_two(s):
    y = s.header("SEED WORDS (BIP39 ENGLISH WORDLIST)",
                 "Whoever holds these words holds the key. Print in archival pigment ink. Do not join letters up.", 2)

    y = s.warnbox(y, [
        "Length used:   [  ] 12 words      [  ] 18 words      [  ] 24 words        Strike through every unused row.",
        "Write the WORD NUMBER (1-2048) beside every word. If your handwriting is ever misread, the number saves you.",
    ], size=8.2)

    top = y
    rows = 12
    rh = 10.6 * mm
    colw = s.CW / 2.0

    for cidx in range(2):
        cx = s.M + cidx * colw
        s.text(cx + 12 * mm, top + 1 * mm, "WORD", size=6.5, color=GREY)
        s.text(cx + 62 * mm, top + 1 * mm, "NO. (1-2048)", size=6.5, color=GREY)
        for r in range(rows):
            n = cidx * rows + r + 1
            yy = top - (r + 1) * rh
            s.rtext(cx + 8 * mm, yy + 3.6 * mm, "%d." % n, size=8.5, color=GREY)
            s.boxes(cx + 11 * mm, yy + 1.0 * mm, 8, 6.1 * mm, 8.8 * mm)
            s.boxes(cx + 62 * mm, yy + 1.0 * mm, 4, 5.6 * mm, 8.8 * mm)

    y = top - rows * rh - 7 * mm

    s.warnbox(y, [
        "The last word is a checksum, so any single mistyped word will be rejected outright by wallet software. A",
        "phrase that 'almost works' means a transcription error, not a lost wallet - re-read this sheet against the",
        "handwriting key on Sheet 4. Only the first four letters of each word are needed to identify it.",
    ], title="IF YOU ARE RECOVERING AND IT DOES NOT WORK", size=8)

    s.footer("Sheet 2 of 4 - Seed words")
    s.page()


# ------------------------------------------------------------------ page 3

def page_three(s):
    y = s.header("PASSPHRASE - THE BIP39 25TH WORD",
                 "This sheet may be held separately from Sheets 1 and 2. Read the box below before storing it.", 3)

    y = s.warnbox(y, [
        "This sheet CANNOT move any funds on its own. It is worthless without the seed words on Sheet 2, and the",
        "seed words are worthless without it. Held by two different people, the two halves work like a 2-of-2 lock.",
        "SINGLE-SIG: splitting is the point. Keeping this sheet beside Sheet 2 cancels the passphrase out entirely.",
        "MULTISIG: keeping it beside Sheet 2 is usually correct - one compromised key still cannot spend, and the",
        "far greater risk is that you or your heir never recovers the passphrase at all.",
    ], title="WHAT THIS SHEET IS", size=8)

    x = s.M
    x = s.checkbox(x, y - 3 * mm, "No passphrase used - destroy this sheet", fsize=8.5) + 10 * mm
    x = s.checkbox(x, y - 3 * mm, "In use, stored with Sheets 1-2", fsize=8.5) + 10 * mm
    s.checkbox(x, y - 3 * mm, "In use, stored separately", fsize=8.5)
    y -= 13 * mm

    y = s.band(y, "How to choose one")
    s.wrap(s.M, y, s.CW,
           "Use four or more words from the BIP39 English wordlist, all lowercase, separated by single spaces. "
           "Nothing else: no capitals, no punctuation, no accented letters, no emoji, and never a space at the start "
           "or end. Those characters are invisible on paper or normalised differently by different wallets.", size=8)
    y -= 17 * mm

    y = s.band(y, "The passphrase - one character per box, one empty box per space")
    per_row = 20
    bw = s.CW / per_row
    for r in range(5):
        s.rtext(s.M - 2 * mm, y - 7.8 * mm, "%d" % (r * per_row + 1), size=6, color=GREY)
        s.boxes(s.M, y - 11.6 * mm, per_row, bw, 11.6 * mm)
        y -= 12.8 * mm
    y -= 2 * mm

    s.text(s.M, y, "WRITTEN ABOVE IN (tick one)", size=7, color=GREY)
    y -= 6.5 * mm
    x = s.M
    x = s.checkbox(x, y, "Exactly the characters used", fsize=8.5) + 14 * mm
    s.checkbox(x, y, "CAPITALS for legibility only - the real passphrase is all lowercase", fsize=8.5)
    y -= 12 * mm

    # --- identity block for a separately-held sheet
    y = s.band(y, "If this sheet is held separately - complete all of this")
    s.boxes(s.M, y - 8.5 * mm, 8, 8 * mm, 8.5 * mm)
    s.text(s.M, y + 1.2 * mm, "MASTER FINGERPRINT (COPY FROM SHEET 1)", size=6.5, color=GREY)
    s.wrap(s.M + 74 * mm, y - 0.5 * mm, s.CW - 74 * mm,
           "This says which wallet the passphrase belongs to, and lets the holder of the seed confirm the passphrase "
           "is right: load seed plus passphrase, and the device must show this exact fingerprint. It reveals nothing "
           "on its own. Leave blank if this sheet stays with Sheet 1.", size=6.8, color=GREY)
    y -= 15 * mm
    half = s.CW / 2.0
    s.field(s.M, y, half - 5 * mm, "Who holds the seed words (Sheets 1 and 2)")
    s.field(s.M + half, y, half, "How to reach them")
    y -= 11 * mm
    s.field(s.M, y, s.CW,
            "Optional hint (must mean nothing to a stranger, and must still mean something to you in twenty years)")

    s.footer("Sheet 3 of 4 - Passphrase")
    s.page()


# ------------------------------------------------------------------ page 4

def page_four(s):
    y = s.header("INSTRUCTIONS FOR WHOEVER IS READING THIS",
                 "Print one copy of this sheet for every person holding any part of the backup.", 4,
                 secret=False)

    steps = [
        ("What this is",
         "These sheets back up a Bitcoin wallet. The words on Sheet 2 are the equivalent of the key to a safe. They "
         "are not a password that can be reset, and no company anywhere can recover them for you."),
        ("Do this first: nothing",
         "There is no deadline and no emergency. Funds do not expire. Rushing is how people lose money here."),
        ("Never type, photograph or upload any of these sheets",
         "No legitimate service, app, exchange or support agent will ever ask for the words on Sheet 2 or the "
         "passphrase on Sheet 3. Everyone who asks is stealing from you, without exception - including anyone who "
         "telephones or emails offering to help with this wallet. Do not scan these sheets, do not photograph them "
         "'just to be safe', do not put them in cloud storage, and do not email them to a relative."),
        ("You may be holding only part of it",
         "Sheet 3 is sometimes given to a different person from Sheets 1 and 2. Neither half can move funds alone. "
         "Whichever you hold, the contact details on it name the person holding the other."),
        ("Find the wallet descriptor backup",
         "If Sheet 1 lists a multisig wallet, the seed words alone are NOT enough. You also need the configuration "
         "backup named on Sheet 1, and the other keys."),
        ("Get competent help",
         "Ask a Bitcoin professional you verified independently - a firm with a real address and reputation, never "
         "someone who contacted you first. Show them this sheet only. A trustworthy helper never needs to hold your "
         "seed words."),
    ]

    for title, body in steps:
        s.text(s.M, y, title.upper(), size=8.3, font="Helvetica-Bold")
        y -= 4.3 * mm
        y = s.wrap(s.M + 4 * mm, y, s.CW - 4 * mm, body, size=7.9, leading=10.0)
        y -= 3.2 * mm

    y -= 0.5 * mm
    s.field(s.M, y, s.CW / 2 - 5 * mm, "Person to contact for help (name and how to reach them)")
    s.field(s.M + s.CW / 2, y, s.CW / 2, "Second contact")
    y -= 13 * mm

    # ---- handwriting key
    y = s.band(y, "Handwriting key - fill this in now, while you are still the one who can read it")
    s.wrap(s.M, y, s.CW,
           "Everything on these sheets is lowercase letters and digits only. These are the pairs that get confused. "
           "Write each one in the box beneath its name; the small word is how the character is spoken.", size=7.3)
    y -= 9 * mm

    pairs = [("0", "zero"), ("o", "oh"), ("1", "one"), ("l", "ell"),
             ("2", "two"), ("z", "zed"), ("5", "five"), ("s", "ess"),
             ("6", "six"), ("b", "bee"), ("9", "nine"), ("g", "gee"),
             ("u", "you"), ("v", "vee"), ("n", "en"), ("m", "em")]
    ncol = 8
    bw = s.CW / ncol
    for r in range(2):
        for i in range(ncol):
            ch, name = pairs[r * ncol + i]
            cx = s.M + i * bw
            s.ctext(cx + bw / 2, y - 3.2 * mm, ch, size=10, font="Courier-Bold")
            s.ctext(cx + bw / 2, y - 7.0 * mm, name, size=6, color=GREY)
            s.c.setStrokeColor(LIGHT)
            s.c.setLineWidth(0.6)
            s.c.rect(cx + 2 * mm, y - 17.0 * mm, bw - 4 * mm, 9 * mm, stroke=1, fill=0)
        y -= 19.5 * mm
    y -= 3.5 * mm

    # ---- test log
    y = s.band(y, "Recovery test log - an untested backup is a guess")
    s.wrap(s.M, y, s.CW,
           "Restore the seed onto a spare device, confirm it produces the master fingerprint on Sheet 1, then wipe "
           "the test device. Repeat every year or two, and after every house move.", size=7.3)
    y -= 8 * mm

    blockw = 85 * mm
    gap = s.CW - 2 * blockw
    cwid = [22 * mm, 46 * mm, 17 * mm]
    for b in range(2):
        bx = s.M + b * (blockw + gap)
        hx = bx
        for w, h in zip(cwid, ["DATE", "TESTED BY", "PASSED?"]):
            s.text(hx + 1.2 * mm, y, h, size=6, color=GREY)
            hx += w
    yy = y - 2 * mm
    for r in range(6):
        for b in range(2):
            bx = s.M + b * (blockw + gap)
            hx = bx
            s.c.setStrokeColor(LIGHT)
            s.c.setLineWidth(0.6)
            for w in cwid:
                s.c.rect(hx, yy - 6.2 * mm, w, 6.2 * mm, stroke=1, fill=0)
                hx += w
        yy -= 6.2 * mm
    y = yy - 5 * mm

    s.warnbox(y, [
        "Paper burns and fades. Transfer the seed words to stamped or punched stainless steel, and keep copies in",
        "two separate buildings. A backup you have never tested is a backup you do not have.",
    ], title="LAST THING", size=7.8)

    s.footer("Sheet 4 of 4 - Instructions, handwriting key, test log")
    s.page()


def build(path, pagesize):
    s = Sheet(path, pagesize)
    page_one(s)
    page_two(s)
    page_three(s)
    page_four(s)
    s.save()


if __name__ == "__main__":
    build("/mnt/user-data/outputs/seed-backup-record-%s-A4.pdf" % VERSION, A4)
    build("/mnt/user-data/outputs/seed-backup-record-%s-Letter.pdf" % VERSION, LETTER)
    print("done")
