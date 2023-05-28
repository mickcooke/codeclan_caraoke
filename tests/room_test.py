import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.pizza import Pizza

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song2 = Song("Making Your Mind Up", "Bucks Fizz")
        self.song3 = Song("White Lines", "Melle Mel")
        self.harry = Guest("Harry", 32, 50.00, self.song2)
        self.zainib = Guest("Zainib", 25, 25.00, self.song3)
        self.room = Room("The Viper Room", 650.00, 10.00, 16)
        self.pizza1 = Pizza("Margerita", 9.50)
        self.pizza2 = Pizza("Hawaiian", 10.50)
        self.pizzas = [{"name": self.pizza1.name, "price" : self.pizza1.price, "number": 6}, {"name": self.pizza2.name, "price" : self.pizza2.price, "number": 5}]

    def test_room_has_name(self):
        self.assertEqual("The Viper Room", self.room.name)

    def test_room_has_till(self):
        self.assertEqual(650.00, self.room.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(10.00, self.room.entry_fee)

    def test_room_has_capacity(self):
        self.assertEqual(16, self.room.capacity)

    def test_check_in_guest_not_full(self):
        self.room.capacity = 1
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

    def test_remove_song(self):
        self.room.add_song(self.song2)
        self.room.remove_song(self.song2)
        self.assertEqual(0, len(self.room.songs))

    def test_space_in_room_True(self):
        self.room.capacity = 2
        self.room.check_in_guest(self.zainib)
        self.check_capacity = self.room.space_in_room()
        self.assertEqual(True, self.check_capacity)

    def test_space_in_room_False(self):
        self.room.capacity = 1
        self.room.check_in_guest(self.zainib)
        self.check_capacity = self.room.space_in_room()
        self.assertEqual(False, self.check_capacity)

    def test_check_in_guest_full(self):
        self.room.capacity = 1
        self.room.check_in_guest(self.zainib)
        self.result = self.room.check_in_guest(self.harry)
        self.assertEqual("No space!", self.result)

    def test_take_guest_money(self):
        self.guest = self.zainib
        self.room.check_in_guest(self.guest)
        self.result = self.guest.wallet
        self.assertEqual(15.00, self.result)

    def test_till_increases(self):
        self.guest = self.zainib
        self.room.check_in_guest(self.guest)
        self.result = self.room.till
        self.assertEqual(660.00, self.result)

    def test_welcome(self):
        self.guest = self.zainib
        self.welcome = self.room.check_in_guest(self.guest)
        self.assertEqual("Welcome to The Viper Room!", self.welcome)

    def test_customer_cannot_afford_entry(self):
        self.guest = self.zainib
        self.guest.wallet = 2.00
        self.result = self.room.check_in_guest(self.guest)
        self.assertEqual("There's a bank machine round the corner", self.result)

    def test_add_pizzas(self):
        self.room.add_pizzas(self.pizzas)
        self.result = len(self.room.pizzas)
        self.assertEqual(2, self.result)

    def test_get_pizza_by_name(self):
        self.room.add_pizzas(self.pizzas)
        self.pizza_object = self.room.get_pizza_by_name("Margerita")
        self.result = self.pizza_object["price"]
        self.assertEqual(9.50, self.result)

    def test_remove_pizza_from_pizza_stock(self):
        self.room.add_pizzas(self.pizzas)
        self.room.remove_pizza_from_pizza_stock("Margerita")
        self.result = self.room.pizzas[0]["number"]
        self.assertEqual(5, self.result)

    def test_get_pizza_price(self):
        self.room.add_pizzas(self.pizzas)
        self.result = self.room.get_pizza_price("Margerita")
        self.assertEqual(9.50, self.result)

    def test_sell_pizza_successful(self):
        self.room.add_pizzas(self.pizzas)
        self.room.sell_pizza(self.harry, "Margerita")
        self.result = self.room.till
        self.assertEqual(659.50, self.result)

    def test_sell_pizza_fail(self):
        self.harry.wallet = 4.00
        self.room.add_pizzas(self.pizzas)
        self.result = self.room.sell_pizza(self.harry, "Margerita")
        self.assertEqual("There's a bank machine round the corner", self.result)

    def test_get_song_by_title(self):
        self.room.add_song(self.song2)
        self.result = self.room.get_song_by_title("Making Your Mind Up")
        self.assertEqual("Bucks Fizz", self.result.artist)
        

















    



    
