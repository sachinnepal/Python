from models.patient import Patient


def insert_patient(patient: Patient) -> None:
    allergies = (
        ", ".join(patient.allergies)
        if patient.allergies
        else "None"
    )

    print(
        f"Patient: {patient.name}\n"
        f"Age: {patient.age}\n"
        f"Weight: {patient.weight}\n"
        f"BMI: {patient.bmi:.2f}\n"
        f"Email: {patient.email}\n"
        f"Allergies: {allergies}"
    )