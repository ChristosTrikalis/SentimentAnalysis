import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
# import tensorflow

class Preprocessing:
    def get_data(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
        self.dict_to_dataframe(data)

    def dict_to_dataframe(self, data):
        titles_and_links = pd.DataFrame()
        titles = []
        links = []
        dates = []
        length = len(data)
        print(length)
        for p in range(length - 1):
            values = list(data[p].values())
            titles.append(values[0])
            dates.append(values[1])
            links.append(values[2])

        titles_and_links['titles'] = titles  # fills first column with titles
        titles_and_links['links'] = links  # fills second column with links
        titles_and_links['datetime'] = dates
        self.debug(titles_and_links)

    @staticmethod
    def debug(data):
        with pd.option_context('display.max_rows', 25, 'display.max_columns', 63):
            print(data.head())

    @staticmethod
    def stopwords_removal_and_canonicalization(data):
        stop_words = set(stopwords.words('english'))
        sentences = []
        import string
        for i in data:
            result = i.translate(str.maketrans('', '', string.punctuation))
            word_tokens = word_tokenize(result)
            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words:
                    filtered_sentence.append(w)
            sentences.append(filtered_sentence)
        return sentences
