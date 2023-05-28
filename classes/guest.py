class Guest:
    def __init__(self, name, age, wallet, fav_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fav_song = fav_song

    def can_afford(self, amount):
        if self.wallet >= amount :
            return True
        else:
            return False
        
    def spend(self, amount):
        self.wallet -= amount

    def fav_song_react(self, room):
        for song in room.songs:
            if self.fav_song == song:
                return "Woo!"
            
        return "Boo!"
    
    


            
