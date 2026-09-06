from fastapi import FastAPI

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


loans = [
    {
        "id": 1,
        "customer_name": "John Doe",
        "amount": 100000,
        "interest_rate": 12,
        "term_months": 12
    },
    {
        "id": 2,
        "customer_name": "Jane Smith",
        "amount": 250000,
        "interest_rate": 10,
        "term_months": 24
    }
]


@app.get("/loans")
def get_loans():
    return loans


@app.get("/loans/search")
def search_loans(customer_name: str | None = None):
    if customer_name is None:
        return loans

    results = []

    for loan in loans:
        if customer_name.lower() in loan["customer_name"].lower():
            results.append(loan)

    return results


@app.get("/loans/{loan_id}")
def get_loan(loan_id: int):
    for loan in loans:
        if loan["id"] == loan_id:
            return loan

    return {
        "message": "Loan not found"
    }


@app.post("/loans")
def create_loan(loan: dict):
    loan["id"] = len(loans) + 1
    loans.append(loan)

    return loan


@app.put("/loans/{loan_id}")
def update_loan(loan_id: int, updated_loan: dict):
    for loan in loans:
        if loan["id"] == loan_id:
            loan.update(updated_loan)
            return loan

    return {
        "message": "Loan not found"
    }