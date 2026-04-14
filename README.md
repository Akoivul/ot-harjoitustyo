# Game Backlog

Sovelluksen avulla voi seurata ja hallita peli backlogia.
## Dokumentaatio
[Vaatimusmäärittely](https://github.com/Akoivul/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Akoivul/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/Akoivul/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/Akoivul/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet:
```
poetry install
```
2. Alusta tietokanta:
```
poetry run invoke build
```
3. Käynnistä sovellus:
```
poetry run invoke start
```

## Muut komennot

Aja testit:
```
poetry run invoke test
```
Generoi testikattavuusraportti:
```
poetry run invoke coverage-report
```
Raportti on hakemistossa htmlcov tiedosto index.html

Pylint tarkistus:
```
poetry run invoke lint
```
