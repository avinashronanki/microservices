#https://www.youtube.com/watch?v=GQ6OT2HyfPs
import pandas as pd
import numpy as np
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cluster
# nltk.download('stopwords')
stemmer = PorterStemmer()
sw = stopwords.words('english')


def tokenizer(keyword):
    return [stemmer.stem(w) for w in keyword.split()]


keywords = [
    'campaign building',
    'ppc campaign generator',
    'how to build ppc campaigns',
    'how do you group keywords',
    'how to group keywords',
    'keyword grouper',
    'keyword grouping software',
    'ppc campaign builder',
    'best software to group keywords'
]

tfidf = TfidfVectorizer(tokenizer=tokenizer, stop_words=sw)
X = pd.DataFrame(tfidf.fit_transform(keywords).toarray(),
                 index=keywords, columns=tfidf.get_feature_names())
c = cluster.AffinityPropagation()
pred = c.fit_predict(X)
