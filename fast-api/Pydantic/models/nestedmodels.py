from pydantic import BaseModel

class address(BaseModel): 
    street: str
    city: str
    state: str
    zip_code: str   



class patient(BaseModel):
    
    name: str
    age: int
    gender: str
    address: address
   

address1=address(
    street="123 Main St",
    city="Anytown",
    state="CA",
    zip_code="12345"
)   

patient1=patient(
    name="John Doe",
    age=30,
    gender="Male",
    address=address1
)


# print(patient1)
# print(patient1.address.city)  # Accessing nested model attribute    
# print(patient1.dict())  # Convert to dictionary
# print(patient1.json())  # Convert to JSON string
# print(patient1.schema())  # Get the schema of the model
print(patient1.dict(exclude={"address"}))  # Exclude nested model from dictionary