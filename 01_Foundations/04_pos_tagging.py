import spacy
nlp = spacy.load("fr_core_news_sm")
doc = nlp("Le chat noir dort sur le tapis.")
for token in doc:
    print(f"{token.text} -> {token.pos_} (dépendance: {token.dep_})")