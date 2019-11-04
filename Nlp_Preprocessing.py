import operator

import nltk
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import json
import os
import collections

def get_data():

    with open("C:\\Users\\Trika\\Desktop\\ScrapyProjectExample\\tutorial\\example.json") as json_file:
        data = json.load(json_file)
    print(len(data)/2)
    dict_to_dataframe(data)


def dict_to_dataframe(data):
    dfTitles = pd.DataFrame()
    dfLinks = pd.DataFrame()
    title_keys = []
    link_keys = []
    titles = []
    links = []
    length = (len(data)/2).__int__()
    for i in range(0,length):
        dictTemp = data[i]
        for k,v in dictTemp.items():
            title_keys.append(k)
            titles.append(v)
    for i in range(length,len(data)):
        dictTemp = data[i]
        for k, v in dictTemp.items():
            link_keys.append(k)
            links.append(v)

    dfTitles['numOftitle'] = title_keys
    dfTitles['titles'] = titles
    dfLinks['numOfLink'] = link_keys
    dfLinks['links'] = links
    print(dfTitles)
    print(dfLinks)
    dfTitles['titles'] = stopwords_removal(dfTitles['titles'])

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


    print(sentences)
get_data()