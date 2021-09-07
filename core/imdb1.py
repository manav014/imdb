from textblob import TextBlob
import nltk
from nltk import sent_tokenize, word_tokenize, WordPunctTokenizer
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pprint
from .models import Data

lemmatizer = WordNetLemmatizer()

stopwords_english = stopwords.words('english')

dt = pd.read_csv('IMDB.csv')
[r, c] = dt.shape

dt2_pos = dt[dt['sentiment'] == 'positive']
dt2_neg = dt[dt['sentiment'] == 'negative']
txt_pos = dt2_pos.iloc[:, 0]
txt_neg = dt2_neg.iloc[:, 0]
lst_pos = list(txt_pos.values.flatten())
lst_neg = list(txt_neg.values.flatten())


stopwords_english = stopwords.words('english')
# sample of 1500 reviews
new_wordlist_pos = []
postlist_pos = []
countlist_pos = []
for k in range(100):
    words = nltk.word_tokenize(lst_pos[k])
    new_words = [word for word in words if word.isalnum()]
    new_words2 = [word for word in new_words if word not in stopwords_english]
    ml = len(new_words2)
    new_words1 = []
    for j in range(ml):
        wrd2 = lemmatizer.lemmatize(new_words2[j])
        new_words1.append(wrd2)
    new_wordlist_pos.append(new_words1)
    tagged = nltk.pos_tag(new_words1)
    postlist_pos.append(tagged)
    counts = Counter(tag for word, tag in tagged)
    countlist_pos.append(counts)



new_wordlist_neg = []
postlist_neg = []
countlist_neg = []
for k in range(100):
    words = nltk.word_tokenize(lst_neg[k])
    new_words = [word for word in words if word.isalnum()]
    new_words2 = [word for word in new_words if word not in stopwords_english]
    ml = len(new_words2)
    new_words1 = []
    for j in range(ml):
        wrd2 = lemmatizer.lemmatize(new_words2[j])
        new_words1.append(wrd2)

    new_wordlist_neg.append(new_words1)
    tagged = nltk.pos_tag(new_words1)
    postlist_neg.append(tagged)
    counts = Counter(tag for word, tag in tagged)
    countlist_neg.append(counts)

df_pos_tagged_pos = pd.DataFrame(list(zip(new_wordlist_pos, countlist_pos, postlist_pos)),
                                 columns=['words', 'count', 'poslist'])
dict1 = nltk.defaultdict()
for list in new_wordlist_pos:
    for word in list:
        dict1[word] = dict1.get(word, 0) + 1
tagged = nltk.pos_tag(dict1.keys())
l1 = []
for i in tagged:
    if (i[0] in dict1.keys()):
        l1.append(i[1])

k_pos = [(i, j) for i, j in zip(dict1.items(), l1)]


df_pos_tagged_neg = pd.DataFrame(list(zip(new_wordlist_neg, countlist_neg, postlist_neg)),
                                 columns=['words', 'count', 'poslist'])
dict1 = nltk.defaultdict()
for list in new_wordlist_neg:
    for word in list:
        dict1[word] = dict1.get(word, 0) + 1
tagged = nltk.pos_tag(dict1.keys())
l1 = []
for i in tagged:
    if (i[0] in dict1.keys()):
        l1.append(i[1])

k_neg = [(i, j) for i, j in zip(dict1.items(), l1)]

pprint.pprint(k_neg)




'''
## Dictionary from GITHUB
positive_words = []
negative_words = []
with open('positive-words.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        words = lemmatizer.lemmatize(currentPlace)
        positive_words.append(words)

with open('negative-words.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        words = lemmatizer.lemmatize(currentPlace)
        negative_words.append(words)

pos_words = [w for w in new_words1 if w.lower() in positive_words]
neg_words = [w for w in new_words1 if w.lower() in negative_words]

pos_words_tagged = nltk.pos_tag(pos_words)
neg_words_tagged = nltk.pos_tag(neg_words)
df_pos_tagged = pd.DataFrame(list(zip(pos_words_tagged, neg_words_tagged)),
                   columns =['poswords','negwords'])
df_pos_tagged.head()

'''
