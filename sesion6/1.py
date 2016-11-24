import os
CORPUS_PATH = os.path.join('data', 'austen-bronte-split')
filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])
print(len(filenames))

import numpy as np
import sklearn.feature_extraction.text as text
vectorizer = text.CountVectorizer(input='filename', stop_words='english', min_df=1)
dtm = vectorizer.fit_transform(filenames).toarray()
vocab = np.array(vectorizer.get_feature_names())
print(vocab)

from sklearn import decomposition
num_topics = 20
num_top_words = 20
clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)
topic_words = []
for topic in clf.components_:
    word_idx = np.argsort(topic)[::-1][0:num_top_words]
    a = np.argsort(topic)
    b = a[::-1]
    c = b[0:num_top_words]
    topic_words.append([vocab[i] for i in word_idx])
doctopic = doctopic / np.sum(doctopic, axis=1, keepdims=True)
print(topic_words)
