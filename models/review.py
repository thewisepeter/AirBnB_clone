from models.base_model import BaseModel


class Review(BaseModel):
    """
    A subclass of BaseModel representing a review.
    
    Public class attributes:
        place_id: (str) the ID of the place being reviewed
        user_id: (str) the ID of the user who wrote the review
        text: (str) the content of the review
    """
    
    def __init__(self, place_id="", user_id="", text=""):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
