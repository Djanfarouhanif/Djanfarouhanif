import random
game = False
while game == False:
    n = [ 1, 2, 3, 4, 5, 6]
    counter = 0
    entre = input("debut du jeux choisie un nombre  au hasard entre 1 et 6 : ")
    number_mystic = random.choice(n)

    try:
        entre_int = int(entre)
        if entre_int <= 0 :
            print("Nombre trop petit")
        elif entre_int > 6:
            print("Nombre trop grand")

        if number_mystic == entre_int:
            print("Felicitation du a gagner")
        else:
            print("perdu")
            break
    except:
        print("Veuiller utiliser les chiffre ")




