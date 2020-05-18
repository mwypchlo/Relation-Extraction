import nltk
from nltk.corpus import stopwords

def get_sentences(text):
    data = nltk.sent_tokenize(text)
    return data

def get_words(text):
    data = nltk.word_tokenize(text)
    return data

def remove_stopwords(text):
    filtered_words=[]
    words=get_words(text)
    for w in words:
        if w not in stopwords.words('english'):
            filtered_words.append(w)
    return filtered_words

def tagging_data(text):##explanations of tags in tags_explanation file
    for t in text:
        words=get_words(text)
        tagged= nltk.pos_tag(words)
    return tagged

def entity_recognition(text):
    namedEnt = nltk.ne_chunk(tagging_data(text))
    return namedEnt

##test
text = "Bill Gates is best known as the co-founder of Microsoft Corporation"

print(get_sentences(text))
print(get_words(text))
print(remove_stopwords(text))
print(tagging_data(text))
print(entity_recognition(text))
