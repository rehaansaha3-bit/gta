
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from A1 import register_player
from A2 import verify_login
from A3 import refresh_access_token

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

