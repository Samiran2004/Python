def main():
    print("Hello from pydantic!")


from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

user = UserProfile(name="Samiran", age=21, email="samiran@gmail.com")

if __name__ == "__main__":
    main()
    print(user.name)
