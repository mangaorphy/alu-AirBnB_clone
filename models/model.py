import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.created_at = datetime.now()  # Set created_at to current datetime
        self.updated_at = self.created_at  # Set updated_at to current datetime

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),  # Convert to ISO format
            "updated_at": self.updated_at.isoformat()   # Convert to ISO format
        }

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"