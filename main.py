import random
game = False
counter = 2
point = 0
n = [ 1, 2, 3, 4, 5, 6]
number_mystic = random.choice(n)
while game == False:

    entre = input("debut du jeux choisie un nombre  au hasard entre 1 et 6 : ")

    try:
        entre_int = int(entre)
        if entre_int <= 0 or entre_int >6:
            print("Nombre trop petit")
        else:

            if number_mystic == entre_int:
                print("Felicitation du a gagner")
                point += 2
                print(f"\nVous avez {point} point")
                number_mystic  = random.choice(n)
            else:
                if counter !=0:
                    counter -= 1
                    print(f"\nIl vous reste {counter} chance")
                if counter == 0:
                    print(f"\nFin du jeux vous avez accumiler {point}  point")
                    break
    except:
        print("Veuiller utiliser les chiffre ")




