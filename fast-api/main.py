from fastapi import FastAPI, Path, HTTPException, Query
import json

from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional


app = FastAPI()


# ============================================================
# PATIENT MODEL
# ============================================================

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
        str,
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

    # ========================================================
    # COMPUTED BMI
    # ========================================================

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    # ========================================================
    # COMPUTED VERDICT
    # ========================================================

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


# ============================================================
# PATIENT UPDATE MODEL
# ============================================================

class PatientUpdate(BaseModel):

    name: Annotated[
        Optional[str],
        Field(
            default=None,
            description="The name of the patient",
            examples=["John Doe"]
        )
    ]

    age: Annotated[
        Optional[int],
        Field(
            default=None,
            gt=0,
            lt=50,
            description="The age of the patient",
            examples=[30]
        )
    ]

    gender: Annotated[
        Optional[Literal["Male", "Female", "Other"]],
        Field(
            default=None,
            description="The gender of the patient",
            examples=["Male"]
        )
    ]

    city: Annotated[
        Optional[str],
        Field(
            default=None,
            description="The city where the patient resides",
            examples=["Kathmandu"]
        )
    ]

    height: Annotated[
        Optional[float],
        Field(
            default=None,
            gt=0,
            description="The height of the patient in meters",
            examples=[1.75]
        )
    ]

    weight: Annotated[
        Optional[float],
        Field(
            default=None,
            gt=0,
            description="The weight of the patient in kilograms",
            examples=[70.0]
        )
    ]


# ============================================================
# LOAD DATA
# ============================================================

def load_data():

    with open("patients.json", "r") as f:
        return json.load(f)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def hello():

    return {
        "message": "PATIENT MANAGEMENT SYSTEM"
    }


# ============================================================
# ABOUT
# ============================================================

@app.get("/about")
def about():

    return {
        "message": "This is a Patient Management System for managing patient records."
    }


# ============================================================
# VIEW ALL PATIENTS
# ============================================================

@app.get("/view")
def view_patients():

    data = load_data()

    patients = [
        Patient(
            id=patient_id,
            **patient_data
        )
        for patient_id, patient_data in data.items()
    ]

    return {
        "patients": patients
    }


# ============================================================
# VIEW ONE PATIENT
# ============================================================

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

    patient = Patient(
        id=patient_id,
        **data[patient_id]
    )

    return patient


# ============================================================
# SORT PATIENTS
# ============================================================

@app.get("/sort")
def sort_patients(

    sort_by: str = Query(
        ...,
        description="The field to sort patients by",
        examples=["age"]
    ),

    order: str = Query(
        "asc",
        description="The order of sorting: asc or desc",
        examples=["asc"]
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

    # Check sort field
    if sort_by not in valid_fields:

        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}"
        )

    # Check sorting order
    if order not in ["asc", "desc"]:

        raise HTTPException(
            status_code=400,
            detail="Order must be 'asc' or 'desc'"
        )

    data = load_data()

    patients = [
        Patient(
            id=patient_id,
            **patient_data
        )
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


# ============================================================
# ADD PATIENT
# ============================================================

@app.post("/add")
def add_patient(patient: Patient):

    data = load_data()

    # Check if patient ID already exists
    if patient.id in data:

        raise HTTPException(
            status_code=400,
            detail="Patient with this ID already exists"
        )

    # Store only actual patient data
    # ID is used as the dictionary key
    data[patient.id] = {

        "name": patient.name,

        "age": patient.age,

        "gender": patient.gender,

        "city": patient.city,

        "height": patient.height,

        "weight": patient.weight
    }

    # Save data
    with open("patients.json", "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )

    return {
        "message": "Patient added successfully",
        "patient": patient
    }


# ============================================================
# UPDATE PATIENT
# ============================================================

@app.put("/update/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):

    data = load_data()

    # --------------------------------------------------------
    # Check if patient exists
    # --------------------------------------------------------

    if patient_id not in data:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    # --------------------------------------------------------
    # Update only fields provided by the user
    # --------------------------------------------------------

    update_data = patient_update.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():

        data[patient_id][field] = value

    # --------------------------------------------------------
    # Create Pydantic object
    #
    # BMI and verdict are calculated automatically
    # --------------------------------------------------------

    patient_pydantic_object = Patient(
        id=patient_id,
        **data[patient_id]
    )

    # --------------------------------------------------------
    # Save ONLY actual patient information
    #
    # Do NOT save:
    # id
    # bmi
    # verdict
    # --------------------------------------------------------

    data[patient_id] = {

        "name": patient_pydantic_object.name,

        "age": patient_pydantic_object.age,

        "gender": patient_pydantic_object.gender,

        "city": patient_pydantic_object.city,

        "height": patient_pydantic_object.height,

        "weight": patient_pydantic_object.weight
    }

    # --------------------------------------------------------
    # Save updated data to JSON
    # --------------------------------------------------------

    with open("patients.json", "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )

    # --------------------------------------------------------
    # Return updated patient
    # --------------------------------------------------------

    return {

        "message": "Patient updated successfully",

        "patient": patient_pydantic_object
    }

@app.delete("/delete/{patient_id}")
def delete_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient to delete",
        examples=["P001"]
    )
):

    data = load_data()

    if patient_id not in data:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    # Delete patient
    del data[patient_id]

    # Save updated data to JSON
    with open("patients.json", "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )

    return {
        "message": "Patient deleted successfully"
    }