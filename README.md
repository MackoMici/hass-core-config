# Home Assistant Konfiguráció

[Home Assistant OS](https://community-scripts.org/scripts/haos-vm) fut egy Intel(R) Core (TM) i5-7500 CPU @ 3.40 GHz Debian Serveren 16GB RAM-mal. Egy fali tablet [Chuwi HiPad XPro](https://www.chuwi.com/product/items/chuwi-hipad-xpro.html) felel a megjelenítésért, amin [Fully Kiosk Browser](https://www.fully-kiosk.com/#get-kiosk-apps) fut. Valamint okostelefonokra optimalizált felület is van. Mindezt úgy megírva, hogy ami lehetséges csak egy helyen legyen és ha máshol is kell akkor include-oljuk az adott tartalmat.

![lovelace](/readme-img/tablet_kezdolap.png)
| <img src="/readme-img/mobil_kezdolap.png" width=30%> | <img src="/readme-img/mobil_futes.png" width=30%> | <img src="/readme-img/mobil_klima.png" width=30%> |
|:---:|:---:|:---:|

## Kinézet

* [Dashboard (Lovelace)](https://www.home-assistant.io/lovelace/) tabletre és telefonokra optimalizálva a megjelenítés, szinte csak a [Bubble Card](https://github.com/Clooos/bubble-card)-ot használtam és annak a felugró ablakait.
* [HA Floorplan](https://github.com/ExperienceLovelace/ha-floorplan)-t használok a 3D-s alaprajz megjelenítéséhez, melyen minden a házban található eszközt lehet vezérelni. [BitBorn](https://www.youtube.com/watch?v=MCNxgb0mrSA) videója apalján készült az új felület immár több kisebb png fájllal a világítás vezérlés miatt.
* Mint a tableten és a mobilon a felület úgy lett kialakítva, hogy ne legyen ismétlés így sokkal könnyebb átalakítani vagy javítani. Ehhez nagyrészt a [Streamline Card](https://github.com/brunosabot/streamline-card)-ot valamint 1 opcióhoz a [Decluttering Card](https://github.com/custom-cards/decluttering-card)-ot használtam.
* Ezúttal a falakra lett feltéve a hőmérséklet és páratartalom érték CSS segítségével elérve a szép összhatást.


#### Oldalsáv

* A pontos idő és dátum megjelenítés
* Adott napi időjárás, ahol kattintásra megjelenik a részletes időjárás, vaéamint hosszan nyomvatartásra a radarkép
* Legallul a közelgő események megjelenítése kapott még helyet.

| <img src="/readme-img/mobil_tv.png" width=30%><br>TV | <img src="/readme-img/mobil_kapcsolok.png" width=30%><br>Kapcsolók | <img src="/readme-img/mobil_noveny.png" width=30%><br>Növény |
|:---:|:---:|:---:|
| <img src="/readme-img/mobil_parasito.png" width=30%><br>Párásító | <img src="/readme-img/mobil_light.png" width=30%><br>Világítás | <img src="/readme-img/mobil_popup.png" width=20%><br>PopUp |
| <img src="/readme-img/mobil_system.png" width=10%><br>Rendszer
| [![battery](/readme-img/tablet_battery.png)](/readme-img/tablet_battery.png)<br>**Battery** | [![idojaras](/readme-img/tablet_idojaras.png)](/readme-img/tablet_idojaras.png)<br>**Időjárás előrejelzés** | [![idojaras2](/readme-img/tablet_radar.png)](/readme-img/tablet_radar.png)<br>**Időjárás Radar** |
| [![noveny](/readme-img/tablet_noveny.png)](/readme-img/tablet_noveny.png)<br>**Nővény** | [![vilagitas](/readme-img/tablet_vilagitas.png)](/readme-img/tablet_vilagitas.png)<br>**Világítás** | [![system](/readme-img/tablet_system.png)](/readme-img/tablet_system.png)<br>**System** |
| [![tablet](/readme-img/tablet_tablet.png)](/readme-img/tablet_tablet.png)<br>**Tablet Infó** | [![system](/readme-img/tablet_system.gif)](/readme-img/tablet_system.gif)<br>**System** | [![Light](/readme-img/tablet_light.gif)](/readme-img/tablet_light.gif)<br>**Világítás válzotás** |

#### Kinézet

[Bubble](https://github.com/Clooos/Bubble)

## Eszközök

| Gyártó | Termék | Integráció |
|---|---|---|
| Mikrotik | [hAP ac²](https://mikrotik.com/product/hap_ax3) | [mikrotik extended](https://github.com/Csontikka/ha-mikrotik-extended) |
| Samsung | [Q80 Smart Tv](https://www.samsung.com/hu/tvs/qled-tv/q80t-65-inch-qled-4k-smart-tv-qe65q80tatxxh/) | [samsung smart](https://github.com/ollo69/ha-samsungtv-smart) |
| Xiaomi | [Xiaomi Gateway 3](https://xiaomishop.hu/mi-smart-home-hub-cn-valtozat-zigbee-30-gateway-okosotthon-kozponti-egyseg) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Temperature and Humidity Monitor 2](https://xiaomishop.hu/okos-otthon/mi-temperature-and-humidity-monitor-2-bluetooth-homerseklet-es-paratartalom-mero) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Door and Window Sensor 2](https://xiaomishop.hu/okos-otthon/szenzorok-es-kapcsolok/mi-door-and-window-sensor-2-ajto-es-ablaknyitas-erzekelo-fenyerzekelovel) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Xiaomi | [Mi Smart Home növényszenzor](https://xiaomishop.hu/mi_smart_home_novenyszenzor) | [xiaomi gateway 3](https://github.com/AlexxIT/XiaomiGateway3) |
| Sonoff | [Basic R3](https://sonoff.tech/product-document/diy-smart-switches-doc/basicr3-doc/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [Mini R2](https://sonoff.tech/product/diy-smart-switches/minir2/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [ZbMini Extreme](https://sonoff.tech/product/diy-smart-switches/zbmini-l2/) | [zha](https://www.home-assistant.io/integrations/zha) |
| Sonoff | [TX 1C](https://sonoff.tech/product/smart-wall-switches/tx-series/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [S26 R2](https://sonoff.tech/product/smart-plugs/s26r2/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN) |
| Sonoff | [DW2-Wifi](https://sonoff.tech/product/gateway-and-sensors/dw2-wifi/) | [sonoff lan](https://github.com/AlexxIT/SonoffLAN)
| Gree | [Comfort X](https://gree-magyarorszag.hu/klima/gree-comfort-x-inverter-27-kw-klima-szett/) | [gree climate](https://www.home-assistant.io/integrations/gree) , [gree extension](https://github.com/mullerdavid/hass_GreeExt)|
| Honeywell | [T6 Thermosztát](https://getconnected.honeywellhome.com/hu/t6.html) | [honeywell lyric](https://www.home-assistant.io/integrations/lyric) |
| Blitzwolf | [BW-LT31](https://blitzwolf.hu/BlitzWolf-BW-LT31-smart-LED-fenycsik-5m-/10m-hossz) | [tuya-local](https://github.com/make-all/tuya-local) |
| GX.Diffuser | [Aroma Diffuser](https://sea.banggood.com/GX_Diffuser-Intelligent-Air-Humidifier-Essential-Oil-Diffuser-Support-for-GeogleandAlexa-Voice-Control-Negative-Ion-Purification-p-1597711.html?rmmds=myorder&cur_warehouse=CN) | [tuya-local](https://github.com/make-all/tuya-local) |
| Yeelight | [Xiaomi Yeelight Smart LED Bulb W3](https://www.pcx.hu/xiaomi-yeelight-smart-led-bulb-w3-multicolor-okos-izzo-yldp005-00432819) | [yeelight](https://www.home-assistant.io/integrations/yeelight) |
| Gosund | [Gosund EP2](https://www.emag.hu/gosund-wifis-okoskonnektor-ep2/pd/DKX2Y4MBM/) | [tuya-local](https://github.com/make-all/tuya-local) |
| CHUWI | [HiPad XPro](https://www.chuwi.com/product/items/chuwi-hipad-xpro.html) | [fully kiosk browser](https://www.home-assistant.io/integrations/fully_kiosk), [mqtt](https://www.home-assistant.io/integrations/mqtt/), [mobil app](https://www.home-assistant.io/integrations/mobile_app) |
| IKEA | [TRADFRI E14](https://www.ikea.com/hu/hu/p/tradfri-led-izzo-e14-470-lumen-okos-eszkoez-vezetek-nelkueli-szabalyozo-feher-spektrum-csillar-20486784/) | [zha](https://www.home-assistant.io/integrations/zha) |
| JOAN | [JOAN6](https://support.getjoan.com/knowledge/joan-6-technical-specifications) | [Visiontech Joan](https://github.com/Adam7411/visionect_joan) |


## Integrációk

| Integrációk |
|---|
| [Alert2](https://github.com/redstone99/hass-alert2) |
| [Backup](https://www.home-assistant.io/integrations/backup) |
| [Battery Notes](https://codechimp.org/HA-Battery-Notes/)|
| [Browser mod](https://github.com/thomasloven/hass-browser_mod/blob/master/README.md) |
| [Bubble Card Tools](https://github.com/Clooos/Bubble-Card-Tools) |
| [Drinking Water Quality](https://github.com/tomorigabor/drinkingwaterquality_hu_nnk) |
| [Season](https://www.home-assistant.io/integrations/season) |
| [File size](https://www.home-assistant.io/integrations/filesize) |
| [Fully Kiosk Browser](https://www.home-assistant.io/integrations/fully_kiosk) |
| [Google Calendar](https://www.home-assistant.io/integrations/google) |
| [HACS](https://hacs.xyz/docs/configuration/basic/) |
| [ical Sensor](https://www.home-assistant.io/integrations/ical) |
| [iPhone Detect](https://github.com/mudape/iphonedetect) |
| [Meteorologisk institutt (Met.no)](https://www.home-assistant.io/integrations/met) |
| [Multiscrape](https://github.com/danieldotnl/ha-multiscrape) |
| [Workday](https://www.home-assistant.io/integrations/workday) |
| [Sun](https://www.home-assistant.io/integrations/sun) |
| [Homeassistant-plant](https://github.com/Olen/homeassistant-plant/) |
| [Openplantbook](https://github.com/Olen/home-assistant-openplantbook/) |
| [Thermal Comfort](https://github.com/dolezsa/thermal_comfort/blob/master/README.md) |
| [Uptime](https://www.home-assistant.io/integrations/uptime) |
| [Ha Floorplan](https://github.com/ExperienceLovelace/ha-floorplan) |
| [Home Assistant Swipe Navigation](https://github.com/zanna-37/hass-swipe-navigation) |
| [card-mod 3](https://github.com/thomasloven/lovelace-card-mod) |
| [auto-entities](https://github.com/thomasloven/lovelace-auto-entities) |
| [Decluttering Card](https://github.com/custom-cards/decluttering-card) |
| [Weather Radar Card](https://github.com/Makin-Things/weather-radar-card) |
| [Valetudo Map Card](https://github.com/Hypfer/lovelace-valetudo-map-card) |
| [Pi-Hole](https://github.com/bastgau/ha-pi-hole-v6) |
| [Proxmox VE](https://github.com/dougiteixeira/proxmoxve) |
| [Streamline Card](https://github.com/brunosabot/streamline-card) |
| [Certificate Expiry](https://www.home-assistant.io/integrations/cert_expiry) |




## Automatizációk

* Alert2 értesítések éjszakai kikapcsolása
* Ajtó nyitás tablen mozgás érzékelő bekapcsolás
* Fürdőszoba szellőztetés vezérlés külső belső páratartalom figyelenbevételével
* Előszoba világítás ki/be kapcsolás, bejárati ajtó nyitás-ra
* Fürdőszoba fűtés
* Home Assistant Nightly Git Backup
* Joan időjárás frissítés
* Kamra világítás vezérlés
* Lemerülő elemek
* Riasztó bekapcsolás
* Tablet töltés
* Tablet mozgásra képkészítés és e-mail küldés
* Tanusítvány lejárat figyelés
* Világítás kikapcsolás ha elhagyjuk a házat
* WC frissítő vezérlés

## Szkriptek

* Időjárás - a Joan6-on való megjelenítéshez
* Input datetime állítás - a fűtés időpontok vezérléshez
* Üzenet küldés Zolinak

## Leírás

* <a href="/readme-docs/Floorplan_felulet.md">Floorplan felület kialakítás</a>
* <a href="/readme-docs/Mobil_felulet.md">Mobil felület kialakítás</a>
* <a href="/readme-docs/Futes_vezerles.md">Fűtés vezérlés kialakítás</a>
* <a href="/readme-docs/Idojaras_tts.md">Időjárás felolvasás</a>
* <a href="/readme-docs/Tuya_local.md">Tuya Local saját konfig készítés</a>
* <a href="/readme-docs/Multiscrape.md">Multiscrape használata</a>