# Maskinläsning (HTR)

Rå utdata från Transkribus-modellen **The Swedish Lion I** (modell 55158, Olof Karsvall 2023;
PyLaia; tränad på 61 356 sidor svensk handskrift 1600–1800-tal från Riksarkivet,
Kansallisarkisto m.fl.; https://www.transkribus.org/models/swedish-lion-i).

- `swedish-lion/NNN.txt` – modellens text för bild NNN, oredigerad, en rad per rad modellen hittade
  (radindelningen följer modellens egen segmentering, inte transkriptionens radnummer).
- Körd av ägaren i Transkribus webbapp och inklistrad här.

Hur den används: modellen är en **fjärde, oberoende läsare** (efter första läsning,
dubbelläsning och tredje läsning). Den markerar ingen osäkerhet och förvanskar ofta namn och
siffror, så den är aldrig facit. Varje skillnad prövas mot bilden; rättelser görs bara med
konkret grund i bilden och dokumenteras i transkriptionsfilen under
"## Maskinläsning (Transkribus, The Swedish Lion I)" och "## Rättelser efter dubbelläsning",
märkta "Extern källa: Transkribus, The Swedish Lion I (modell 55158)" (CLAUDE.md regel 7).
