# tydda-texter

Transkription av handlingar från ett hemman i Överpurmo by, Pedersöre socken,
Österbotten: Härmälä N:o 6 och från 1843 Sandnabba N:o 8, 1802–1966.

**Webbvisare (bild och transkription sida vid sida):**
https://joablo.github.io/tydda-texter/

## Innehåll

- `bilder/` – fotografierna, 001.jpg–326.jpg i kronologisk ordning
- `transkriptioner/` – en .md-fil per bild med numrerad transkription, osäkra
  passager, helhetsbedömning, dubbelläsning och rättelser
- `namn.md` – personer, orter, skrivarhänder, förkortningar, kronologi och
  konventioner
- `beslut.md` – beslutslogg: öppna frågor, bilder som bör tas om
- `CLAUDE.md` – arbetsregler för transkriptionen
- `index.html`, `pages.json`, `bygg_index.py` – webbvisaren. Kör
  `python3 bygg_index.py` när transkriptionerna ändrats, så uppdateras
  `pages.json` (sidlista, sökindex och statistik).

Lokalt: `python3 -m http.server` i mappen och öppna http://localhost:8000/
(sidan läser filerna med fetch och fungerar inte som `file://`).
