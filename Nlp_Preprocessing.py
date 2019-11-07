import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json

def get_data():
    with open("C:\\Users\\Trika\\Desktop\\ScrapyProjectExample\\tutorial\\example.json") as json_file:
        data = json.load(json_file)
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

    print(titles_and_links.iloc[1,0])                                                    #debugging before text normalization
    titles_and_links['titles'] = stopwords_removal_and_canonicalization(titles_and_links['titles'])
    print("Canonicalization and stop words removal: \n")
    print(titles_and_links.iloc[1,0])                                                    #debugging after text normalization

def stopwords_removal_and_canonicalization(data):
    stop_words = set(stopwords.words('english'))
    sentences = []
    import string
    for i in data:
        result = i.translate(str.maketrans('', '', string.punctuation))
        word_tokens=word_tokenize(result)
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        sentences.append(filtered_sentence)
    return sentences
get_data()