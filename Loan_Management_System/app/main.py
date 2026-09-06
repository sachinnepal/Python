from fastapi import FastAPI
from app.routers.loans import router as loan_router


app = FastAPI(
    title="Loan Management System",
    description="A learning project built with FastAPI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Loan Management System API is running"
    }


app.include_router(loan_router)