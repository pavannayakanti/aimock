from utils.nlp_utils import nlp

def similarity_score(answer, ideal_answer):
    doc1 = nlp(answer)
    doc2 = nlp(ideal_answer)
    return doc1.similarity(doc2)
