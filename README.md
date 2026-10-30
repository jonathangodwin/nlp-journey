# 🚀 NLP Journey: From Basics to LLMs

Ce dépôt GitHub est un voyage dans l'univers du NLP : depuis les basiques jusqu'à une représentation dynamique du langage (LLMs). Nous allons voir comment nous sommes passés de représentations statiques du langage à des représentations beaucoup plus dynamiques, qui ont abouti à la révolution des Grands Modèles de Langage (LLMs) tels qu'on les connaît aujourd'hui.

Je vous préviens, il va y avoir des secousses en cours de vol ! Entre l'avènement du Deep Learning pour aider à contextualiser, et les nombreuses résolutions de problèmes qui, mis bout à bout, nous ont conduit à ce que l'on connaît aujourd'hui... ça sera passionnant comme voyage. Alors, attachez bien vos ceintures... 🎢

## 🔬 Une lecture Kuhienne de cette aventure

Avant de décoller, prenons un instant pour regarder ce voyage avec les lunettes de la philosophie des sciences. En parcourant ce dépôt, vous verrez que l'évolution du NLP n'est pas une simple ligne droite cumulative. Elle est une parfaite illustration de ce que **Thomas Kuhn** décrivait dans *La Structure des révolutions scientifiques* (1962). 

La science ne progresse pas par simple accumulation(comme on pourrait le croire), elle fonctionne par **paradigmes** :
1. **La science normale** : une communauté travaille avec un cadre théorique établi.
2. **Les anomalies** : des problèmes insolubles apparaissent, que le paradigme ne peut pas expliquer.
3. **La crise** : les anomalies s'accumulent et rendent la pratique normale impossible.
4. **La révolution** : un changement de paradigme radical (une "Gestalt") vient tout remplacer.

## 🎯 Le fil rouge : Les deux grandes anomalies du NLP classique

C'est exactement ce qui s'est passé en NLP. Le "paradigme classique" (les vecteurs épars, le comptage de mots) était notre science normale. Mais il souffrait de deux anomalies fondamentales :

1. **La malédiction de la dimensionnalité** : Le vocabulaire étant parfois de l'ordre de 100 000 termes, la matrice TF-IDF était très coûteuse computationnellement et nous limitait énormément. *Alors, comment résoudre ce problème ?*
2. **L'absence de contexte (représentation statique)** : Certes, on pouvait avoir une représentation des mots, mais celle-ci était statique, indépendante du texte. Un mot dans un contexte différent était toujours vu comme identique. *Comment rendre cette représentation beaucoup plus dynamique ?*

Ce sont ces deux anomalies qui vont guider le cheminement de ce dépôt. Nous verrons comment la résolution d'un problème fait naître un autre problème, et comment, à chaque fois, une idée brillante (une nouvelle théorie) nous permet de passer à l'étape suivante. 

Nous verrons que les chercheurs ont d'abord tenté de sauver le paradigme classique (avec des méthodes comme la LSA/SVD) avant de céder à la **révolution connexionniste** (Word2Vec, RNN), pour finalement aboutir à la rupture épistémologique majeure : les **Transformers**.

C'est une histoire fascinante, non seulement d'un point de vue informatique, mais aussi d'un point de vue scientifique de façon générale. Comprendre comment la science évolue à travers de nombreux défis et énigmes à résoudre, et qui permettent finalement d'aboutir à de magnifiques innovations, construites brique par brique. 🧱

---

## 🗺️ La feuille de route (Roadmap)

- [ ] **Moment 1 : Les Fondations** (Encodages, Tokenisation BPE, POS Tagging)
- [ ] **Moment 2 : Représentations denses** (TF-IDF, SVD/LSA, Word2Vec, GloVe)
- [ ] **Moment 3 : Évaluation & Classification** (Métriques, Matrice de confusion)
- [ ] **Moment 4 : Contexte séquentiel** (RNN, LSTM, Attention de Bahdanau)
- [ ] **Moment 5 : La révolution Transformer** (Self-Attention, Multi-Head)
- [ ] **Moment 6 : L'ère des LLMs** (BERT, GPT, Fine-tuning)
- [ ] **Moment 7 : Extension Vision** (ViT : Vision Transformers)
- [ ] **Moment 8 : État de l'art** (Multimodal, RAG, Agents)

*Prêt pour le décollage ? 🚀*

---

## 📚 Bibliographie & Auteurs du Voyage

Comme dans toute dissertation, les idées ne tombent pas du ciel. Ce voyage est jalonné par les travaux de chercheuses et de chercheurs qui ont bousculé les paradigmes. Voici les "auteurs" majeurs qui seront cités tout au long de ce dépôt :

- **Mikolov et al. (2013)** – *Word2Vec* : La première tentative réussie de donner une âme mathématique (géométrique) au sens des mots.
- **Bahdanau et al. (2014)** – *L'Attention* : L'art de ne pas tout oublier et de briser le goulot d'étranglement de la mémoire.
- **Vaswani et al. (2017)** – *Transformer* : La rupture épistémologique. "L'attention est tout ce dont vous avez besoin". La fin de la récurrence.
- **Devlin et al. (2018)** – *BERT* : La double lecture (bidirectionnelle) du contexte.
- **Kuhn, T. (1962)** – *La Structure des révolutions scientifiques* : Pour comprendre comment toutes ces idées s'articulent et se remplacent.

### 🧠 Pour aller plus loin (Philosophie & Anthropologie)
*A venir*

