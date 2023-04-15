import argparse


def cryptage(phrase, key):
    """
    Cette fonction prend en entrée une phrase et une clé et retourne le cryptage du texte en utilisant le chiffrement de Vigenère.

    :param phrase: la phrase à encrypter.
    :param key: la clé à utiliser.
    :les paramètres sont forcément en string vu qu'on est dans la console
    :return: le cryptage du texte (string).
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


def main():
    # On crée un objet ArgumentParser pour récupérer les arguments de la ligne de commande
    parser = argparse.ArgumentParser()

    # On ajoute les arguments "phrase" et "key"
    # "phrase" est l'argument pour les entrées de l'utilisateur (le message a chiffer )
    # "key" est l'argument ou l'utilisateur va donner la clé de chiffrage pour le message
    parser.add_argument('phrase')
    parser.add_argument('key')

    # On récupère les arguments de la ligne de commande
    args = parser.parse_args()

    # On appelle la fonction encodage_vigenere avec les arguments fournis et on stocke le résultat encrypté dans la variable encrypt_result
    encrypt_result = cryptage(args.phrase, args.key)

    # On affiche le résultat encrypté
    print("Message codé:", encrypt_result)


if __name__ == '__main__':
    # On exécute la fonction main si le programme est exécuté en tant que script
    main()