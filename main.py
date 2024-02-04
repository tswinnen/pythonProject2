# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import random


    # on demande à l'ordinateur de choisir un nombre
    # on entre une borne supérieure
nb_max = input()

nb_cherche = random.randint(1,int(nb_max))
print("j'ai choisi", nb_cherche )

    # on tape un chiffre
nb_propose = int(nb_max)+1
while (int(nb_propose) != int(nb_cherche)) :
    nb_propose = input()
    print('vous avez entré le nb', nb_propose)
        # l'oridnateur nous dit si c'est plus grand ou plus petit
        # TODO: plus chaud, plus froid
        # TODO: faire tout cela dans une "vraie" fenêtre.
    if (int(nb_propose) == int(nb_cherche)) :
        print('bravo')
    if (int(nb_propose) > int(nb_cherche)) :
        print('trop grand')
    if (int(nb_propose) < int(nb_cherche)):
            print('trop petit')

    # on continue jusqu'au moment où on a bon


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
