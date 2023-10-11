# Floorplan felület kialakítás

Nagy segítségre volt az alábbi videó a felület elkészítésében [BitBorn Youtube](https://www.youtube.com/watch?v=MCNxgb0mrSA)

## Sweethome 3D

A felület kialakításához a [Sweet Home 3D](https://www.sweethome3d.com/) programot használtam.
![sweethome](/readme-img/sweethome.png)
A programban nagyon sok bútor elemet megtalálni, de ha mégse lenne meg valami, lehet hozzá ingyenes csomagokat letölteni, hátha találuk benne megfelelőt. Sajnos robotporszívó az pont nem létezik így az nálam is lemaradt a tervrajzról. Majd jön az időigényes munka a felületet le kell konvertálni png-be, hogy lehessen használni. a _3D nézet_ menüben érdemes bekapcsolni, hogy egy külső ablakban jelenjen meg a 3D-s nézet így könnyebb beállítani hogyan nézzen ki az elkészített kép.  Érdemes itt jó alaposan megnézni a képet hogy minden olyan elem jól látható a képen amit vezérelni szertnénk (pl. nálam az egyik ablak azért lett nyitva mert nem tudtam olyan nézetet választani ahol minden jól látszik).
![sweethome_nezet](/readme-img/sweethome_nezet.png)
Utána mindenképp tároljuk el a _Megfigyelő pont_-ot szintén a _3D nézet_ menüben. Jöhet a fotó készítés, ahol érdemes már a tablet kijelző felbontást figyelembe venni, valamint egy korai időpontot kiválasztani, hogy a nappali fény ne legyen túl zavaró. Ja és előtte minden fényforrás fényerősségét 0%-ra kell kapcsolni. Keressük meg az oldalsó listában ahol a bútorelemek vannak felsorolva az egyes fényforrásokat és _Ctrl + E_ vagy _dupla klikkel_ tudjuk szerkeszteni.**Megjegyzés: mivel nem csak az alaprajz van a tableten így a legvégén a svg file mérete már kisebb lett mint a tablet kijelző mérete.**
 - png méret: 1523x1200
 - svg mérete: 1289x1179
 - tablet mérete: 1920x1200

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
Mostmár csak dulikálni kell a képet annyiszor ahány világítós képünk van. Természetesen az _id_, _href_ és az _xlink_-et át kell írni. Mivel az svg egy szöveges fájl így akár el is menthetjük és szöveges fájlként is szerkeszthetjük.
![ink5](/readme-img/inkscape_5.png)
Így már a világítás meg is van oldva minden egyes eszköznél és a felületen is szépen fog látszódni mit fog megvilágítani, valamint így a szint és az erősséget is lehet állítani.
Ne felejtsük el a _light-overlays_-t láthatatlanná tenni, mert küldönben zavaró lesz, hogy nem látjuk a teljes tervrajzot. Jöhetnek a helységek, adjunk hozzá egy _areas_ réteget és ez alatt hozzunk látre minden helységnek egy külön réteget. Itt se felejtsük el az _id_-t átnevezni (_areas.helységneve_). Utána nincs más dolgunk mint minden helységet szépen körberajzolni, hogy a megadjuk melyik területen érzékeljék a gombnyomást, valamint össze kell kötni az adott körvonalat és fényforrást. Ehhez kézzel adjunk hozzá egy _Új elemcsomópont_-ot _svg:use_ taggal majd az _id_-t nevezzük át az adott fényforrásra és adjunk hozzá _xlink:href_ tulajdonságot ahol az _érték_ a körberajzolt terület _id_-ja lesz.
![ink6](/readme-img/inkscape_6.png)
Most az _entities_ követlezik ahol a különböző tárgyakat rajzoljuk körbe és nevezzük el. **Fontos és érdemes a _HA_-ban használt neveket használni és azokat is egységesíteni, hogy később könnyebb legyen a feület kódolása** Végül a _sensors_ réteget kell megcsinálni ahol a helységek hőmérsékletét illetve páratartalmát akarjuk kiíratni akár a falakra. Ez egy sima szöveges elem csak az _id_-t ne feledjük el átnevezni.
Jöhet a mentés sima _svg_ fájlba mentsük le elsőre, majd _optimalizált svg_-be így kisebb lesz a fájl és jópár felesleges dolog törlődik belőle.
![ink7](/readme-img/inkscape_7.png)
**Érdekesség:** Mivel az aroma diffusor tud világítani is így valahogy 1 tárgyon meg kellett oldani, hogy két különböző módon tudjon viselkedni, így ott is egy linket készítettem.
```
<path id="fan.aroma_diffuser" d="m1176 186.39c-2.8527-0.97807-6.4955-0.81545-9.6397 0.33398-3.1442 1.1494-5.7888 3.2857-8.4234 5.9773-2.6347 2.6916-5.2592 5.9382-5.2293 8.9851 0.03 3.0468 2.7133 5.8928 5.039 7.6977s4.2938 2.5694 6.1411 2.731c1.8473 0.16159 3.5752-0.27889 5.6814-1.1816 2.1061-0.90273 4.5894-2.2669 7.2752-4.4335 2.6859-2.1666 5.5719-5.1336 6.6279-7.7495 1.0559-2.616 0.2805-4.8812-1.1382-7.0728-1.4187-2.1917-3.4813-4.3094-6.334-5.2875z" fill="none" stroke-width="1px"/>
<use id="light.aroma_diffuser_nightlight" xlink:href="fan.aroma_diffuser"/>
```

## Home Assistant

A teljes kódot _yaml_ fájlban írtam, megtalálható a [repo](/floorplan.yaml)-ban, a decluttering card miatt, hogy ne legyenek ismétlések és mindent csak 1 helyen kelljen kijavítani. Bár így is van ismétlés, de azt később még javítva lesz. A _template_-k includolása után kettéosztjuk a felületett _custom:grid-layout_-tal, majd mivel vannak a felületen plussz gombok, így az egészet egy _horizontal-stack_ kártyában helyetem el. utána már jöhet is a _floorplan_ kártya kialakítása.
```
- type: custom:floorplan-card
  style: |
    ha-card {
        max-width: 100%;
        margin: 0 auto;
        background: none;
        box-shadow: none;
    }
  config:
    image: /local/floorplan/House_2023_optimized.svg
    stylesheet: /local/floorplan/House_2023.css
    defaults:
      tap_action: none
```
**Fontos figyelni az elérési útvonalakra**, majd jöhetnek a vezérlő elemek szabályai első körben adjunk értéket a hő és páratartalom szövegeknek, mivel az svg fájlban is az _id_-nek ezt a nevet adtuk, így nem kell még külön _element_ nevet is megadni a kódban:
```
- name: Hőmérséklet
  entities:
    - sensor.haloszoba_temperature
    - sensor.konyha_temperature
    - sensor.nappali_temperature
    - sensor.ebedlo_temperature
    - sensor.gyerekszoba_temperature
    - sensor.furdoszoba_homerseklet
  state_action:
    - service: floorplan.text_set
      service_data: '${(entity.state !== undefined) ? Math.round(entity.state* 10) / 10 + "°C" : "unknown"}'
- name: Páratartalom
  entities:
    - sensor.haloszoba_humidity
    - sensor.konyha_humidity
    - sensor.nappali_humidity
    - sensor.ebedlo_humidity
    - sensor.gyerekszoba_humidity
    - sensor.furdoszoba_paratartalom
  state_action:
    - service: floorplan.text_set
      service_data: '${(entity.state !== undefined) ? Math.round(entity.state * 10) / 10 + "%" : "unknown"}'
```
Ahhoz, hogy az értékek úgy nézzenek ki mintha a falon lennének a _css_ fájl lesz a segítségre, itt lehet a szint az árnyékot és a transfomációt megadni, nem kell aggódni, elsőre elég nehéz eltalálni hogyan kellen forgatni a szöveget, de a böngészőben _F12_ gombra megnyílik a szerkesztés és ott finomíthatunk rajta végül csak az értékeket kell átírni a _css_ fájlban:
```
g#sensors text {
  fill: #ffffff26;
  position: fixed;
  text-shadow: 2px 2px #191919;
}

g#nappali text {
  transform: skew(145deg) scale(.8) translateY(22px) translateX(347px);
}
```
Következnek az entitások és a további szenzorok, itt állapottól függően adunk értéket mindennek és a _css_-ben megadjuk hogy hogyan reagáljanak különböző állapotokra.
```
- name: Entitások
  entities:
    - switch.sonoff_furdo_szelloztetes
    - switch.sonoff_illatosito
    - switch.sonoff_furdoszoba_futes
    - media_player.samsung_q80_series_65
    - fan.aroma_diffuser
    - climate.gree_klima
  state_action:
    action: call-service
    service: floorplan.class_set
    service_data: entities entity-state-${entity.state}
```
Például ha elérhetetlen egy eszköz akkor az piros körvonallal jelezze.
```
g#entities .entities.entity-state-unavailable {
  stroke: #ff000087;
  stroke-width: 2px;
}
```
Csak a képzelet szab határt, hogy mit hogyan szeretnénk jelezni a felületen, jó pár variáció van az én configomban is, amúgy a _css_ részét én sem vágom annyira, de vagy találok segítséget vagy valahol a neten van hozzá infó.
Most pedig jöjjön a világítás, ahhoz hogy a lámpánk színe és erőssége a felületen is megjelenjen az alábbi kódot kell használni, figyelve a stílus formázásra, mert máshogy nekem sem akarta elfogadni. Nem probléma ha nem minden lámpa tud fényerőt vagy színt váltani attól még ugyanúgy fel lehet itt őket sorolni nem fog  hibát okozni.
```
- name: Fények 2
  entities:
    - light.eloszoba_main
    - light.furdo_main
    - light.kamra_main
    - light.wc_main
    - light.halo_main
    - light.nappali_asztali_lampa
    - light.aroma_diffuser_nightlight
  tap_action:
    action: toggle
  state_action:
    action: call-service
    service: floorplan.style_set
    service_data:
      element: ${entity.entity_id.replace('light.', 'light_overlay.')}
      style: |
        >
        if( entity.state !== "on" )
            return "display: none;";
        let hue = 0;
        let sat = 0;
        if( entity.attributes.hs_color ) {
            hue = entity.attributes.hs_color[0];
            sat = entity.attributes.hs_color[1];
        }
        if( sat < 10 ) {
            return `
              display: block;
              filter:
                brightness(calc( ${entity.attributes.brightness} / 255));`
        }
        return `
          display: block;
          filter:
            sepia(100%)
            hue-rotate(calc( ${hue}deg - 55deg ))
            saturate(calc( ${sat}% * 2 ))
            brightness(calc( ${entity.attributes.brightness} / 255));`
``` 
Ott ahol lehet vezérelni a fényerőt vagy a színt ott nem csak a *tap_action* van használva hanem *hold_action* is, hogy a vezérlő elemeket elő lehessen hozni. Mivel elég hozzú a kód és nagyon sok hasonló információ van bennük így mindent nem írok ide részletesen csak a legfontosabbakat.
Most lássuk hogyan is néz ki egy falugró ablak hívás, a _content_ részen belül lehet akár _include_-ot is csinálni vagy amit szeretnénk, ha nem vagyunk benne biztosan inkább szerkesszük meg egy másik _yaml_-ben vagy kattingassuk össze és a kódot ide beillesztve működni fog.
```
- name: Törölköző szárító
  entity: switch.sonoff_furdoszoba_futes
  tap_action: toggle
  hold_action:
    action: fire-dom-event
    browser_mod:
      service: browser_mod.popup
      data:
        style: *browser_mod
        content:
          type: custom:decluttering-card
          template: mushroom_number_template
          variables:
            - entity: input_number.furdoszoba_futes
```
Ami sok gondott okozott a tablet visszjelzés, ott ugye a töltés és ha esetleg be van kapcsolva a tablet azt is szükséges jelezni, bár egyszerre két animáció nem fog megjelenni, de alapból amíg töltött addig nem tudta jelezni, hogy most épp be van kapcsolva vagy nincs a tablet képernyő, illetve fordítva, de sikerüölt megoldani. Itt azt is meg lehet nézni hogy _element_ van használva, mivel két külön entitást kell figyelni.
```
- name: Tablet
  entities:
    - switch.hipad_xpro_kepernyo
    - binary_sensor.hipad_xpro_csatlakoztatva
  element: switch.hipad_xpro_kepernyo
  state_action:
    action: call-service
    service: floorplan.class_set
    service_data: |
      >
      let classes = [];

      if (entities['binary_sensor.hipad_xpro_csatlakoztatva'].state === 'on')
        classes.push('charging charge-state-on');
      else
        classes.push('charging charge-state-off')

      if (entities['switch.hipad_xpro_kepernyo'].state === 'on')
        classes.push('entities entity-state-on');
      else
        classes.push('entities entity-state-off');

      return classes.join(' ');
```
Az alábbi kóddal lettek elhelyezve a felületen az extra gombok, mivel itt egyenlőre nem sikerült olyan megoldást találni, hogy bármilyen felbontáson ugyan oda helyezze el a gombokat itt a tablet felületén kellett nézni, hogy a pozicíó megfelelő-e.
```
- type: custom:mod-card
  card_mod:
    style: |
      :host {
        transform: translate( 0, 0 );
        top: 310px;
        right: 655px;
        position: absolute;
        width: 75px;
      }
  card:
    type: vertical-stack
    cards:
```