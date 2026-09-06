from pydantic import BaseModel, Field


class LoanCreate(BaseModel):
    customer_name: str
    amount: float = Field(gt=0)
    interest_rate: float = Field(gt=0)
    term_months: int = Field(gt=0)
    purpose: str | None = None

class LoanUpdate(BaseModel):
    customer_name: str
    amount: float = Field(gt=0)
    interest_rate: float = Field(gt=0)
    term_months: int = Field(gt=0)
    purpose: str | None = None

class LoanResponse(BaseModel):
    id: int
    customer_name: str
    amount: float
    interest_rate: float
    term_months: int
    purpose: str | None = None

class MessageResponse(BaseModel):
    message: str