from models.base_model import BaseModel


class Place(BaseModel):
    """
    A subclass of BaseModel representing a place.
    
    Public class attributes:
        city_id: (str) the ID of the city where the place is located
        user_id: (str) the ID of the user who owns the place
        name: (str) the name of the place
        description: (str) the description of the place
        number_rooms: (int) the number of rooms in the place
        number_bathrooms: (int) the number of bathrooms in the place
        max_guest: (int) the maximum number of guests the place can accommodate
        price_by_night: (int) the price per night for the place
        latitude: (float) the latitude coordinate of the place's location
        longitude: (float) the longitude coordinate of the place's location
        amenity_ids: (list) a list of IDs of amenities available at the place
    """
    
    def __init__(self, city_id="", user_id="", name="", description="", number_rooms=0,
                 number_bathrooms=0, max_guest=0, price_by_night=0, latitude=0.0,
                 longitude=0.0, amenity_ids=None):
        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = [] if amenity_ids is None else amenity_ids
