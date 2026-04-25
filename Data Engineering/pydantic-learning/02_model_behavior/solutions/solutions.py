'''
Todo: Create Booking Model
Fields:
    - user_id: int
    - room_id: int
    - nights: int (must be >= 1)
    - rate_per_night: float
    Also, add computed field: total_amount = nights * rate_per_night
'''

from pydantic import BaseModel, Field, computed_field, model_validator, field_validator

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int
    @field_validator('nights')
    def check_nights(cls, v):
        if v < 1:
            raise ValueError("Nights must be >= 1.")
        
    rate_per_night: float
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.rate_per_night * self.nights