import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import random


def open_pkl(pkl_name):
    with open(pkl_name, 'br') as f: # br - открытие байтового файла (обученной модели)
        model = pickle.load(f)
        return model


def open_json(json_name):
    with open (json_name, 'r', encoding="utf8") as f:
        data = json.load(f)
        return data


def all_info_intends(json_name):
    examples_responses = []
    intents = []
    data = open_json(json_name)
    for intent in data:
        for example in data[intent]['examples']:
            examples_responses.append(example)
            intents.append(intent)
        for response in data[intent]['responses']:
            examples_responses.append(response)
            intents.append(intent)
    return examples_responses

# model = MLPClassifier()
# model.fit(examples_responses, intents) обучение модели, обучение прощло, модель сохранена


def create_vektor(json_name):
    vectorizer = CountVectorizer()
    vectorizer.fit(all_info_intends(json_name))
    return vectorizer


def get_intent(text,json_name, pkl_name):
    model = open_pkl(pkl_name)
    text_vec = create_vektor(json_name).transform([text])  # поэтому текст оформляем как список из одного элемента
    return model.predict(text_vec)[0]


def get_response(intent):
    data = open_json('mashing_learning/intents_dataset.json')
    return random.choice(data[intent]['responses'])


# with open('model.pkl', 'wb') as f:  сохранение обученной модели
#     pickle.dump(model, f)