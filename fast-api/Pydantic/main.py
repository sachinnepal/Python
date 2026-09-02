from models.patient import Patient
from services.patient_service import insert_patient

patient_info = {
    "name": "sachin nepal",
    "email": "sachin.nepal@nabil.com",
    "url": "http://sachin.nepal@nabil.com",
    "age": 25,
    "weight": 70.0,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_details": {
        "email": "sachin.nepal@nabil.com",
        "phone": "123-456-7890",
    },
}

patient = Patient(**patient_info)
insert_patient(patient)