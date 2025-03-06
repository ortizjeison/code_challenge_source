import spacy

# Load SpaCy's English model
nlp = spacy.load('en_core_web_trf')


def extract_entities(text):

    # Process text with SpaCy
    doc = nlp(text)

    # Extract named entities
    entities = {"PERSON": [], "ORG": [], "GPE": []}

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities

extract_entities("Brazil's legal betting and Elon Musk market surges with 1.7 billion hits on bet.br domain, overtake YouTube and Instagram in online traffic")