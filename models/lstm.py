from models.rnn import Rnn

from tensorflow.keras.layers import Dense, Dropout, LSTM, Embedding

class Lstm(Rnn):

    def __init__(self):
        super().__init__()

    def build_model(self, input_length):
        # input_length = X.shape[1]
        self.model.add(Embedding(5000, 256, input_length=input_length))
        self.model.add(Dropout(0.3))
        self.model.add(LSTM(256, return_sequences=True, dropout=0.3, recurrent_dropout=0.2))
        self.model.add(LSTM(256, dropout=0.3, recurrent_dropout=0.2))
        self.model.add(Dense(2, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.summary()
