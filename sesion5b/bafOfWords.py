from sklearn.feature_extraction.text import CountVectorizer

filenames = [
    'data/Austen_Emma.txt',
    'data/Austen_Pride.txt',
    'data/Austen_Sense.txt',
    'data/CBronte_Jane.txt',
    'data/CBronte_Professor.txt',
    'data/CBronte_Villette.txt']

vectorizer = CountVectorizer(input='filename')
print(vectorizer)

dtm = vectorizer.fit_transform(filenames)
# print(dtm)

vocab = vectorizer.get_feature_names()
# print(vocab)
print(len(vocab))

