#Vraux Igor et Wiaux Bastien

def load(file):
    try:
        with open(file,'r') as fichier:
            return fichier.read()
    except FileNotFoundError:
        return None

def search(mot,fichier): #utilisation de la fonction binary-research modifiée
    first = 0
    last = len(fichier)-1
    found = False
    while first<=last and not found: 
        middle = (first + last)//2
        if fichier[middle][0] == mot:
            found = True
            proche = fichier[middle][0]
        else:
            if sorted([mot,fichier[middle][0]])[0] == mot:
                last = middle-1
            else:
                first = middle+1
    if not found:
        proche = fichier[middle+1][0]
    return proche

command = input("> ")
fichier = None
while command != "exit":
    command = command.split(" ")
    
    if command [0] == "file":
        try:
            fichier = load(command[1])
            if fichier == None:
                print("Erreur: Fichier inexistant")
            else:
                print("Chargé {}".format(command[1]))
        except IndexError:
            print("Erreur: Précisez un fichier")
    
    elif command [0] == "info":
        if fichier == None:
            print("pas de fichier chargé")
        elif fichier == "":
            print("fichier vide")
        else:
            print("{} lignes\n{} caractères".format(len(fichier.split("\n")),len(fichier)-len(fichier.split("\n"))+1))

    elif command[0] == "dictionary":
        if fichier == None:
            print("pas de fichier chargé")
        else:
            lst1 = fichier.split("\n")
            while lst1[-1] == "":
                lst1 = lst1[:-1]
            fichier = []
            for i in lst1:
                if len(i.split(",")) < 2:
                    print(i.split(","))
                    print("Le fichier n'est pas lisible comme dictionnaire")
                else:
                    if type(i.split(",")[0]) == str and i.split(",")[1].isnumeric():
                        fichier.append(i.split(",") )
                    else:
                        print(i.split(","))
                        print("Le fichier n'est pas lisible comme dictionnaire")
                        break
                    if len(fichier) == len(lst1):
                        fichier.sort()
                        print("Lit le fichier comme un dictionnaire")

    elif command[0] == "search":
        if fichier == None:
            print("Pas de fichier chargé")
        elif type(fichier) is not list:
            print("Veuillez d'abord convertir en dictionnaire")
        else:
            mot = search(command[1],fichier)
            print("le mot le plus proche est {}".format(mot))

    elif command[0] == "sum":
        if len(command[1:]) == 0:
            print("Erreur: précisez au moins un nombre")
        else:
            try:
                print(sum([float(i) for i in command[1:]]))
            except ValueError:
                print("Erreur: nombre non valide")

    elif command[0] == "avg":
        try:
            print(sum([float(i) for i in command[1:]])/len(command[1:]))
        except ValueError:
            print("Erreur: nombre non valide")
        except ZeroDivisionError:
            print("Erreur: précisez au moins un nombre")

    elif command[0] == "help":
        com = ["file","info","dictionary","search","sum","avg","help","exit"]
        expl = ["file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler",\
        "montre le nombre de lignes et de caractères du fichier",\
        "utilise le fichier comme dictionnaire à partir de maintenant",\
        "search <word>: cherche le mot le plus similaire au mot spécifié dans le dictionnaire",\
        "sum <number1> ... <numbern>: calcule la somme des nombres spécifiés",\
        "avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés",\
        "montre des instructions à l'utilisateur",\
        "arrête l'outil"]
        for i in range(len(com)):
            print("{}\t{}".format(com[i],expl[i]))
        
    else:
        print("{} n'est pas une commmande valide".format(command[0]))
    command = input("> ")
