
```
import random

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_keypair(p, q, perm, shift):
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((n, e, perm, shift), (n, d, perm, shift))

def encrypt(pk, plaintext):
    n, e, perm, shift = pk
    cipher = ''
    for char in plaintext:
        if char in perm:
            idx = perm.index(char)
            idx = (idx + shift) % len(perm)
            cipher += perm[idx]
        else:
            cipher += char
    return ''.join([chr((ord(char) ** e) % n) for char in cipher])

def decrypt(pk, ciphertext):
    n, d, perm, shift = pk
    plain = ''
    for char in ciphertext:
        if char in perm:
            idx = perm.index(char)
            idx = (idx - shift) % len(perm)
            plain += perm[idx]
        else:
            plain += char
    return ''.join([chr((ord(char) ** d) % n) for char in plain])
```

#Explications :

#- La fonction `gcd` calcule le plus grand commun diviseur de deux nombres a et b à l'aide de l'algorithme d'Euclide.
#- La fonction `mod_inverse` calcule l'inverse modulaire de a modulo m en utilisant une boucle de recherche exhaustive.
#- La fonction `generate_keypair` génère une paire de clés RSA à partir de deux nombres premiers p et q, d'une permutation et d'un ordre de décalage. Elle retourne un tuple contenant la clé publique (n,e,perm,shift) et la clé privée (n,d,perm,shift).
#- La fonction `encrypt` chiffre un message en utilisant la clé publique. Elle applique d'abord la permutation et le décalage choisis par l'utilisateur, puis elle chiffre chaque caractère du message en utilisant l'exponentiation modulaire.
#- La fonction `decrypt` déchiffre un message en utilisant la clé privée. Elle applique d'abord l'inverse de la permutation et du décalage choisis par l'utilisateur, puis elle déchiffre chaque caractère du message en utilisant l'exponentiation modulaire.
 
