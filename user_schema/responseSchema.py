from pydantic import BaseModel

class Response_schema(BaseModel):
    label:str
    prediction:float
    # confidence:float
    
        