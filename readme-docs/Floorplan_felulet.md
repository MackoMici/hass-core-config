# Floorplan felület kialakítás - update 2023-10-09

Nagy segítségre volt az alábbi videó a felület elkészítésében [BitBorn Youtube](https://www.youtube.com/watch?v=MCNxgb0mrSA)

A felület kialakításához a [Sweet Home 3D](https://www.sweethome3d.com/) programot használtam.
![sweethome](https://github.com/MackoMici/hass-core-config/blob/main/readme-img/sweethome.png)
A programban nagyon sok bútor elemet megtalálni, de ha mégse lenne meg valami, lehet hozzá ingyenes csomagokat letölteni, hátha találuk benne megfelelőt. Sajnos robotporszívó az pont nem létezik így az nálam is lemaradt a tervrajzról. Majd jön az időigényes munka a felületet le kell konvertálni png-be, hogy lehessen használni. a 3D nézet menüben érdemes bekapcsolni, hogy egy külső ablakban jelenjen meg a 3D-s nézet így könnyebb beállítani hogyan nézzen ki az elkészített kép.  Érdemes itt jó alaposan megnézni a képet hogy minden olyan elem jól látható a képen amit vezérelni szertnénk (pl. nálam az egyik ablak azért lett nyitva mert nem tudtam olyan nézetet választani ahol minden jól látszik).
![sweethome_nezet](https://github.com/MackoMici/hass-core-config/blob/main/readme-img/sweethome_nezet.png)
Utána mindenképp tároljuk el a Megfigyelő pontot szintén a 3D nézet menüben. Jöhet a fotó készítés, ahol érdemes már a tablet kijelző felbontást figyelembe venni, valamint egy korai időpontot kiválasztani, hogy a nappali fény ne legyen túl zavaró. Ja és előtte minden fényforrás fényerősségét 0%-ra kell kapcsolni. Keressük meg az oldalsó listában ahol a bútorelemek vannak felsorolva az egyes fényforrásokat és Ctrl + E vagy dupla klikkel tudjuk szerkeszteni.
<img src="https://github.com/MackoMici/hass-core-config/blob/main/readme-img/sweethome_foto.png" width=30%>
Ha kész a fő 3D-s nézetünk és meg vagyunk elégedve a képpel, akkor szépen minden egyes fényforrás erősségét vegyük fel a nekünk tetsző szintre (nálan 50% volt a kisebb, helységekbe csak 25%) és generáljunk egy képet immár éjszakai időbeállítással, hogy csak az adott készülék fénye legyen látható. A fotó készítése ablakot nem fontos bezárni, így valamivel gyorsabban lehet haladni a konvertálással, csak ne feledjük a fényeket ki és bekapcsolni
![sweethome_foto](https://github.com/MackoMici/hass-core-config/blob/main/readme-img/sweethome_foto.png)

Ha kész minden fényforrás akkor már csak a felesleges hátteret kell eltávolítani a képeken ehhez a [GIMP](https://www.gimp.org/) nevű képszerkesztőt használtam, mivel sok kép van és csak az alaprajzon látszik jól minden, így érdemes azt betölteni kijelölni amit ki szeretnénk vágni majd utána a többi képet alá betölteni és akkor azokon is könnyen ugyan azokat a részeket el lehet távolítani. Az alfa csatornát hozzá kell adni minden képhez még vágás előtt és a végén szépen egyesével elmenteni. Itt már érdemes egységes nevet adni neki a későbbi könnyebb szerkesztés miatt.
![gimp](https://github.com/MackoMici/hass-core-config/blob/main/readme-img/gimp.png)

Jöhet az [Inkscape](https://inkscape.org/) program amivel az svg fájlt készítjük itt fogunk miven vezérelhető elemnek nevet adni és megadni a területet mikor mire reagáljon