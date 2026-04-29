import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Pre_Processing import for_cleaning,for_padding,for_tokenization
# i am going to load the pickle file model and test it myself here

from tensorflow.keras.models import Sequential
model=Sequential()

import pickle as pkl
with open("model.pkl","rb") as f:
    model=pkl.load(file=f)

data=input("Enter an sms here: ")

print(data," before cleaning \n ")
data=for_cleaning.clean_text(data)
print(data," before rokenization \n")
data=for_tokenization.func(data)
print(data," before pading \n")
data=for_padding.func(data)
print(data)
print(model.predict(data))