from class_room import Room


class VIPRoom(Room):
    def __init__(self, room_number, capacity, price_per_night, additional_services):
        super().__init__(room_number, capacity, price_per_night)
        self.additional_services = additional_services

    def __str__(self):
        return (f"VIP Room {self.room_number}, Capacity: {self.capacity}, Price per Night: ${self.price_per_night}, "
                f"Additional Services: {self.additional_services}")
