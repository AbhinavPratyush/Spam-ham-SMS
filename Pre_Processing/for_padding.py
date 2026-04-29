from tensorflow.keras.preprocessing.sequence import pad_sequences
def func(input_list):
        padded_input=pad_sequences(input_list,maxlen=153,padding='pre')
        return padded_input