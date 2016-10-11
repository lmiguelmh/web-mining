from nltk.tokenize import RegexpTokenizer
import re
import sys

for arg in sys.argv[1:]:
    f = open(arg, "rU")
    text = f.read()

    # ignora "S"
    tokenizer = RegexpTokenizer("[S]\w+")
    tokens = tokenizer.tokenize(text)
    print "using: [S]\w+"
    print tokens

    # incluye "S"
    tokenizer = RegexpTokenizer("[S]\w{0,}")
    tokens = tokenizer.tokenize(text)
    print "using: [S]\w+"
    print tokens

    # incluye "S"
    tokenizer = RegexpTokenizer("\s[S]\w*|^[S]\w*")
    tokens = tokenizer.tokenize(text)
    print "using: \s[S]\w*|^[S]\w*"
    print tokens
