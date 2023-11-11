class Platform:
    def __init__(self):
        self.hotels = []

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def display_hotels(self):
        for hotel in self.hotels:
            print(f"\nAvailable rooms in \"{hotel.name}\" hotel")
            hotel.display_available_rooms()
