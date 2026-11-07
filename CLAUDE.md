# Transkription av gamla handskrifter

## Kontext
- Tidsperiod: Kanske 1900–1970
- Språk: Svenska, ev. finska
- Typ av dokument: protojoll, kyrkbok, brev, dagbok
- Namn och orter som förekommer: Pedersöre, Sandnabba, Purmo, Österbotten, ...

## Mappar
- bilder/ – originalbilderna, numrerade 001.jpg, 002.jpg …
- transkriptioner/ – en .md-fil per bild med samma namn (001.jpg → 001.md)

## Arbetssätt
Du är en erfaren paleograf. Ta en bild i taget, i filnamnsordning.
Hoppa över bilder som redan har en fil i transkriptioner/.
Är bilden vriden, räta upp den och spara den rättvända versionen
i bilder/ innan du läser (originalet finns kvar i git-historiken).

## Regler för transkription
1. Återge texten exakt som den står – behåll gammal stavning,
   förkortningar, radbrytningar och överstrykningar. Modernisera inte.
2. Numrera varje rad (1, 2, 3 …) så att numreringen motsvarar
   originalets rader. Slå aldrig ihop rader.
3. Markera osäkerhet i texten:
   - [ord?] = osäker läsning
   - [ord1/ord2?] = två möjliga läsningar
   - [oläsligt] = går inte att läsa
   - [...] = skadad eller saknad text
4. Gissa aldrig tyst. Markera hellre osäkerhet än att skriva
   något som ser säkert ut.
5. Under transkriptionen i samma fil: lista osäkra passager med
   radnummer, bästa gissning och varför du är osäker.
6. Sist i filen: hur säker du är på helheten (hög/medel/låg)
   och om bilden behöver tas om.

## Efter varje omgång
Committa de nya filerna med meddelandet "Transkription 001–010"
(rätt nummer) och pusha.