from fastapi import FastAPI, BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


app = FastAPI()

@app.post("/api/users")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}

