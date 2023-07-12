from models.base_model import BaseModel


class State(BaseModel):
    """
    A subclass of BaseModel representing a state.
    
    Public class attribute:
        name: (str) the name of the state
    """
    
    def __init__(self, name=""):
        super().__init__()
        self.name = name
