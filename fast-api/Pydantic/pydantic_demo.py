from typing import Annotated
from pydantic import (
    AnyUrl,
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    model_validator,
    computed_field,  # 1. Imported computed_field
)


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            ...,
            max_length=100,
            title="Patient Name",
            description="Name of the patient",
        ),
    ]

    email: EmailStr
    url: AnyUrl

    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=50,
            title="Age",
            description="Age of the patient in years",
        ),
    ]
    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            strict=True,
            title="Weight",
            description="Weight of the patient in kilograms",
        ),
    ]

    married: Annotated[
        bool | None,
        Field(
            default=False,
            title="Married",
            description="Whether the patient is married",
        ),
    ]
    allergies: Annotated[
        list[str] | None,
        Field(
            default=None,
            title="Allergies",
            description="List of patient allergies",
        ),
    ]
    contact_details: Annotated[
        dict[str, str],
        Field(
            ...,
            title="Contact Details",
            description="Contact details of the patient",
        ),
    ]

    # 2. Added @property so Pydantic treats this as a standard field
    @computed_field(title="BMI", description="Body Mass Index of the patient")
    @property
    def bmi(self) -> float:
        """Calculates the Body Mass Index (BMI) of the patient."""
        height_m = 1.75  # Assuming a fixed height for demonstration
        return self.weight / (height_m ** 2)
        
    @field_validator("email", mode="before")
    @classmethod
    def validate_email(cls, value: str) -> str:
        valid_domains = ["nabil.com", "gibl.com"]
        domain = value.split("@")[-1]

        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value

    @field_validator("name")
    @classmethod
    def capital_name(cls, value: str) -> str:
        return value.upper()

    # Fixed syntax for Pydantic v2 'after' model validator (uses self)
    @model_validator(mode="after")
    def validate_model(self) -> "Patient":
        if self.married and self.age < 18:
            raise ValueError("Married patients must be at least 18 years old.")
        return self


def insert_patient(patient: Patient) -> None:
    allergies_str = (
        ", ".join(patient.allergies) if patient.allergies else "None"
    )

    print(
        f"Inserting patient: {patient.name}\n"
        f"URL: {patient.url}\n"
        f"Age: {patient.age}\n"
        f"Weight: {patient.weight} kg\n"
        f"BMI: {patient.bmi:.2f}\n"  # Output the computed BMI formatted to 2 decimals
        f"Married: {patient.married}\n"
        f"Allergies: {allergies_str}\n"
        f"Contact Email: {patient.contact_details.get('email', 'N/A')}\n"
        f"Contact Phone: {patient.contact_details.get('phone', 'N/A')}\n"
        f"Email: {patient.email}\n"
    )


patient_info = {
    "name": "sachin nepal",
    "email": "sachin.nepal@nabil.com",
    "url": "http://sachin.nepal@nabil.com",
    "age": "25",  # 3. Changed from 17 to 25 so the married validation passes
    "weight": 70.0,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_details": {
        "email": "sachin.nepal@nabil.com",
        "phone": "123-456-7890",
    },
}

patient1 = Patient(**patient_info)
insert_patient(patient1)