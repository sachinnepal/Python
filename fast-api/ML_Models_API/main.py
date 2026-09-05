from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
import pickle
import pandas as pd
from fastapi.responses import JSONResponse
from typing import Literal, Annotated


# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
    print(model)
    preprocessor = model.named_steps["preprocessor"]

encoder = preprocessor.named_transformers_["cat"]

print("Categories:")
for column, categories in zip(
    ["age_group", "lifestyle_risk", "occupation", "city_tier"],
    encoder.categories_
):
    print(column, "=>", categories)


app = FastAPI()


tier_1_cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Pune"
]


tier_2_cities = [
    "Jaipur",
    "Chandigarh",
    "Indore",
    "Lucknow",
    "Patna",
    "Ranchi",
    "Visakhapatnam",
    "Coimbatore",
    "Bhopal",
    "Nagpur",
    "Vadodara",
    "Surat",
    "Rajkot",
    "Jodhpur",
    "Raipur",
    "Amritsar",
    "Varanasi",
    "Agra",
    "Dehradun",
    "Mysore",
    "Jabalpur",
    "Guwahati",
    "Thiruvananthapuram",
    "Ludhiana",
    "Nashik",
    "Allahabad",
    "Udaipur",
    "Aurangabad",
    "Hubli",
    "Belgaum",
    "Salem",
    "Vijayawada",
    "Tiruchirappalli",
    "Bhavnagar",
    "Gwalior",
    "Dhanbad",
    "Bareilly",
    "Aligarh",
    "Gaya",
    "Kozhikode",
    "Warangal",
    "Kollhapur",
    "Bilaspur",
    "Jalandhar",
    "Noida",
    "Guntur",
    "Asansol",
    "Siliguri"
]


class UserInput(BaseModel):

    age: Annotated[
        int,
        Field(..., gt=0, lt=100)
    ]

    weight: Annotated[
        float,
        Field(..., gt=0, lt=200)
    ]

    height: Annotated[
        float,
        Field(..., gt=0, lt=3)
    ]

    income_lpa: Annotated[
        float,
        Field(..., gt=0)
    ]

    smoker: Annotated[
        bool,
        Field(...)
    ]

    city: Annotated[
        str,
        Field(...)
    ]

    occupation: Annotated[
        Literal[
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job"
        ],
        Field(...)
    ]


    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


    @computed_field
    @property
    def lifestyle_risk(self) -> str:

        if self.smoker and self.bmi > 30:
            return "high"

        elif self.smoker or self.bmi > 27:
            return "medium"

        else:
            return "low"


    @computed_field
    @property
    def age_group(self) -> str:

        if self.age < 25:
            return "young"

        elif self.age < 45:
            return "adult"

        elif self.age < 60:
            return "middle-aged"

        else:
            return "senior"


    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3


@app.post("/predict")
def predict(user_input: UserInput):

    input_df = pd.DataFrame([{
        "bmi": user_input.bmi,
        "lifestyle_risk": user_input.lifestyle_risk,
        "age_group": user_input.age_group,
        "city_tier": user_input.city_tier,
        "income_lpa": user_input.income_lpa,
        "occupation": user_input.occupation
    }])

    prediction = model.predict(input_df)

    return JSONResponse(
        status_code=200,
        content={
            "predicted_category": prediction[0]
        }
    )