from nltk.tokenize import RegexpTokenizer
import re
import sys

for arg in sys.argv[1:]:
    f = open(arg, "rU")
    text = f.read()
    tokenizer = RegexpTokenizer("\w+")
    tokens = tokenizer.tokenize(text)
    print tokens