#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:  # If kwargs is not empty
            for key, value in kwargs.items():
                if key != "__class__":  # Skip the __class__ key
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
        else:  # If kwargs is empty, create a new instance
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()  # Set created_at to current datetime
            self.updated_at = self.crated_at  # Set updated_at to current datetime
            storage.new(self)  # Add this instance to storage

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4
        

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()  # Save to storage

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