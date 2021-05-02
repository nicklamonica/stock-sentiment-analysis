import yaml
import sys
import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from models.lstm import Lstm
from models.gru import Gru


def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return None


def main(args):
    if args[0] == "train":
        train_models()
    else:
        predict()


def predict():
    # get real data
    # load models
    # use loaded models to predict data
    pass

def train_models():
    # read data
    df = pd.read_csv("apis/tweet_data.csv")

    # sample data
    df = df.sample(frac=1).reset_index(drop=True)

    # clean tweet text
    df['Text'] = df['Text'].apply(lambda x: x.lower())  # transform text to lowercase
    df['Text'] = df['Text'].apply(lambda x: re.sub('[^a-zA-z0-9\s]', '', x))
    print(df.shape)

    # X as tokenize data
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(df['Text'].values)
    X = tokenizer.texts_to_sequences(df['Text'].values)
    X = pad_sequences(X)
    print("X tokenized data = ", X[:5])

    # Y as buckets of Sentiment column
    y = pd.get_dummies(df['Sentiment']).values
    [print(df['Sentiment'][i], y[i]) for i in range(0, 5)]

    # split data into sample and
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


    # LSTM MODEL TRAINING
    # create rnn with lstm cells
    lstm = Lstm()
    lstm.build_model(X.shape[1])

    # train model
    lstm.train(X_train, y_train)

    # save model
    lstm.save("lstm_model")
    # make predictions on test data
    predictions = lstm.predict(X_test)
    # determine accuracy of predictions

    # GRU MODEL TRAINING
    gru = Gru()
    gru.build_model(X.shape[1])

    # train model
    gru.train(X_train, y_train)

    # save model
    gru.save("gru_model")
    # make predictions on test data
    predictions = gru.predict(X_test)
    # determine accuracy of predicionts

    # # plot average predictions
    # avg_neg = np.mean([prediction[0] for prediction in predictions])
    # avg_pos = np.mean([prediction[1] for prediction in predictions])
    # print(f"Average negative sentiment score = {avg_neg}\nAverage positive sentiment score = {avg_pos}")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        print("missing command line arguments, check README")
    else:
        main(args)
