Wifi-s Tuya eszközök többnyire gondot okoznak, mivel 3 integráció van de nem mindig jó egyik sem, példa kedvéért van egy Blitzwolf BW-LT31 Led szalag, adjuk hozzá gyári [Tuya](https://www.home-assistant.io/integrations/tuya/) integrációval eredmény a képen látható. Ki/be kapcsolás működik más semmit nem ismer fel. :(
![tuya](/readme-img/tuya.png)

Nézzük hát a [Local Tuya](https://github.com/rospogrigio/localtuya) integrációt, itt is be tudtam állítani kapcsolónak, de sajna a világítás része nem jött össze gondolom nem tudom jól eltalálni a kért DP-ket.
![local_tuya](/readme-img/local_tuya.png)

Végül jött a [Tuya Local](https://github.com/make-all/tuya-local) integráció ami mivel saját fájlokat is lehet hozzáadni így egész jó csak ki kell találni itt is mit és hogyan kell csinálni, de már alapból is felismer sok eszközt csak nem biztos, hogy 100%-ig jó nekünk. Alább látható a képen, hogy 4 konfigoráció is részben vagy egészben megfelel a mi led szalagunknak
![tuya_local_add](/readme-img/tuya_local_add.png)

Érdemes mindent kipróbálni hátha van teljes egyezés.
![smart_led_strip](/readme-img/smart_led_strip.png)
HA logban ilyenkor egyébként látni hogy hány %-os az egyezés, nálam a legjobb az 38% volt de már működött a ki/be kapcsolás és a music mód valamint a szín váltás.

Jöhet a saját konfiguráció készítés, keressünk első körben egy olyan yaml fájlt, amivel valamennyire működött a saját eszközünk "/custom_components/tuya_local/devices" mappában kell keresni.
![file](/readme-img/file.png)

Ez alapján kezdjük el az új fájl készítést, ha a fent megadott könyvtárba csináljuk a fájlunkat akár kis is tudjuk próbálni csak figyeljünk rá, hogyha közben frissül a Tuya Local akkor el fog veszni a fájl, legyen róla biztonsági másolat.
```
name: Blitzwolf BW-LT31 LED Strip
products:
  - id: 66072501f4cfa2fe2887
    name: Blitzwolf BW-LT31 LED Strip
primary_entity:
  entity: light
  icon: "mdi:led-strip-variant"
  dps:
    - id: 20
      type: boolean
      name: switch
```
Nézzük honnét vannak az új adatok.[IoT Tuya](https://iot.tuya.com/) oldalt nyissuk meg jelentkezzünk be és ott először a _Cloud/Development_ részt nyissuk meg és azon belül az _Open Project_.
![development](/readme-img/development.png)

Itt válaszuk a _Devices_ részt azon belül az _All Devices_
![device](/readme-img/device.png)

Meg is van a _Device Id_ ezt a fájl elejére be is rakhatjuk mert az eszköz hozzáadásánál kelleni fog. Ez az oldal maradjon is nyitva, mert még visszatérünk ide, a _Cloud/API Explorer_ oldalt nyissuk meg onnét is kelleni fog 1-2 adat.
![api_explorer](/readme-img/api_explorer.png)

A bal felső sarokban keressük ki a _Smart Home Basic Service_ opciót és válaszuk ki, majd az alatta megjelenő listában a _Smart Home Device Management_ nyissuk ki és válasszuk a _Get Device Details_ opciót, utána adjuk meg a **Device Id**-t és mehet a _Submit Request_, ha minden jól ment akkor egy csomó infót szerzünk az eszközről, bár csak 1 fontos lesz a **local_key** ezt jegyezzük fel, mert eszköz hozzáadáshoz kellni fog.
![local_key](/readme-img/local_key.png)

Maradva ezen az oldalon _Smart Home Device Control_-t nyissuk ki és ott a _Get Device Specification_-t választva megint jöhet a  **Device Id** és a _Submit_.
![device_id](/readme-img/device_id.png)

A képen látható a jobb alsó sarokban az infó az eszközökről és itt láthatóak a **DP ID**-k is, bár nekem ez egy másik eszközről készült, de ezeket kell használni majd a konfiguráció megírásához.
```
    - id: 22
      name: brightness
      type: integer
      range:
        min: 10
        max: 1000
      mapping:
        - dps_val: null
          value: 0
        - scale: 3.92
    - id: 24
      name: rgbhsv
      type: hex
      format:
        - name: h
          bytes: 2
          range:
            min: 0
            max: 360
        - name: s
          bytes: 2
          range:
            min: 0
            max: 1000
        - name: v
          bytes: 2
          range:
            min: 0
            max: 1000
```
Ezek alapján már bővül is a konfigunk és vissza is térhetünk a _Devices_ oldalra ott pedig válaszuk a _Debug Device_ gombot az adott eszköznél. Itt tudjuk majd pontosan a különböző _id_-knak milyen értéket kell küldeni és a **Scene**-ket beállítani. Nézzük, hogy mi kell csinálni első körben bal oldalt válaszuk ki az adott eszközt, felül pedig a _Device Logs_ részt.
![search](/readme-img/search.png)

Valami hasonló oldal fog megjelenni, itt nyomjunk egy _F12_-t és navigáljuk a _network_ fülre, innét tudjuk az _Id_-t számként kiolvasni. A Tuya oldalon a _select_-nél válaszunk ki egy nekünk tetsző sort majd nyomjunk a **Search** gombra, ha minden jó akkor csak a kiválasztott _DP ID_-t fogja megmutatni hogy volt-e művelet az adott időben. Közben a _Network_ rész alatt a _Name_ táblában meg fog jelenni egy _list_ sor amit ki kell választani és a _Payload_ ablakban látni kell a hozzá tartozó _code_-ot, az lesz az _Id_ ami nekünk kell.
![consol](/readme-img/consol.png)

Ahhoz, hogy minden jó legyen a konfigba először írjuk fel az össze Id-t és hozzá a neveket, ha ez megvan akkor jöhet a játszadozás. Az én led szalagon tud **dinamikus**, **színes**, **jelenet** és **zene** mód közt váltani, a honlapon pedig a _mode_-t kell a keresőben kiválasztani ott adja vissza az infót, szépen a telefonon a _Tuya app_-ban elkezdjük az egyiket kiválasztani és utána a honlapon a _Search_ gombot nyomogatni kis idő után megjelenik hogy módot váltott ekkor kell az _Event Details_ oszlop első eleme innét tudjuk mit kell az értékekhez írni.
![mode](/readme-img/mode.png)

```    
    - id: 21
      type: string
      name: color_mode
      mapping:
        - dps_val: dynamic_mod
          value: Dynamic
        - dps_val: colour
          value: hs
        - dps_val: scene_mod
          value: Scene
        - dps_val: music
          value: Music
```
A jelenetek információjához is hasonlóan járunk el mint az előbb, megkeressük az első elemet ami változik egy jelenet kiválasztásakor és utána már csak az app-ban kell váltogatni a jeleneteket és a honlapon pedig frissíteni. A végeredmény valami hasonló kép lesz.
![consol](/readme-img/consol.png)

Közben érdemes a konfig fájt folyamatosan írni mivel ezek az infók oda kerülnek bele. alább a fenti képhez tartozó kód részlet, remélem így érthető és ki tudjátok nyerni az infót ti is. Figyelni kell arra, hogy a _Scene_ az már egy második entitás. 
```
secondary_entities:
  - entity: select
    name: Scene
    icon: "mdi:palette"
    category: config
    dps:
      - id: 108
        type: string
        name: option
        optional: true
        mapping:
          - dps_val: "CJ_YD"
            value: "Reading"
            # color: white, static
          - dps_val: "CJ_QC"
            value: "Get Up"
            # color: white, yellow, static
          - dps_val: "CJ_WA"
            value: "Good Night"
            # color: red, static
          - dps_val: "CJ_XK"
            value: "Starry"
            # color: blue, flash
          - dps_val: "CJ_JH"
            value: "Party"
            # color* All, Flash, Mid speed
          - dps_val: "CJ_YS"
            value: "Film"
            # color: lightblue, static
```
Végül néhány plusz infó az általam használt led szalagnál a **dinamikus** és **zene** módoknál lehet előre beállítani színeket és tempót esetleg érzékenységet, és a honlapon kapsz egy _Event Details_t ami az adott beállításoknak fele meg, de ha állítasz rajta akkor már változni fog ez az érték, ezért is van néhol kommentelve hogy milyen beállításnak felel meg az érték. A teljes kód itt látható:

```
name: Blitzwolf BW-LT31 LED Strip
products:
  - id: 66072501f4cfa2fe2887
    name: Blitzwolf BW-LT31 LED Strip
primary_entity:
  entity: light
  icon: "mdi:led-strip-variant"
  dps:
    - id: 20
      type: boolean
      name: switch
    - id: 21
      type: string
      name: color_mode
      mapping:
        - dps_val: dynamic_mod
          value: Dynamic
        - dps_val: colour
          value: hs
        - dps_val: scene_mod
          value: Scene
        - dps_val: music
          value: Music
    - id: 22
      name: brightness
      type: integer
      range:
        min: 10
        max: 1000
      mapping:
        - dps_val: null
          value: 0
        - scale: 3.92
    - id: 24
      name: rgbhsv
      type: hex
      format:
        - name: h
          bytes: 2
          range:
            min: 0
            max: 360
        - name: s
          bytes: 2
          range:
            min: 0
            max: 1000
        - name: v
          bytes: 2
          range:
            min: 0
            max: 1000
    - id: 102
      name: music_data
      type: integer
    - id: 103
      name: line_sequence_adjustment
      # 线序调整
      type: integer
      hidden: true
    - id: 104
      name: strip_points
      # 灯带点数
      type: integer
      hidden: true
    - id: 106
      name: dynamic_data
      type: hex
    - id: 108
      name: scene_data
      type: base64
secondary_entities:
  - entity: select
    name: Music
    icon: "mdi:palette"
    category: config
    dps:
      - id: 102
        type: string
        name: option
        optional: true
        mapping:
          - dps_val: 164
            value: "Classic"
          - dps_val: 264
            value: "Soft"
          - dps_val: 364
            value: "Dynamic"
          - dps_val: 414
            value: "Disco"
  - entity: select
    name: Dynamic
    icon: "mdi:palette"
    category: config
    dps:
      - id: 106
        type: string
        name: option
        optional: true
        mapping:
          - dps_val: "010148000003e803e8008d03e803e800ee03e803e8003803e803e8012a03e803e8011a03e803e8"
            value: "Breath"
            # color* R+G+B+Y+C+P, breath, Low speed
          - dps_val: "02321e003503e803e8001a03e803e8"
            value: "Flash"
            # color* Y+O, Flash, Mid speed
          - dps_val: "03281e000003e803e8007803e803e800f003e803e8003b03e803e8013603e803e8010e03e803e8"
            value: "Jump"
            # color* R+G+B+Y+C+P, jump, Mid speed
          - dps_val: "041e3c002303e803e8003a03e803e8"
            value: "Gradient"
            # color* O+Y, flash, Low speed
          - dps_val: "053264"
            value: "Symphony"
            # color* All, wave, Mid speed
          - dps_val: "063264000003e803e8"
            value: "Chasing"
            # color* R, chasing, Mid speed
          - dps_val: "073264000003e803e8"
            value: "Meteor"
            # color* R, wave, Mid speed
          - dps_val: "083228003203e803e8"
            value: "Stacking"
            # color* Y, wave, Mid speed
          - dps_val: "093264003603e803e8"
            value: "Adjoint"
            # color* Y, wave, Mid speed
  - entity: select
    name: Scene
    icon: "mdi:palette"
    category: config
    dps:
      - id: 108
        type: string
        name: option
        optional: true
        mapping:
          - dps_val: "CJ_YD"
            value: "Reading"
            # color: white, static
          - dps_val: "CJ_QC"
            value: "Get Up"
            # color: white, yellow, static
          - dps_val: "CJ_WA"
            value: "Good Night"
            # color: red, static
          - dps_val: "CJ_XK"
            value: "Starry"
            # color: blue, flash
          - dps_val: "CJ_JH"
            value: "Party"
            # color* All, Flash, Mid speed
          - dps_val: "CJ_YS"
            value: "Film"
            # color: lightblue, static
```