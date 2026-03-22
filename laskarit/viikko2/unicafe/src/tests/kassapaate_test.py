import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
    
    def test_kassapaatteen_raha_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_kassapaatteen_myydyt_edulliset_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassapaatteen_myydyt_maukkaat_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassassa_oleva_rahamaara_oikea_edullisen_oston_jalkeen_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_vaihtoraha_oikea_edullisen_oston_jalkeen_kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
    
    def test_edullisten_lounaiden_määrä_oikea_edullisen_oston_jalkeen_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kassassa_oleva_rahamaara_ei_muutu_edullisen_oston_jalkeen_liian_vahalla_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_edullisten_lounaiden_määrä_oikea_edullisen_oston_jalkeen_liian_vahalla_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kaikki_rahat_palautetaan_edullisen_oston_jalkeen_liian_vahalla_kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    def test_kassassa_oleva_rahamaara_oikea_maukkaan_oston_jalkeen_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
    
    def test_vaihtoraha_oikea_maukkaan_oston_jalkeen_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)
    
    def test_edullisten_lounaiden_määrä_oikea_maukkaan_oston_jalkeen_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kassassa_oleva_rahamaara_ei_muutu_maukkaan_oston_jalkeen_liian_vahalla_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_edullisten_lounaiden_määrä_oikea_maukkaan_oston_jalkeen_liian_vahalla_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kaikki_rahat_palautetaan_maukkaan_oston_jalkeen_liian_vahalla_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(350), 350)
    
    def test_korttiosto_toimii_edullisella_kun_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_myytyjen_edullisten_määrä_nousee_korttioston_jalkeen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_ei_toimi_edullisella_kun_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
    
    def test_kortin_rahamaara_ei_muutu_jos_rahaa_ei_ole_tarpeeksi_edulliseen(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_myytyjen_edullisten_määrä_ei_muutu_jos_rahaa_ei_ole_tarpeeksi_korttioston_jalkeen(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassan_rahamaara_ei_muutu_edullisen_korttioston_jälkeen_jos_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttiosto_toimii_maukkaalla_kun_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_myytyjen_maukkaiden_määrä_nousee_korttioston_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_ei_toimi_maukkaalla_kun_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    
    def test_kortin_rahamaara_ei_muutu_jos_rahaa_ei_ole_tarpeeksi_maukkaaseen(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_myytyjen_maukkaiden_määrä_ei_muutu_jos_rahaa_ei_ole_tarpeeksi_korttioston_jalkeen(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassan_rahamaara_ei_muutu_maukkaan_korttioston_jälkeen_jos_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.maksukortti.saldo, 600)
    
    def test_kortille_rahaa_ladattaessa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)
    
    def test_kortille_rahaa_ladattaessa_kortin_saldo_ei_muutu_jos_ladattava_arvo_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.maksukortti.saldo, 500)
    
    def test_kortille_rahaa_ladattaessa_kassan_rahamaara_ei_kasva_jos_ladattava_arvo_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    
    