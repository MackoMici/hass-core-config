# Home Assistant Konfiguráció - update 2023-10-08

[Home Assistant Core](https://www.home-assistant.io/installation/#compare-installation-methods) fut egy Intel(R) Core (TM) i5-7500 CPU @ 3.40 GHz Debian Serveren. Egy fali tablet [Chuwi HiPad XPro](https://www.chuwi.com/product/items/chuwi-hipad-xpro.html) felel a megjelenítésért, amin [Fully Kiosk Browser](https://www.fully-kiosk.com/#get-kiosk-apps) fut. Valamint okostelefonokra optimalizált felület is van.

![lovelace](/readme-img/tablet_kezdolap.png)
| <img src="/readme-img/mobil_kezdolap.png" width=30%> | <img src="/readme-img/mobil_futes.png" width=30%> | <img src="/readme-img/mobil_klima.png" width=30%> |
|:---:|:---:|:---:|

## Kinézet

* [Dashboard (Lovelace)](https://www.home-assistant.io/lovelace/) tabletre és telefonokra optimalizálva a megjelenítés.
* [HA Floorplan](https://github.com/ExperienceLovelace/ha-floorplan)-t használok a 3D-s alaprajz megjelenítéséhez, melyen minden a házban található eszközt lehet vezérelni. [BitBorn](https://www.youtube.com/watch?v=MCNxgb0mrSA) videója apalján készült az új felület immár több kisebb png fájllal a világítás vezérlés miatt.
* Tableten ez eszközök vezérlése előugró ablakokon keresztűl működik ([browser_mod](https://github.com/thomasloven/hass-browser_mod/blob/master/README.md)), valamint a mobilos nézetben is vannnak ilyen funkciók a ritkán használt opciókhoz.
* Mint a tableten és a mobilon a felület úgy lett kialakítva, hogy ne legyen ismétlés így sokkal könnyebb átalakítani vagy javítani (kivétel a system menu). Ehhez a [Decluttering Card](https://github.com/custom-cards/decluttering-card)-ot használtam, valamint az [apexcharts-card](https://github.com/RomRider/apexcharts-card)-nál is sablonok lettek létrehozva.
* Ezúttal a falakra lett feltéve a hőmérséklet és páratartalom érték CSS segítségével elérve a szép összhatást.


#### Oldalsáv

* A pontos idő és dátum megjelenítés
* Adott napi időjárás [Hourly Weather Card](https://github.com/decompil3d/lovelace-hourly-weather)
* Valamint a közelgő események megjelenítése [Atomic Calendar Revive](https://github.com/totaldebug/atomic-calendar-revive)

| <img src="/readme-img/mobil_tv.png" width=30%><br>TV | <img src="/readme-img/mobil_vacuum.png" width=30%><br>Robot porszívó | <img src="/readme-img/mobil_noveny.png" width=30%><br>Növény |
|:---:|:---:|:---:|
| <img src="/readme-img/mobil_parasito.png" width=30%><br>Párásító | <img src="/readme-img/mobil_light.png" width=30%><br>Kapcsolók | <img src="/readme-img/mobil_idojaras.png" width=20%><br>Időjárás |
| <img src="/readme-img/mobil_system.png" width=10%><br>Rendszer
| [![battery](/readme-img/tablet_battery.png)](/readme-img/tablet_battery.png)<br>**Battery** | [![klima](/readme-img/tablet_klima.png)](/readme-img/tablet_klima.png)<br>**Klima** | [![noveny](/readme-img/tablet_noveny.png)](/readme-img/tablet_noveny.png)<br>**Nővény** |
| [![parasito](/readme-img/tablet_parasito.png)](/readme-img/rendszer.png)<br>**Párásító** | [![vacuum](/readme-img/tablet_vacuum.png)](/readme-img/tablet_vacuum.png)<br>**Vacuum**| [![tablet](/readme-img/tablet_tablet.png)](/readme-img/tablet_tablet.png)<br>**Tablet** |
| [![user](/readme-img/tablet_user.png)](/readme-img/tablet_user.png)<br>**User**| [![system](/readme-img/tablet_system.gif)](/readme-img/tablet_system.gif)<br>**System** | [![Light](/readme-img/tablet_light.gif)](/readme-img/tablet_light.gif)<br>**Világítás** |

#### Kinézet

[Waves Theme](https://github.com/tgcowell/waves)

## Eszközök

| Gyártó | Termék | Integráció |
|---|---|---|
| Mikrotik | [hAP ac²](https://mikrotik.com/product/hap_ac2) | [mikrotik router](https://github.com/tomaae/homeassistant-mikrotik_router) |
| Samsung | [Q80 Smart Tv](https://www.samsung.com/hu/tvs/qled-tv/q80t-65-inch-qled-4k-smart-tv-qe65q80tatxxh/) | [samsung smart](https://github.com/ollo69/ha-samsungtv-smart) |
| Xiaomi | [Viomi SE](https://www.viomi.com/robot-vacuums/viomi-se) | [mqtt](https://www.home-assistant.io/integrations/mqtt/) |
| Xiaomi | [Xiaomi Gateway 3](https://xiaomishop.hu/mi-smart-home-hub-cn-valtozat-zigbee-30-gateway-okosotthon-kozponti-egyseg) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Temperature and Humidity Monitor 2](https://xiaomishop.hu/okos-otthon/mi-temperature-and-humidity-monitor-2-bluetooth-homerseklet-es-paratartalom-mero) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Door and Window Sensor 2](https://xiaomishop.hu/okos-otthon/szenzorok-es-kapcsolok/mi-door-and-window-sensor-2-ajto-es-ablaknyitas-erzekelo-fenyerzekelovel) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Smart Home növényszenzor](https://xiaomishop.hu/mi_smart_home_novenyszenzor) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Sonoff | [Basic R3](https://sonoff.tech/product-document/diy-smart-switches-doc/basicr3-doc/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [Mini R2](https://sonoff.tech/product/diy-smart-switches/minir2/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [TX 1C](https://sonoff.tech/product/smart-wall-switches/tx-series/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [S26 R2](https://sonoff.tech/product/smart-plugs/s26r2/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [DW2-Wifi](https://sonoff.tech/product/gateway-and-sensors/dw2-wifi/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN)
| Gree | [Comfort X](https://gree-magyarorszag.hu/klima/gree-comfort-x-inverter-27-kw-klima-szett/) | [gree climate](https://www.home-assistant.io/integrations/gree) |
| Honeywell | [T6 Thermosztát](https://getconnected.honeywellhome.com/hu/t6.html) | [honeywell lyric](https://www.home-assistant.io/integrations/lyric) |
| Broadlink | [RM4 mini](https://www.broadlink.ae/product-page/broadlink-rm4-mini) | [broadlink remote](https://www.home-assistant.io/integrations/broadlink) |
| Blitzwolf | [BW-LT31](https://blitzwolf.hu/BlitzWolf-BW-LT31-smart-LED-fenycsik-5m-/10m-hossz) | [tuya-local](https://github.com/make-all/tuya-local) |
| GX.Diffuser | [Aroma Diffuser](https://sea.banggood.com/GX_Diffuser-Intelligent-Air-Humidifier-Essential-Oil-Diffuser-Support-for-GeogleandAlexa-Voice-Control-Negative-Ion-Purification-p-1597711.html?rmmds=myorder&cur_warehouse=CN) | [tuya-local](https://github.com/make-all/tuya-local) |
| Yeelight | [Xiaomi Yeelight Smart LED Bulb W3](https://www.pcx.hu/xiaomi-yeelight-smart-led-bulb-w3-multicolor-okos-izzo-yldp005-00432819) | [yeelight](https://www.home-assistant.io/integrations/yeelight) |
| Gosund | [Gosund EP2](https://www.emag.hu/gosund-wifis-okoskonnektor-ep2/pd/DKX2Y4MBM/) | [tuya-local](https://github.com/make-all/tuya-local) |
| CHUWI | [HiPad XPro](https://www.chuwi.com/product/items/chuwi-hipad-xpro.html) | [fully kiosk browser](https://www.home-assistant.io/integrations/fully_kiosk), [mqtt](https://www.home-assistant.io/integrations/mqtt/), [mobil app](https://www.home-assistant.io/integrations/mobile_app) |
| IKEA | [TRADFRI E14](https://www.ikea.com/hu/hu/p/tradfri-led-izzo-e14-470-lumen-okos-eszkoez-vezetek-nelkueli-szabalyozo-feher-spektrum-csillar-20486784/) | [zha](https://www.home-assistant.io/integrations/zha) |

## Integrációk

| Integrációk |
|---|
| [Generic Camera](https://www.home-assistant.io/integrations/generic) |
| [Browser mod](https://github.com/thomasloven/hass-browser_mod/blob/master/README.md) |
| [Season](https://www.home-assistant.io/integrations/season) |
| [File size](https://www.home-assistant.io/integrations/filesize) |
| [Google Calendar](https://www.home-assistant.io/integrations/google) |
| [Gree Extension](https://github.com/mullerdavid/hass_GreeExt) |
| [HACS](https://hacs.xyz/docs/configuration/basic/) |
| [ical Sensor](https://www.home-assistant.io/integrations/ical) |
| [Meteorologisk institutt (Met.no)](https://www.home-assistant.io/integrations/met) |
| [Multiscrape](https://github.com/danieldotnl/ha-multiscrape) |
| [Workday](https://www.home-assistant.io/integrations/workday) |
| [Sun](https://www.home-assistant.io/integrations/sun) |
| [Homeassistant-plant](https://github.com/Olen/homeassistant-plant/) |
| [Openplantbook](https://github.com/Olen/home-assistant-openplantbook/) |
| [Scheduler](https://github.com/nielsfaber/scheduler-component) |
| [Thermal Comfort](https://github.com/dolezsa/thermal_comfort/blob/master/README.md) |
| [Uptime](https://www.home-assistant.io/integrations/uptime) |
| [Version](https://www.home-assistant.io/integrations/version) |
| [card-tools](https://github.com/thomasloven/lovelace-card-tools) |
| [layout-card](https://github.com/thomasloven/lovelace-layout-card) |
| [Ha Floorplan](https://github.com/ExperienceLovelace/ha-floorplan) |
| [Home Assistant Swipe Navigation](https://github.com/zanna-37/hass-swipe-navigation) |
| [Bar Card](https://github.com/custom-cards/bar-card) |
| [Clock Weather Card](https://github.com/pkissling/clock-weather-card) |
| [Config Template Card](https://github.com/iantrich/config-template-card) |
| [Atomic Calendar Revive](https://github.com/totaldebug/atomic-calendar-revive) |
| [Mushroom](https://github.com/piitaya/lovelace-mushroom) |
| [card-mod 3](https://github.com/thomasloven/lovelace-card-mod) |
| [Lovelace swipe card](https://github.com/bramkragten/swipe-card) |
| [auto-entities](https://github.com/thomasloven/lovelace-auto-entities) |
| [apexcharts-card](https://github.com/RomRider/apexcharts-card) |
| [Hourly Weather Card](https://github.com/decompil3d/lovelace-hourly-weather) |
| [Flower Card](https://github.com/Olen/lovelace-flower-card) |
| [Decluttering Card](https://github.com/custom-cards/decluttering-card) |
| [Scheduler Card](https://github.com/nielsfaber/scheduler-card) |
| [Weather Radar Card](https://github.com/Makin-Things/weather-radar-card) |
| [Stack In Card](https://github.com/custom-cards/stack-in-card) |
| [state-switch](https://github.com/thomasloven/lovelace-state-switch) |
| [Valetudo Map Card](https://github.com/Hypfer/lovelace-valetudo-map-card) |
| [Mini Media Player](https://github.com/kalkih/mini-media-player) |

## Automatizációk

* Ablak nyitás klíma kikapcsolás
* Ajtó nyitás tablen mozgás érzékelő bekapcsolás
* Fürdőszoba szellőztetés vezérlés külső belső páratartalom figyelenbevételével
* Előszoba világítás ki/be kapcsolás, bejárati ajtó nyitás-ra
* Kamra világítás vezérlés
* Kapcsolók időzítés figyelése (Fűttés mindenképp, Fürdőszaoba fűttés)
* Riasztó bekapcsolás
* Tablet töltés
* Tanusítvány lejárat figyelés
* Világítás kikapcsolás ha elhagyjuk a házat
* WC frissítő vezérlés
* Párásító világítás kikapcsolás
* Reggeli információ engedélyezés
* Reggeli információ felolvasás

## Szkriptek

* Reggeli információk, időjárás jelentés naptár események
* Robot porszívó adott helység takarítás
* Fényfűzérhez színek és módok váltásához

## Leírás - update 2023-10-09

* <a href="/readme-docs/Floorplan_felulet.md">Floorplan felület kialakítás</a>