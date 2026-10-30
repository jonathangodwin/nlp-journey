# 02_cosine_similarity.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

corpus = [
    "Le chat dort sur le tapis.",
    "Le chien dort sur le tapis.",
    "La voiture roule sur la route."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Similarité entre phrase 0 et 1 (chat vs chien)
sim_0_1 = cosine_similarity(X[0], X[1])[0][0]
# Similarité entre phrase 0 et 2 (chat vs voiture)
sim_0_2 = cosine_similarity(X[0], X[2])[0][0]

print(f"Similarité 'chat dort' / 'chien dort' : {sim_0_1:.2f}") # Élevée
print(f"Similarité 'chat dort' / 'voiture roule' : {sim_0_2:.2f}") # Très faible