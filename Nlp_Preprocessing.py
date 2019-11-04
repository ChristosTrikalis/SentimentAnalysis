import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json

def get_data():
    with open("C:\\Users\\Trika\\Desktop\\ScrapyProjectExample\\tutorial\\example.json") as json_file:
        data = json.load(json_file)
    print(len(data)/2)
    dict_to_dataframe(data)

def dict_to_dataframe(data):
    titles_and_links = pd.DataFrame()
    titles = []
    links = []
    length = (len(data)/2).__int__()

    for i in range(0,length):
        dictTemp1 = data[i]
        dictTemp2 = data[i+length]
        for k,v in dictTemp1.items():
            titles.append(v)
        for k,v in dictTemp2.items():
            links.append(v)

    titles_and_links['titles'] = titles                                        #fills first column with titles
    titles_and_links['links'] = links                                          #fills second column with links
    print(titles_and_links)                                                  #debugging
    titles_and_links['titles'] = stopwords_removal(titles_and_links['titles'])

def stopwords_removal(data):
    stop_words = set(stopwords.words('english'))
    sentences = []

    for i in data:
        word_tokens=word_tokenize(i)
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        sentences.append(filtered_sentence)

get_data()