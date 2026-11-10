# Ordlista

Förklaringar av ord, titlar, handlingstyper, mynt och mått som förekommer i handlingarna. Ordlistan är ett **läsarstöd**. Den ändrar ingenting i transkriptionerna: där står orden exakt som i källan. I webbvisaren stryks orden under med prickad linje. För muspekaren över ordet eller tryck på det för att se förklaringen. Knappen **Ord** i verktygsraden slår av och på understrykningen.

**Grund** anger varifrån förklaringen kommer:

- **allmän** – allmän historisk kunskap, sammanställd av Claude (språkmodell) 2026-11-10. Förklaringen är **inte kontrollerad mot en namngiven källa**. Kontrollera vid behov i t.ex. Svenska Akademiens ordbok (SAOB, https://www.saob.se) eller Nationalencyklopedin.
- **materialet** – betydelsen eller värdet framgår av handlingarna själva (hänvisning i kolumnen Exempel).
- **FO (extern källa)** – Ordbok över Finlands svenska folkmål, Institutet för de inhemska språken, https://kaino.kotus.fi/fo/ (hämtat 2026-11-09). Se också avsnittet "Ordförklaringar ur dialektordboken" i namn.md.

Kolumnen **Former** styr vilka ord som stryks under:

- `*` i slutet betyder alla ord som börjar så, till exempel `sytning*`, som ger sytning, Sytnings och sytningen.
- Utan `*` måste ordet stå exakt så.
- Stora och små bokstäver räknas lika.

Formerna är valda så att ord med annan betydelse inte stryks under. Till exempel stryks "ting" bara under i uttryck som "lagtima ting", eftersom "i de ting som mig" (020:18) betyder saker. Lägg till nya former här och kör `python3 bygg_index.py`.

## Handlingar och rättsliga begrepp

| Ord | Former | Förklaring | Grund | Exempel |
|---|---|---|---|---|
| afhandling, avhandling | `afhandl*` `avhandl*` | Skriftligt avtal mellan parter, t.ex. köp, gåva eller överlåtelse av en hemmansdel. Ordet betyder här inte en vetenskaplig uppsats. | allmän | 297:1; 212 |
| köpebrev | `köpebref*` `köpebrev*` | Skriftligt köpeavtal om fast egendom. | allmän | 207; 225 |
| gåvobrev | `gåfvobref*` `gåvobrev*` | Skriftlig överlåtelse som gåva. I materialet ges hemmanet ofta som gåva till ett barn mot sytning och mot utlösen till syskonen. | allmän, materialet | 219:1–7; 184:18–19 |
| kj, qv (äldre stavning) | `kjöp*` `qvitt*` `qvins` | Äldre stavning: *kj* = k (Kjöparen = köparen), *qv* = kv (qvitteras = kvitteras, qvins = kvinns). | allmän | 207:8, 11; 216:17 |
| afskrift | `afskrift*` | Avskrift, en kopia av en handling. | allmän | 177:13 |
| bestyrka | `bestyrk*` | Intyga att något är riktigt, t.ex. att en avskrift stämmer med originalet. | allmän | 009:5–7 |
| bouppteckning | `bouppteckn*` | Förteckning över en avlidens tillgångar och skulder, med värdering. Den gjordes inom några månader efter dödsfallet. | allmän | 151; 304 |
| arvskifte, skifte | `arfskift*` `arvskift*` `skifte*` | 1) *Arvskifte*: fördelningen av den avlidnes egendom mellan arvingarna, ofta samma dag som bouppteckningen. 2) I lantmäterihandlingarna: ett sammanhängande jordområde som en gård äger ("sina ägor i 3 skiften"), eller själva jorddelningen. | allmän | 166–167; 184:5; 138:25 |
| avvittring | `afvittr*` `avvittr*` | Barnens arv efter en avliden förälder avskiljs från den efterlevandes egendom, t.ex. innan den efterlevande gifter om sig. | allmän | 190 |
| mödernearv | `mödernearf*` `möderne arf` | Barnens arv efter modern. | allmän | 205:10; 212:8 |
| bakarv | `bakarf*` | Arv som går "baklänges", från ett barn som dör till föräldern. I materialet ärver Jakob Björklund sin dotter Emelia, som dog tre veckor efter modern. | allmän, materialet | 192:20–22 |
| arvslott | `arfslott*` `arvslott*` | En arvinges andel av arvet. | allmän | 205:23 |
| giftorätt | `giftorätt*` | Den efterlevande makens andel av makarnas gemensamma bo. Enligt 1734 års lag fick hustrun på landet 1/3 och mannen 2/3. Räkningen i 033 går jämnt ut just så (se beslut 2026-11-09). | allmän, materialet | 031:14; 156:8 |
| lösöre | `lösöre*` | Lös egendom (möbler, redskap, djur), till skillnad från fast egendom (jord och hus). | allmän | 212:25 |
| inventarium, behållning, afkortning | `inventari*` `behållning*` `afkortning*` `avkortning*` | I bouppteckningar: *inventarium* = summan av tillgångarna, *afkortning* = avdrag (skulder, begravning, avgifter), *behållning* = det som blir kvar att dela. | allmän | 184:25–31 |
| transport | `transport` | Bokföringsterm: summan förs över från föregående sida, eller vidare till nästa. | allmän | 152:36; 305:1 |
| dito | `dito` `d:o` | Detsamma som ovan, för att slippa upprepa ett ord i listor. | allmän | 152:10 |
| sterbhus | `sterbhus*` `dödsbo*` | Dödsbo; *sterbhusdelägare* = dödsbodelägare (arvingarna och den efterlevande maken). | allmän | 237:1 |
| sytning | `sytning*` `sÿtning*` `undantager` | Finlandssvensk term för undantag eller födoråd: de äldre lämnar gården till nästa generation mot livslångt uppehälle med bostad, mat, kläder, skötsel och begravning. | allmän, materialet | 212:10–23; 233 |
| afträdare | `afträd*` | Den som lämnar över (avträder) gården, ofta mot sytning. | allmän, materialet | 213:5–6; 219 |
| utlösen | `utlös*` | Ersättning till de syskon som inte får gården, så att de "löses ut" ur arvet. | allmän, materialet | 210:7–8; 248–251 |
| förskrivning, skuldsedel, revers | `förskrifn*` `förskrivn*` `skuldsedel*` `revers` `reversen` `reversens` | Skriftligt skuldebrev: gäldenären lovar att betala ett belopp, ofta med ränta. | allmän | 246; 253 |
| inteckning | `inteckn*` `intekn*` | Säkerhet för ett lån i fast egendom, inskriven vid domstolen. Om lånet inte betalas kan långivaren få betalt ur hemmanet. | allmän | 077–082 |
| lagfart | `lagfart*` | Domstolens inskrivning av en ny ägare till fast egendom. | allmän | 001; 062 |
| uppbud | `uppbud*` `uppbj*` | Ett köp eller en gåva av jord kungjordes offentligt vid tre ting i rad, så att den som hade invändningar kunde anmäla dem. Efter det tredje uppbudet utan klander utfärdades fastebrev. | allmän, materialet | 001 → 013 → 015; 016 → 024 → 026 |
| fastebrev | `fasteb*` | Domstolens bevis om att den nya ägaren har laga fång (laglig äganderätt) till jorden, utfärdat efter det tredje uppbudet. | allmän, materialet | 276–280 |
| utslag | `utslag*` | Domstolens eller myndighetens beslut i ett ärende. | allmän | 290–295 |
| bomärke | `bomärke*` | Personligt tecken som användes i stället för namnteckning av den som inte kunde skriva. Det kunde gå i arv inom gården. I transkriptionerna står `[bomärke]` där tecknet finns. | allmän | 004; 233:27 |
| förmyndare, omyndig, myndling | `förmyndar*` `omyndig*` `myndig` `myndiga` `myndige` `myndling*` | Den omyndiga (minderåriga) behövde en förmyndare som bevakade hans eller hennes rätt, t.ex. vid arvskifte. *Myndling* = den som har förmyndare. | allmän | 184:12–14; 264–268 |
| bevaka | `bevaka*` | *Bevaka någons rätt* = föra en annans talan, t.ex. ett omyndigt barns, vid en förrättning eller i rätten. | allmän | 190; 241:2 |
| godeman | `godem*` | Betrodd person från socknen som medverkade vid bouppteckningar och lantmäteriförrättningar och intygade dem. | allmän | 065:24–25; 129:12–18 |
| godman | `godman*` | Person som domstolen förordnar att sköta en frånvarandes angelägenheter, i materialet 1942 för syskonen Svanbäck i Amerika. Inte samma sak som godeman. | allmän, materialet | 102–104 |
| förrättning | `förrättning*` | Officiell åtgärd på plats, t.ex. bouppteckning eller lantmäteriförrättning. *Förrättningsman* = den som utför den. | allmän | 129; 184 |
| testamente, J. B., Ä. B. | `J. B.` `J. B:` `J: B.` `J: B:` `Ä. B.` | Hänvisningar till lagen: *J. B.* = Jordabalken, *Ä. B.* = Ärvdabalken i 1734 års lag, som gällde i Finland långt in på 1900-talet. "1 § 4 kap. J. B." = paragraf 1 i kapitel 4 i jordabalken. | allmän | 022:6; 108:1 |

## Domstolar, myndigheter och titlar

| Ord | Former | Förklaring | Grund | Exempel |
|---|---|---|---|---|
| härad, häradsrätt | `härads` `häradsrätt*` | *Härad* = domsområde på landsbygden. *Häradsrätten* = den lokala domstolen för landsbygden, med en domare (häradshövdingen) och nämndemän. | allmän | 001:3; 042 |
| ting, lagtima, urtima | `lagtima ting` `urtima ting` `winter ting` `höste ting*` `vinter ting*` `detta ting` `Pedersöre ting` `ting i Pedersöre` `ting med` `tinget` `lagtima` `urtima` | *Ting* = domstolens sammanträde. *Lagtima ting* = de ordinarie tingen (vinterting och höstting). *Urtima ting* = ett extra ting. | allmän | 001:3–4; 102 |
| tingslag | `tingslag*` | Det område (en eller flera socknar) som hörde till samma ting. | allmän | 042 |
| domsaga | `domsaga*` | En häradshövdings hela domkrets, ofta flera tingslag. Purmo hörde bl.a. till Mellersta Österbottens övre domsaga och senare till Nykarleby domsaga. | allmän, materialet | 279:2–3; 042 |
| häradshövding | `häradshöfd*` `häradshövd*` | Domaren i häradsrätten. *Vice häradshövding* var en titel för jurister som hade fullgjort domstolstjänstgöring, ofta för den som vikarierade som domare. | allmän | 279:1–2; 276:1–2 |
| domhavande | `domhafv*` `domhav*` `domareämbet*` `domareembet*` `domarämbet*` | Den som utövar domarämbetet, ordinarie eller tillförordnad domare. | allmän | 113:18–20 |
| nämndeman | `nämndem*` | Lekman, ofta en betrodd bonde, som satt i häradsrätten tillsammans med domaren. Nämndemän anlitades också som ombud och vittnen. | allmän | 042:19–20; 151:5 |
| Kejsarens Befallningshavande | `kejsarens` `befallningshafv*` `guvernör` `landshövd*` | Guvernören (landshövdingen) i länet. Under den ryska tiden 1809–1917 utfärdade han beslut i kejsarens namn. | allmän | 290:1–2 |
| kronolänsman | `kronolänsm*` `kronofogd*` | Statens tjänsteman i socknen med polis- och uppbördsuppgifter. *Kronofogde* = hans överordnade i fögderiet. | allmän | 102:17 |
| sockenskrivare | `sockneskrifv*` `sokneskrifv*` | Skrivkunnig man i socknen som mot betalning skrev handlingar åt bönderna och var deras ombud vid tinget. | allmän | 001:10–11 |
| häradsskrivare | `häradsskrifvare*` | Tjänsteman som förde jordeboken och mantalslängden för häradet. | allmän | 008:9–10 |
| rådman | `rådman*` | Ledamot av stadens magistrat och rådhusrätt. Titeln bars ofta av förmögna borgare. | allmän | 078:13; 246 |
| kommerseråd | `Com: Rådet` | Hederstitel för framstående köpmän och fabrikörer. | allmän | 318:29 |
| kyrkovärd | `kyrkovärd*` | Förtroendeman som skötte församlingens ekonomi. I materialet kvitterar kyrkovärden avgiften till de fattiga vid bouppteckningar. | allmän, materialet | 161:33–36; 180 |
| lasarett, fattiga | `lazarett*` `lasarett*` `fattigprocent*` | Vid bouppteckning betalades en liten lagstadgad avgift till socknens fattiga och till länets lasarett (sjukhus), i materialet 1/8 procent vardera. | materialet | 184:28–29 |
| arvsskatt | `arvsskatt*` | Skatt på arv. Arvsskattenämnden beslutade om den; 1950 beslöts att ingen arvsskatt skulle tas ut. | materialet | 203:1–6 |
| stämpelpapper | `stämpelm*` `stämpelskatt*` | Stämpelskatt betalades genom att handlingen skrevs på stämplat papper eller försågs med stämpelmärken. Därför har många handlingar ett tryckt sigill eller frimärksliknande märken. | allmän | 042; 219 |

## Jord och gård

| Ord | Former | Förklaring | Grund | Exempel |
|---|---|---|---|---|
| hemman | `hemman*` | Gård som var en enhet i jordeboken, med ett nummer i byn (Sandnabba N:o 8, Härmälä N:o 6). Ett hemman kunde ägas av flera, var och en med sin andel. | allmän | 001:16–18 |
| mantal | `mantal*` | Skatteenhet för jord, inte ett ytmått. Ett helt hemman var t.ex. 1 mantal eller en del av ett. Bråk som 5/48 eller 5/96 mantal anger hur stor andel av skatten och därmed av hemmanet en ägare hade. | allmän | 001:16–18; 042 |
| skattehemman, kronohemman | `skattehemman*` `skatte hemman*` `skatte` `krono` | *Skattehemman* = ett hemman som bonden ägde själv och betalade grundskatt för. *Kronohemman* = ett hemman som ägdes av kronan (staten) och brukades av en åbo. | allmän | 001:18 |
| hemmanstal | `hemmanstal*` | Andel av ett hemman (jorden), till skillnad från mantalet (skatten). | allmän | 058:25 |
| jordebok | `jordebok*` | Statens register över skattepliktiga hemman och deras mantal och skatter. | allmän | 008 |
| grundränta | `grund=ränta` `grundränta*` | Den fasta årliga skatten på jorden. | allmän | 045:14 |
| utskylder | `utskyld*` | Skatter och avgifter till stat, kyrka och kommun. | allmän | 044:2 |
| lägenhet | `lägenhet*` | I jordsammanhang: ett jordområde eller en fastighet, inte en bostad. *Torplägenhet* = ett torps område. | allmän | 217:1–4; 237:4 |
| klyvning | `klyfning*` `klyvning*` `delningsinstrument*` | Lantmäteriförrättning där ett samägt hemman delas i självständiga lotter med egna gränser. Delningsinstrumentet är förrättningens slutliga handling. | allmän | 129–146 |
| storskifte | `storskift*` | Den stora omfördelningen av byarnas jord från 1700-talet, där varje gård fick sin jord samlad i färre skiften. | allmän | 070:1 |
| littera | `littera` | Bokstav eller nummer som betecknar en lott vid skifte eller klyvning. | allmän | 129:20–24 |
| parcell, stomhemman | `parcell*` `stomhemman*` `stomlägenhet*` `avgäld*` | *Parcell* = ett område som avstyckats från ett hemman. *Stomhemman* eller *stomlägenhet* = det som blir kvar. *Avgäld* = den årliga avgift som parcellen betalar till stomhemmanet. | allmän, materialet | 058:9–25 |
| impediment | `impediment*` | Mark som inte kan odlas eller ge skog, t.ex. berg eller myr. | allmän | 058:15–16 |
| torp, torpare | `torp` `torpare*` `torplägenhet*` | *Torp* = ett mindre jordbruk på ett hemmans mark. Torparen arrenderade det mot betalning i pengar och dagsverken. | allmän, materialet | 215:2–19; 228:18 |
| dagsverke | `dagsverk*` | En dags arbete som betalning, t.ex. torparens skyldighet att arbeta på hemmanet. | allmän | 215:18 |
| legoavtal | `legoavtal*` | Arrendeavtal. *Lega* betyder hyra. | allmän | 227 |
| backstuga | `backstug*` | Liten stuga på någon annans mark utan egen jord att bruka. *Backstugukarl* = den som bodde där. | allmän | 158:6; 126:21 |
| bondeson | `bondeson*` `bonde son*` | Son på en bondgård som ännu inte själv var ägare. Titeln ändras till *bonde* när han tar över. | allmän, materialet | 016:24 → 026:9 |
| enka, enkling | `enka` `enkan` `enkans` `enkling*` `enklin` `änckling*` `bondeenk*` | Äldre stavning av änka och änkling. | allmän | 031:17; 168:14 |
| farstugukammare | `farstugukammar*` | Rummet intill farstun (förstugan) i en bondstuga. Det var en vanlig bostad för de gamla på sytning. | allmän | 233:9 |
| päron | `päron` | I äldre finlandssvenska: potatis (jordpäron), inte frukten. "Fyratunnor päron" i sytningen 1868 är alltså potatis. | allmän | 210:11; 212:13 |
| skjuts | `skjuts*` | Transport med häst och vagn eller släde. | allmän | 233:23 |

## Mynt

Purmo hörde till Sverige till 1809. Svenska pengar användes ändå i Finland långt efteråt, till myntreformen på 1840-talet. Därefter räknades i rubel och från 1860 i finsk mark.

| Ord | Former | Förklaring | Grund | Exempel |
|---|---|---|---|---|
| riksdaler | `riksdaler*` `r:dr` `rd` | Svensk myntenhet. 1 riksdaler = 48 skilling. | allmän | 290–291; 308:31 |
| riksgälds, banco | `riksgälds*` `banco` | Två slags svenska pengar: *riksgäldssedlar* var Riksgäldskontorets sedlar och var mindre värda än *banco*, Riksbankens räkneenhet. I materialet motsvarar 397 rubel 50 kopek silver 795 riksdaler riksgälds (1840). | allmän, materialet | 302; 322 |
| skilling | `skilling*` `ß` | Svenskt skiljemynt, 1/48 riksdaler. Tecknet ß i bouppteckningen 1802 = skilling. | allmän | 305:3 |
| rubel, kopek | `rubel*` `rub:` `rb` `kopek*` `kop` `kop:` `kop.` | Rysk myntenhet som användes i Finland: 1 rubel = 100 kopek. | allmän | 001:21–004:17 |
| silverrubel, assignationer | `silfver*` `assignati*` | Rubel kunde vara *silverrubel* (silfver) eller *banco-assignationer*, pappersrubel med lägre värde. I bouppteckningar står *Silfver* också för föremål av silver. | allmän | 205:13; 297 |
| mark, penni | `mark` `fmk` `penni` `finskt mynt` | Finsk mark (Fmk), Finlands egen valuta från 1860. 1 mark = 100 penni. | allmän | 184; 246 |

## Mått och vikt

| Ord | Former | Förklaring | Grund | Exempel |
|---|---|---|---|---|
| kanna, stop | `kanna` `kannor` `kans` `stop` | Rymdmått: 1 kanna ≈ 2,6 liter = 2 stop. "7 Kans Gryta" = en gryta som rymmer 7 kannor. | allmän | 152:34; 212:17–18 |
| tunna, kappa | `tunna` `tunnor` `kappa` | Rymdmått för spannmål: 1 tunna ≈ 146 liter. En kappa var en mindre del av en tunna. | allmän | 212:12–13; 018:14 |
| tunnland, kappland | `tunnland*` `kappland*` | Ytmått: 1 tunnland ≈ 0,5 hektar. *Kappland* var en mindre del av ett tunnland. | allmän | 215:9; 123:7 |
| aln | `aln` | Längdmått, ≈ 59 cm. | allmän | 133:14–15 |
| skålpund, lispund | `skålpund*` `lispund*` `℔` `℔℔` | Viktmått: 1 skålpund (℔) ≈ 425 gram. 1 lispund (℔℔) = 20 skålpund ≈ 8,5 kg. | allmän | 212:13–15 |

## Föremål, kläder och redskap

| Ord | Former | Förklaring | Grund | Exempel |
|---|---|---|---|---|
| gångkläder | `gångkläder*` | En persons kläder, till skillnad från sängkläder och vävnader. | allmän | 184:24 |
| pjäxor | `pjexor` `pjäxor` `pjexband` | "finn-pjäxa, mjukt skoplagg sytt i ett stycke med näbbformad tådel" (FO). | FO (extern källa) | 212:17; 029:9 |
| kortull, långull | `kortull` `långull` | Ull med korta respektive långa fibrer, för olika slags garn. | allmän | 233:15–18 |
| bladtobak | `bladtubak` `tubak` `tobacks blad` | Torkade tobaksblad som man själv skar till pip- eller tuggtobak. | allmän | 212:15; 233:17 |
| fyrskaft | `fyrskaft*` | "fyrskäftad vävnad" (FO). | FO (extern källa) | 154:35 |
| häckla | `häckla` | "redskap att frånskilja blånorna med från lin el. hampa efter bråkningen" (FO). | FO (extern källa) | 153:11 |
| kytta | `kytta*` | "område som beretts … för odling gm avbrännande av ytskikt av mossa el. torv" (FO). I materialet är det ett ägonamn. | FO (extern källa) | 148:5, 7 |
| kardor | `kardor` | Ett par borstliknande redskap för att kamma (karda) ull före spinningen. | allmän | 305:45 |
| spinnrock | `spin rock` | Redskap för att spinna garn. | allmän | 305:36 |
| bila | `bila` | Bredbladig yxa för att hugga timmer släta. | allmän | 305:7 |
| navare | `nafwar*` | Borr med tvärhandtag för att borra hål i trä. | allmän | 305:16–17 |
| lie, skära | `liar` `skäror` | Skördeverktyg: *lie* för gräs och säd med långt skaft, *skära* liten och böjd för säd. | allmän | 152:19–21 |
| skrinda | `skrind*` | Hövagn eller hösläde med höga lämmar. | allmän | 306:14 |
| malm | `Malm:` `og malm` | I bouppteckningar: gjutmetall, mässing eller klockmalm (t.ex. ljusstakar). Obs: *Malm* är också ett efternamn i materialet (318). | allmän | 168:31; 304:24 |
| bläck | `bläck` | I bouppteckningar: tunnplåt, förtent järnplåt ("bläckplåt"). Ordet betyder här inte skrivbläck. | allmän | 158:20 |
| påstlin | `påstlin*` | Porslin. | allmän | 306:35–38 |
