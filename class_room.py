class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        else:
            return False

    def __str__(self):
        return f"Room {self.room_number}, Capacity: {self.capacity}, Price per Night: ${self.price_per_night}"
