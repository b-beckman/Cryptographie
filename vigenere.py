import argparse

def codage_vigenere(phrase, key):
    """
    Cette fonction prend en entrée une phrase et une clé et retourne le codage_vigenere du texte en utilisant le chiffrement de Vigenère.

    :param phrase: la phrase à encrypter.
    :param key: la clé à utiliser.
    :les paramètres sont forcément en string vu qu'on est dans la console
    :return: le codage_vigenere du texte (string).
    """
    # On initialise la variable qui contiendra le résultat encrypté
    encrypt_result = ""

    # On initialise la variable qui servira à parcourir la clé
    key_index = 0

    # On parcourt chaque caractère de la phrase à encrypter
    for chara in phrase:
        # Si le caractère est une lettre de l'alphabet
        if chara.isalpha():
            # On convertit la lettre de la clé en ASCII et on la normalise entre 0 et 25 (correspondant aux lettres de l'alphabet)
            shift = ord(key[key_index % len(key)].lower()) - 97

            # On convertit la lettre en ASCII et on la normalise entre 0 et 25 (correspondant aux lettres de l'alphabet)
            chara_ascii = ord(chara.lower()) - 97

            # On applique la formule du chiffrement de Vigenère pour obtenir la lettre encryptée
            encrypted_chara = chr((chara_ascii + shift) % 26 + 97)

            # On ajoute la lettre encryptée au résultat final
            encrypt_result += encrypted_chara

            # On incrémente l'index de la clé pour passer à la lettre suivante
            key_index += 1
        else:
            # Si le caractère n'est pas une lettre de l'alphabet, on ne l'encrypte pas et on l'ajoute directement au résultat final
            encrypt_result += chara

    # On retourne le résultat final
    return encrypt_result

def decodage_vigenere(phraseDeco, key):
    #Cette fonction prend en paramètres une phrase chiffrée et une clé, et retourne la phrase déchiffrée en utilisant le chiffrement de Vigenère.

    #param phraseDeco: la phrase à déchiffrer.
    #param key: la clé à utiliser.
    #return: la phrase déchiffrée (string).
    # On initialise la variable qui contiendra le résultat décrypté
    decrypt_result = ""

    # On initialise la variable qui servira à parcourir la clé
    key_index = 0

    # On parcourt chaque caractère de la phrase à décrypter
    for chara in phraseDeco:
        # Si le caractère est une lettre de l'alphabet
        if chara.isalpha():
            # On convertit la lettre de la clé en ASCII et on la normalise entre 0 et 25 (correspondant aux lettres de l'alphabet)
            shift = ord(key[key_index % len(key)].lower()) - 97

            # On applique la formule du déchiffrement de Vigenère pour obtenir la lettre décryptée
            decrypted_chara = chr((ord(chara.lower()) - 97 - shift) % 26 + 97)

            # On ajoute la lettre décryptée au résultat final
            decrypt_result += decrypted_chara

            # On incrémente l'index de la clé pour passer à la lettre suivante
            key_index += 1
        else:
            # Si le caractère n'est pas une lettre de l'alphabet, on ne le décrypte pas et on l'ajoute directement au résultat final
            decrypt_result += chara

    # On retourne le résultat final
    return decrypt_result

def main():
    # On crée un objet ArgumentParser pour récupérer les arguments de la ligne de commande
    parser = argparse.ArgumentParser()

    # On ajoute les arguments "phrase" et "key"
    parser.add_argument('phrase' help="Phrase à encrypter")
    parser.add_argument('key' help="clé de cryptage")
    # Ajout d'un flag pour le decodage
    parser.add_argument('--decode', action='store_true' help="decodage")
    # On récupère les arguments de la ligne de commande
    args = parser.parse_args()

    # Condition pour savoir quel fonction l'utilisateur veut appeler
    # Les deux conditions fonctionnent de la même manière appel de la fonction,
    # puis print du resultat
    if args.decode:
        decrypt_result = decodage_vigenere(args.phrase, args.key)
        print("Message décodé:", decrypt_result)
    else:
        encrypt_result = encodage_vigenere(args.phrase, args.key)
        print("Message codé:", encrypt_result)

if __name__ == '__main__':
    main()