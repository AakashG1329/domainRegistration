from fastapi import FastAPI
from deomainRegistration.routers import domain,user,hosting
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)
app.include_router(domain.router)
app.include_router(hosting.router)
