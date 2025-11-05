def encrypt_poly_shift(plaintext, odd_shift, even_shift):
    lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    upper_alphabet = lower_alphabet.upper()
    n = len(lower_alphabet)

    result = []
    for i, char in enumerate(plaintext):
        if char in lower_alphabet:
            alphabet = lower_alphabet
        elif char in upper_alphabet:
            alphabet = upper_alphabet
        else:
            result.append(char)
            continue

        shift = even_shift if i % 2 == 0 else odd_shift

        old_index = alphabet.index(char)
        new_index = (old_index + shift) % n
        result.append(alphabet[new_index])

    return "".join(result)


print(encrypt_poly_shift("Привет, мир!", 1, 2))
