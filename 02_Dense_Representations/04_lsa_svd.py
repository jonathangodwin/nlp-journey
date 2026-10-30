# Fichier : 04_lsa_svd.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Un corpus un peu plus grand pour voir l'effet
corpus = [
    "Le chat dort sur le tapis.",
    "Le chien dort sur le tapis.",
    "La voiture roule sur la route.",
    "La moto roule sur l'autoroute."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# On réduit de N dimensions à 2 dimensions
svd = TruncatedSVD(n_components=2)
X_reduit = svd.fit_transform(X)

print(f"Matrice originale : {X.shape}") # (4 documents, ~15 mots)
print(f"Matrice réduite : {X_reduit.shape}") # (4 documents, 2 dimensions)

# Afficher les coordonnées des documents dans l'espace réduit
for i, doc in enumerate(corpus):
    print(f"Doc {i} : {X_reduit[i]}")