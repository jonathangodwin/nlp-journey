# Moment 1 : Les Fondations

Cette étape pose les bases de la tokenisation et de l'analyse linguistique.

## 🛠️ Ce que j'ai implémenté
- [x] **Encodage UTF-8** : Démonstration qu'un caractère n'est pas un octet (ex: l'Euro `€`).
- [x] **Normalisation NFC** : Comparaison de chaînes Unicode équivalentes mais non-identiques en mémoire.
- [x] **Tokenisation BPE** : Visualisation du découpage en sous-mots avec l'encodeur de GPT-4 (`tiktoken`).
- [x] **POS Tagging** : Analyse morphosyntaxique et dépendances avec `spaCy`.

## 🧠 Ce que j'ai retenu
- Le langage n'est pas une suite de mots, c'est une suite de **tokens**. Le choix du tokenizer (BPE, WordPiece) conditionne ce que le modèle pourra apprendre.
- La normalisation est cruciale : sans elle, les programmes voient "café" (1 caractère) et "cafe\u0301" (2 caractères) comme deux mots différents.
- La tokenisation BPE résout le problème des mots inconnus (OOV) en les découpant en morceaux fréquents.

**Prochaine étape** : Les représentations vectorielles (TF-IDF, Word2Vec) et la malédiction de la dimensionnalité.