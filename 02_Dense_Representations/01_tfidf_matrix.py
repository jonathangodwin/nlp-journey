# 01_tfidf_matrix.py

from sklearn.feature_extraction.text import TfidfVectorizer

# Un petit corpus de 3 phrases
corpus = [
    "Le chat dort sur le tapis.",
    "Le chien dort sur le tapis.",
    "La voiture roule sur la route."
]

# On initialise le vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# 1. Voir le vocabulaire (les dimensions)
print(f"Vocabulaire (dimensions) : {vectorizer.get_feature_names_out()}")

# 2. matrice TF-IDF 
print(f"Forme de la matrice : {X.shape}") # (3 documents, N mots)
print(f"Matrice TF-IDF :\n{X.toarray()}")
