#!/usr/bin/env python3
"""Bygger pages.json för webbvisaren (index.html).

Kör:  python3 bygg_index.py
Läser transkriptioner/NNN.md och skriver pages.json med metadata och
transkriptionstext per sida (för sidlista, sökning och statistik).
Kör om skriptet varje gång transkriptionerna ändrats.
"""
import json, re, pathlib

ROT = pathlib.Path(__file__).parent
UT = ROT / "pages.json"
MARK = re.compile(r"\[[^\]]*\?\]|\[oläsligt\]|\[\.\.\.\]")

def kort(s, n=160):
    s = re.sub(r"\*\*|`", "", s).strip()
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"

sidor = []
for p in sorted((ROT / "transkriptioner").glob("[0-9][0-9][0-9].md")):
    t = p.read_text(encoding="utf-8")
    nr = p.stem
    m = re.search(r"^\*\*Dokumenttyp:\*\*\s*(.+)$", t, re.M)
    doktyp = kort(m.group(1)) if m else ""
    m = re.search(r"^## Helhetsbedömning\s*\n+\s*\*\*Säkerhet:\s*([^*]+?)\.?\*\*", t, re.M)
    sak = m.group(1).strip() if m else ""
    sak = re.sub(r"[.,;:]+$", "", sak)
    m = re.search(r"^```\n(.*?)^```", t, re.M | re.S)
    block = m.group(1) if m else ""
    rader = [r for r in block.splitlines() if r.strip()]
    sidor.append({
        "nr": nr,
        "bild": f"bilder/{nr}.jpg",
        "fil": f"transkriptioner/{nr}.md",
        "doktyp": doktyp,
        "sakerhet": sak,
        "rader": len(rader),
        "osakra": len(MARK.findall(block)),
        "dubbel": "## Dubbelläsning" in t,
        "rattad": "## Rättelser efter dubbelläsning" in t,
        "tredje": "## Tredje läsning" in t,
        "extern": "Extern källa" in t or "extern källa" in t,
        "text": block,
    })

UT.write_text(json.dumps(sidor, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"{len(sidor)} sidor → {UT.name} ({UT.stat().st_size // 1024} kB)")
