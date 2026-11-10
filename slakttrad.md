# Släktträd – underlag

Underlaget till släktträdet i webbvisaren. Varje rad är en person. Kolumnerna **Far**, **Mor** och **Gift med** innehåller ID från första kolumnen. Släktträdet ritas av webbvisaren från den här tabellen (kör `python3 bygg_index.py` efter ändringar).

**Säkerhet** gäller personens koppling till föräldrarna:

- **belagt** – släktskapen står i materialet (se Källa).
- **extern** – släktskapen bygger på en extern källa, i regel HisKi Purmo (Genealogiska Samfundet i Finland, https://hiski.genealogia.fi/hiski?se+0420, sökt 2026-11-08–09). Den står inte i handlingarna själva. Extern källa.
- **slutsats** – släktskapen är en slutsats (t.ex. av ett patronymikon) och inte belagd. Den ritas streckad.

Levnadsår märkta "(HisKi)" kommer från den externa källan, övriga från materialet. Mer om varje person finns i namn.md (sök på texten i kolumnen Sök). Sammanställt av Claude 2026-11-10 ur namn.md och transkriptionerna.

## Personer

| ID | Namn | Levnad | Far | Mor | Gift med | Säkerhet | Källa | Anm. | Sök |
|---|---|---|---|---|---|---|---|---|---|
| jacob1802 | Jacob Jacobsson Härmelä | d. 1802 | | | margareta, anna | belagt | 304:2–5 | Bonde på Härmälä N:o 6, 25/96 mantal | Härmelä (d. 1802 |
| margareta | Margareta Johansdotter | d. 1788 (HisKi) | | | jacob1802 | extern | HisKi Purmo (extern källa) | Första hustru; nämns inte i handlingarna | Margareta Johansdotter |
| anna | Anna Isaksdotter (Isacsdotter) | | | | jacob1802 | belagt | 304:5–8; 298:9–11 | Änka 1802. Hennes bror Pähr Isacson Slipp var förmyndare (304:8–11) | Anna Isac |
| maria1776 | Maria (Maja) Jacobsdotter | f. 1776 (HisKi) | jacob1802 | margareta | eric_ede | belagt | 304:12; 298:18 | Mor enligt HisKi (extern källa) | Maria Jacobsdotter |
| eric_ede | Eric Mattsson Ede | | | | maria1776 | belagt | 304:13; 298:22 | Jfr gården Ejde/Eide | Eric Mattsson Ede |
| gretalena | Gretalena Jacobsdotter | f. 1778 (HisKi) | jacob1802 | margareta | anders_nars | belagt | 304:13; 298:18 | | Gretalena |
| anders_nars | Anders Nars / Narsträsk | | | | gretalena | belagt | 304:13–14; 298:24 | | Narsträsk |
| johan1782 | Johan Jacobsson Härmälä | f. 1782 (HisKi) | jacob1802 | margareta | | belagt | 304:9–11; 297:5–6 | Köpte 1826 Isaac Christopherssons andel av Härmälä tillsammans med brodern Jacob (297:1–9); halvbror enligt HisKi (extern källa) | Johan och Jacob Jacobssöner Härmälä |
| britacaisa | Britacaisa Jacobsdotter | f. 1786 (HisKi) | jacob1802 | margareta | pehr_kaldbacka | belagt | 304:14; 300:8–10 | | Britacaisa |
| pehr_kaldbacka | Pehr Mattsson Käldbacka | | | | britacaisa | belagt | 300:8–9, 25 | Möjligen far till Matts Pehrsson Kjäldbacka, som sålde Sandnabba 1843; inte belagt | Pehr Mattsson Käldbacka |
| jacob1861 | Jacob Jacobsson Sandnabba eller Härmälä | 1793–1861 | jacob1802 | anna | elisa | extern | 001:13; 166:3; 304:9 | Köpte Sandnabba 1843. Att han är sonen Jacob i bouppteckningen 1802 bekräftas av HisKi (extern källa); f. 1793-02-06 (HisKi) | (f. 1793-02-06 |
| elisa | Elisa (Lisa) Andersdotter | ca 1792–1848 | | | jacob1861 | belagt | 002:11; 158:4 | Dödsdag 1848-05-08 och dödsorsak "colik" enligt HisKi (extern källa) | Elisa / Lisa Andersdotter |
| annalena1814 | Anna Lena Jacobsdotter | f. 1814 (HisKi) | jacob1861 | elisa | hendric_pass | belagt | 158:5–6; 167:2–8 | | Hendric / Hindrik Jacobsson Pass |
| hendric_pass | Hendric (Hindrik) Jacobsson Pass | | | | annalena1814 | belagt | 158:6; 166:6 | Backstugukarl | Hendric / Hindrik Jacobsson Pass |
| majalisa1816 | Majalisa Jacobsdotter | f. 1816 (HisKi) | jacob1861 | elisa | johan_nybran | belagt | 158:5, 7 | | Johan Andersson Nybrän |
| johan_nybran | Johan Andersson Nybrän | | | | majalisa1816 | belagt | 158:7 | Bondeson | Johan Andersson Nybrän |
| greta1819 | Greta Jacobsdotter | f. 1819 (HisKi) | jacob1861 | elisa | matts_kjacko | belagt | 158:5, 8 | | Matts Andersson [Kjäcko |
| matts_kjacko | Matts Andersson [Kjäcko?] / [Säxiärfve?] | | | | greta1819 | belagt | 158:8; 166:7 | Gårdsnamnet osäkert | Matts Andersson [Kjäcko |
| britacaisa1821 | BritaCaisa Jacobsdotter | f. 1821 (HisKi) | jacob1861 | elisa | simon_nars | belagt | 166:4, 8 | | Simon [Jons?]son Nars |
| simon_nars | Simon [Jons?]son Nars | | | | britacaisa1821 | belagt | 166:8 | Torpare | Simon [Jons?]son Nars |
| jacob1868 | Jacob (Jakob) Jakobsson Sandnabba d.y. | 1825–1868 | jacob1861 | elisa | greta_m, beata | belagt | 158:3–5; 168:19–20; 178:4–5 | Fick hemmanet 1856 (210). Överlät det till sönerna 5 november 1868 (212) och dog dagen därpå (178:4–5). f. 1825-07-20 (HisKi) | Jacob Jacobsson Sandnabba d.y. |
| beata1829 | Beata (Bata) Jacobsdotter | f. 1829 (HisKi) | jacob1861 | elisa | jackob_nybran | belagt | 166:4, 8–9; 018:2 | | Jackob Andersson Nybrän |
| jackob_nybran | Jackob Andersson Nybrän | | | | beata1829 | belagt | 166:9 | Bondeson | Jackob Andersson Nybrän |
| greta_m | Greta Mattsdotter Sandnabba | d. 1864 | | | jacob1868 | belagt | 168:7–9; 017:18 | Från Grägg (HisKi, extern källa) | Greta Mattsdotter Sandnabba |
| simon_stennabba | Simon Petrus Jonaeson Stennabba | | | | gretha_stennabba | extern | HisKi Purmo (extern källa) | Nämns inte i handlingarna | Simon (Petrus) Jonaeson |
| gretha_stennabba | Gretha Mattsdotter (Stennabba) | | | | simon_stennabba | extern | HisKi Purmo (extern källa) | Nämns inte i handlingarna | Gretha Mattsdotter |
| beata | Beata Simonsdotter (Stennabba / Sandnabba) | f. 1834 (HisKi) | simon_stennabba | gretha_stennabba | jacob1868 | extern | 178:3–12; 031:17 | Andra hustru. Föräldrarna enligt HisKi (extern källa). Hade sytning från 1868 (212:10–23) | Beata Simonsdotter (Stennabba |
| petter_stennabba | Petter (Simon Petter) Simonsson Stennabba | f. 1836 (HisKi) | simon_stennabba | gretha_stennabba | | extern | 090:13–15 | Torpare. Förmyndare 1869 för systersonen Simon Petter | Petter Simonsson Stennabba |
| matts1849 | Matts Jakobsson Sandström | f. 1849 (HisKi) | jacob1868 | greta_m | | belagt | 168:7–11; 225:2–5 | Bodde i Svartå, Karis. Sålde sin halva till brodern 1876 och skrev brevet 281 | Matts Jakobsson Sandström |
| jakob1850 | Jakob Jakobsson Sandnabba, kallad Lilqvist | 1850–1908 | jacob1868 | greta_m | majalena | belagt | 168:7–11; 047:19–20; 282 | "Sandnabba Jacob / Lilqvist" på brevet 1876 (282:1–2) | Jakob Jakobsson Lilqvist |
| johan_j | Johan Jakobsson Sandnabba | | jacob1868 | greta_m | | belagt | 168:10–11; 215:1 | Torpare på Sandnabba från 1888 (215) | Johan Jakobsson Sandnabba |
| anders_j | Anders Jakobsson Sandnabba | | jacob1868 | greta_m | | belagt | 168:10–11; 214:1 | Kvitterade sin utlösen 1878 (214) | Anders Jakobsson Sandnabba |
| gustaf_j | Gustaf Jakobsson | | jacob1868 | greta_m | | belagt | 168:10–11; 184:11–12 | Omyndig 1878 | Johan, Anders, Gustaf |
| simonpetter | Simon Petter Jakobsson | ca 1867–1877 | jacob1868 | beata | | belagt | 178:10–13; 184:6–8 | Dog "endast tio år gammal" (184:7) | Simon Petter / Petter Jakobsson |
| majalena | Maja Lena Eriksdotter Sandnabba | 1852–1915 | | | jakob1850 | belagt | 047:21–22; 129:20–21 | Gav gården till sonen Jakob 1913 mot sytning (219; 233) | Maja Lena Eriksdotter |
| jakob_bjorklund | Jakob Björklund (Jakob Jakobsson Björklund) | 1876–1949 | jakob1850 | majalena | sanna, hilda | belagt | 047:21–048:1; 129:20–21; 287 | | Jakob Jakobsson Björklund |
| johanna1879 | Johanna | f. 1879 | jakob1850 | majalena | anders_stennabba | belagt | 048:2–3 | | Johanna (f. 1879 |
| anders_stennabba | Anders Stennabba | | | | johanna1879 | belagt | 048:3 | Handlande | Anders Stennabba |
| annalena1882 | Anna Lena | f. 1882 | jakob1850 | majalena | august_k | belagt | 048:4–6 | | Anna Lena (f. |
| august_k | August Andersson Kauhajärvi | | | | annalena1882 | belagt | 048:5–6 | Bondeson | August Andersson Kauhajärvi |
| finamaria | Fina Maria (troligen = Jusefina) | f. 1885 | jakob1850 | majalena | johan_mh | belagt | 048:7–10 | Kallas Jusefina i 043:18 och 194:7 – troligen samma person (slutsats, se namn.md) | Fina Maria |
| johan_mh | Johan Mattsson Härmälä | | | | finamaria | belagt | 048:8–9 | Bondeson | Johan Mattsson Härmälä |
| herman | Herman Asp (Herman Jakobsson Asp eller Sandnabba) | f. 1894 | jakob1850 | majalena | hilma_asp | belagt | 048:11; 047:14–15 | Tvisten med brodern 1934 (112; 117); köpte sin gårdstomt 1951 (239) | Herman Jakobsson Asp |
| hilma_asp | Hilma Amanda Asp | f. 1894 | | | herman | belagt | 112:12–13; 115:18 | | Hilma Amanda Asp |
| sanna | Sanna Maja Pelkkala (Johansdotter) | 1875–1899 | | | jakob_bjorklund | belagt | 067:5–6; 190 | Första hustru | Sanna Maja Pelkkala |
| emelia | Emelia Maria | d. 1899 | jakob_bjorklund | sanna | | belagt | 190:4–9; 192:20 | Dog tre veckor efter bouppteckningen efter modern | Emelia / Emilia Maria |
| anders_svanback | Anders Johansson Svanbäck | 1856–1936 | | | edla | belagt | 102:22–23 | Torpare, Mattjus N:o 9, Nederpurmo. Lånade ut 35 000 mark till svärsonen 1928 (253) | Anders Johansson Svanbäck |
| edla | Edla Sofia Simonsdotter Käld (Svanbäck) | 1862–1942 | | | anders_svanback | belagt | 102:23–24 | | Edla Sofia Simonsdotter |
| anders_vilhelm | Anders Vilhelm Svanbäck | f. 1882 | anders_svanback | edla | | belagt | 103:1 | "Vistas i Amerika" 1942 | Anders Vilhelm |
| hilda | Hilda Maria Svanbäck (Björklund) | 1884–1939 | anders_svanback | edla | jakob_bjorklund | belagt | 103:2–3; 067:8–9 | Andra hustru, vigd 1905 | Hilda Maria Björklund f. Svanbäck |
| johan_axel | Johan Axel Svanbäck | f. 1886 | anders_svanback | edla | | belagt | 103:9 | "Vistas i Amerika" 1942 | Johan Axel |
| aina | Aina Charlotta Svanbäck | f. 1889 | anders_svanback | edla | | belagt | 103:10 | | Aina Charlotta |
| matts_leander | Matts Leander Svanbäck | f. 1894 | anders_svanback | edla | | belagt | 103:11 | | Matts Leander |
| edla_johanna | Edla Johanna Svanbäck | 1896–1899 | anders_svanback | edla | | belagt | 103:12 | | Edla Johanna |
| hilma_sofia | Hilma Sofia Svanbäck | f. 1898 | anders_svanback | edla | | belagt | 103:13 | Adress okänd 1942 (103:21–22) | Hilma Sofia Svanbäck |
| ivar_svanback | Ivar Svanbäck | f. 1900 | anders_svanback | edla | | belagt | 103:14 | | Ivar (1900) |
| osvald | Jakob Osvald Björklund | f. 1914 | jakob_bjorklund | hilda | signe | belagt | 067:11; 103:4 | Soldat vid Svir 1943 (241) | Jakob Osvald Björklund |
| signe | Signe Maria Manninen | f. 1917 | | | osvald | belagt | 067:11–12 | | Signe Maria Manninen |
| ines | Ines (Inäs) Maria Björklund | f. 1916 | jakob_bjorklund | hilda | konrad | belagt | 067:13; 103:5 | Änka 1943. Hette senare Wennberg (260:8); den andra makens namn står inte i materialet | Ines / Inäs Maria |
| konrad | Konrad Anders Sundstedt | 1917–1943 | | | ines | belagt | 067:13–14 | Död 18 januari 1943 (067:14) | Konrad Anders Sundstedt |
| alice | Alice Margareta Sundstedt | f. 1941 | konrad | ines | | belagt | 067:14–15 | | Alice Margareta |
| milton | Karl Milton Björklund | f. 1918 | jakob_bjorklund | hilda | karin | belagt | 067:16; 103:6 | Tog över gården 1949 (237) | Karl Milton Björklund |
| karin | Karin Inga Maria Rönnqvist | f. 1919 | | | milton | belagt | 067:16–17 | | Karin Inga Maria |
| agnes | Agnes Gertrud Björklund (Novén) | f. 1922 | jakob_bjorklund | hilda | sven_erik | belagt | 067:18; 103:7 | Bodde i Trelleborg | Agnes Gertrud |
| sven_erik | Sven-Erik Novén | f. 1924 | | | agnes | belagt | 067:28–29; 244 | Eldare, Trelleborg | Sven-Erik Novén |
| dagny | Dagny Alexandra Björklund | f. 1925 | jakob_bjorklund | hilda | | belagt | 067:20; 103:8 | | Dagny Alexandra |
| jacob_sandnabba | Jacob (Sandnabba) | | | | | slutsats | 008:1; 155:21–24 | Känd bara genom barnens efternamn "Jacobssöner"; han själv nämns inte | Hans och Matts Jacobssöner |
| hans | Hans Jacobsson Sandnabba | | jacob_sandnabba | | marja | slutsats | 003:4; 155:21–24; 205:1 | Sålde 1836 sin del till brodern Eric mot att denne skulle föda honom till hans död (205:4–6) | Hans Jacobsson Sandnabba |
| marja | Marja (Maria) Hansdotter Sandnabba | d. 1817 | | | hans | belagt | 151:10; 007:1–2 | Hennes bror Johan Hansson [Philpus?] var barnens förmyndare (151:20–21) | Marja / Maria Hansdotter Sandnabba |
| matts_jacobsson | Matts Jacobsson Sandnabba | | jacob_sandnabba | | | slutsats | 007:24–008:1 | Fastebrev 1812 tillsammans med Hans | Matts Jacobsson Sandnabba |
| eric_willbacka | Eric Jacobsson Willbacka (Wilobacka) | | jacob_sandnabba | | | slutsats | 205:1; 155:22 | Bror till Hans (205:1). Sålde 5/48 mantal 1843 | Eric Jacobsson Sandnabba |
| syskon_sandnabba | Petrus, Jonas, Greta, Beata och Anna | | jacob_sandnabba | | | slutsats | 155:21–24 | Hans övriga syskon enligt gåvobrevet 1811 | Hans Jacobsson Sandnabba |
| johan_hansson | Johan Hansson Sandnabba | f. ca 1802 | hans | marja | | belagt | 151:14–16; 205:22–23 | 16 år 1818. Sålde sin arvslott 1830 | Johan Hansson (son) |
| maria_hansdotter | Maria Hansdotter | | hans | marja | matts_kjaldbacka | belagt | 151:16–17; 205:7–8; 207:1–2 | | Maria Hansdotter |
| matts_kjaldbacka | Matts Pehrsson Kjäldbacka | | | | maria_hansdotter | belagt | 207:1–4; 004:7–10 | Sålde Sandnabba till Jacob Jacobsson 1843 (207) | Matts Pehrsson Kjäldbacka |
