from models.base_model import BaseModel


class City(BaseModel):
    """
    A subclass of BaseModel representing a city.
    
    Public class attributes:
        state_id: (str) the ID of the state to which the city belongs
        name: (str) the name of the city
    """
    
    def __init__(self, state_id="", name=""):
        super().__init__()
        self.state_id = state_id
        self.name = name
