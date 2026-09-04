from fastapi import FastAPI, Path, HTTPException, Query
import json

from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal


app = FastAPI()


class Patient(BaseModel):

    id: Annotated[
        str,
        Field(
            ...,
            description="The unique identifier for the patient",
            examples=["P001"]
        )
    ]

    name: Annotated[
        str,
        Field(
            ...,
            description="The name of the patient",
            examples=["John Doe"]
        )
    ]

    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=50,
            description="The age of the patient",
            examples=[30]
        )
    ]

    gender: Annotated[
        Literal["Male", "Female", "Other"],
        Field(
            ...,
            description="The gender of the patient",
            examples=["Male"]
        )
    ]

    city: Annotated[
        Literal["Kathmandu", "Pokhara", "Lalitpur"],
        Field(
            ...,
            description="The city where the patient resides",
            examples=["Kathmandu"]
        )
    ]

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="The height of the patient in meters",
            examples=[1.75]
        )
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="The weight of the patient in kilograms",
            examples=[70.0]
        )
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal weight"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obesity"


# Load patient data
def load_data():
    with open("patients.json", "r") as f:
        return json.load(f)


# Home
@app.get("/")
def hello():
    return {
        "message": "PATIENT MANAGEMENT SYSTEM"
    }


# About
@app.get("/about")
def about():
    return {
        "message": "This is a Patient Management System for managing patient records."
    }


# View all patients
@app.get("/view")
def view_patients():

    data = load_data()

    patients = [
        Patient(id=patient_id, **patient_data)
        for patient_id, patient_data in data.items()
    ]

    return {
        "patients": patients
    }


# View a specific patient
@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient to retrieve",
        examples=["P001"]
    )
):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return Patient(
        id=patient_id,
        **data[patient_id]
    )


# Sort patients
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="The field to sort patients by"
    ),
    order: str = Query(
        "asc",
        description="The order of sorting: asc or desc"
    )
):

    valid_fields = [
        "name",
        "age",
        "gender",
        "city",
        "height",
        "weight",
        "bmi",
        "verdict"
    ]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be 'asc' or 'desc'"
        )

    data = load_data()

    patients = [
        Patient(id=patient_id, **patient_data)
        for patient_id, patient_data in data.items()
    ]

    sorted_data = sorted(
        patients,
        key=lambda patient: getattr(patient, sort_by),
        reverse=(order == "desc")
    )

    return {
        "patients": sorted_data
    }


# Add patient
@app.post("/add")
def add_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient with this ID already exists"
        )

    # Store only actual input fields
    data[patient.id] = {
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "city": patient.city,
        "height": patient.height,
        "weight": patient.weight
    }

    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)

    return {
        "message": "Patient added successfully",
        "patient": patient
    }