from fastapi import FastAPI, HTTPException
from models import User, Gender, Roles, UserMod
from uuid import UUID, uuid4

app = FastAPI()

db : list[User] = [
    User(
        id=UUID("00c74035-fc33-4b3b-a414-150dd8183cab"),
        first_name="Simeone",
        last_name="Keisha",
        gender=Gender.female,
        roles=[Roles.student]
    ),
    User(
        id=UUID("00f3825b-3b70-456c-b258-828445e20806"),
        first_name="Mbuthi",
        last_name="Mungai",
        gender=Gender.male,
        roles=[Roles.user, Roles.admin]
    ),    
]

db2 : list[UserMod] = [
    UserMod(
        id=UUID("ff0a112b-3b25-4332-a9eb-7763f3c3bf60")
    )
]

@app.get("/")
async def root():
    return {"Hello" : "Mbuthi"}

@app.get("/api/v1/users/")
async def fetch_users():
    return db2

@app.post("/api/v1/users/")
async def register_user(user : User):
    db.append(user)
    return {"id" : user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id : UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"msg" : "user deleted"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
    
@app.put("/api/v1/users/{user_id}")
async def update_user(user_id : UUID):
    for user in db2:
        if user.id == user_id:
            user.first_name = "Anthony"
            user.middle_name = "Joshua"
            user.last_name = "Hills"
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )