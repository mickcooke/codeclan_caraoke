import unittest

from classes.guest import Guest
from classes.song import Song
from classes.room import Room

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

    def test_can_afford_true(self):
        self.room = Room("The Viper Room", 650.00, 10.00, 16)
        self.result = self.guest.can_afford(self.room.entry_fee)
        self.assertEqual(True, self.result)

    def test_can_afford_false(self):
        self.room = Room("The Viper Room", 650.00, 100.00, 16)
        self.result = self.guest.can_afford(self.room.entry_fee)
        self.assertEqual(False, self.result)

    def test_spend(self):
        self.guest.spend(10.00)
        self.assertEqual(40.00, self.guest.wallet)

    def test_fav_song_react_True(self):
        self.room = Room("The Viper Room", 650.00, 100.00, 16)
        self.room.add_song(self.guest.fav_song)
        self.result = self.guest.fav_song_react(self.room)
        self.assertEqual("Woo!", self.result)

    def test_fav_song_react_False(self):
        self.room = Room("The Viper Room", 650.00, 100.00, 16)
        self.result = self.guest.fav_song_react(self.room)
        self.assertEqual("Boo!", self.result)



