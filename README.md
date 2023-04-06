# TP Widmer Module 122 : Documentation

## Fonctions utilisées pour les scripts :

## Documentation sur la lib Argparse :

> La librairie (bibliothèque) **Argparse facilite l'écriture d'interface en ligne de commande.** Le programme définit es
> arguments requis et **argparse s'arrange pour analyser ceux provenant de sys.argv.** Le module argparse **génère aussi
> automatiquement les messages d'aide, le mode d'emploi, et lève des erreurs lorsque les utilisateurs fournissent des
> arguments invalides.**


**_L'interface en ligne de commande du module argparse est basée sur une instance d'argparse.ArgumentParser sur laquelle
les arguments et options de l'analyseur sont déclarés :_**

```
  parser = argparse.ArgumentParser(
                    prog='Programme de Leo et Maudelin',
                    description='Mon programme va ètre utiliser afin de crypter et decrypter',
                    epilog='Click pour obtenir de l'aide)
```

**_La méthode ArgumentParser.add_argument() permet de définir les arguments de l'analyseur. Ceux-ci peuvent être des
arguments positionnels, des arguments optionnels ou des drapeaux (qui sont alors traduits en valeurs booléennes). Les
arguments ont la possibilité d'être complétés par des valeurs._**

```
parser.add_argument('test.txt')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
```

**_On peut utiliser plusieurs arguments lorsqu'on utilise add_Argument()_**

* action = Précise la gestion d'un argument

```
store, store_const,store_true,append,append_const,count,help,versio
```

* choice = Limite le choix à certaines valeurs

```
['foo', 'bar'], range(1, 10) ou une instance de Container
``` 

* const = Utilise une valeur constante

* default = Valeur à utiliser en l'absence d'un argument

```
None par défauts
```
* dest = Définit le nom de l'attribut à utiliser dans l'espace de nommage résultant

* help = Message d'aide pour l'argument

* metavar = Autre nom possible pour l'argument, est affiché dans l'aide

* nargs = Précise le nombre de répétitions de l'argument

```
int, '?', '*', '+' ou argparse.REMAINDER
```

* required = Précise si l'argument est obligatoire ou optionnel

```
True ou False
```

* type = Conversion automatique vers le type fourni

```
int, float, argparse.FileType('w') ou une fonction
```

**_La méthode ArgumentParser.parse_args() lance l'analyseur et stocke les résultats dans un objet argparse.Namespace :_**

```
args = parser.parse_args()
print(args.test.txt, args.count, args.verbose)
```

### Créer un analyseur (parser) :

* la premières étape est de créer un arguments (avec l'objet ArgumentParser)

* **L'objet ArgumentParser contient les info. pour savoir comment interprêter la ligne de commande**

``` 
parser = argparse.ArgumentParser(description='Process some integers.')
```

### Ajouter des arguments :

* Pour ajouter des arguments,à l'objet ArgumentParser, il faut utiliser la méthode add_argument().
* **On va lui dire commnent interprêtre les lignes de commandes pour ensuite pouvoir le tranformer en objet**
* On va stocké l'informations avant d'uiliser le résultat avec la fonction parse_args().

```
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
```

## Fonction chiffrement + tests :

## Fonction déchiffrement + tests :

## Conclusion :