# Copilot-ohjeet

## Projektin yleiskuva

Tämä on pieni Python 3.14 -harjoitus ostoskorin toimialueesta. Lähdetiedostot
ovat `src/`-hakemiston tasomoduuleja eivätkä asennettua pakettia:

- `tuote.py` määrittelee `Tuote`-luokan, joka sisältää tuotteen nimen ja
  kokonaislukuna esitetyn yksikköhinnan.
- `ostos.py` määrittelee `Ostos`-luokan. Se sisältää yhden `Tuote`-tuotteen,
  alkaa määrällä 1, rajoittaa määrän vähintään nollaan ja laskee rivin
  kokonaishinnan.
- `ostoskori.py` määrittelee `Ostoskori`-luokan rajapinnan (`lisaa_tuote`,
  `poista_tuote`, `tyhjenna`, `ostokset`, `hinta` ja
  `tavaroita_korissa`). Sen toimintaa kehitetään testien avulla.
- `src/tests/ostoskori_test.py` sisältää ostoskorin testit. Testit käyttävät
  `unittest.TestCase` -tyylistä väite-syntaksia, mutta ne suoritetaan pytestillä.

Pidä toimialuelogiikka näissä moduuleissa ja säilytä nykyiset olioiden väliset
relaatiot: ostoskorin tulee käsitellä tuotteita `Ostos`-instanssien kautta, ja
hintojen summien tulee perustua tuotteen ja ostosrivin metodeihin sen sijaan,
että hinnoittelusääntöjä toistetaan eri paikoissa.

## Kehityskomennot

Suorita komennot hakemistossa `viikko4/tdd-ostoskori/`.

```bash
# Asenna tai synkronoi lukittu ympäristö
uv sync

# Suorita koko testikokoelma
uv run pytest

# Suorita yksi testi
uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

Repositoriossa ei ole määritelty koontikomentoa tai linttaus- ja
muotoilutyökalua tiedostossa `pyproject.toml`. Ainoa kehitysriippuvuus on
pytest.

## Käytännöt

- Suorita testit komennolla `uv run pytest`.
- Älä muuta tiedostoja `src/ostos.py` tai `src/tuote.py`.
- Älä muokkaa testejä, ellei sitä erikseen pyydetä.
- Toteuta aina vain pienin muutos, jolla nykyiset testit menevät läpi. Älä
  toteuta tulevien askelten toiminnallisuutta ennakkoon.
- Käytä nykyisiä suomenkielisiä julkisia nimiä ja metodinimiä, sillä ne ovat
  osa harjoituksen rajapintaa ja testit riippuvat niistä.
- Pidä tyyppimerkinnät yhdenmukaisina nykyisten rakentajien ja metodien kanssa.
- Testit sijaitsevat hakemistossa `src/tests/`, käyttävät
  `unittest.TestCase` -luokkaa ja alustavat yleensä yhteiset testivakiot
  `setUp`-metodissa.
- Tuonnit ovat suoria moduulituonteja, kuten `from tuote import Tuote`, eivät
  pakettien suhteellisia tuonteja. Säilytä tämä rakenne, ellei projektia
  tarkoituksella muuteta paketiksi.
- Määrät ja hinnat esitetään kokonaislukuina. `Ostos.muuta_lukumaaraa` ei saa
  sallia negatiivista määrää, ja tyhjän ostoskorin kokonaishinnan tulee olla
  nolla.
