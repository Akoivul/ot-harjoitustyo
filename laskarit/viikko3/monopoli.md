
```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" --> "1" Aloitusruutu
    Monopolipeli "1" --> "1" Vankila
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asemat
    Ruutu <|-- Laitokset
    Ruutu <|-- Kadut
    Ruutu "1" --> "1" Toiminto
    Sattuma "1" -- "1" Kortit
    Yhteismaa "1" -- "1" Kortit
    Kortit "1" --> "1" Toiminto
    Kadut "1" -- "0..4" Talo
    Kadut "1" -- "0..1" Hotelli
    Kadut "1" -- "0..1" Pelaaja
    Pelaaja "1" -- "1" Raha
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
```
