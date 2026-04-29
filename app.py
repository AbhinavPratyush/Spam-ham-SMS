from user_schema.userSchema import User_Input
from Prediction.pred_mod import predict
from user_schema.responseSchema import Response_schema
from fastapi import FastAPI

app=FastAPI()


@app.post("/prediction",response_model=Response_schema)
def anyfunc(userinput:User_Input):
    inputMsg=userinput.message
    
    try :
        a,b=predict(inputMsg)
    except Exception as e:
        a=0
        b="Invalid"
    response=Response_schema(
        prediction=a,
        label=b
    ) 
    return response