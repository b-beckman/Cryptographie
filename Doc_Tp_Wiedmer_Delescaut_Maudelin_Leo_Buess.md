# TP Widmer Module 122 : Documentation

### Documentation sur la lib Argparse :

> La librairie (bibliothèque) Argparse facilite l'écriture d'interface en ligne de commande. Le programme définit es
> arguments requis et argparse s'arrange pour analyser ceux provenant de sys.argv. Le module argparse génère aussi
> automatiquement les messages d'aide, le mode d'emploi, et lève des erreurs lorsque les utilisateurs fournissent des
> arguments invalides.

> Elle permet de définir et de gérer les arguments passés à un programme en ligne de commande de manière simple et
> efficace.

*  L'interface en ligne de commande du module argparse est basée sur une instance d'argparse.ArgumentParser sur laquelle
  les arguments et options de l'analyseur sont déclarés :

```
  parser = argparse.ArgumentParser(
                    prog='Programme de Leo et Maudelin',
                    description='Mon programme va ètre utiliser afin de crypter et decrypter',
                    epilog='Click pour obtenir de l'aide)
```

* La méthode ArgumentParser.add_argument() permet de définir les arguments de l'analyseur. Ceux-ci peuvent être des
  arguments positionnels, des arguments optionnels ou des drapeaux (qui sont alors traduits en valeurs booléennes). Les
  arguments ont la possibilité d'être complétés par des valeurs.

```
parser.add_argument('test.txt')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
```

* On peut utiliser plusieurs arguments lorsqu'on utilise 

* La méthode ArgumentParser.parse_args() lance l'analyseur et stocke les résultats dans un objet argparse.Namespace :

```
args = parser.parse_args()
print(args.test.txt, args.count, args.verbose)
```