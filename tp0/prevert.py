#2.1
def twoDigit(i:int)-> str:
    if i<=9:
        return "0"+str(i)
    return str(i)
data: str
# ouverture du fichier d'entrée (mode r: read)
with open('data/online_inventaire_prevert.txt', 'r') as input_file:
    data = input_file.read() # lecture du contenu du fichier,
    tab= data.split(';')
    data=""
    for i in range(len(tab)):
        data+=twoDigit(i+1) + " "+ tab[i] + "\n"

# enregistré dans la variable data
# ici, on réalise un traitement sur les données (data)...
# ouverture du fichier de sortie (w: write)
with open('data/inventaire_prevert.txt', 'w') as output_file:
    output_file.write(data) # écriture des données dans le fichier
