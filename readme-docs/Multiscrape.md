Egy kis segítség annak akinek gondjai akadnak a honlapról val információ kinyeréssel kapcsolatban. Első sorban nézzük a _select_ opciót. A [koponyeg.hu](https://koponyeg.hu/elorejelzes/kaposvar) oldalról kaposvár település előrejelzését fogjuk kiolvasni.
![koponyeg](/readme-img/koponyeg.png)

Innét olvassuk ki első körben a napnyugtát. Nincs más dolgunk, mint az egeret a chrome böngészőben a napnyugta felíratra vinni és ott jobb egérgombot nyomni, majd a vizsgálat funkciót választani. Ekkor a böngészáben megjelnik egy új panel ebből kell információt szerezni.
![vizsgalat](/readme-img/vizsgalat.png)

Ha megnézzük az alábbi kódot látjuk a Napnyugta sorban:
```
<div _ngcontent-serverapp-c109="" class="sunset">17:49 Napnyugta</div>
```
A _class_ rész érdekel minket, próbáljuk ki, hogy ha a _scrape select_ sornak ezt az értéket adjuk meg mi történik.
```
select: ".sunset"
```
És láss csodát ki is olvasta, hogy mikor lesz a napnyugta, természetesen nem csak az időpontot, hanem az utána lévő szöveget is. Ezt majd a *value_template* értékkel tudjuk megoldani, ha csak a pontos idő kell nekünk.

Sajnos nem mindig van ilyen könnyű dolgunk, nézzük meg mi van ha például az UV sugárzást szeretnénk kiolvasni az oldalról. Szokásos módon válaszuk a vizsgálat opciót a kívánt értéken.
![uv](/readme-img/uv.png)

Próbálkozzunk itt is a _class_ értékkel, sajnos azt fogja visszaadni, hogy **Nincs** ami a fronthatás értéke. Ha megnézzük a kódot látni fogjuk hogy ott is ugyan az a _class_ szerepel. A scrape pedig mindig az első értéket adja vissza az oldalról.
![fronthatas](/readme-img/fronthatas.png)

Ilyenkor jön jól a _copy selector_ funkció. Megkeressük az UV értékét a kódban azon jobb egérgomb és ott a _copy -> copy selector_ parancsot választjuk. Amit kimásolt nekünk vágólapra azt beillesztjük egy egyszerű szövegszerkesztőbe, mivel a teljes sor nem fog kelleni nekünk.
![copys](/readme-img/copys.png)

```
body > app-root > app-base > div.content-wrap > app-home > section > div > app-layout > kesma-layout > div:nth-child(5) > div.col-12.horizontal.column-border-color-undefined.col-lg-9.ng-star-inserted > div > div.content-container.content-element.content-type-medical-meteorology.layout-element.ng-star-inserted > app-medical-meteorology-adapter > koponyeg-medical-meteorology > div.meteorology-info > div:nth-child(3) > div > span
```
Visszafelé kell olvasni a kódot, _span_ ez adja vissza az értéket *<span _ngcontent-serverapp-c100="" class="meteorology-info-bold">Mérsékelt</span>*. Utána 1 szintel feljebb lépünk _div_ *<div _ngcontent-serverapp-c100="" class="meteorology-info-details">* ezzel nem kell foglalkozzunk. Menjünk feljebb _div:nth-child(3)_ na itt már van valami *<div _ngcontent-serverapp-c100="" class="meteorology-info-item">*, ez mondja meg, hogy nekünk nem a _Fronthatás_ értéke kell hanem a _UV sugárzás_ értéke, látni is hogy ez a 3. div ami azonos szinten van ebben a kód részletben. Ez után menjünk még egy értékkel feljebb _div.meteorology-info_ és így már tujuk is mivel kell kezdeni a _select_ értékünket, csakhogy tutira jó helyről olvassa ki az információt.
```
select: "div.meteorology-info > div:nth-child(3) > div > span"
```

Most nézzük kicsit az [idokep.hu](https://www.idokep.hu/elorejelzes/Szeksz%C3%A1rd) oldalról az előrejelzéseket hogyan tudjuk kiolvasni.
[!idokep](/readme-img/idokep.png)


Itt rögtön 3 _p_ értéket kellene kiolvasni ráadásul az egyiket még két felé is kell osztani. Használhatjuk a _nth-child(x)_-et, de van egy másik megoldás _nth-of-type(x)_. A különbség az két kód között, hogy az elsőnél a szülőhöz képest kell nézni az x-et, míg a másodiknál az adott típushoz.

Olvassuk ki az első napot, ezzel nincs is gond.
```
select: "div.hosszutavu-elorejelzes-container > div > div > p:nth-of-type(1)"
```

Jöhet a 2. és 3. nap mivel ezeket egy _p_ alatt vannak így itt jön képbe a *value_template* amivel szépen fel tujuk osztani részekre. A lenti kódban látható, hogy a _value.split_-tel szépen a _"\n"_-nél ami a sortörést jelenti feldaraboljuk és csak a nekünk kellő részt vesszük ki.
```
select: "div.hosszutavu-elorejelzes-container > div > div > p:nth-of-type(2)"
value_template: '{{ (value.split("\n")[1]) }}'

select: "div.hosszutavu-elorejelzes-container > div > div > p:nth-of-type(2)"
value_template: '{{ (value.split("\n")[3]) }}'
```

Ha a fenti részt _copy select_-el vesszük ki akkor teljesen 
Még egy funkció a kiolvasáshoz, ha mondjuk képként jelenik meg az infó, de a kódban benn van szövegesen is az információ, ezt is ki lehet olvasni, csak kell hozzá egy új funkció, méghozzá az _attribute_. Ezzel azt tudjuk elérni, hogy a lekérdezni kívánt adat jelen esetben az _a_ részből melyik információra lenne nekünk szükségünk. 
[!idokep_szel](/readme-img/idokep_szel.png)
```
select: "div.new-hourly-forecast-card-container > div:nth-child(1) > div.hourly-wind > a"
attribute: "data-bs-content"
```

Fontos, hogy azért kicsit meg is kell nézni/érteni amit a _copy select_ ad vissza, van hogy változtatni kell rajta kicsit. Valamint a value_template_-nek is nagyon sok funkciója létezik.
