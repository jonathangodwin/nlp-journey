# 03_word2vec_embeddings.py
import gensim.downloader as api

# Télécharge un petit modèle GloVe (50 dimensions)
# Attention : le téléchargement peut prendre 1 ou 2 minutes
model = api.load("glove-wiki-gigaword-50")

# 1. Test des synonymes
print("Mots similaires à 'king' :", model.most_similar("king"))

# 2. Le fameux calcul vectoriel (Roi - Homme + Femme = Reine)
resultat = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
print(f"king - man + woman = {resultat[0][0]}") # Devrait afficher 'queen'