#  03_bpe_tokenisation.py
import tiktoken

# On prend l'encodeur utilisé par GPT-4
enc = tiktoken.get_encoding("cl100k_base")

mot = "anticonstitutionnellement"
tokens = enc.encode(mot)

print(f"Mot original : {mot}")
print(f"Nombre de tokens : {len(tokens)}")
print(f"IDs des tokens : {tokens}")

# On décode chaque token pour voir les morceaux
morceaux = [enc.decode([t]) for t in tokens]
print(f"Découpage : {morceaux}")
