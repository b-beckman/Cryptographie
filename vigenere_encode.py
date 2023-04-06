import argparse
import os
import sys


def vigenere_encode(plaintext, key):
    """Encode le texte en utilisant le système de Vigenère"""
    ciphertext = ""
    key_len = len(key)
    for i, char in enumerate(plaintext):
        key_char = key[i % key_len]
        shift = ord(key_char) - ord('a')
        ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
    return ciphertext


if os.name == 'main':
    # Définition des arguments de ligne de commande
    parser = argparse.ArgumentParser(description='Encode un message en utilisant le système de Vigenère.')
    parser.add_argument('message', help='Le message à encoder')
    parser.add_argument('key', help='La clé de chiffrement')
    args = parser.parse_args()

    # Encode le message en utilisant la clé donnée
    ciphertext = vigenere_encode(args.message.lower(), args.key.lower())

    print(f"Message chiffré: {ciphertext}")