class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reviews = []
        self.guests_ever_visited = set()  # we need this so only guests that ever visited the hotel could review it

    def add_room(self, room):
        self.rooms.append(room)

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms if not room.is_booked]
        if available_rooms:
            for room in available_rooms:
                print(room)
        else:
            print("No available rooms.")

    def book_room(self, guest, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.book():
                    print(f"Room {room_number} of \"{self.name}\" hotel booked successfully by {guest.name}.")
                    self.guests_ever_visited.add(guest)
                else:
                    print(f"Room {room_number} of \"{self.name}\" hotel is already booked.")
                return
        print(f"Room {room_number} not found.")

    def add_review(self, review):
        if review.guest in self.guests_ever_visited:
            self.reviews.append(review)
            print(f"{review.guest.name} has added their review on {self.name}")
        else:
            print(f"{review.guest.name} haven't visited {self.name}, they can't review it")

    def display_reviews(self):
        print(f"\nHere are reviews by our guests:")
        for review in self.reviews:
            print(f"Author: {review.guest.name}. Rating: {review.rating} Comment: {review.comment}")
