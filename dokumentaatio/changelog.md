# Changelog

## Viikko3

- Lisätty Game-luokka ja User-luokka, jotka sisältävät pelin ja käyttäjän tiedot
- Lisätty GameRepository-luokka, joka vastaa pelien lisäämisestä tietokantaan ja poistamisesta tietokannasta
- Lisätty UserRepository-luokka, joka vastaa käyttäjien lisäämisestä tietokantaan
- Lisätty GameService-luokka, jonka kautta voi hallinnoida backlogia
- Testattu GameRepository-luokan metodeja eli pelin lisäämistä, poistamista ja kaikkien pelien hakemista tietokannasta


## Viikko4

- Käyttäjä voi luoda käyttäjän ja kirjautua sisään
- Käyttäjä voi lisätä pelejä backlogiin kirjauduttuaan sisään
- Käyttäjä voi kirjautua ulos
- Muokattu luokkia käyttäjän rekisteröinnin, sisään kirjautumisen mahdollistamiseksi ja siten, että lisätyt pelit ovat sidonnaisia käyttäjiin
- Lisätty alustava graafinen käyttöliittymä
- Testattu GameRepository-luokan metodia, jolla voi etsiä pelin käyttäjän perusteella, UserRepository-luokan metodeja eli käyttäjän lisäämistä, kaikkien käyttäjien etsimistä ja yhden käyttäjän etsimistä, GameService-luokan metodeja eli käyttäjän rekisteröintiä, kirjautumista ja pelin lisäämistä backlogiin.
