class Wedding:
    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_wedding(self)

class Chef:
    def prepare_wedding(self, wedding):
        self.prepare_food(wedding.guests)

    def prepare_food(self, guests):
        # implementation goes here
        print(f"{guests} plates full of delicious food are placed around the dining hall.")

class Decorator:
    def prepare_wedding(self, wedding):
        self.decorate_place(wedding.flowers)

    def decorate_place(self, flowers):
        # implementation goes here
        print(f"The area is filled with:")
        for flower in flowers:
            print(f"{flower}s")

class Musician:
    def prepare_wedding(self, wedding):
        self.prepare_performance(wedding.songs)

    def prepare_performance(self, songs):
        # implementation goes here
        print("Musicians played: ")
        for song in songs:
            print(song)

