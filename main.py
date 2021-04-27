import yaml
from models.lstm import Lstm

def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return None


def main():
    # create rnn with lstm cells
    lstm = Lstm()
    lstm.build_model()

    # get data

    # split data into train and test

    # train the model
    lstm.train()

    # test the model


if __name__ == '__main__':
    main()
