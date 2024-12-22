from collections import Counter
import itertools


def find_key(ciphertext, key_length):
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
    groups = [ciphertext[i::key_length] for i in range(key_length)]

    key = ""
    for group in groups:
        freqs = Counter(group)
        most_common = max(freqs, key=freqs.get)
        shift = (alphabet.index(most_common) - alphabet.index('_')) % len(alphabet)
        key += alphabet[shift]

    return key


def decrypt_vigenere(ciphertext, key):
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
    decrypted = ""
    key_index = 0

    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            decrypted_char = alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            decrypted += decrypted_char
            key_index += 1
        else:
            decrypted += char

    return decrypted


ciphertext = "[зашифрованный текст]"

key = find_key(ciphertext, 4)
print("Found key:", key)

decrypted_text = decrypt_vigenere(ciphertext, key)
print("Decrypted text:")
print(decrypted_text)