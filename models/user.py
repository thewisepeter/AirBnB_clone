from models.base_model import BaseModel


class User(BaseModel):
    """
    A subclass of BaseModel representing a user.
    
    Public class attributes:
        email: (str) the email address of the user
        password: (str) the password of the user
        first_name: (str) the first name of the user
        last_name: (str) the last name of the user
    """

    def __init__(self, email="", password="", first_name="", last_name=""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
