import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer=Tokenizer()
with open("tokenizer.pkl","rb") as file:
    tokenizer=pickle.load(file)
def func(message):
    tokenized_message=tokenizer.texts_to_sequences([message])
    return(tokenized_message)
