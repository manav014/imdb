from django.utils import timezone
from django.views.generic.list import ListView
from .models import Data
from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields = '__all__'


class ArticleListView(generics.ListAPIView):
    queryset=Data.objects.all()
    def get(self, request, *args, **kwargs):
        if request.GET.get('keyword')=="init":
            from textblob import TextBlob
            import nltk
            from nltk import sent_tokenize, word_tokenize, WordPunctTokenizer
            import pandas as pd
            from collections import Counter
            from nltk.corpus import stopwords
            from nltk.stem import WordNetLemmatizer

            lemmatizer = WordNetLemmatizer()

            stopwords_english = stopwords.words('english')

            dt = pd.read_csv('IMDB.csv')
            [r, c] = dt.shape

            dt2_pos = dt[dt['sentiment'] == 'positive']
            dt2_neg = dt[dt['sentiment'] == 'negative']
            txt_pos = dt2_pos.iloc[:, 0]
            txt_neg = dt2_neg.iloc[:, 0]
            lst_pos = tuple(txt_pos.values.flatten())
            lst_neg = tuple(txt_neg.values.flatten())


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

            df_pos_tagged_pos = pd.DataFrame(tuple(zip(new_wordlist_pos, countlist_pos, postlist_pos)),
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


            df_pos_tagged_neg = pd.DataFrame(tuple(zip(new_wordlist_neg, countlist_neg, postlist_neg)),
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
            for i in k_neg:
                d=Data.objects.create(tag=i[1], word=i[0][1], count=i[0][1])

        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)