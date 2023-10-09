# Floorplan felület kialakítás - update 2023-10-09

Nagy segítségre volt az alábbi videó a felület elkészítésében [BitBorn Youtube](https://www.youtube.com/watch?v=MCNxgb0mrSA)

## Sweethome 3D

A felület kialakításához a [Sweet Home 3D](https://www.sweethome3d.com/) programot használtam.
![sweethome](/readme-img/sweethome.png)
A programban nagyon sok bútor elemet megtalálni, de ha mégse lenne meg valami, lehet hozzá ingyenes csomagokat letölteni, hátha találuk benne megfelelőt. Sajnos robotporszívó az pont nem létezik így az nálam is lemaradt a tervrajzról. Majd jön az időigényes munka a felületet le kell konvertálni png-be, hogy lehessen használni. a _3D nézet_ menüben érdemes bekapcsolni, hogy egy külső ablakban jelenjen meg a 3D-s nézet így könnyebb beállítani hogyan nézzen ki az elkészített kép.  Érdemes itt jó alaposan megnézni a képet hogy minden olyan elem jól látható a képen amit vezérelni szertnénk (pl. nálam az egyik ablak azért lett nyitva mert nem tudtam olyan nézetet választani ahol minden jól látszik).
![sweethome_nezet](/readme-img/sweethome_nezet.png)
Utána mindenképp tároljuk el a _Megfigyelő pont_-ot szintén a _3D nézet_ menüben. Jöhet a fotó készítés, ahol érdemes már a tablet kijelző felbontást figyelembe venni, valamint egy korai időpontot kiválasztani, hogy a nappali fény ne legyen túl zavaró. Ja és előtte minden fényforrás fényerősségét 0%-ra kell kapcsolni. Keressük meg az oldalsó listában ahol a bútorelemek vannak felsorolva az egyes fényforrásokat és _Ctrl + E_ vagy _dupla klikkel_ tudjuk szerkeszteni.

<img src="/readme-img/sweethome_foto.png" width=30%>

Ha kész a fő 3D-s nézetünk és meg vagyunk elégedve a képpel, akkor szépen minden egyes fényforrás erősségét vegyük fel a nekünk tetsző szintre (nálan 50% volt a kisebb, helységekbe csak 25%) és generáljunk egy képet immár éjszakai időbeállítással, hogy csak az adott készülék fénye legyen látható. A _fotó készítés_-e ablakot nem fontos bezárni, így valamivel gyorsabban lehet haladni a konvertálással, csak ne feledjük a fényeket ki és bekapcsolni
![sweethome_foto](/readme-img/sweethome_feny.png)

## GIMP

Ha kész minden fényforrás akkor már csak a felesleges hátteret kell eltávolítani a képeken ehhez a [GIMP](https://www.gimp.org/) nevű képszerkesztőt használtam, mivel sok kép van és csak az alaprajzon látszik jól minden, így érdemes azt betölteni kijelölni amit ki szeretnénk vágni majd utána a többi képet alá betölteni és akkor azokon is könnyen ugyan azokat a részeket el lehet távolítani. Az _alfa csatornát_ hozzá kell adni minden képhez még vágás előtt és a végén szépen egyesével elmenteni. Itt már érdemes egységes nevet adni neki a későbbi könnyebb szerkesztés miatt.
![gimp](/readme-img/gimp.png)

## Inkscape

Jöhet az [Inkscape](https://inkscape.org/) program amivel az svg fájlt készítjük itt fogunk minden vezérelhető elemnek nevet adni és megadni a területet mikor mire reagáljon.
Elöszön indítsuk el a programot és az alap régeteg nevezzük át _Background_-ra az _XML editor_-ban pedig adjuk meg a méreteket amivel a tabletünk rendelkezik, valamint az _id_-t is írjuk át _background_-ra (bekarikázott részek) **Megjegyzés: az objektumokat nem szükséges átnevezni mivel mentéskor azok automatikusan át fognak neveződni.**
![ink1](/readme-img/inkscape_1.png)
Majd jöhet az alap háttér importálása a _Fájl menü_-ből, figyeljünk rá, hogy _Hivatkozásként_ húzzuk be ne ~~Beágyazva~~, mert akkor nagyon nagy lesz az svg fájl mérete.
![ink2](/readme-img/inkscape_2.png)
Itt is át kell írni a _méretét_ és a _pozicióját_ valamint az _id_-t és hozzá kell adni egy _href_ értéket ahol azt adjuk meg hol találja a képet a rendszer majd a Ha-ban
![ink3](/readme-img/inkscape_3.png)
Következő lépésben adjuk egy régetet a _Background_ réteg alrétegeként és nevezzük el _Light Overlays_-nek, az _id_-t itt se felejtsük el átnevezni. Ezután importájuk be az első képet amin valamelyik világítás be van kapcsolva, ugyanúgy ahogy a legelső alkalommal tettük és végezzük el itt is a _méret_ és _id_ átnevezést.
![ink4](/readme-img/inkscape_4.png)
Mostmár csak dulikálni kell a képet annyiszor ahány világítós képünk van. természetesen az _id_, _href_ és az _xlink_-et át kell írni. Mivel az svg egy szöveges fájl így akár el is menthetjük és szöveges fájlként is szerkeszthetjük.
![ink5](/readme-img/inkscape_5.png)