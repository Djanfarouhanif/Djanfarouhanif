import random
game = False
counter = 3
while game == False:
    n = [ 1, 2, 3, 4, 5, 6]
    entre = input("debut du jeux choisie un nombre  au hasard entre 1 et 6 : ")
    number_mystic = random.choice(n)
    try:
        entre_int = int(entre)
        if entre_int <= 0 or entre_int >6:
            print("Nombre trop petit")
        else:

            if number_mystic == entre_int:
                print("Felicitation du a gagner")
            else:
                if counter !=0:
                    counter -= 1
                    print(f"Il vous reste {counter} point")
                if counter == 0:
                    print("Fin du jeux")
                    break
    except:
        print("Veuiller utiliser les chiffre ")




