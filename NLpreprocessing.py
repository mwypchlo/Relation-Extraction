import nltk
from nltk.corpus import stopwords
from nltk.tree import Tree

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

def get_continuous_chunks(text):
    chunked = nltk.ne_chunk(tagging_data(text))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk