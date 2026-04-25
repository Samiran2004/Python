from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict, field_serializer

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    # --- CLASS LEVEL LOGIC GOES HERE ---
    model_config = ConfigDict(str_strip_whitespace=True)
    
    @field_serializer('created_at')
    def serialize_date(self, dt: datetime, _info):
        return dt.strftime('%d-%m-%Y %H:%M:%S')

# --- DATA INSTANTIATION GOES HERE ---
user = User(
    id=1,
    name="Samiran Samanta",
    email="samiran@gmail.com",
    is_active=True,
    created_at=datetime(2026, 3, 15, 14, 30),
    address=Address(
        street="123",
        city="Kolaghat",
        zip_code="721154"
    ),
    tags=["premium", "subscriber"]
)

# using model_dump() -> dict
python_dict = user.model_dump()

# using model_dump_json() -> json
json_str = user.model_dump_json(indent=2)

print("--- User Object ---")
print(user)
print("\n--- Python Dict (Native Datetime) ---")
print(python_dict['created_at'])
print("\n--- JSON String (Formatted Date) ---")
print(json_str)