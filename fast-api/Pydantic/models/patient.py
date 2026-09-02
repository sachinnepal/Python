from typing import Annotated
from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    computed_field,
    field_validator,
    model_validator,
)

from validators.patient_validators import (
    validate_email_domain,
    capitalize_name,
)


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=100)]
    email: EmailStr
    url: AnyUrl

    age: Annotated[int, Field(gt=0, lt=50)]
    weight: Annotated[float, Field(gt=0, strict=True)]

    married: bool = False
    allergies: list[str] | None = None
    contact_details: dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        height = 1.75
        return self.weight / (height**2)

    @field_validator("email", mode="before")
    @classmethod
    def email_validator(cls, value):
        return validate_email_domain(value)

    @field_validator("name")
    @classmethod
    def name_validator(cls, value):
        return capitalize_name(value)

    @model_validator(mode="after")
    def married_age_validator(self):
        if self.married and self.age < 18:
            raise ValueError("Married patients must be at least 18.")
        return self