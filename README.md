# Home Assistant Configuration

[Home Assistant Core](https://www.home-assistant.io/installation/#compare-installation-methods) fut egy Intel(R) Core (TM) i5-7500 CPU @ 3.40 GHz Debian Serveren. Mejelenítését egy [Alldocube iPlay 10 Pro](https://www.alldocube.com/en/products/iplay10pro/) tablet végzi [Fully Kiosk Browser](https://www.fully-kiosk.com/#get-kiosk-apps) segítségével.

![lovelance](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/lovelance.png)

## Kinézet

* [Dashboard (Lovelace)](https://www.home-assistant.io/lovelace/) tabletre van optimalízálva a megjelenítés
* [HA Floorplan-t](https://github.com/ExperienceLovelace/ha-floorplan) használok a 3D-s alaprajz megjelenítéséhez, melyen minden a házban található eszköz megjelenik és interaktív
* Minden extra információ előugró ablakban jelenik meg

#### Oldalsáv

* Felhasznalói információk
* A pontos idő és dátum megjelenítés
* Valamint a közelgő események megjelenítése [Atomic Calenrad revive-ben](https://github.com/totaldebug/atomic-calendar-revive)

![user](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/user.png)

#### Előugró ablakok

Ami az alaprajzon kezelhető az mind előugró ablakban fog megjelenni, melyhez a [browser_mod-ot](https://github.com/thomasloven/hass-browser_mod) használom.


| [![futes](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/futes.png)](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/futes.png)<br>Fűtés | [![klima](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/klima.png)](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/klima.png)<br>Klíma | [![idojaras](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/idojaras.png)](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/idojaras.png)<br>Időjárás |
|:---:|:---:|:---:|
| [![vacuum](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/vacuum.png)](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/vacuum.png)<br>**Vacuum** | [![rendszer](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/rendszer.png)](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/rendszer.png)<br>**Rendszer** | [![tv](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/tv.png)](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/tv.png)<br>**TV** |
| [![flora](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/flora.png)](https://github.com/MackoMici/hass-core-config/blob/05a3491ac6e59330f02a7574c0858129abf68554/readme-img/flora.png)<br>**Növény** |

#### Kinézet

[Waves Theme](https://github.com/tgcowell/waves)

## Eszközök

| Gyártó | Termék | Integráció |
|---|---|---|
| Mikrotik | [hAP ac²](https://mikrotik.com/product/hap_ac2) | [mikrotik router](https://github.com/tomaae/homeassistant-mikrotik_router) |
| Samsung | [Q80 Smart Tv](https://www.samsung.com/hu/tvs/qled-tv/q80t-65-inch-qled-4k-smart-tv-qe65q80tatxxh/) | [samsung smart](https://github.com/ollo69/ha-samsungtv-smart) |
| Xiaomi | [Viomi SE](https://www.viomi.com/robot-vacuums/viomi-se) | [vacuum viomise](https://github.com/marotoweb/home-assistant-vacuum-viomise) |
| Xiaomi | [Xiaomi Gateway 3](https://xiaomishop.hu/mi-smart-home-hub-cn-valtozat-zigbee-30-gateway-okosotthon-kozponti-egyseg) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Temperature and Humidity Monitor 2](https://xiaomishop.hu/okos-otthon/mi-temperature-and-humidity-monitor-2-bluetooth-homerseklet-es-paratartalom-mero) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Door and Window Sensor 2](https://xiaomishop.hu/okos-otthon/szenzorok-es-kapcsolok/mi-door-and-window-sensor-2-ajto-es-ablaknyitas-erzekelo-fenyerzekelovel) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Smart Home növényszenzor](https://xiaomishop.hu/mi_smart_home_novenyszenzor) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Sonoff | [Basic R3](https://itead.cc/product/sonoff-basicr3-wifi-diy-smart-switch/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [Mini R2](https://itead.cc/product/sonoff-mini/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [TX 1C](https://itead.cc/product/sonoff-tx-series-wifi-smart-wall-switches/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [S26 R2](https://itead.cc/product/sonoff-s26-wifi-smart-plug/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Gree | [Comfort X](https://gree-magyarorszag.hu/klima/gree-comfort-x-inverter-27-kw-klima-szett/) | [gree climate](https://www.home-assistant.io/integrations/gree) |
| Honeywell | [T6 Thermosztát](https://getconnected.honeywellhome.com/hu/t6.html) | [honeywell lyric](https://www.home-assistant.io/integrations/lyric) |

## Automatizációk

* Fürdőszoba szellőztetés vezérlés külső belső páratartalom figyelenbevételével
* Előszoba világítás ki/be kapcsolás, bejárati ajtó nyitás-ra
* Fűtés automatikus vezérlés, jelenlét és külső hőmérséklet figyelembevételével
* Alacsony elem riasztás küldés
* Tablet töltés és képernyő kikapcsolás
* Hazaérkezéskor köszöntés és informáűciók felolvasása

## Szkriptek

* Reggeli információk, időjárás jelentés naptár események
* Robot porszívó adott helység takarítás
