# 01_encodage.py
"""
L'Euro est un caractère unique (U+20AC). 
Mais il nécessite 3 octets en UTF-8 (E2 82 AC). 
C'est pour cela que les algorithmes de NLP doivent d'abord gérer l'encodage avant de découper le texte. 
Sinon ils risquent de couper un caractère en deux.
"""

# 1. Le caractère Euro
euro = "€"
print(f"Caractère affiché : {euro}")

# 2. Combien de caractères visuels ?
print(f"Nombre de caractères : {len(euro)}") # Résultat : 1

# 3. Combien d'octets réels en UTF-8 ?
print(f"Nombre d'octets : {len(euro.encode('utf-8'))}") # Résultat : 3

# 4. Regardons la "vraie" nature de l'Euro (en hexadécimal)
print(f"Code point Unicode : {hex(ord(euro))}") # Résultat : 0x20ac (U+20AC)
print(f"Octets en UTF-8 : {euro.encode('utf-8')}") # Résultat : b'\xe2\x82\xac' (E2 82 AC)