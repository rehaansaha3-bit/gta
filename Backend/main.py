
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from A1 import register_player
from A2 import verify_login
from A3 import refresh_access_token
from E1 import create_mission_manager
from sqlalchemy.orm import Session
from database import engine, User
from A3 import verify_token
from E2 import create_mission
app = FastAPI()


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


@app.post("/auth/register")
def register(data: RegisterRequest):

    result = register_player(
        username=data.username,
        email=data.email,
        password=data.password
    )

    if result == False:
        raise HTTPException(status_code=400, detail="Email already registered")

    return {"message": "Player registered successfully"}


@app.get("/")
def home():
    return {"message": "GTA Mission Hub Backend Running"}


class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/auth/login")
def login(data: LoginRequest):

    result = verify_login(
        email=data.email,
        password=data.password
    )

    if result == False:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return result

# a3
class RefreshRequest(BaseModel):             
    refresh_token: str


@app.post("/auth/refresh")
def refresh(data: RefreshRequest):

    result = refresh_access_token(data.refresh_token)

    if result == False:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    return {"access_token": result}

class ManagerRequest(BaseModel):
    username: str
    email: str
    password: str

@app.post("/admin/mission-managers")
def create_manager(data: ManagerRequest):

    result = create_mission_manager(
        data.username,
        data.email,
        data.password
    )

    if result == False:
        raise HTTPException(status_code=400, detail="Email already registered")

    return {"message": "Mission manager created successfully"}


# E2 - Create Mission

class MissionRequest(BaseModel):
    access_token: str
    title: str
    description: str
    difficulty: str
    location: str
    reward: int


@app.post("/missions")
def add_mission(data: MissionRequest):

    email = verify_token(data.access_token, "access")

    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    session = Session(engine)
    user = session.query(User).filter_by(email=email).first()

    if user is None or user.role != "mission_manager":
        session.close()
        raise HTTPException(status_code=403, detail="Only mission managers can create missions")

    manager_id = user.id
    session.close()

    if data.difficulty.lower() not in ["easy", "medium", "hard", "special"]:
        raise HTTPException(status_code=400, detail="Invalid difficulty")

    mission_id = create_mission(
        data.title,
        data.description,
        data.difficulty.lower(),
        data.location,
        data.reward,
        manager_id
    )

    return {
        "message": "Mission created successfully",
        "mission_id": mission_id
    }
