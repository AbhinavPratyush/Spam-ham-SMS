import pickle
with open("tokenizer.pkl","r") as file:
    tokenizer=pickle.dumps(file)
print(tokenizer.word_index)