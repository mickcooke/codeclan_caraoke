import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.fav_song = Song("Making Your Mind Up", "Bucks Fizz")
        self.guest = Guest("Harry", 32, 50.00, self.fav_song)

    def test_guest_has_name(self):
        self.assertEqual("Harry", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(32, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("Making Your Mind Up", self.guest.fav_song.title)
