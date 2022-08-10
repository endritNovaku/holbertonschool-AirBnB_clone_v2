#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *


# creation of a State
state = state.State(name="Italy")
state.save()

# creation of a City
city = city.City(state_id=state.id, name="Milano")
city.save()

# creation of a User
user = user.User(email="bob@example.com", password="bob")
user.save()

# creation of 2 Places
place_1 = place.Place(user_id=user.id, city_id=city.id, name="House 3")
place_1.save()
place_2 = place.Place(user_id=user.id, city_id=city.id, name="MyHouse1")
place_2.save()

# creation of 3 various Amenity
amenity_1 = amenity.Amenity(name="NoWifi")
amenity_1.save()
amenity_2 = amenity.Amenity(name="NOCable")
amenity_2.save()
amenity_3 = amenity.Amenity(name="NoOven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")
