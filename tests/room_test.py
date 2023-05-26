import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song2 = Song("Making Your Mind Up", "Bucks Fizz")
        self.song3 = Song("White Lines", "Melle Mel")
        self.harry = Guest("Harry", 32, 50.00, self.song2)
        self.zainib = Guest("Zainib", 25, 25.00, self.song3)
        self.room = Room("The Viper Room", 650.00, 10.00, 16)

    def test_room_has_name(self):
        self.assertEqual("The Viper Room", self.room.name)

    def test_room_has_till(self):
        self.assertEqual(650.00, self.room.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(10.00, self.room.entry_fee)

    def test_room_has_capacity(self):
        self.assertEqual(16, self.room.capacity)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.zainib)
        self.added_guest = self.room.guests[0]
        self.added_guest_name = self.added_guest.name
        self.assertEqual("Zainib", self.added_guest_name)

    def test_check_out_guest(self):
        self.room.check_in_guest(self.zainib)
        self.room.check_out_guest(self.zainib)
        self.assertEqual(0, len(self.room.guests))

    def test_add_song(self):
        self.room.add_song(self.song2)
        self.added_song = self.room.songs[0]
        self.added_song_title = self.added_song.title
        self.assertEqual("Making Your Mind Up", self.added_song_title)

    
