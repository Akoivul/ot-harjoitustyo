# Testausdokumentti
Sovellusta on testattu automatisoiduilla yksikkö- ja integraatiotesteillä sekä manuaalisesti järjestelmätasolla.

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
`GameService`-luokka vastaa sovelluslogiikasta, ja sitä on testattu `TestGameService`-testiluokalla. `GameService`-luokan testeissä kutsutaan `UserRepository`- ja `GameRepository`-olioita, ja testeissä on käytössä vain testaamisessa käytetty .env.test-tiedostossa määritelty tietokantatiedosto.

### Repositorio-luokat
`UserRepository`-luokkaa on testattu `TestUserRepository`-testiluokalla ja `GameRepository`-luokkaa on testattu `TestGameRepository`-testiluokalla. `UserRepository`- ja `GameRepository`-luokkien testeissä on käytössä sama vain testaamisessa käytetty .env.test-tiedostossa määritelty tietokantatiedosto.

## Testikattavuus
Sovelluksen testauksen haarautumakattavuus on 98%. Käyttöliittymä on jätetty testikattavuuden ulkopuolelle.
![coverage-report](./kuvat/coverage-report.png)

## Järjestelmätestaus
Järjestelmätestaus on tehty manuaalisesti sovellusta käyttäen.

### Asennus ja käynnistäminen
Sovellus on ladattu ja käynnistetty käyttöohjetta seuraten Cubbli Linux-ympäristössä.

### Toiminnallisuudet
Vaatimusmäärittelyssä määritellyt sovelluksen toiminnallisuudet on testattu manuaalisesti oikeilla ja virheellisillä syötteillä.

## Sovellukseen jääneet laatuongelmat
- Sovelluksessa ei ole määritelty virheilmoitusta tilanteelle, jossa tietokantaa ei ole alustettu.
- Käyttäjän salasanan pituudelle ei ole rajaa.
