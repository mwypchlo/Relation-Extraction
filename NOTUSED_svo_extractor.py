import spacy
nlp = spacy.load("en_core_web_sm")

OBJECT_DEPS = {"dobj", "dative", "attr", "oprd"}
SUBJECT_DEPS = {"nsubj", "nsubjpass", "csubj", "agent", "expl", 'pobj'}
WH_WORDS = {"WP", "WP$", "WRB"}

def extract_svo(doc):
    sub = []
    at = []
    ve = []
    for token in doc:
        if token.pos_ == "VERB":
            ve.append(token.text)
        if token.dep_ in OBJECT_DEPS or token.head.dep_ in OBJECT_DEPS:
            at.append(token.text)
        if token.dep_ in SUBJECT_DEPS or token.head.dep_ in SUBJECT_DEPS:
            sub.append(token.text)
    return " ".join(sub).strip().lower(), " ".join(ve).strip().lower(), " ".join(at).strip().lower()

def is_question(doc):
    if len(doc) > 0 and doc[0].pos_ == "VERB":
        return True, ""
    for token in doc:
        if token.tag_ in WH_WORDS:
            return True, token.text.lower()
    return False, ""

if __name__=='__main__':
    sentence='Zayn Malik Leaves One Direction.'
    doc = nlp(sentence)
    for token in doc:
        print("Token {} POS: {}, dep: {}".format(token.text, token.pos_, token.dep_))

    subject, verb, attribute = extract_svo(doc)
    question, wh_word = is_question(doc)
    print("svo:, subject: {}, verb: {}, attribute: {}, question: {}, wh_word: {}".format(subject, verb, attribute, question, wh_word))
