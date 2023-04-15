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
    parser.add_argument('phrase', nargs='?', help="Phrase à encrypter")
    parser.add_argument('key', nargs='?', help="clé de cryptage")
    # Ajout d'un flag pour le decodage
    parser.add_argument('--decode', action='store_true', help="decodage")
    # Ajout d'un argument pour le fichier d'entrée
    parser.add_argument('--input', '-i', help="Fichier d'entrée")
    # Ajout d'un argument pour le fichier de sortie
    parser.add_argument('--output', '-o', help="Fichier de sortie")
    
    # On récupère les arguments de la ligne de commande
    args = parser.parse_args()

    # Si un fichier d'entrée est spécifié, on lit le contenu du fichier au lieu de l'argument "phrase"
    if args.input:
        with open(args.input, 'r') as f:
            phrase = f.read()
    else:
        phrase = args.phrase
        
    # Si un fichier d'entrée est spécifié, on lit la clé du fichier au lieu de l'argument "key"
    if args.input:
        with open(args.input, 'r') as f:
            key = f.readline().strip()
    else:
        key = args.key
    
    # Condition pour savoir quel fonction l'utilisateur veut appeler
    # Les deux conditions fonctionnent de la même manière appel de la fonction,
    # puis print du resultat
    if args.decode:
        result = decodage_vigenere(phrase, key)
        print("Message décodé:", result)
    else:
        result = codage_vigenere(phrase, key)
        print("Message codé:", result)
    
    # Si un fichier de sortie est spécifié, on écrit le résultat dans le fichier au lieu de l'afficher
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)

if __name__ == '__main__':
    main()