from nltk.tag import pos_tag, PerceptronTagger, UnigramTagger, BrillTagger, BigramTagger, TrigramTagger, ContextTagger
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize, word_tokenize

import sys

f = open(sys.argv[1], 'rU')
corpus = f.read()
sentences = sent_tokenize(corpus)
print len(sentences)

tokens = word_tokenize(corpus)
print tokens

tagged_tokens = pos_tag(tokens)
print tagged_tokens


tags = {
    "CC": "Coordinating conjunction",
    "CD": "Cardinal number",
    "DT": "Determiner",
    "EX": "Existential there",
    "FW": "Foreign word",
    "IN": "Preposition or subordinating conjunction",
    "JJ": "Adjective",
    "JJR": "Adjective, comparative",
    "JJS": "Adjective, superlative",
    "NN": "Noun, singular or mass",
    "NNS": "Noun, plural",
    "NNP": "Proper noun, singular",
    "NNPS": "Proper noun, plural",
    "PDT": "Predeterminer",
    "POS": "Possessive ending",
    "PRP": "Personal pronoun",
    "LS": "List item marker",
    "MD": "Modal",
    "RB": "Adverb",
    "RBR": "Adverb, comparative",
    "RBS": "Adverb, superlative",
    "RP": "Particle",
    "SYM": "Symbol",
    "TO": "to",
    "UH": "Interjection",
    "VB": "Verb, base form",
    "VBD": "Verb, past tense",
    "VBG": "Verb, gerund or present participle",
    "VBN": "Verb, past participle",
    "VBP": "Verb, non-3rd person singular present",
    "VBZ": "Verb, 3rd person singular present",
    "WDT": "Wh-determiner",
    "WP": "Wh-pronoun",
    "WRB": "Wh-adverb",
    "PRP$": "Possessive pronoun",
    "WP$": "Possessive wh-pronoun"
}

for sentence in sentences:
    words = word_tokenize(sentence)
    for word, tag in pos_tag(words):
        if tag in tags:
            # print word, '->', tag, "=", tags[tag]
            print tag, '->', word, "=", tags[tag]
        else:
            # print word, '->', tag, "=", "NOT FOUND"
            print tag, '->', word, "=", "NOT FOUND"


# taggers = [UnigramTagger(brown.tagged_sents(categories='news'))]
# # taggers = [UnigramTagger()]
# for tagger in taggers:
#      print tagger.tag(corpus)

print pos_tag(tokens, 'universal')
print pos_tag(tokens, 'wsj')
print pos_tag(tokens, 'brown')


print "cleaning"
stopword_tags = {
    "CC": "Coordinating conjunction",
    "CD": "Cardinal number",
    "DT": "Determiner"
}

corpus_without_sw = []
for sentence in sentences:
    words = word_tokenize(sentence)
    for word, tag in pos_tag(words):
        if tag not in stopword_tags:
            corpus_without_sw.append(word)
print corpus_without_sw