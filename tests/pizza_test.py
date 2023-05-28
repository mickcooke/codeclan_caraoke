import unittest

from classes.pizza import Pizza

class TestPizza(unittest.TestCase):

    def setUp(self):
        self.pizza = Pizza("Margerita", 9.50)

    def test_pizza_has_name(self):
        self.assertEqual("Margerita", self.pizza.name)

    def test_pizza_has_price(self):
        self.assertEqual(9.50, self.pizza.price)