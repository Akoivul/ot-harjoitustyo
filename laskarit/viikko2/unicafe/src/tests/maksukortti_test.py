import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)
    
    def test_saldo_vähenee_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)
    
    def test_saldo_ei_vähene_kun_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_ota_rahaa_metodi_palauttaa_True_kun_rahaa_on_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_ota_rahaa_metodi_palauttaa_False_kun_rahaa_ei_ole_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
    
    def test_maksukortin_str_metodi_toimii(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
