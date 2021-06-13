import re

def count_words(sentence):
    sentence = re.sub('["!.:,_&@$%^]',' ', sentence)
    
    sentenceWords = {}
    
    for word in sentence.lower().split():
        if word.startswith("'") or word.endswith("'"):
            word = word.replace("'", '')
        if word in sentenceWords:
            sentenceWords[word] += 1
        else:
            sentenceWords.setdefault(word, 1)
    return sentenceWords