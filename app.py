from flask import Flask, render_template, jsonify

app = Flask(__name__)

QUESTIONS = [
    {
        "q": "1.	Kako je organizirano gasilstvo v Sloveniji?",
        "A": "v društvih in podjetjih",
        "B": "v prostovoljnih in poklicnih gasilskih organizacijah",
        "C": "v poklicnih in neprofitnih organizacijah",
        "correct": "B"
    },
    {
        "q": "2.	Koliko članstva je vključeno v prostovoljne gasilske organizacije v Sloveniji?",
        "A": "pod 80.000",
        "B": "med 90.000 in 100.000",
        "C": "več kot 170.000",
        "correct": "B"
    },
    {
        "q": "3.	Koliko prostovoljnih gasilskih društev (PGD in PIGD) je v Sloveniji?",
        "A": "pod 500",
        "B": "več kot 1300",
        "C": "okoli 700",
        "correct": "C"
    }
    ,
    {
        "q": "4.	Katere so prostovoljne gasilske organizacije?",
        "A": "prostovoljna gasilska društva, gasilske zveze, Gasilska zveza Slovenije",
        "B": "poklicna jedra, gasilske zveze, Gasilska zveza Slovenije",
        "C": "prostovoljna gasilska društva, javni gasilski zavodi, gasilske zveze, Gasilska zveza Slovenije",
        "correct": "C"
    }
    ,
    {
        "q": "5.	Katere so poklicne gasilske organizacije?",
        "A": "poklicna jedra v podjetjih in prostovoljna industrijska gasilska društva",
        "B": "prostovoljna industrijska gasilska društva in gasilski zavodi ",
        "C": "javni gasilski zavodi in poklicne enote v podjetjih",
        "correct": "C"
    }
    ,
    {
        "q": "6. Kateri so simboli v prostovoljnem gasilstvu?",
        "A": "priznanja in odlikovanja",
        "B": "gasilski znak, gasilski grb, prapori, gasilska zastava, tekmovalna zastava, gasilska himna",
        "C": "gasilski čini in specialnosti",
        "correct": "B"
    },
    {
        "q": "7. Kaj sestavlja gasilski znak?",
        "A": "prekrižana bakla in sekirica",
        "B": "gasilska čelada, za čelado prekrižani levo bakla in desno gasilska sekirica",
        "C": "slovenska zastava ter prekrižana bakla in sekirica",
        "correct": "B"
    },
    {
        "q": "8. Kakšna organizacija je prostovoljno gasilsko društvo?",
        "A": "humanitarna, nestrankarska in neprofitna organizacija",
        "B": "združenje poklicnih gasilcev",
        "C": "organizacija, ki se ustanovi zaradi političnih interesov občanov",
        "correct": "A"
    },
    {
        "q": "9. Katera pravnoformalna oblika organiziranosti je prostovoljno gasilsko društvo?",
        "A": "družba z neomejeno odgovornostjo",
        "B": "pravna oseba",
        "C": "pravna oseba zasebnega prava",
        "correct": "C"
    },
    {
        "q": "10. Ali lahko tujec postane član PGD?",
        "A": "ne",
        "B": "da, pod enakimi pogoji, kot je za slovenske državljane",
        "C": "lahko le, če ima na območju delovanja društva sorodnike",
        "correct": "B"
    },
    {
        "q": "11. Kateri je temeljni akt PGD in ureja njegovo delovanje?",
        "A": "Pravila gasilske službe",
        "B": "Statut PGD",
        "C": "Zakon o gasilstvu",
        "correct": "B"
    },
    {
        "q": "12. Kaj je statut društva?",
        "A": "listina, ki določa: ime in sedež društva, namen, cilje, naloge društva, pogoje in način včlanjevanja in prenehanja članstva, pravice in obveznosti članov, način upravljanja in zastopanja društva, financiranje, način zagotavljanja javnosti dela, način prenehanja",
        "B": "listina, ki določa financiranje društva ter odnose med društvom in občino",
        "C": "listina, ki določa operativno organiziranost, kazenske določbe v društvu, načine pridobivanja činov in specialnosti",
        "correct": "A"
    },
    {
        "q": "13. Kateri so viri financiranja prostovoljnih gasilskih društev?",
        "A": "samo članarina",
        "B": "proračun lokalne skupnosti, sredstva požarne takse, članarina, sredstva iz dejavnosti PGD, darila, donacije, odstopljena dohodnina in drugi viri",
        "C": "proračun občine in države, izstavljeni računi za pridobitno dejavnost",
        "correct": "B"
    },
    {
        "q": "14. Kje opravimo registracijo gasilskega društva?",
        "A": "na Gasilski zvezi Slovenije",
        "B": "na občini",
        "C": "na upravni enoti",
        "correct": "C"
    },
    {
        "q": "15. Katera od naštetih organizacij je najvišja oblika organiziranosti prostovoljnega gasilstva?",
        "A": "Uprava RS za zaščito in reševanje",
        "B": "Gasilska zveza Slovenije",
        "C": "Prostovoljno gasilsko društvo",
        "correct": "B"
    },
    {
        "q": "16. Inšpektorat, ki nadzira področje varstva pred požarom, se imenuje:",
        "A": "Inšpektorat RS za varstvo pred naravnimi in drugimi nesrečami",
        "B": "Požarni inšpektorat",
        "C": "Inšpektorat za okolje in prostor",
        "correct": "A"
    },
    {
        "q": "17. Kateri je najvišji organ prostovoljnega gasilskega društva?",
        "A": "Upravni odbor",
        "B": "Nadzorni odbor",
        "C": "Občni zbor",
        "correct": "C"
    },
    {
        "q": "18. Koliko gasilskih regij je v Sloveniji?",
        "A": "17",
        "B": "13",
        "C": "19",
        "correct": "B"
    },
    {
        "q": "19. Kaj ureja Zakon o gasilstvu?",
        "A": "sistem varstva pred požarom",
        "B": "nalogo, organizacijo in status gasilstva",
        "C": "sistem zaščite in reševanja",
        "correct": "B"
    },
    {
        "q": "20. Kako članom preneha članstvo v PGD?",
        "A": "z izstopom ali smrtjo",
        "B": "z izstopom, izključitvijo, črtanjem ali smrtjo",
        "C": "samo s smrtjo",
        "correct": "B"
    },
    {
        "q": "21. Ali lahko PGD opravlja izključno pridobitne dejavnosti?",
        "A": "da, če plača davek",
        "B": "ne",
        "C": "da",
        "correct": "B"
    },
    {
        "q": "22. Kakšen je temeljni namen Pravil gasilske službe prostovoljnih gasilcev?",
        "A": "ureditev delovanja prostovoljnih gasilcev, usposabljanja, pravic, dolžnosti, opreme in tekmovanj",
        "B": "ureditev sistema zaščite in reševanja",
        "C": "ureditev pravil ravnanja vseh gasilcev in javne gasilske službe",
        "correct": "A"
    },
    {
        "q": "23. Ali je poveljnik član Upravnega odbora PGD?",
        "A": "ne",
        "B": "samo, če želi",
        "C": "da",
        "correct": "C"
    },
    {
        "q": "24. Kako delimo formacije gasilskih enot glede na število članstva?",
        "A": "gasilska skupina, oddelek, vod, četa, bataljon, brigada",
        "B": "enota, vod, četa",
        "C": "desetina, odred, ešalon",
        "correct": "A"
    },
    {
        "q": "25. Društvo ima 53 operativnih gasilcev. Kdo vodi vod s 26 gasilci?",
        "A": "nižji gasilski častnik",
        "B": "desetar",
        "C": "vodnik",
        "correct": "C"
    },
    {
        "q": "26. Kdo je gasilec pripravnik?",
        "A": "še ni član PGD",
        "B": "član PGD, star najmanj 16 let, z opravljenim usposabljanjem",
        "C": "član PGD med 16. in 18. letom",
        "correct": "B"
    },
    {
        "q": "27. Kdo je prostovoljni operativni gasilec v PGD?",
        "A": "vsak član PGD",
        "B": "aktivni član PGD",
        "C": "oseba, ki izpolnjuje vse strokovne, zdravstvene in zakonske pogoje za opravljanje operativnih nalog",
        "correct": "C"
    }
    ,
    {
        "q": "28. Kdo je rezervni prostovoljni operativni gasilec?",
        "A": "prostovoljni operativni gasilec, ki zaradi zdravstvenih ali drugih razlogov ne more opravljati vseh nalog gasilske službe",
        "B": "gasilski veteran",
        "C": "podporni član",
        "correct": "A"
    },
    {
        "q": "29. Kaj pomeni kratica SPIN?",
        "A": "Sistemsko poročanje in nadziranje",
        "B": "Sistem za poročanje o intervencijah in nesrečah",
        "C": "Sistem za ocenjevanje škode po nesrečah",
        "correct": "B"
    },
    {
        "q": "30. Kaj podpiše član ob vstopu v operativno gasilsko enoto?",
        "A": "kodeks etike",
        "B": "pogodbo o opravljanju javne gasilske službe",
        "C": "slovesno izjavo, da bo gasilsko službo opravljal vestno in požrtvovalno",
        "correct": "C"
    },
    {
        "q": "31. Kdo je najvišji operativni vodja v PGD?",
        "A": "predsednik",
        "B": "poveljnik",
        "C": "vodja intervencije",
        "correct": "B"
    },
    {
        "q": "32. Najmanj koliko operativnih gasilcev mora imeti PGD I. kategorije?",
        "A": "3",
        "B": "9",
        "C": "12",
        "correct": "B"
    },
    {
        "q": "33. Kaj ureja operativni gasilski načrt?",
        "A": "obveščanje, aktiviranje in delovanje gasilskih enot ter je del občinskega načrta zaščite in reševanja",
        "B": "vedenje operativnih gasilcev na intervencijah",
        "C": "temeljno in dopolnilno usposabljanje gasilcev",
        "correct": "A"
    },
    {
        "q": "34. Kaj je namen sistema opazovanja, obveščanja in alarmiranja?",
        "A": "ureditev odnosov med operaterji in vodji intervencij",
        "B": "zgodnje odkrivanje nevarnosti, obveščanje, alarmiranje ter izvajanje zaščite, reševanja in pomoči",
        "C": "ureditev načina prižiganja siren",
        "correct": "B"
    },
    {
        "q": "35. Kateri organ voli poveljnika in predsednika PGD?",
        "A": "Upravni odbor",
        "B": "Občni zbor",
        "C": "Nadzorni odbor",
        "correct": "B"
    },
    {
        "q": "36. Kdo sestavlja poveljstvo PGD?",
        "A": "vodnik, desetar, vodja skupine",
        "B": "desetarji, strojniki, mentorji",
        "C": "poveljnik, namestnik, podpoveljniki, pomočniki, vodje oddelkov, glavni strojnik, orodjar",
        "correct": "C"
    },
    {
        "q": "37. Katere vrste usposabljanja poznamo v prostovoljnem gasilstvu?",
        "A": "temeljna, dopolnilna strokovna, ostala dodatna strokovna",
        "B": "temeljna, nadaljevalna, visoka",
        "C": "strokovna, specialna",
        "correct": "A"
    },
    {
        "q": "38. Kateri nivo organizira tečaj za gasilca pripravnika?",
        "A": "prostovoljno gasilsko društvo",
        "B": "Gasilska zveza Slovenije",
        "C": "gasilska zveza",
        "correct": "C"
    },
    {
        "q": "39. Kateri nivo organizira tečaj za operativnega gasilca?",
        "A": "gasilska zveza",
        "B": "Gasilska zveza Slovenije",
        "C": "prostovoljno gasilsko društvo",
        "correct": "A"
    },
    {
        "q": "40. Kaj predstavljajo čini v prostovoljnem gasilstvu?",
        "A": "položajno funkcijo",
        "B": "splošno izobrazbo",
        "C": "stopnjo strokovne gasilske usposobljenosti",
        "correct": "C"
    },
    {
        "q": "41. Kje na gasilski uniformi nosimo oznake činov?",
        "A": "na spodnjem delu ovratnika",
        "B": "na naramniku oz. epoleti",
        "C": "činov ne nosimo",
        "correct": "B"
    },
    {
        "q": "42. Kaj predstavljajo položajne oznake?",
        "A": "vodstvene naloge gasilskih vodij",
        "B": "strokovno usposobljenost",
        "C": "naloge tekmovalnih enot",
        "correct": "A"
    },
    {
        "q": "43. Kaj predstavljajo gasilske specialnosti?",
        "A": "vodstvene naloge",
        "B": "strokovno usposobljenost za posamezna dela",
        "C": "funkcijo člana v društvu",
        "correct": "B"
    },
    {
        "q": "44. Po čem se gasilci v uniformah naslavljajo?",
        "A": "po funkciji in činu",
        "B": "po izobrazbi",
        "C": "po stažu",
        "correct": "A"
    },
    {
        "q": "45. Na katerem rokavu nosimo znak pripadnosti?",
        "A": "na levem",
        "B": "na desnem",
        "C": "ga ne nosimo",
        "correct": "A"
    },
    {
        "q": "46. Ali Pravila gasilske službe urejajo gasilske slovesnosti?",
        "A": "ne",
        "B": "da",
        "C": "ne, to urejajo statuti",
        "correct": "B"
    },
    {
        "q": "47. Kdo je odgovorna oseba za požarno varnost v lokalni skupnosti?",
        "A": "občinski gasilski poveljnik",
        "B": "župan občine",
        "C": "direktor občinske uprave",
        "correct": "B"
    },
    {
        "q": "48. Kako se imenuje informacijski sistem evidenc gasilcev?",
        "A": "GAS 2000",
        "B": "Ujma",
        "C": "Vulkan",
        "correct": "C"
    },
    {
        "q": "49. Kateri jubilej bo slovensko gasilstvo praznovalo leta 2029?",
        "A": "160 let",
        "B": "170 let",
        "C": "150 let",
        "correct": "B"
    },
    {
        "q": "50. Ali smo gasilci vključeni v sistem varstva pred nesrečami?",
        "A": "da",
        "B": "ne",
        "C": "samo ob velikih nesrečah",
        "correct": "A"
    },
    {
        "q": "51. Telefonska številka Centra za obveščanje RS je:",
        "A": "92",
        "B": "113",
        "C": "112",
        "correct": "C"
    },
    {
        "q": "52. Kateri so cilji varstva pred nesrečami?",
        "A": "zmanjšanje števila nesreč in posledic",
        "B": "gašenje in reševanje",
        "C": "nadzor predpisov",
        "correct": "A"
    },
    {
        "q": "53. Kaj povemo ob klicu na 112?",
        "A": "lokacijo",
        "B": "kdo kliče, kaj, kje, koliko ponesrečencev, poškodbe in pomoč",
        "C": "kaj se je zgodilo",
        "correct": "B"
    },
    {
        "q": "54. Koliko Regijskih centrov za obveščanje je v Sloveniji?",
        "A": "17",
        "B": "13",
        "C": "10",
        "correct": "B"
    },
    {
        "q": "55. Kaj je namen varstva pri delu v gasilstvu?",
        "A": "seznanitev z nevarnostmi",
        "B": "preizkusi znanja",
        "C": "zagotoviti varne pogoje za gasilca",
        "correct": "C"
    },
    {
        "q": "56. Kako delimo gasilsko zaščitno opremo?",
        "A": "na osebno in skupno",
        "B": "na zasebno in društveno",
        "C": "na operativno in organizacijsko",
        "correct": "A"
    },
    {
        "q": "57. Kaj sestavlja osebno zaščitno opremo?",
        "A": "delovna obleka",
        "B": "IDA, zaščitna obleka, čelada, škornji, podkapa, rokavice",
        "C": "zaščitna obleka, podobleka, čelada, škornji, rokavice",
        "correct": "C"
    },
    {
        "q": "58. Kaj sestavlja skupno zaščitno opremo?",
        "A": "specialna zaščitna in reševalna oprema",
        "B": "delovne in zaščitne obleke",
        "C": "čelade",
        "correct": "A"
    },
    {
        "q": "59. Kateri so deli gasilske zaščitne čelade?",
        "A": "školjka in ščitnik",
        "B": "školjka, notranja košara, ščitnik, jermen, zaščita tilnika",
        "C": "školjka in ščitnik za vrat",
        "correct": "B"
    },
    {
        "q": "60. Katere naprave morajo imeti navodila za varno delo?",
        "A": "gospodinjske",
        "B": "motorne",
        "C": "vsaka delovna naprava",
        "correct": "C"
    },
    {
        "q": "61. Katera načela obsega prva pomoč?",
        "A": "hitre in pravilne začasne ukrepe",
        "B": "operacije",
        "C": "prevoz",
        "correct": "A"
    },
    {
        "q": "62. Kakšen je namen prve pomoči?",
        "A": "čimprejšnji prihod do medicinske pomoči",
        "B": "olajšanje dela zdravnikom",
        "C": "zadrževanje poškodovancev",
        "correct": "A"
    },
    {
        "q": "63. Kako ukrepamo ob več poškodovancih?",
        "A": "naključno",
        "B": "ne nudimo pomoči",
        "C": "najprej najbolj ogroženim",
        "correct": "C"
    },
    {
        "q": "64. Kako namestimo nezavestnega poškodovanca?",
        "A": "na bok",
        "B": "na hrbet",
        "C": "na trebuh",
        "correct": "A"
    },
    {
        "q": "65. Zakaj je najprimernejši prvi povoj?",
        "A": "za opornice",
        "B": "za previjanje ran",
        "C": "za obvezo glave",
        "correct": "B"
    },
    {
        "q": "66. Kaj je povoj?",
        "A": "trak iz mehke tkanine",
        "B": "lepilni trak",
        "C": "zapenjalo",
        "correct": "A"
    },
    {
        "q": "67. Zakaj uporabljamo trikotno ruto?",
        "A": "za prenos",
        "B": "za obveze in imobilizacijo",
        "C": "za gretje",
        "correct": "B"
    },
    {
        "q": "68. Kaj je rana?",
        "A": "vsaka poškodba",
        "B": "poškodba s trajno posledico",
        "C": "mehanska poškodba, ki sega skozi kožo",
        "correct": "C"
    },
    {
        "q": "69. Kateri so cilji varstva pred požarom?",
        "A": "varovanje ljudi, živali, premoženja in okolja",
        "B": "preprečevanje vseh nesreč",
        "C": "usposabljanje sil",
        "correct": "A"
    }
,
    {
        "q": "70. Kaj je požar?",
        "A": "hitra oksidacija ali razpad",
        "B": "hitro gorenje, ki se nenadzorovano širi v prostoru in času",
        "C": "hiter umik ljudi na varno mesto",
        "correct": "B"
    },
    {
        "q": "71. Kaj je eksplozija?",
        "A": "zelo hitra oksidacija ali razpad, posledica česar je povišanje temperature ali tlaka oz. obeh hkrati",
        "B": "hitro gorenje, ki se nenadzorovano širi v prostoru in času",
        "C": "verjetnost, da bo požar nastal",
        "correct": "A"
    },
    {
        "q": "72. Kaj je požarna ogroženost?",
        "A": "verjetnost, da bo nastal požar, ki bo povzročil žrtve ali škodo",
        "B": "potencialna nevarnost za izgubo življenja ali materialno škodo ob požaru",
        "C": "varnost ljudi, živali in premoženja ob požaru",
        "correct": "B"
    },
    {
        "q": "73. Kaj je požarno tveganje?",
        "A": "verjetnost, da bo prišlo do požara z žrtvami ali škodo",
        "B": "varnost ljudi, živali in premoženja ob požaru",
        "C": "možna nevarnost za smrt ali škodo ob požaru",
        "correct": "A"
    },
    {
        "q": "74. Kaj je požarna varnost?",
        "A": "varnost ljudi, živali in premoženja ob požaru",
        "B": "verjetnost nastanka požara",
        "C": "možna nevarnost za smrt ali škodo",
        "correct": "A"
    },
    {
        "q": "75. Kaj je evakuacija?",
        "A": "umik opreme in naprav",
        "B": "urejeno gibanje oseb na varno mesto",
        "C": "organizirana akcija gašenja",
        "correct": "B"
    },
    {
        "q": "76. Kateri so ukrepi varstva pred požarom?",
        "A": "ukrepi, ki povečujejo ogroženost",
        "B": "ukrepi, ki povečujejo tveganje",
        "C": "ukrepi, ki zmanjšujejo tveganje in zagotavljajo varnost",
        "correct": "C"
    },
    {
        "q": "77. Kateri so preventivni ukrepi varstva pred požarom?",
        "A": "ukrepi, ki zmanjšujejo možnost nastanka požara",
        "B": "ukrepi za gašenje",
        "C": "ukrepi za reševanje",
        "correct": "A"
    },
    {
        "q": "78. Kateri so aktivni ukrepi varstva pred požarom?",
        "A": "ukrepi za reševanje ljudi",
        "B": "ukrepi za gašenje požara",
        "C": "preventivni ukrepi",
        "correct": "B"
    },
    {
        "q": "79. Kako se imenuje državni program varstva pred požarom?",
        "A": "nacionalni program varstva pred naravnimi in drugimi nesrečami",
        "B": "republiški program intervencij",
        "C": "požarni sklad",
        "correct": "A"
    },
    {
        "q": "80. Kdo lahko izdela študijo požarne varnosti?",
        "A": "posamezniki ali podjetja s predpisanimi pogoji",
        "B": "vsak gasilec",
        "C": "inšpektorji",
        "correct": "A"
    },
    {
        "q": "81. Kdo lahko servisira gasilnike?",
        "A": "vsak gasilec",
        "B": "pooblaščeni posamezniki ali podjetja",
        "C": "samo orodjarji",
        "correct": "B"
    },
    {
        "q": "82. Kateri inšpekcijski organ nadzira varstvo pred požarom?",
        "A": "Požarni inšpektorat RS",
        "B": "Nadzorni odbor GZS",
        "C": "Inšpektorat RS za varstvo pred naravnimi in drugimi nesrečami",
        "correct": "C"
    },
    {
        "q": "83. Kdaj mora delodajalec zagotoviti poučitev o varstvu pred požarom?",
        "A": "le ob veliki ogroženosti",
        "B": "ob nastopu dela in vseh pomembnih spremembah",
        "C": "samo ob nastopu dela",
        "correct": "B"
    },
    {
        "q": "84. Katere stopnje požarne ogroženosti poznamo?",
        "A": "zelo majhna do zelo velika",
        "B": "majhna, srednja, visoka",
        "C": "minimalna, srednja, maksimalna",
        "correct": "A"
    },
    {
        "q": "85. Kaj vsebuje požarni red?",
        "A": "evidenco požarov",
        "B": "organizacijo, ukrepe in navodila ob požaru",
        "C": "študijo požarnega varstva",
        "correct": "B"
    },
    {
        "q": "86. Kaj je požarni načrt?",
        "A": "enako kot požarni red",
        "B": "grafični prikaz objekta z označeno požarno zaščito",
        "C": "skica možnih požarov",
        "correct": "B"
    },
    {
        "q": "87. Kateri so naravni vzroki požarov?",
        "A": "strela, neurje, samovžig, potres",
        "B": "trenje, udarec",
        "C": "kratek stik",
        "correct": "A"
    },
    {
        "q": "88. Kateri so kemični vzroki požarov?",
        "A": "trenje in udarci",
        "B": "samovžig in eksotermne reakcije",
        "C": "električna toplota",
        "correct": "B"
    },
    {
        "q": "89. Kakšne barve so opozorilne table za nevarne snovi?",
        "A": "rumene",
        "B": "rdeče",
        "C": "oranžne",
        "correct": "C"
    },
    {
        "q": "90. Kaj pomeni zgornje število na tabli za nevarne snovi?",
        "A": "UN številko",
        "B": "Kemlerjevo število",
        "C": "številko vozila",
        "correct": "B"
    },
    {
        "q": "91. Kaj pomeni spodnje število na tabli za nevarne snovi?",
        "A": "številko vozila",
        "B": "Kemlerjevo število",
        "C": "UN številko",
        "correct": "C"
    },
    {
        "q": "92. Kaj pomeni črka X pri Kemlerjevem številu?",
        "A": "radioaktivno snov",
        "B": "nevarna reakcija z vodo",
        "C": "jedka snov",
        "correct": "B"
    },
    {
        "q": "93. Katero stražo opravljajo gasilci na nevarnih prireditvah?",
        "A": "gasilsko",
        "B": "eksplozijsko",
        "C": "požarno",
        "correct": "C"
    },
    {
        "q": "94. Koliko časa je potrebna požarna straža?",
        "A": "dokler obstaja požarna nevarnost",
        "B": "najmanj 3 ure",
        "C": "najmanj 5 ur",
        "correct": "A"
    },
    {
        "q": "95. Kdaj je treba organizirati požarno stražo?",
        "A": "pri vsakem požaru",
        "B": "ob prireditvah in nevarnih delih",
        "C": "po končanem gašenju",
        "correct": "B"
    },
    {
        "q": "96. Kaj je gasilska straža?",
        "A": "nadzor po gašenju",
        "B": "naloge na intervenciji",
        "C": "nadzor ob povečani požarni nevarnosti",
        "correct": "C"
    },
    {
        "q": "97. Kje smemo hraniti polne plinske jeklenke?",
        "A": "v zaprtih kleteh",
        "B": "v garaži ali spalnici",
        "C": "nad površino zemlje, v zračenih prostorih",
        "correct": "C"
    },
    {
        "q": "98. Kje ne smemo hraniti polnih plinskih jeklenk?",
        "A": "v višjih prostorih",
        "B": "v zračenih prostorih",
        "C": "v zaprtih kletnih prostorih",
        "correct": "C"
    },
    {
        "q": "99. Kdaj smemo nalivati kurilno olje v peč?",
        "A": "ko je peč popolnoma hladna",
        "B": "ko zmanjka olja",
        "C": "ko zmanjšamo plamen",
        "correct": "A"
    },
    {
        "q": "100. Kaj je eksplozivna zmes?",
        "A": "zmes, kjer ni eksplozije",
        "B": "zmes, ki ob iskri povzroči eksplozijo",
        "C": "zmes, kjer gorenje preneha",
        "correct": "B"
    },
    {
        "q": "101. Kaj je spodnja meja eksplozivnosti?",
        "A": "nad katero ni eksplozivno",
        "B": "nad katero je eksplozivno",
        "C": "pod katero ni eksplozivno",
        "correct": "C"
    },
    {
        "q": "102. Kaj je zgornja meja eksplozivnosti?",
        "A": "nad katero je eksplozivno",
        "B": "pod katero ni eksplozivno",
        "C": "pod katero je eksplozivno",
        "correct": "B"
    },
    {
        "q": "103. Kakšna je osnovna ureditev gasilske enote?",
        "A": "enovrstna",
        "B": "dvovrstna",
        "C": "kolona po dva",
        "correct": "B"
    },
    {
        "q": "104. Kakšno mora biti povelje?",
        "A": "jasno, glasno in popolno",
        "B": "tiho in jasno",
        "C": "samo popolno",
        "correct": "A"
    },
    {
        "q": "105. V katero ureditev se razvrstijo gasilci ob povelju »dve vrsti zbor«?",
        "A": "dvovrstno",
        "B": "enovrstno",
        "C": "kolona po eden",
        "correct": "A"
    },
    {
        "q": "106. S katero roko gasilci pozdravljamo?",
        "A": "z nobeno",
        "B": "z levo",
        "C": "z desno",
        "correct": "C"
    },
    {
        "q": "107. Kaj poveljuje vodja za zavijanje v levo?",
        "A": "z levim krilom",
        "B": "z desnim krilom",
        "C": "na levo",
        "correct": "B"
    },
    {
        "q": "108. Katere vrste korakov poznamo?",
        "A": "pohodni, prosti, žalni, tek",
        "B": "napetostni in prosti",
        "C": "gasilski in vojaški",
        "correct": "B"
    },
    {
        "q": "109. Kaj pomeni povelje »polkrog na desno«?",
        "A": "½ kroga",
        "B": "¼ kroga",
        "C": "povelje ne obstaja",
        "correct": "B"
    }
,
    {
        "q": "110. Kako gasilci pozdravljajo?",
        "A": "samo z roko",
        "B": "samo z obračanjem glave",
        "C": "z roko, pa tudi z obračanjem glave",
        "correct": "C"
    },
    {
        "q": "111. Kaj od naštetega ima ureditev enote pri razvrščanju?",
        "A": "čelo, krilo, bok",
        "B": "glavo, krilo, bok",
        "C": "čelo, krilo, rob",
        "correct": "A"
    },
    {
        "q": "112. S katero nogo se začne premikanje?",
        "A": "z desno nogo",
        "B": "vseeno s katero nogo",
        "C": "z levo nogo",
        "correct": "C"
    },
    {
        "q": "113. Kaj je električna napetost?",
        "A": "potencialna razlika med dvema točkama",
        "B": "usmerjeno gibanje elektronov",
        "C": "produkt sile in poti",
        "correct": "A"
    },
    {
        "q": "114. Kakšno električno napetost poznamo?",
        "A": "varno in nevarno",
        "B": "enosmerno in izmenično",
        "C": "enosmerno in krožno",
        "correct": "B"
    },
    {
        "q": "115. Kaj je električni tok?",
        "A": "produkt sile in poti",
        "B": "urejeno gibanje elektronov",
        "C": "potencialna razlika med dvema točkama",
        "correct": "B"
    },
    {
        "q": "116. V kateri enoti izražamo električni upor?",
        "A": "v Ohmih",
        "B": "v Joulih",
        "C": "v Watih",
        "correct": "A"
    },
    {
        "q": "117. Kaj opisuje Ohmov zakon?",
        "A": "razmerje med silo in potjo",
        "B": "razmerje med električnim tokom, napetostjo in upornostjo",
        "C": "razmerje med jakostjo in smerjo električnega toka",
        "correct": "B"
    },
    {
        "q": "118. Katere so najpomembnejše naprave za proizvodnjo električne energije?",
        "A": "elektromotorji, svetila, grelna telesa, elektronika",
        "B": "elektrogeneratorji, akumulatorji, baterije, fotocelice, gorivne celice",
        "C": "transformatorji, usmerniki, pretvorniki",
        "correct": "B"
    },
    {
        "q": "119. Kateri so najpomembnejši porabniki električne energije?",
        "A": "elektrogeneratorji, baterije, fotocelice",
        "B": "transformatorji, usmerniki",
        "C": "elektromotorji, svetila, grelna telesa, elektronika",
        "correct": "C"
    },
    {
        "q": "120. Kaj je transformator?",
        "A": "pretvarja električno v mehansko energijo",
        "B": "pretvarja električno energijo ene napetosti v drugo napetost",
        "C": "pretvarja mehansko v kinetično energijo",
        "correct": "B"
    },
    {
        "q": "121. Kaj je elektromotor?",
        "A": "mehansko v kinetično",
        "B": "električno v mehansko ali kinetično",
        "C": "napetost v napetost",
        "correct": "B"
    },
    {
        "q": "122. Kaj je strela?",
        "A": "električni preboj med oblakom in zemljo",
        "B": "pretvorba napetosti",
        "C": "ni električni pojav",
        "correct": "A"
    },
    {
        "q": "123. Kako se kažejo poškodbe električnega toka skozi telo?",
        "A": "rahlo tresenje",
        "B": "brez poškodb",
        "C": "opekline, ožganine, poškodbe organov",
        "correct": "C"
    },
    {
        "q": "124. Kako ugotovimo ustreznost gasilske delovne obleke?",
        "A": "etiketa proizvajalca",
        "B": "oštevilčen znak GZS in tipizacija",
        "C": "barva obleke",
        "correct": "B"
    },
    {
        "q": "125. Kateri so sestavni deli izolirnega dihalnega aparata?",
        "A": "ogrodje, jeklenka, maska",
        "B": "ogrodje, jeklenka, ventil, piščalka, manometer, maska",
        "C": "jeklenka in maska",
        "correct": "B"
    },
    {
        "q": "126. Kako delimo gasilnike?",
        "A": "po barvi",
        "B": "po starosti",
        "C": "po vrsti in količini gasilnega sredstva",
        "correct": "C"
    },
    {
        "q": "127. Kako delimo gasilne cevi glede na dimenzijo?",
        "A": "sesalne, tlačne",
        "B": "A, B, C, D",
        "C": "1, 2, 3, 4",
        "correct": "B"
    },
    {
        "q": "128. Kako delimo gasilne cevi glede na vrsto?",
        "A": "A, B, C, D",
        "B": "gumijaste in plastične",
        "C": "sesalne, tlačne",
        "correct": "C"
    },
    {
        "q": "129. Kakšen premer ima C-cev?",
        "A": "52 (42) mm",
        "B": "25 mm",
        "C": "75 mm",
        "correct": "A"
    },
    {
        "q": "130. Kakšen premer ima A-cev?",
        "A": "75 mm",
        "B": "25 mm",
        "C": "110 mm",
        "correct": "C"
    },
    {
        "q": "131. Katere so osnovne oblike vodnih curkov?",
        "A": "polni, razpršeni, kombinirani, vodna megla",
        "B": "polni, prazni, kombinirani",
        "C": "polni, nepolni, kombinirani",
        "correct": "A"
    },
    {
        "q": "132. V katere skupine delimo ročnike?",
        "A": "polni, razpršeni, kombinirani",
        "B": "navadni, univerzalni, posebni ali kombinirani",
        "C": "sesalni, tlačni, prehodni",
        "correct": "B"
    },
    {
        "q": "133. Zakaj uporabljamo gasilne spojke?",
        "A": "spajanje cevi in armatur",
        "B": "gašenje začetnih požarov",
        "C": "mešanje vode in penila",
        "correct": "A"
    },
    {
        "q": "134. Kako delimo gasilne spojke glede na dimenzijo?",
        "A": "1, 2, 3, 4",
        "B": "majhne, srednje, velike",
        "C": "A, B, C, D",
        "correct": "C"
    },
    {
        "q": "135. Kako delimo gasilne spojke glede na funkcijo?",
        "A": "sesalne, tlačne, toge, slepe, prehodne",
        "B": "gasilne in reševalne",
        "C": "samo po dimenziji",
        "correct": "A"
    },
    {
        "q": "136. Kaj je penilno število?",
        "A": "količina penila v peni v %",
        "B": "razmerje pene in mešanice vode in penila",
        "C": "količina zraka v peni",
        "correct": "B"
    },
    {
        "q": "137. Katere snovi se mešata v mešalcu pene?",
        "A": "zrak in voda",
        "B": "zrak in penilo",
        "C": "voda in penilo",
        "correct": "C"
    },
    {
        "q": "138. Kako delimo gasilske črpalke glede na tlak?",
        "A": "nizko, srednje, visoko tlačne",
        "B": "malo in veliko tlačne",
        "C": "ne delimo jih",
        "correct": "A"
    },
    {
        "q": "139. Kaj pomeni 8/8 motorna brizgalna?",
        "A": "80 l/min pri 8 bar",
        "B": "8000 l/min pri 8 bar",
        "C": "800 l/min pri 8 bar",
        "correct": "C"
    },
    {
        "q": "140. Katere naprave so za reševanje z višin?",
        "A": "ročniki",
        "B": "vskočnica, spustnica, lestev",
        "C": "ventili",
        "correct": "B"
    },
    {
        "q": "141. Katere vrste lestev poznamo?",
        "A": "lesena, aluminijasta",
        "B": "gasilska, pleskarska",
        "C": "prislanjalna, zložljiva, stikalna, raztegljiva, kljukasta",
        "correct": "C"
    },
    {
        "q": "142. Katera vozila so gasilska vozila?",
        "A": "vsa za gašenje in reševanje",
        "B": "vozila z modro lučjo",
        "C": "vozila gasilskih društev",
        "correct": "A"
    },
    {
        "q": "143. Kaj pomeni GVC-1?",
        "A": "2000–3000 l vode, 1+5 do 1+8",
        "B": "1600 l vode",
        "C": "1500 l vode",
        "correct": "A"
    },
    {
        "q": "144. Kaj pomeni GVC-2?",
        "A": "2400 l vode",
        "B": "4000–6000 l vode, 1+2",
        "C": "1600 l vode",
        "correct": "B"
    },
    {
        "q": "145. Kaj pomeni GVC-3?",
        "A": "5000 l vode",
        "B": "5000 l vode + penilo",
        "C": "6000–9000 l vode, 1+1 ali 1+2",
        "correct": "C"
    },
    {
        "q": "146. Kaj pomeni GVL-1?",
        "A": "logistično vozilo",
        "B": "vozilo za vodo",
        "C": "vozilo za lestev",
        "correct": "A"
    },
    {
        "q": "147. Kaj pomeni GVM-1?",
        "A": "prevoz mladine",
        "B": "prevoz moštva",
        "C": "motorna brizgalna",
        "correct": "B"
    },
    {
        "q": "148. Kaj pomeni GV-1?",
        "A": "1+5 do 1+8 posadka",
        "B": "1000 l vode",
        "C": "1+9 posadka",
        "correct": "A"
    },
    {
        "q": "149. Kaj pomeni GVV-1?",
        "A": "1+5 do 1+8 + 300 l vode",
        "B": "vozilo za vodo",
        "C": "brez vode",
        "correct": "A"
    },
    {
        "q": "150. Kaj pomeni PV-1?",
        "A": "vozilo za vodo",
        "B": "manjše poveljniško vozilo",
        "C": "večje poveljniško vozilo",
        "correct": "B"
    },
    {
        "q": "151. Koliko šteje posadka GVV-1?",
        "A": "1+5 do 1+8",
        "B": "1+2",
        "C": "1+1",
        "correct": "A"
    },
    {
        "q": "152. Koliko šteje posadka GVC-2?",
        "A": "1+8",
        "B": "1+5",
        "C": "1+2",
        "correct": "C"
    },
    {
        "q": "153. Kaj pomeni GVGP-1?",
        "A": "prevoz gasilcev",
        "B": "gašenje gozdnih požarov (večje)",
        "C": "gašenje gozdnih požarov (manjše)",
        "correct": "C"
    },
    {
        "q": "154. Katero vozilo mora imeti visokotlačno črpalko?",
        "A": "GVV-2",
        "B": "GVC-1",
        "C": "GVC-4",
        "correct": "A"
    },
    {
        "q": "155. Ali je tipizacija GZS obvezna?",
        "A": "ne",
        "B": "da",
        "C": "po želji",
        "correct": "B"
    },
    {
        "q": "156. Katere radijske postaje poznamo?",
        "A": "prenosne, vgrajene",
        "B": "ročne, avtomobilske",
        "C": "ročne, mobilne, stabilne",
        "correct": "C"
    },
    {
        "q": "157. Kaj je gorenje?",
        "A": "tlenje lesa",
        "B": "trohnenje",
        "C": "kemijska reakcija s kisikom, toploto in svetlobo",
        "correct": "C"
    },
    {
        "q": "158. Kateri pogoji so potrebni za gorenje?",
        "A": "gorljiva snov, CO2, toplota",
        "B": "gorljiva snov, kisik, toplota",
        "C": "kisik, vžigalica, voda",
        "correct": "B"
    },
    {
        "q": "159. Kaj tvori trikotnik gorenja?",
        "A": "negorljiva snov, kisik, toplota",
        "B": "gorljiva snov, CO2, toplota",
        "C": "gorljiva snov, kisik, toplota",
        "correct": "C"
    },
    {
        "q": "160. Kaj je žarenje?",
        "A": "način gorenja trdnih snovi",
        "B": "plamen",
        "C": "dim",
        "correct": "A"
    },
    {
        "q": "161. Kaj je temperatura plamenišča?",
        "A": "vrelišče",
        "B": "temperatura, kjer plamen ne ugasne",
        "C": "temperatura, kjer nastanejo hlapi in gorenje preneha po odstranitvi plamena",
        "correct": "C"
    },
    {
        "q": "162. Kaj je vžigna temperatura?",
        "A": "najnižja temperatura za vžig z zunanjim virom",
        "B": "vrelišče",
        "C": "plamenišče",
        "correct": "A"
    },
    {
        "q": "163. Kaj je temperatura samovžiga?",
        "A": "vžig z zunanjim virom",
        "B": "plamen ne ugasne",
        "C": "vžig brez zunanjega vira",
        "correct": "C"
    },
    {
        "q": "164. Kaj je meja vnetljivosti?",
        "A": "temperatura vžiga",
        "B": "koncentracija hlapov za vžig",
        "C": "vrelišče",
        "correct": "B"
    },
    {
        "q": "165. Kako delimo požare glede na okolje?",
        "A": "urbani, industrijski, naravni",
        "B": "zgradbe, narava",
        "C": "A, B, C, D",
        "correct": "B"
    },
    {
        "q": "166. Kako delimo požare glede na velikost?",
        "A": "majhni, veliki",
        "B": "majhni, srednji, veliki, katastrofalni",
        "C": "začetni, razširjeni",
        "correct": "B"
    },
    {
        "q": "167. Kako delimo požare glede na material?",
        "A": "A, B, C, D razredi",
        "B": "trdni in netrdni",
        "C": "naravni in umetni",
        "correct": "A"
    },
    {
        "q": "168. V kakšnem stanju so gorljive snovi?",
        "A": "trdnem ali plinastem",
        "B": "vnetljivem",
        "C": "trdnem, tekočem in plinastem",
        "correct": "C"
    },
    {
        "q": "169. Kateri plin je v gospodinjski jeklenki?",
        "A": "helij",
        "B": "mešanica plinov",
        "C": "propan butan",
        "correct": "C"
    }
,
  {
    "q": "170. V kakšnem agregatnem stanju je gospodinjski plin v jeklenkah?",
    "A": "v plinastem stanju",
    "B": "v tekočem stanju",
    "C": "v trdnem stanju",
    "correct": "B"
  },
  {
    "q": "171. Požari razreda A so požari:",
    "A": "gorljivih tekočih snovi",
    "B": "gorljivih plinov",
    "C": "gorljivih trdnih snovi",
    "correct": "C"
  },
  {
    "q": "172. Požari razreda B so požari:",
    "A": "požari lahkih kovin",
    "B": "gorljivih tekočih snovi",
    "C": "gorljivih plinov",
    "correct": "B"
  },
  {
    "q": "173. Požari razreda C so požari:",
    "A": "gorljivih plinov",
    "B": "požari lahkih kovin",
    "C": "gorljivih trdnih snovi",
    "correct": "A"
  },
  {
    "q": "174. Požari razreda D so požari:",
    "A": "gorljivih tekočih snovi",
    "B": "požari lahkih kovin",
    "C": "gorljivih plinov",
    "correct": "B"
  },
  {
    "q": "175. Katere so faze požara v objektu?",
    "A": "faza začetnega, srednjega, končnega požara",
    "B": "faza začetnega, razvitega, nehajočega požara",
    "C": "faza začetnega, rastočega, razvitega, pojemajočega požara",
    "correct": "C"
  },
  {
    "q": "176. Kaj se zgodi v fazi začetnega požara?",
    "A": "pride do vžiga in začetka gorenja gorljivega materiala",
    "B": "pride do pojemanja požara",
    "C": "pride do zelo hitrega gorenja",
    "correct": "A"
  },
  {
    "q": "177. Kaj je »požarni preskok« ali »flashover«?",
    "A": "pride do pojemanja požara",
    "B": "plameni zajamejo ves prostor in požar preide v polno razviti požar",
    "C": "to je trenutek, ko ogenj popolnoma ugasne",
    "correct": "B"
  },
  {
    "q": "178. Po katerih treh mehanizmih se toplota širi iz toplejšega na hladnejše območje?",
    "A": "prevajanje, vzgon, sevanje",
    "B": "izolativnost, integriteta, stabilnost",
    "C": "požarna obremenitev, površina gorljivih materialov, potreba po kisiku",
    "correct": "A"
  },
  {
    "q": "179. Kaj je sevanje ali radiacija?",
    "A": "prenos toplote skozi materiale",
    "B": "prenos toplotne energije z elektromagnetnim valovanjem",
    "C": "gibanje toplejšega in redkejšega plina skozi hladnejši in gostejši plin",
    "correct": "B"
  },
  {
    "q": "180. Kaj je prevajanje ali kondukcija?",
    "A": "gibanje toplejšega in redkejšega plina skozi hladnejši in gostejši plin",
    "B": "prenos toplotne energije z elektromagnetnim valovanjem",
    "C": "prenos toplote skozi materiale",
    "correct": "C"
  },
  {
    "q": "181. Kaj predstavlja požarna obremenitev?",
    "A": "prenos toplotne energije z elektromagnetnim valovanjem",
    "B": "skupno količino toplote, ki bi se sprostila pri popolnem sežigu vseh gorljivih materialov v prostoru",
    "C": "prenos toplote skozi materiale",
    "correct": "B"
  },
  {
    "q": "182. Kateri so kriteriji za požarno odpornost?",
    "A": "izolativnost, integriteta, stabilnost",
    "B": "prevajanje, vzgon, sevanje",
    "C": "konvekcija, radiacija, kondukcija",
    "correct": "A"
  },
  {
    "q": "183. Kaj je gašenje?",
    "A": "vsaka snov, ki prekine proces gorenja",
    "B": "spajanje gorljive snovi s kisikom",
    "C": "vsaka prekinitev procesa gorenja",
    "correct": "C"
  },
  {
    "q": "184. Kaj je gasilno sredstvo?",
    "A": "vsaka negorljiva snov",
    "B": "vsaka snov, ki prekine proces gorenja",
    "C": "vsaka snov, ki lahko ob prisotnosti kisika in toplote povzroči gorenje",
    "correct": "B"
  },
  {
    "q": "185. Katere so metode gašenja z gasilnimi sredstvi?",
    "A": "odstranitev gorljive snovi, odstranitev kisika, odstranitev toplote, motnja kemijskih reakcij gorenja",
    "B": "poznamo samo ohladitev ali zadušitev",
    "C": "gašenje z vodo, peno, prahom, ogljikovim dioksidom",
    "correct": "A"
  },
  {
    "q": "186. Katero gasilno sredstvo je najcenejše in najbolj razširjeno?",
    "A": "ogljikov dioksid",
    "B": "pena",
    "C": "voda",
    "correct": "C"
  },
  {
    "q": "187. Kako deluje voda kot gasilno sredstvo?",
    "A": "samo hladilno",
    "B": "hladilno in dušilno",
    "C": "samo dušilno",
    "correct": "B"
  },
  {
    "q": "188. Kaj sestavlja gasilno peno?",
    "A": "voda, penilno sredstvo in zrak",
    "B": "voda, penilno sredstvo, zrak, penilno število",
    "C": "voda in penilno sredstvo",
    "correct": "A"
  },
  {
    "q": "189. Kako deluje pena kot gasilno sredstvo?",
    "A": "samo dušilno",
    "B": "samo hladilno",
    "C": "dušilno in hladilno",
    "correct": "C"
  },
  {
    "q": "190. Kako deluje ogljikov dioksid kot gasilno sredstvo?",
    "A": "samo dušilno",
    "B": "dušilno in ohlajevalno",
    "C": "samo ohlajevalno",
    "correct": "A"
  },
  {
    "q": "191. Ali je ogljikov dioksid težji od zraka?",
    "A": "ne, je lažji od zraka",
    "B": "da",
    "C": "ne, je enako težak kot zrak",
    "correct": "B"
  },
  {
    "q": "192. S katerim gasilnim sredstvom so polnjeni ročni gasilni aparati z oznako S?",
    "A": "s prahom",
    "B": "z ogljikovim dioksidom",
    "C": "s peno",
    "correct": "A"
  },
  {
    "q": "193. Kako gasimo s prahom?",
    "A": "prah usmerimo nad gorečo površino, prah duši požar",
    "B": "prah slabo gasi ogenj",
    "C": "prah vržemo v žerjavico",
    "correct": "A"
  },
  {
    "q": "194. Kako gasimo s peno pokončne stene?",
    "A": "cik-cak od spodaj navzgor",
    "B": "cik-cak od zgoraj navzdol",
    "C": "vseeno kako",
    "correct": "A"
  },
  {
    "q": "195. Ali lahko požar, ki ga je povzročila elektrika, gasimo z vodo?",
    "A": "da, če so okna in vrata odprta",
    "B": "ne",
    "C": "da, če smo izključili električno napetost",
    "correct": "B"
  },
  {
    "q": "196. Požare na električnih napravah uspešno gasimo z naslednjim gasilnim sredstvom:",
    "A": "s prahom in ogljikovim dioksidom",
    "B": "s curkom vode",
    "C": "z lahko peno",
    "correct": "A"
  },
  {
    "q": "197. Požare razreda »C« uspešno gasimo z naslednjim gasilnim sredstvom:",
    "A": "s peno in vodo",
    "B": "s prahom in ogljikovim dioksidom",
    "C": "samo z vodo",
    "correct": "B"
  },
  {
    "q": "198. Katera so priročna gasilna sredstva?",
    "A": "pesek, zemlja",
    "B": "voda",
    "C": "požarna metla",
    "correct": "A"
  },
  {
    "q": "199. Za gašenje katerih požarov uporabljamo požarno metlo?",
    "A": "za gašenje požarov na strehi",
    "B": "za gašenje travniških in talnih gozdnih požarov",
    "C": "za gašenje zunanjih požarov",
    "correct": "B"
  },
  {
    "q": "200. Kam usmerimo curek, ko gasimo z vodo?",
    "A": "v plamen",
    "B": "nad plamenom",
    "C": "v žarišče požara",
    "correct": "C"
  },
  {
    "q": "201. Na kakšen način smo pogasili ogenj v ponvi, ki smo jo pokrili s pokrovko?",
    "A": "odstranili smo gorljivo snov",
    "B": "odstranili smo toploto",
    "C": "odstranili smo kisik",
    "correct": "C"
  },
  {
    "q": "202. Kakšne javljalnike požarov poznamo glede na način delovanja?",
    "A": "prenosne in vgrajene",
    "B": "ročne in avtomatske",
    "C": "ročne in mobilne",
    "correct": "B"
  },
  {
    "q": "203. Kaj je gradbeništvo?",
    "A": "tehnična dejavnost gradnje cest",
    "B": "tehnična dejavnost gradnje stavb",
    "C": "tehnična dejavnost graditve in vzdrževanja objektov",
    "correct": "C"
  },
  {
    "q": "204. Kako se deli panoga gradbeništvo?",
    "A": "na novo in staro gradnjo",
    "B": "na visoko gradnjo, nizko gradnjo, vodogradnjo",
    "C": "na visoko in nizko gradnjo",
    "correct": "B"
  },
  {
    "q": "205. V katere 3 skupine delimo gradbeni material?",
    "A": "glavni, vezni, pomožni",
    "B": "beton, les, železo",
    "C": "gorljiv, polgorljiv, negorljiv",
    "correct": "C"
  },
  {
    "q": "206. Kako delimo gradbeni material glede na izvor?",
    "A": "gorljiv in negorljiv",
    "B": "naravni in umetni",
    "C": "glavni in pomožni",
    "correct": "B"
  },
  {
    "q": "207. Kako delimo material glede na obnašanje materiala ob visokih temperaturah?",
    "A": "vnetljiv, gorljiv, negorljiv",
    "B": "gorljiv, polgorljiv, negorljiv",
    "C": "zelo lahko vnetljiv, lahko vnetljiv, vnetljiv, gorljiv, težko gorljiv, negorljiv",
    "correct": "C"
  },
  {
    "q": "208. Naštej glavne dele stavbe!",
    "A": "zidovi in stebri, stropi, stopnišča, streha",
    "B": "temelji, zidovi in stebri, stropi in podvlake, stopnišča, strešna konstrukcija s strešno kritino",
    "C": "temelji, zidovi in stropi, stopnice, streha",
    "correct": "B"
  },
  {
    "q": "209. Kaj je požarni zid?",
    "A": "vsak zid, ki deli večji objekt na dva ali več delov",
    "B": "vsak zid, ki je zgrajen iz gorljivega materiala",
    "C": "stenska stavbna konstrukcija, ki deli objekt v dva ali več požarnih sektorjev",
    "correct": "C"
  },
  {
    "q": "210. Katera mesta za odvzem vode poznamo?",
    "A": "stalna, občasna, pomožna",
    "B": "začasna in stalna",
    "C": "glavna in pomožna",
    "correct": "C"
  },
  {
    "q": "211. Ali lahko pri gašenju z vodo uporabljamo slano (morsko) vodo?",
    "A": "ne",
    "B": "da",
    "C": "samo v primeru požara v naravi",
    "correct": "B"
  },
  {
    "q": "212. Katera 2 sistema vodovodnega omrežja poznamo?",
    "A": "vejnato in krožno omrežje",
    "B": "verižno in krožno omrežje",
    "C": "vejnato in verižno omrežje",
    "correct": "A"
  },
  {
    "q": "213. Katere 3 vrste hidrantov poznamo?",
    "A": "zemeljski, nadzemeljski, vzidani",
    "B": "podzemni, nadzemni, zidni",
    "C": "zunanji, notranji, zemeljski",
    "correct": "A"
  },
  {
    "q": "214. Kako je zaznamovana lega hidrantov?",
    "A": "lega ni nič zaznamovana",
    "B": "lega je označena samo na požarnih načrtih",
    "C": "s hidrantnimi tablicami",
    "correct": "C"
  },
  {
    "q": "215. Na osnovi katerih požarnih veličin odkrivajo javljalniki požara?",
    "A": "teme, vročine, dima",
    "B": "dima, toplote, plamena",
    "C": "mraza, dima, svetlobe",
    "correct": "B"
  },
  {
    "q": "216. Kako delimo javljalnike glede na način javljanja?",
    "A": "prenosne in stabilne",
    "B": "ročne in mobilne",
    "C": "ročne in avtomatske",
    "correct": "C"
  },
  {
    "q": "217. Pod kakšnimi pogoji deluje ionizacijski javljalnik požara?",
    "A": "na osnovi temperature",
    "B": "na osnovi svetlobe",
    "C": "na osnovi dima",
    "correct": "C"
  },
  {
    "q": "218. Pod kakšnimi pogoji deluje plamenski javljalnik požara?",
    "A": "na osnovi dima",
    "B": "na osnovi svetlobe",
    "C": "na osnovi temperature",
    "correct": "B"
  },
  {
    "q": "219. Kako imenujemo javljalnike, ki reagirajo zaradi hitrega porasta temperature?",
    "A": "linearni termični",
    "B": "termomaksimalni",
    "C": "termodiferencialni",
    "correct": "C"
  },
  {
    "q": "220. Kaj je tehnično reševanje?",
    "A": "sposobnost uporabe tehničnih metod za odpravo ogrožanja",
    "B": "reševanje tehničnih predmetov",
    "C": "reševanje ljudi iz tehničnih nezgod",
    "correct": "A"
  },
  {
    "q": "221. Kaj je nezgoda?",
    "A": "dogodek, ki povzroči samo poškodbo ljudi",
    "B": "nepričakovan dogodek, ki lahko povzroči škodo",
    "C": "vsak dogodek, ki povzroči poškodbo lastnine",
    "correct": "B"
  },
  {
    "q": "222. Kateri so vzroki za nezgodo?",
    "A": "naravne in nenaravne nesreče",
    "B": "naravne in prometne nezgode",
    "C": "naravne, tehnične in prometne nezgode",
    "correct": "C"
  },
  {
    "q": "223. Katere so naravne nesreče?",
    "A": "požar na objektu, potres, plaz",
    "B": "potres, povodenj, neurje, zmrzal, žled",
    "C": "poplava, potres, požar večjega objekta",
    "correct": "B"
  },
  {
    "q": "224. Najpogostejše nesreče za tehnično reševanje so:",
    "A": "prometne nesreče, padci, reševanje iz ruševin, vode",
    "B": "padci letal, ledene površine",
    "C": "reševanje plovil, eksplozivni plini",
    "correct": "A"
  },
  {
    "q": "225. Kaj je potrebno za tehnični poseg?",
    "A": "le gasilci in oprema",
    "B": "vodenje, disciplina, strokovnjaki, oprema",
    "C": "samo oprema",
    "correct": "B"
  },
  {
    "q": "226. Sporazumevanje brez radijskih zvez:",
    "A": "SMS",
    "B": "pozivniki",
    "C": "signali z rokami, vrvjo, lučjo, piščalko",
    "correct": "C"
  },
  {
    "q": "227. Dvignjena desna roka pomeni:",
    "A": "nimam zraka",
    "B": "vse je v redu",
    "C": "nekaj je narobe",
    "correct": "B"
  },
  {
    "q": "228. Kaj je gasilska taktika?",
    "A": "alarmiranje sil",
    "B": "način ukrepanja ob intervenciji",
    "C": "prihod na intervencijo",
    "correct": "B"
  },
  {
    "q": "229. Pravilo gašenja:",
    "A": "hitrost ni pomembna",
    "B": "hitrost je edina pomembna",
    "C": "hitro, učinkovito in z ustrezno količino sredstva",
    "correct": "C"
  },
  {
    "q": "230. Taktični nastopi voda:",
    "A": "samostojni in skupinski",
    "B": "različni tipi nastopov",
    "C": "notranji in zunanji",
    "correct": "B"
  },
  {
    "q": "231. Ločeni nastop:",
    "A": "povezava več črpalk zaradi razdalje",
    "B": "dovolj opreme",
    "C": "obkroženje požara",
    "correct": "A"
  },
  {
    "q": "232. Relejni nastop:",
    "A": "več črpalk v verigi",
    "B": "en oddelek oskrbuje drugega",
    "C": "dva cevovoda",
    "correct": "A"
  },
  {
    "q": "233. Pred gašenjem se prepričamo:",
    "A": "samo o ljudeh",
    "B": "samo kaj gori",
    "C": "o vseh pogojih na terenu",
    "correct": "C"
  },
  {
    "q": "234. Aktivna požarna obramba:",
    "A": "gašenje",
    "B": "neposreden napad",
    "C": "zaščita ogroženih objektov",
    "correct": "C"
  },
  {
    "q": "235. Pasivna požarna obramba:",
    "A": "zaščita ogroženih objektov",
    "B": "reševanje ljudi",
    "C": "neposreden napad",
    "correct": "A"
  },
  {
    "q": "236. Vrste napadov:",
    "A": "hitri, počasni",
    "B": "samostojni, skupinski",
    "C": "notranji, zunanji, sestavljeni, čelni, obkroženje",
    "correct": "C"
  },
  {
    "q": "237. Sestavljeni napad:",
    "A": "ena stran",
    "B": "notranji in zunanji hkrati",
    "C": "brez notranjega napada",
    "correct": "B"
  },
  {
    "q": "238. Čelni napad:",
    "A": "ni več notranjega napada",
    "B": "notranji in zunanji",
    "C": "ena stran objekta",
    "correct": "C"
  },
  {
    "q": "239. Napad z obkroženjem:",
    "A": "več strani objekta",
    "B": "ena stran",
    "C": "notranji in zunanji",
    "correct": "A"
  },
  {
    "q": "240. Nevarnosti notranjih požarov:",
    "A": "enake kot vedno",
    "B": "elektrika, plini, eksplozije, rušenje",
    "C": "kot pri zunanjih",
    "correct": "B"
  },
  {
    "q": "241. Vstop v zadimljen prostor:",
    "A": "hitro",
    "B": "počasi in varno z opremo",
    "C": "počakamo",
    "correct": "B"
  },
  {
    "q": "242. Dimniški požar:",
    "A": "voda od zgoraj",
    "B": "prah ali CO2 skozi vratca",
    "C": "zadušitev od zgoraj",
    "correct": "B"
  },
  {
    "q": "243. Goreča oseba:",
    "A": "vlažna krpa",
    "B": "voda",
    "C": "zadušitev",
    "correct": "C"
  },
  {
    "q": "244. Namen gasilskih tekmovanj:",
    "A": "preverjanje opreme",
    "B": "tradicija",
    "C": "preverjanje usposobljenosti",
    "correct": "C"
  },
  {
    "q": "245. Gasilska tekmovanja spadajo v:",
    "A": "šport",
    "B": "usposabljanja",
    "C": "tehniko",
    "correct": "B"
  },
  {
    "q": "246. Tekmovalne kategorije:",
    "A": "pionirji, mladinci, člani, starejši gasilci (razširjeno)",
    "B": "osnovne skupine",
    "C": "poklicni in prostovoljni",
    "correct": "A"
  },
  {
    "q": "247. Rokavice na tekmovanjih:",
    "A": "delovne",
    "B": "zaščitne",
    "C": "gasilske zaščitne ali usnjene",
    "correct": "C"
  },
  {
    "q": "248. Sesalne cevi:",
    "A": "6",
    "B": "4",
    "C": "2",
    "correct": "C"
  },
  {
    "q": "249. Člani A starost:",
    "A": "30+",
    "B": "16+",
    "C": "povprečje 30+",
    "correct": "B"
  },
  {
    "q": "250. Člani B starost:",
    "A": "30+ vsi",
    "B": "več kot polovica nad 30 let",
    "C": "16+",
    "correct": "B"
  }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/questions")
def questions():
    return jsonify(QUESTIONS)

if __name__ == "__main__":
    app.run(debug=True)