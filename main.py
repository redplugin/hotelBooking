# Student: Darmen Tuyakayev
# Course: Python developer 14
# Project: Hotel Booking Platform

from class_platform import Platform
from class_hotel import Hotel
from class_room import Room
from class_vip_room import VIPRoom
from class_guest import Guest
from class_review import Review

# Creating rooms for "Almaty Inn" hotel
room1 = Room(101, 2, 50)
room2 = Room(102, 2, 50)
room3 = Room(103, 2, 50)
room4 = VIPRoom(201, 3, 150, "All inclusive, Hot tub")
room5 = VIPRoom(202, 3, 150, "All inclusive, Hot tub")

# Creating "Almaty Inn" hotel and fill it with rooms
almaty_inn = Hotel("Almaty Inn")
almaty_inn.add_room(room1)
almaty_inn.add_room(room2)
almaty_inn.add_room(room3)
almaty_inn.add_room(room4)
almaty_inn.add_room(room5)

# Creating rooms for "Aunt's house" hotel
room1 = Room(101, 5, 10)
room2 = Room(102, 5, 10)
room3 = Room(103, 5, 10)
room4 = Room(104, 5, 10)
room5 = VIPRoom(105, 5, 15, "No cockroaches")

# Creating "Aunt's house" hotel and fill it with rooms
aunts_house = Hotel("Aunt's House")
aunts_house.add_room(room1)
aunts_house.add_room(room2)
aunts_house.add_room(room3)
aunts_house.add_room(room4)
aunts_house.add_room(room5)

# Creating a platform and add the hotel
platform = Platform()
platform.add_hotel(almaty_inn)
platform.add_hotel(aunts_house)

# Create guests
guest_arman = Guest("Arman", "arman@gmail.com")
guest_john = Guest("John", "john@gmail.com")
guest_alex = Guest("Alex", "alex@yandex.ru")

# Display hotels and vacant rooms
print("\n=== Display hotels and vacant rooms on a platform ===")
platform.display_hotels()

# Booking rooms
print("\n=== Book a room ===")
almaty_inn.book_room(guest_arman, 101)
almaty_inn.book_room(guest_john, 202)
aunts_house.book_room(guest_alex, 105)

# Display hotels and vacant rooms after booking
print("\n=== Display hotels and vacant rooms on a platform AFTER BOOKING ===")
platform.display_hotels()

# Create reviews
review1 = Review(guest_alex, 1, "Haven't been there, but here's one star, just because I'm a jerk")
review2 = Review(guest_john, 4, "I liked it")
review3 = Review(guest_arman, 5, "Everything was great")

# Try to add a review by a guest who've never visited the hotel
print("\nTry to add a review by a guest who've never visited the hotel:")
almaty_inn.add_review(review1)

# Add reviews by those who visited the hotel
almaty_inn.add_review(review2)
almaty_inn.add_review(review3)


# Display reviews about a hotel
almaty_inn.display_reviews()
