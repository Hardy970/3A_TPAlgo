import sys
from curses.ascii import isdigit

from sympy.strategies.core import switch


#1.1
def input_number_from_kb(prompt: str='Saisir un nombre entier : ') -> int:
    return int(input(prompt))

"""if __name__ =='__main__':
    print(input_number_from_kb())"""
#1.2
def input_number_from_kb2(prompt: str='Saisir un nombre entier : ') -> int:
    try:
        return int(input(prompt))
    except ValueError:
        return input_number_from_kb(prompt)
"""if __name__ =='__main__':
    print(input_number_from_kb()) """
#3.1
"""def input_nums_from_cli() -> list[int]:
    l=[]
    for i in range(1,len(sys.argv)):
        if int(sys.argv[i]):
             l.append(int(sys.argv[i]))
    return l"""
#3.2
def input_nums_from_cli() -> list[int]:
    if sys.argv[1]=='--sum':
            l = [0]
            for i in range(2, len(sys.argv)):
                if int(sys.argv[i]):
                    l[0]+=int(sys.argv[i])
            return l
    elif sys.argv[1]=='--help':
            print("""usage: python -m tp0.inout [--help] [--sum] [NOMBRE ...]
                Collecte les nombres passés en ligne de commande
                arguments:
                NOMBRE série de nombres à collecter
                options:
                --help affiche ce message d'aide et termine
                --sum réalise la somme des nombres""")
            return []
    elif sys.argv[1][:6]== '--file':
            data: str
            # ouverture du fichier d'entrée (mode r: read)
            with open(sys.argv[1][7:], 'r') as input_file:
                data = input_file.read()  # lecture du contenu du fichier,
                tab = data.split('\n')
                tab2=[]
                for i in range(len(tab)):
                    if int(tab[i]):
                        tab2.append(int(tab[i]))
            return tab2
    else:
        return []
if __name__ =='__main__':
    print(input_nums_from_cli())

