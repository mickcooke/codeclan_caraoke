class Room:
    def __init__(self, name, till, entry_fee, capacity):
        self.name = name
        self.till = till
        self.entry_fee = entry_fee
        self.capacity = capacity
        self.guests = []
        self.songs = []

    def check_in_guest(self,guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)


