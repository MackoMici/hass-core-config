Ez az egyetlen komolyabb automatizmus amire nem csináltam blueprint-et eddig. Microsoft TTS szolgáltatás végzi a felolvasást, beállításai a [Config](/configuration.yaml#L130C1-L136C14)-ban találhatóak.

[Időjárés felolvasás Automatizmus](automations.yaml#L1)

Trigger: a _Fully Kiosk Browser_ integráció képernyő bekapcsolás vagy a _Browser mod_ integráció képernyő bekapcsolás ez utóbbira azért van szükség, hogy amikor elindul az időjárás felolvasás, akkor a képernyőn megjelenjen egy felhő térkép felugró ablakban.

Condition: csak ha valaki tartózkodik otthon, illetve a _Browser mod_ képernyő be van kapcsolva, engedélyezve van a felolvasás és külön hétköznap és hétvégén a megadott időkereten belül vagyunk csak akkor fogja felolvasni. Korábban volt hogy a tablet mozgásérzékelője be volt kapcsolva és akkor automatikusan lefutott, de ez most egyenlőre ki van iktatva

Action: először a tablet képernyő kikapcsolás időt állítjuk 90 mp-re kb. annyi idő alatt felolvassa az időjárást. Láttam olyan megoldást, hogy a hanganyag hosszát adták itt meg, de sajnos ez nálam nem megoldható. Majd megjelenítjük a felhő térképet és 60 mp-ig marad a képernyőn. jöhet a felolvasó script, várakozás 90 mp-ig végül tiltjuk a felolvasást mára illetve a tablet képernyő kikacsolást visszaállítjuk.

[Időjárás felolvasás Automatizmus](scripts.yaml#L1)

Sajnos hiába formázza meg az ember szépen ha a felületen egyszer hozzányúlsz akkor mindig elrontja a formázást. Első körben rögtön csinálunk két változót a hónapokra és a napokra, majd jöhet a pontos idő és a mai névnap. Ehhez kell egy google naptár integráció amiben a névnapok vannak.
```
{% set honap =
  { 1: 'Január',
    2: 'Február',
    3: 'Március',
    4: 'Április',
    5: 'Május',
    6: 'Június',
    7: 'Július',
    8: 'Augusztus',
    9: 'Szeptember',
    10: 'Október',
    11: 'November',
    12: 'December',
  }
%}
{% set napok =
  { 0: 'Ma',
    1: 'Holnap',
    2: 'Holnapután',
  }
%}
A mai dátum {{ now().year | string }} {{ honap[now().month] }} {{ now().day | string }}.
A pontos idő {{ now().strftime('%-H') }} óra {{ now().strftime('%-M') }} perc.
A mai névnap {{ state_attr('calendar.magyar_nevnapok', 'message') }}.
```

Második lépés megvizsgáljuk hogy a saját naptárban van-e esemény 3 napon belül, ha igen, akkor abból a legelső eseményt felolvassuk pontos kezdési idővel.
```
{% if ((states.calendar.macko_mici_gmail_com.attributes.start_time | as_datetime | as_local).date() - (now() | as_local).date()).days | int < 3 -%}
  Zoltán naptárjában a következő naptári esemény:
  {{ napok[((states.calendar.macko_mici_gmail_com.attributes.start_time | as_datetime | as_local).date() - (now() | as_local).date()).days | int] }},
  {{ state_attr('calendar.macko_mici_gmail_com', 'message') }}.
{% endif %}
```

Jöhetnek a páron naptár bejegyzései, itt már több csavar is van a dologban, neki vannak szép számmal bejegyzései és nem mind egész napos, így a google calendar nem elég mivel az csak mindig a következő eseményt tudja olvasni. Ehhez van az [iCal Sensor](https://github.com/tybritten/ical-sensor-homeassistant) integráció, ehhez szükség van egy ical url-re ezt a google felületen meg lehet szerezni, mindig csak a bejelentkezett felhasználó eseményei lesznek benne és vigyázni rá mert aki ezt megszerzi az láthat minden eseményt. Jöhet az alap 3 napos vizsgálat, majd mivel a következő 5 eseményt listázta ki az _iCal_ így azokon végig kell menni és ami 3 napon belül van az mind fel lesz olvasva.
```
{% if ((states.calendar.szakacskata_gmail_com.attributes.start_time | as_datetime | as_local).date() - (now() | as_local).date()).days | int < 3 -%}
  Kata naptárjában a következő naptári esemény:
  {% for i in range(0, 5) %}
    {% if is_state('sensor.ical_szakacs_katalin_event_' + i | string, 'unavailable') %}
      A naptár elérhetetlen.
    {% elif ((as_timestamp(state_attr('sensor.ical_szakacs_katalin_event_' + i | string, 'start')) | as_datetime | as_local).date() - (now() | as_local).date()).days | int < 3 %}
      {{ napok[((as_timestamp(state_attr('sensor.ical_szakacs_katalin_event_' + i | string, 'start')) | as_datetime | as_local).date() - (now() | as_local).date()).days | int] }}
      {% if is_state_attr('sensor.ical_szakacs_katalin_event_' + i | string, 'all_day', true) %}
        egész nap
      {% else %}
        {{ as_timestamp(state_attr('sensor.ical_szakacs_katalin_event_' + i | string, 'start')) | timestamp_custom('%H:%M') }}
      {% endif %}
      {{ state_attr('sensor.ical_szakacs_katalin_event_' + i | string, 'summary') }}.
    {% endif %}
  {% endfor %}
{% endif %}
```

A munkarenden elég változatos, így felolvastatom mikor kell legközelebb dolgozni, itt egy plusz szűrést alkalmazva hogy csak azok az események lesznek felolvasva amik nem egész naposak.
```
{% if ((states.calendar.zoltan_hunyadvari_gmail_com.attributes.start_time | as_datetime | as_local).date() - (now() | as_local).date()).days | int < 3 and is_state('calendar.zoltan_hunyadvari_gmail_com', 'off') and is_state_attr('calendar.zoltan_hunyadvari_gmail_com', 'all_day', false) %}
  A következő munkanap:
  {{ napok[((states.calendar.zoltan_hunyadvari_gmail_com.attributes.start_time | as_datetime | as_local).date() - (now() | as_local).date()).days | int] }},
  {{ (states.calendar.zoltan_hunyadvari_gmail_com.attributes.start_time | as_datetime | as_local).time() }}.
{% endif %}
```

Következik az időjárás jelentés első körben ha elérhető akkor az _időkép_ előrejelzését felolvassa. Ehhez a [multiscrape](https://github.com/danieldotnl/ha-multiscrape) kiegészítőt használom a linken elérhető [kóddal](/include/multiscrape.yaml).
```
{% if not is_state('sensor.idokep_elorejelzes', 'unavailable') %}
  Országos időjárás jelentés:
  {{ state_attr('sensor.idokep_elorejelzes', 'details') }}
{% endif %}
```
Végül ha elérhető a helyi időjárás kerül felolvasásra, szélsebesség és csapadák mennyiséggel. Ehhez a [Meteorologisk institutt (Met.no)](https://www.home-assistant.io/integrations/met) integrációt használom.
```
{% set odakinn = states('sensor.kulteri_homerseklet') %}
{% if not is_state('weather.forecast_home', 'unavailable') %}
  {% set odakinn = state_attr('weather.forecast_home', 'temperature') %}
  {% set idok =
    { 'clear-night': 'Tiszta este',
      'cloudy': 'Felhős idő',
      'exceptional': 'Extrém idő',
      'fog': 'Köd',
      'hail': 'Jégeső',
      'lightning': 'Vihar',
      'lightning-rainy': 'Viharos eső',
      'partlycloudy': 'Részben felhős idő',
      'pouring': 'Szakadó eső',
      'rainy': 'Esős idő',
      'snowy': 'Havazás',
      'snowy-rainy': 'Havas eső',
      'sunny': 'Napos idő',
      'windy': 'Szeles idő',
      'windy-variant': 'Változóan szeles idő',
    }
  %}
  Helyi időjárás:
  {{ idok[states.weather.forecast_home.state] }}
  várható
  {{ [ 'ma', 'mára', 'a mai napra', 'az előrejelzés szerint', 'az időjós békám szerint'] | random }},
  {{ states.weather.forecast_home.attributes.forecast[0].templow }}
  és
  {{ states.weather.forecast_home.attributes.forecast[0].temperature }}
  fok közötti hőmérséklettel.
  {% if state_attr('weather.forecast_home', 'wind_speed') | int > 10 %}
    A szélsebesség
    {{ state_attr('weather.forecast_home', 'wind_speed') }}
    kilométer per óra.
  {% endif %}
  {% if states.weather.forecast_home.attributes.forecast[0].precipitation | float(0) == 0 %}
    A mai egy csapadékmentes nap lesz.
  {% else %}
    Körülbelül
    {{ states.weather.forecast_home.attributes.forecast[0].precipitation | float(0) }}
    milliméter csapadék várható.
  {% endif %}
{% else %}
  Az időjárás előrejelző szolgáltatás sajnos nem elérhető.
{% endif %}
{{ ['Most épp', 'Jelenleg', 'Pillanatnyilag'] | random }} {{ odakinn }}
fok
{{ ['van', 'a kinti hőmérséklet', 'van odakinn'] | random }}.
```

És az egész scriptet futtatva a következő erédményt adja, a sok sorköz nem érdekes attól még szépen felolvassa a szöveget.
```
      A mai dátum 2023 Október 17.

      A pontos idő 8 óra 38 perc.

      A mai névnap Hedvig.



        A következő munkanap: Holnap, 08:00:00.



        Országos időjárás előrejelzés: 
        
      Kedden reggel sokfelé erősen fátyolfelhős lesz az ég, de helyenként
      vastagabb felhők is megjelenhetnek az égen. Elsősorban délnyugaton és
      északkeleten számíthatunk pára és köd kialakulására. Napközben változó
      mennyiségű fátyolfelhőzet szűri majd a napsütést, emellett
      északon-északkeleten gomolyfelhők is lehetnek az égen. Esni sehol sem fog.
      A Fertő-tó térségében a déli-délkeleti szél átmenetileg megélénkülhet. A
      minimum-hőmérséklet -4 és +5 fok között alakulhat, míg délutánra 11-16
      fokig melegszik a levegő. 




        

        
        Helyi időjárás:
        Részben felhős idő várható az előrejelzés szerint, 5.1 és 13.7 fok közötti hőmérséklettel.

        

        
          A mai egy csapadékmentes nap lesz.
        

      Pillanatnyilag 5.1 fok  van odakinn.
```