def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    if len(keyword)<len(plaintext):
        keyword=keyword*(len(plaintext)//len(keyword)+1)
    ciphertext = ""
    low="abcdefghijklmnopqrstuvwxyz"
    up=low.upper()
    i=0
    while i<len(plaintext):
        c=plaintext[i]
        shift=low.find(keyword.lower()[i])
        if c.isdigit():
            ciphertext+=c
            i+=1
            continue
        if c.isspace():
            ciphertext+=c
            i+=1
            continue
        if c.isalpha():
            if c.isupper():
                if (up.find(c) + shift)>=len(up):
                    a=(up.find(c)+shift)%len(up)
                else:
                    a=up.find(c)+shift
                b=up[a]
            else:
                if (low.find(c) + shift)>=len(up):
                    a=(low.find(c)+shift)%len(up)
                else:
                    a=low.find(c)+shift
                b=low[a]

            ciphertext+=b
            i+=1

            #a=ord(c)+shift
            #ciphertext+=chr(a)
            continue
        ciphertext+=c
        i+=1
        
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    if len(keyword)<len(ciphertext):
        keyword=keyword*(len(ciphertext)//len(keyword)+1)
    plaintext = ""
    low="abcdefghijklmnopqrstuvwxyz"
    up=low.upper()
    i=0
    while i<len(ciphertext):
        c=ciphertext[i]
        shift=low.find(keyword.lower()[i])
        if c.isdigit():
            plaintext+=c
            i+=1
            continue
        if c.isspace():
            plaintext+=c
            i+=1
            continue
        if c.isalpha():
            if c.isupper():
                if (up.find(c) - shift)<0:
                    a=(up.find(c)-shift)%len(up)
                else:
                    a=up.find(c)-shift
                b=up[a]
            else:
                if (low.find(c) - shift)<0:
                    a=(low.find(c)-shift)%len(up)
                else:
                    a=low.find(c)-shift
                b=low[a]

            plaintext+=b
            i+=1

            #a=ord(c)+shift
            #ciphertext+=chr(a)
            continue
        plaintext+=c
        i+=1
    return plaintext

print(encrypt_vigenere("ATTACKATDAWN","LEMONLEMONLE"))
print(decrypt_vigenere("PYTHON","A"))