# GTA – Open World Mission Hub

## 1. Project Overview

GTA – Open World Mission Hub is a backend application inspired by open-world games. Players can explore available missions, accept missions, complete objectives and earn rewards.

Administrators manage the platform, while mission managers create missions and verify mission completions.

**Technology Stack:**
- Python
- FastAPI
- SQLite
- SQLAlchemy
- JWT Authentication
- Argon2 Password Hashing
- Docker
- AWS EC2
- GitHub Actions

## 2. Team Members

| Name | Role |
|---|---|
| Rehaan Saha | Backend Developer |

*This project is being implemented individually.*

## 3. Live Application

**API Base URL:** `http://YOUR_EC2_PUBLIC_IP:8001`

**Swagger API Documentation:** `http://YOUR_EC2_PUBLIC_IP:8001/docs`

Replace `YOUR_EC2_PUBLIC_IP` with your EC2 instance's public IP address.

## 4. How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd GTA/Backend
```

### Step 2: Create a Virtual Environment

```bash
py -m venv venv
```

### Step 3: Activate the Virtual Environment

```powershell
venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Start the Backend

```bash
python -m uvicorn main:app --reload --port 8001
```

Open the API documentation:

`http://127.0.0.1:8001/docs`

## 5. API Endpoints

The application contains 18 APIs: 3 authentication APIs and 15 project-specific APIs.

### A. Authentication APIs

| ID | Method | Endpoint | Description |
|---|---|---|---|
| A1 | POST | `/auth/register` | Register a new player |
| A2 | POST | `/auth/login` | Login and generate access and refresh tokens |
| A3 | POST | `/auth/refresh` | Generate a new access token |

### B. Project-Specific APIs

| ID | Method | Endpoint | Access | Description |
|---|---|---|---|---|
| E1 | POST | `/admin/mission-managers` | Admin | Create a mission manager account |
| E2 | POST | `/missions` | Mission Manager | Create a new mission |
| E3 | GET | `/missions` | All | Get all available missions |
| E4 | GET | `/missions/{mission_id}` | All | Get details of a mission |
| E5 | PATCH | `/missions/{mission_id}` | Mission Manager | Update mission details or availability |
| E6 | POST | `/missions/{mission_id}/accept` | Player | Accept a mission |
| E7 | GET | `/players/me/missions` | Player | Get accepted missions |
| E8 | POST | `/missions/{mission_id}/complete` | Player | Submit mission completion details |
| E9 | PATCH | `/completions/{completion_id}/review` | Mission Manager | Approve or reject completion |
| E10 | GET | `/players/me/history` | Player | Get completed mission history |
| E11 | POST | `/rewards` | Mission Manager | Create a reward |
| E12 | GET | `/rewards` | All | Get available rewards |
| E13 | POST | `/rewards/assign` | Mission Manager | Assign a reward to a player |
| E14 | GET | `/leaderboard` | All | Get player rankings |
| E15 | GET | `/players/{player_id}/profile` | All | Get player profile and statistics |

*The project-specific endpoint paths and HTTP methods are the proposed API design for this project.*

## 6. User Roles

| Role | Responsibilities |
|---|---|
| Admin | Manage mission managers and platform activities |
| Mission Manager | Create missions, manage availability and verify completion |
| Player | Accept missions, submit completion details and earn rewards |

New registrations receive the player role by default. Only admins can create mission manager accounts.

## 7. Database Design

The application uses SQLite for storing application data.

Planned database tables:

| Table | Purpose |
|---|---|
| users | Store user details, passwords and roles |
| missions | Store mission details and availability |
| player_missions | Store missions accepted by players |
| completions | Store submitted mission completion details |
| rewards | Store mission rewards |
| player_rewards | Store rewards assigned to players |

## 8. Reward System

Players earn experience points (XP) after their mission completion is approved.

| Mission Difficulty | Experience Points |
|---|---:|
| Easy | 50 XP |
| Medium | 100 XP |
| Hard | 200 XP |
| Special | 500 XP |

The leaderboard ranks players based on their accumulated experience points.

## 9. Docker Deployment

The application is containerized using Docker and runs on port `8001`.

### Build Docker Image

```bash
docker build -t gta-backend .
```

### Run Docker Container

```bash
docker run -d --name gta-backend -p 8001:8001 gta-backend
```

## 10. AWS Deployment

The backend application is deployed on an AWS EC2 instance using Docker.

- AWS EC2 is used to host the backend.
- Docker runs the FastAPI application inside a container.
- Port `8001` is exposed to access the API.
- SQLite data is intended to be persisted using a mounted directory.

## 11. CI/CD Pipeline

GitHub Actions is used to automate the deployment process.

The pipeline performs the following steps:

1. Detects code changes pushed to the GitHub repository.
2. Builds the Docker image.
3. Pushes the image to Docker Hub.
4. Connects to the AWS EC2 instance.
5. Pulls the latest Docker image.
6. Replaces the existing running container with the updated container.

GitHub Secrets are used to securely store Docker Hub credentials and EC2 SSH access details.

## 12. Development Progress

| Component | Status |
|---|---|
| A1 – Player Registration | Completed |
| A2 – Login | Completed |
| A3 – Refresh Token | Completed |
| E1 – Create Mission Manager | In Progress |
| E2–E15 – Project APIs | Pending |
| Docker Setup | Completed |
| AWS EC2 Deployment | Completed |
| GitHub Actions CI/CD | Configured |

## 13. Future Improvements

- Complete all 15 project-specific APIs.
- Implement role-based access control for all protected endpoints.
- Complete mission completion and reward workflows.
- Implement player profiles and leaderboard functionality.
- Complete and test automated CI/CD deployment.
