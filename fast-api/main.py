from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()


# Load patient data from JSON file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


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

    return {
        "patients": data
    }


# View a specific patient
@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient to retrieve",
        example="P001"
    )
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
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
    
    # Fields allowed for sorting
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

    # Check if sort field is valid
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

    # Load data
    data = load_data()

    # Sort patients
    sorted_data = sorted(
        data.values(),
        key=lambda patient: patient[sort_by],
        reverse=(order == "desc")
    )

    return {
        "patients": sorted_data
    }