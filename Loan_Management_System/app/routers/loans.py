from fastapi import APIRouter,HTTPException
from app.schemas.loan import LoanCreate,LoanUpdate,LoanResponse,MessageResponse
from app.data.loans import loans


router = APIRouter()



@router.get("/loans", response_model=list[LoanResponse])
def get_loans():
    return loans


@router.get("/loans/search", response_model=list[LoanResponse])
def search_loans(customer_name: str | None = None):
    if customer_name is None:
        return loans

    results = []

    for loan in loans:
        if customer_name.lower() in loan["customer_name"].lower():
            results.append(loan)

    return results


@router.get("/loans/{loan_id}", response_model=LoanResponse)
def get_loan(loan_id: int):
    for loan in loans:
        if loan["id"] == loan_id:
            return loan

    raise HTTPException(
        status_code=404,
        detail="Loan not found"
    )


@router.post("/loans", response_model=LoanResponse)
def create_loan(loan: LoanCreate):
    loan_data = loan.model_dump()
    loan_data["id"] = len(loans) + 1
    loans.append(loan_data)

    return loan_data


@router.put("/loans/{loan_id}", response_model=LoanResponse)
def update_loan(loan_id: int, updated_loan: LoanUpdate):
    for loan in loans:
        if loan["id"] == loan_id:
            loan.update(updated_loan)
            return loan

    raise HTTPException(
        status_code=404,
        detail="Loan not found"
    )


@router.delete("/loans/{loan_id}", response_model=MessageResponse)
def delete_loan(loan_id: int):
    for loan in loans:
        if loan["id"] == loan_id:
            loans.remove(loan)

            return {
                "message": "Loan deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Loan not found"
    )