class Room:
    def __init__(self, name, till, entry_fee, capacity):
        self.name = name
        self.till = till
        self.entry_fee = entry_fee
        self.capacity = capacity
        self.guests = []
        self.songs = []
        self.pizzas = []

    def check_in_guest(self, guest):
        if self.space_in_room() and guest.can_afford(self.entry_fee):
            self.guests.append(guest)
            self.increase_till(self.entry_fee)
            guest.spend(self.entry_fee)
            return f"Welcome to {self.name}!"
        elif self.space_in_room() == False:
            return "No space!"
        elif guest.can_afford(self.entry_fee) == False:
            return "There's a bank machine round the corner"
            

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def space_in_room(self):
        if len(self.guests) < self.capacity:
            return True
        else:
            return False
        
    def increase_till(self, amount):
        self.till += amount
        

    def get_pizza_by_name(self, name):
        for pizza in self.pizzas:
            if pizza["name"] == name:
                return pizza
            
    def add_pizzas(self, pizzas):
        for pizza in pizzas:
            self.pizzas.append(pizza)
            
    def remove_pizza_from_pizza_stock(self, pizza_name):
        for pizza in self.pizzas:
            if pizza["name"] == pizza_name:
                pizza["number"] -= 1

        return None
    
    def get_pizza_price(self, pizza_name):
        for pizza in self.pizzas:
            if pizza["name"] == pizza_name:
                return pizza["price"]
            
    def sell_pizza(self, guest, pizza_name):
        self.pizza = self.get_pizza_by_name(pizza_name)
        self.pizza_price = self.get_pizza_price(pizza_name)
        if guest.can_afford(self.pizza["price"]):
            self.increase_till(self.pizza_price)
            guest.spend(self.pizza_price)
            self.remove_pizza_from_pizza_stock(pizza_name)
            return f"Enjoy your {pizza_name}!"
        else:
            return "There's a bank machine round the corner"
        
    def get_song_by_title(self, title):
        for song in self.songs:
            if song.title == title: 
                return song











