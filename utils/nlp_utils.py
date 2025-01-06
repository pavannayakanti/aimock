import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_answer(answer):
    doc = nlp(answer)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords
