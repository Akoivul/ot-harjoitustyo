# Changelog

## Viikko 3

- Lisätty Game-luokka ja User-luokka, jotka sisältävät pelin ja käyttäjän tiedot
- Lisätty GameRepository-luokka, joka vastaa pelien lisäämisestä tietokantaan ja poistamisesta tietokannasta
- Lisätty UserRepository-luokka, joka vastaa käyttäjien lisäämisestä tietokantaan
- Lisätty GameService-luokka, jonka kautta voi hallinnoida backlogia
- Testattu GameRepository-luokan metodeja eli pelin lisäämistä, poistamista ja kaikkien pelien hakemista tietokannasta


## Viikko 4

- Käyttäjä voi luoda käyttäjän ja kirjautua sisään
- Käyttäjä voi lisätä pelejä backlogiin kirjauduttuaan sisään
- Käyttäjä voi kirjautua ulos
- Muokattu luokkia käyttäjän rekisteröinnin, sisään kirjautumisen mahdollistamiseksi ja siten, että lisätyt pelit ovat sidonnaisia käyttäjiin
- Lisätty alustava graafinen käyttöliittymä
- Testattu GameRepository-luokan metodia, jolla voi etsiä pelin käyttäjän perusteella, UserRepository-luokan metodeja eli käyttäjän lisäämistä, kaikkien käyttäjien etsimistä ja yhden käyttäjän etsimistä, GameService-luokan metodeja eli käyttäjän rekisteröintiä, kirjautumista ja pelin lisäämistä backlogiin.

## Viikko 5

- Käyttäjä voi muuttaa pelin tilaa backlogissa
- Käyttäjä voi poistaa pelin backlogista
- Muokattu käyttöliittymää siten, että eri tiloissa olevat pelit ovat omilla sarakkeilla
- Testattu GameRepository-luokan metodia, joka muuttaa pelin tilan
- Testattu GameService-luokan metodia, jolla voi poistaa pelin

## Viikko 6

- Käyttäjä voi muokata tilojen nimiä
- Lisätty GameService- ja UserRepository-luokkiin metodeja tilon nimien muokkauksen mahdollistamiseksi
- Lisätty käyttöliittymään tilojen nimien muokkaamiseen avautuva oma ikkuna
- Testattu GameService-luokan metodeja eli, että tilojen nimien muokkaaminen toimii oikein eli ei onnistu, jos jokin nimistä on tyhjä tai nimet eivät ole uniikkeja.
- Testattu UserRepositoryn metodeja, joilla voi etsiä käyttäjän omat tilojen nimet ja muuttaa ne.
