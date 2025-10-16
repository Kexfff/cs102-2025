def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    low = "abcdefghijklmnopqrstuvwxyz"
    up = low.upper()
    ciphertext = ""
    if shift == 0:
        return plaintext
    for c in plaintext:
        if c.isdigit():
            ciphertext += c
            continue
        if c.isspace():
            ciphertext += c
            continue
        if c.isalpha():
            if c.isupper():
                if (up.find(c) + shift) >= len(up):
                    a = up.find(c) + shift - len(up)
                else:
                    a = up.find(c) + shift
                b = up[a]
            else:
                if (low.find(c) + shift) >= len(up):
                    a = low.find(c) + shift - len(up)
                else:
                    a = low.find(c) + shift
                b = low[a]

            ciphertext += b

            # a=ord(c)+shift
            # ciphertext+=chr(a)
            continue
        ciphertext += c
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    low = "abcdefghijklmnopqrstuvwxyz"
    up = low.upper()
    plaintext = ""
    if shift == 0:
        return ciphertext
    for c in ciphertext:
        if c.isdigit():
            plaintext += c
            continue
        if c.isspace():
            plaintext += c
            continue
        if c.isalpha():
            if c.isupper():
                if (up.find(c) - shift) < 0:
                    a = up.find(c) - shift + len(up)
                else:
                    a = up.find(c) - shift
                b = up[a]
            else:
                if (low.find(c) - shift) < 0:
                    a = low.find(c) - shift + len(up)
                else:
                    a = low.find(c) - shift
                b = low[a]

            plaintext += b

            # a=ord(c)+shift
            # ciphertext+=chr(a)
            continue
        plaintext += c

    return plaintext


print(encrypt_caesar("Python3.6", 3))
print(decrypt_caesar("Sbwkrq3.6", 3))
