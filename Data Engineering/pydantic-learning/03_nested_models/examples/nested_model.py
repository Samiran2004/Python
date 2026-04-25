from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
class User(BaseModel):
    id: int
    name: str
    address: Address
    
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None
    
Comment.model_rebuild()

address = Address(
    street="123 Something",
    city="Kolaghat",
    postal_code="721154"
)

user = User(
    id=1,
    name="Samiran Samanta",
    address=address
)

comment = Comment(
    id=1,
    content="Comment 1",
    replies=[
        Comment(
            id=2,
            content="Comment 2",
            replies=[
                Comment(
                    id=3,
                    content="Comment 3"
                )
            ]
        ),
        Comment(
            id=4,
            content="Comment 4"
        )
    ]
)

print(user)
print(address)
print(comment)