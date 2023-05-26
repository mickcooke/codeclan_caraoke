import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Since Youve Been Gone", "Rainbow")

    def test_song_has_title(self):
        self.assertEqual("Since Youve Been Gone", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Rainbow", self.song.artist)