## 📊 Bilan de l'étape 2

| Concept | Ce que j'ai compris | Mon code |
| :--- | :--- | :--- |
| **TF-IDF** | Matrice éparse (creuse) qui donne du poids aux mots rares et pénalise les mots fréquents. La dimension dépend de la taille du vocabulaire, ce qui pose problème. | [Voir le code](./01_tfidf_matrix.py) |
| **Cosinus** | Mesure l'angle entre deux vecteurs (produit scalaire normalisé). C'est la base mathématique de l'Attention dans les Transformers. | [Voir le code](./02_cosine_similarity.py) |
| **Word2Vec** | Vecteurs denses qui capturent la sémantique et le contexte local. Permet des opérations mathématiques comme les analogies (Roi - Homme + Femme = Reine). | [Voir le code](./03_word2vec_embeddings.py) |
| **LSA (SVD)** | Réduction de dimension linéaire (SVD tronquée) appliquée à la matrice TF-IDF. Fait émerger les concepts latents en rapprochant les synonymes. | [Voir le code](./04_lsa_svd.py) |