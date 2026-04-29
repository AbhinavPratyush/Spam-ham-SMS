**# Spam-ham-SMS**
this is built to act as an API that will communicate with my another repository and works with coherence.
How to run it combinely with another spam repository is the main agenda of this repo.

**python version used 3.8.10**
dataset link: https://www.kaggle.com/datasets/junioralive/india-spam-sms-classification

##libraries used
* pydantic
* fastapi
* tensorflow
* numpy
* sklearn
* b4s
* uvicorn

##how to run 

assuming you have everything downloaded prehand

  <uvicorn app:app --reload>

this may or may not work for you in my system there was an error sometimes, so use this 

  <python -m uvicorn app:app --reload>


##some key points
* try not to save the deep learning model in pkl use file_model.keras instead
* using pydantic you dont need to define constructors
* pydantic models are accepted by fast api only
