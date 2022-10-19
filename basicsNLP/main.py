import json
import requests
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
import main_functions
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from pprint import pprint
#from wordcloud import WordCloud
import matplotlib.pyplot as plt
#nltk.download("punkt")
#nltk.download("stopwords")
#
#url ="https://api.nytimes.com/svc/topstories/v2/arts.json?api-key="
#api_key = main_functions.read_from_file("JSON_Files/api_key.json")
#final_url = url + api_key["my_key"]
#response = requests.get(final_url).json()
#
#main_functions.save_to_file(response, "JSON_Files/response.json")

my_articles = main_functions.read_from_file("JSON_Files/response.json")
#pprint(my_articles)
str1=""
for i in my_articles["results"]:
    str1 = str1 + i["abstract"]

print(str1)

sentence = sent_tokenize(str1)
print(len(sentence))
print(sentence)

words = word_tokenize(str1)
print(len(words))
print(words)

fdist = FreqDist(words)

print(fdist.most_common(10))       #Frequency distribution, will return 10 most common words

words_no_punc = []
for w in words:
    if w.isalpha():                 #isAlpha method checks if a str is punctuation
        words_no_punc.append(w.lower())
print(words_no_punc)

fdist2 = FreqDist(words_no_punc)
pprint(fdist2.most_common(10))
stopwords = stopwords.words("english")

print(stopwords)
clean_words=[]

for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)

print(len(clean_words))
fdist3 = FreqDist(clean_words)
pprint(fdist3.most_common(10))

