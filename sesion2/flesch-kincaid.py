from nltk.tokenize import RegexpTokenizer
import re
import sys

for arg in sys.argv[1:]:
    f = open(arg, "rU")
    text = f.read()
    f.close()

    # STEP 1: PREPROCESSING
    # clean punctuation and other separators ***
    text = re.sub('[\,\'\"\-\(\)]+', ' ', text)
    # clean numeric values
    text = re.sub('\${0,1}\d+[\.\,]{0,1}\d*', '###', text)
    # quit dots from abbreviations
    text = re.sub('\s([A-Z][a-z]{1,2})\.\s', ' \g<1> ', text)
    # replace special cases ***
    text = re.sub(' U\.S\. ', ' US ', text)

    # STEP 2: COUNTING
    # number of sentences
    tokenizer = RegexpTokenizer("\s*\.\s*", gaps=True)
    tokens = tokenizer.tokenize(text)
    sentences = len(tokens)

    # number of words
    tokenizer = RegexpTokenizer("\w+")
    tokens = tokenizer.tokenize(text)
    words = len(tokens)

    # number of syllabes
    syllabes = 0
    for token in tokens:
        lowertoken = token.lower()
        retknzr = RegexpTokenizer("[aeiouy]+")
        retkns = retknzr.tokenize(lowertoken)
        syllabes += len(retkns)

    # STEP 3: SCORE F-K
    scorefk = (206.835 - 1.015 * ((1. * words) / sentences) - 84.6 * ((1. * syllabes) / words))

    print "words:", words
    print "sentences:", sentences
    print "syllabes:", syllabes  # ***
    print "score f-k:", scorefk
