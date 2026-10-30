# 02_normalisation.py
import unicodedata

# Deux façons d'écrire "café"
s1 = "café"               # 'é' est un seul caractère (U+00E9)
s2 = "cafe\u0301"         # 'e' + accent combinant (U+0065 U+0301)

print(f"s1 == s2 ? {s1 == s2}") # Résultat : False (Surprise !)

# On applique la normalisation NFC
s1_nfc = unicodedata.normalize('NFC', s1)
s2_nfc = unicodedata.normalize('NFC', s2)

print(f"s1_nfc == s2_nfc ? {s1_nfc == s2_nfc}") # Résultat : True