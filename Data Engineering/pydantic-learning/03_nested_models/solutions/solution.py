'''
Todo: Create Course model
Each course has modules
Each Module has lessons
'''

from typing import List

from pydantic import BaseModel


class Lesson(BaseModel):
    id: int
    topic: str
    
class Module(BaseModel):
    id: int
    name: str
    lessons: List[Lesson]
    
class Course(BaseModel):
    id: int
    title: str
    modules: List[Module]

