from tensorflow.keras.models import Sequential

class Rnn:

    def __init__(self):
        self.model = Sequential()

    # input_length = X.shape[1]
    def build_model(self, input_length):
        pass

    def train(self, x_train, y_train, epochs=8, batch_size=32):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=2)

    def predict(self, x):
        return self.model.predict(x)

    def save(self):
        self.model.save("lstm_model.h5", overwrite=True)
