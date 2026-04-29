from tensorflow.keras.models import Sequential
model=Sequential()

import pickle
with open("model.pkl","rb") as file:
    model=pickle.load(file)

from Pre_Processing import for_cleaning,for_padding,for_tokenization    
def predict(msg:str):
    clean_msg=for_cleaning.clean_text(msg)
    tokenized_msg=for_tokenization.func(clean_msg)
    padded_tokenized_msg=for_padding.func(tokenized_msg)
    prediction=model.predict(padded_tokenized_msg)
    return prediction[0][0], "Spam" if (prediction[0][0]>0.4) else "Ham"
    