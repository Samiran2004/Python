from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    

input_data = {
    'id': 101,
    'name': "Samiran Samanta",
    'is_active': 'True'
}

user = User(**input_data)
print(user)