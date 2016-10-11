from nltk.tokenize import WhitespaceTokenizer
import sys
for arg in sys.argv[1:]:
    f = open(arg, "rU")
    text = f.read()
    tokens = WhitespaceTokenizer().tokenize(text)
    print tokens
