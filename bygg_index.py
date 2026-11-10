#!/usr/bin/env python3
"""Bygger pages.json för webbvisaren (index.html).

Kör:  python3 bygg_index.py
Läser transkriptioner/NNN.md och namn.md och skriver pages.json med
  sidor      – metadata och transkriptionstext per bild (sidlista, sökning, statistik)
  dokument   – bilder grupperade till handlingar (dokumentvyn)
  kronologi  – tabellen "Handlingar och kronologi" i namn.md, sorterad (tidslinjen)
Kör om skriptet varje gång transkriptionerna eller namn.md ändrats.
"""
import json, re, pathlib

ROT = pathlib.Path(__file__).parent
UT = ROT / "pages.json"
MARK = re.compile(r"\[[^\]]*\?\]|\[oläsligt\]|\[\.\.\.\]")
# dokumenttypen börjar så här när bilden fortsätter föregående handling
FORTS = re.compile(r"^(Fortsättning|Fortsätter|Baksida|Sista sidan|Slutet|Samma sida|Samma blad|"
                   r"Högra|Andra sidan|Sida \d|Insidan|Tom sida|Närbild|Påskriftssida|"
                   r"Kyrkovärdens kvittens|Utsidan|Högra innersidan|Lös |Nytt avsnitt på samma)", re.I)

def kort(s, n=160):
    s = re.sub(r"\*\*|`", "", s).strip()
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"

def titel(doktyp):
    s = re.sub(r"\*\*|`", "", doktyp)
    s = re.sub(r"^(Nytt|Ny)\b[^:(]*(\([^)]*\))?[^:(]*:\s*", "", s)
    s = s[:1].upper() + s[1:]
    delar = re.split(r"(?<=[a-zåäö0-9\)]{3})\.\s", s)
    t = delar[0]
    if len(t) < 30 and len(delar) > 1:
        t += ". " + delar[1]
    return kort(t, 110)

sidor = []
for p in sorted((ROT / "transkriptioner").glob("[0-9][0-9][0-9].md")):
    t = p.read_text(encoding="utf-8")
    nr = p.stem
    m = re.search(r"^\*\*Dokumenttyp:\*\*\s*(.+)$", t, re.M)
    doktyp_full = m.group(1) if m else ""
    m = re.search(r"^## Helhetsbedömning\s*\n+\s*\*\*Säkerhet:\s*([^*]+?)\.?\*\*", t, re.M)
    sak = re.sub(r"[.,;:]+$", "", m.group(1).strip()) if m else ""
    m = re.search(r"^```\n(.*?)^```", t, re.M | re.S)
    block = m.group(1) if m else ""
    rader = [r for r in block.splitlines() if r.strip()]
    sidor.append({
        "nr": nr,
        "bild": f"bilder/{nr}.jpg",
        "fil": f"transkriptioner/{nr}.md",
        "doktyp": kort(doktyp_full),
        "fortsattning": bool(FORTS.match(re.sub(r"\*\*", "", doktyp_full))),
        "titel": titel(doktyp_full),
        "sakerhet": sak,
        "rader": len(rader),
        "osakra": len(MARK.findall(block)),
        "dubbel": "## Dubbelläsning" in t,
        "rattad": "## Rättelser efter dubbelläsning" in t,
        "tredje": "## Tredje läsning" in t,
        "extern": "xtern källa" in t,
        "text": block,
    })

# dokument: en ny handling börjar när bilden inte är en fortsättning
dokument = []
for s in sidor:
    if not dokument or not s["fortsattning"]:
        dokument.append({"id": len(dokument), "titel": s["titel"], "sidor": []})
    dokument[-1]["sidor"].append(s["nr"])
    s["dok"] = dokument[-1]["id"]
for s in sidor:
    del s["fortsattning"], s["titel"]

# kronologi ur namn.md
kronologi = []
namn = (ROT / "namn.md").read_text(encoding="utf-8")
sek = re.search(r"^## Handlingar och kronologi.*?\n(.*?)(?=^## )", namn, re.M | re.S)
if sek:
    for r in sek.group(1).splitlines():
        if not r.startswith("|") or re.match(r"^\|[\s:|-]+\|?\s*$", r) or r.startswith("| Datum"):
            continue
        c = [x.strip() for x in r.strip().strip("|").split("|")]
        if len(c) < 3:
            continue
        ar = re.search(r"\b(1[789]\d\d)\b", c[0])
        kronologi.append({"datum": c[0], "handling": c[1], "kalla": c[2],
                          "sort": (c[0][:10] if ar else "9999")})
kronologi.sort(key=lambda k: k["sort"])

# miniatyrer för dokumentvyn (bilder/thumb/NNN.jpg, 600 px) – skapas om de saknas eller är äldre
try:
    from PIL import Image, ImageOps
    (ROT / "bilder" / "thumb").mkdir(exist_ok=True)
    for s in sidor:
        src, dst = ROT / s["bild"], ROT / "bilder" / "thumb" / f"{s['nr']}.jpg"
        if src.exists() and (not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime):
            im = ImageOps.exif_transpose(Image.open(src)); im.thumbnail((600, 800))
            im.convert("RGB").save(dst, quality=72, optimize=True)
except ImportError:
    print("Pillow saknas – miniatyrerna uppdaterades inte (pip install pillow)")

def md_tabellrader(text):
    """Alla datarader i markdown-tabeller som lista av cellistor (rubrikrader hoppas över)."""
    ut, rubrik = [], True
    for r in text.splitlines():
        if not r.startswith("|"):
            rubrik = True
            continue
        if re.match(r"^\|[\s:|-]+\|?\s*$", r):
            continue
        if rubrik:  # första raden i varje tabell är rubriken
            rubrik = False
            continue
        ut.append([c.strip() for c in r.strip().strip("|").split("|")])
    return ut

# ordlista ur ordlista.md – former (`…`) används för understrykning i transkriptionerna
ordlista = []
p = ROT / "ordlista.md"
if p.exists():
    for c in md_tabellrader(p.read_text(encoding="utf-8")):
        if len(c) < 4:
            continue
        former = re.findall(r"`([^`]+)`", c[1])
        if former:
            ordlista.append({"ord": c[0], "former": former, "forklaring": c[2], "grund": c[3],
                             "exempel": c[4] if len(c) > 4 else ""})

# släktträd ur slakttrad.md
slakt = []
p = ROT / "slakttrad.md"
if p.exists():
    nycklar = ["id", "namn", "levnad", "far", "mor", "gift", "sak", "kalla", "anm", "sok"]
    for c in md_tabellrader(p.read_text(encoding="utf-8")):
        if len(c) >= 9 and re.match(r"^[a-z_0-9]+$", c[0]):
            d = dict(zip(nycklar, c + [""] * (10 - len(c))))
            d["gift"] = [x.strip() for x in d["gift"].split(",") if x.strip()]
            slakt.append(d)
    ids = {d["id"] for d in slakt}
    for d in slakt:
        for k in [d["far"], d["mor"], *d["gift"]]:
            if k and k not in ids:
                print(f"VARNING slakttrad.md: {d['id']} hänvisar till okänt ID '{k}'")

data = {"sidor": sidor, "dokument": dokument, "kronologi": kronologi, "ordlista": ordlista, "slakt": slakt}
UT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"{len(sidor)} sidor, {len(dokument)} dokument, {len(kronologi)} händelser, {len(ordlista)} ord, {len(slakt)} personer → {UT.name} "
      f"({UT.stat().st_size // 1024} kB)")
