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


##test
text = "Rick Grimes is a sheriff of King County"

print(get_sentences(text))
print(get_words(text))
print(remove_stopwords(text))
