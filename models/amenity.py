from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A subclass of BaseModel representing an amenity.
    
    Public class attribute:
        name: (str) the name of the amenity
    """
    
    def __init__(self, name=""):
        super().__init__()
        self.name = name
