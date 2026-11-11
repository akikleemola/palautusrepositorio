# Projektiohjeet

## Koonti ja testaus

- Projekti käyttää Python 3.14+:aa, `uv`:ia, Flaskia ja Robot Frameworkia. Asenna tai synkronoi riippuvuudet komennolla `uv sync`.
- Käynnistä selain-testien palvelin komennolla `uv run python src/index.py`. Se kuuntelee osoitteessa `http://localhost:5001`.
- Suorita kaikki selain-testit komennolla `uv run robot src/tests`.
- Suorita yksi testisarja komennolla `uv run robot src/tests/login.robot` tai yksi testi komennolla `uv run robot -t "Login With Correct Credentials" src/tests/login.robot`.
- Suorita selain-testit ilman käyttöliittymää komennolla `uv run robot -v HEADLESS:true src/tests`.
- `pyproject.toml` ei määritä erillistä lint- tai yksikkötestikomentoa.

## Arkkitehtuuri

- `src/index.py` on käynnistyspiste ja tuo Flask-sovelluksen tiedostosta `src/app.py`.
- `src/app.py` sisältää HTTP-reitit ja Jinja-renderöinnin. GET-reitit näyttävät templatet; POST-käsittelijät kutsuvat `UserService`-luokkaa ja ohjaavat onnistumisen tai virheen jälkeen oikealle sivulle.
- Tiedoston `src/services/user_service.py` `UserService`-luokan `validate`-metodi tekee rekisteröitymisen validoinnin. Sama palvelu tarkistaa myös kirjautumistiedot.
- `src/repositories/user_repository.py` tarjoaa muistissa toimivan `UserRepository`-singletonin, joten käyttäjät säilyvät vain käynnissä olevan prosessin ajan.
- `src/entities/user.py` sisältää käyttäjämallin. `src/templates/` sisältää `layout.html`-tiedostosta periytyvät käyttöliittymätemplatet.
- `src/tests/` sisältää Robot Frameworkin päästä päähän -testit. `resource.robot` määrittää Browserin ja Pythonin `AppLibrary`-kirjaston; `AppLibrary.py` nollaa ja alustaa sovelluksen HTTP-kutsuilla.

## Käytännöt

- Selain-testit olettavat palvelimen olevan käynnissä portissa 5001 ja nollaavat sovelluksen jokaisen testin alussa. Säilytä `/tests/reset` ja `AppLibrary`-apuohjelmat testitilaa muuttaessa.
- Pidä kirjautumisen ja rekisteröitymisen säännöt `UserService`-luokassa. Reittien tulee edelleen välittää palveluvirheet flash-viesteinä ja uudelleenohjauksina.
- Robot-testit tarkistavat sivujen otsikoita ja näkyvää tekstiä. Päivitä `src/tests/`-testit, jos muutat template-otsikoita, kenttien ID-tunnisteita, painikkeita tai flash-viestejä.
- Repository on tarkoituksella vain prosessin muistissa; tietokantaa tai migraatioita ei ole.
