import random
from Data import lista_de_celebritati

logo = '''
█████████████▀████████████████████████████
█─█─█▄─▄█─▄▄▄▄█─█─███▄─▄███─▄▄─█▄─█▀▀▀█─▄█
█─▄─██─██─██▄─█─▄─████─██▀█─██─██─█─█─█─██
▀▄▀▄▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀'''

vs = '''
╭╮╱╱╭┳━━━╮
┃╰╮╭╯┃╭━╮┃
╰╮┃┃╭┫╰━━╮
╱┃╰╯┃╰━━╮┃
╱╰╮╭╯┃╰━╯┣╮
╱╱╰╯╱╰━━━┻╯'''

score = 0
print(f"Your score is {score}")
#fac un dictionary de date cu key numele si cu data follower count-ul.

#fac functie de joc care da return cand greseste
def game(previous_celebrity):
    global score
    first_value = lista_de_celebritati[previous_celebrity]
    new_celebrity = random.choice(list(lista_de_celebritati))
    second_value = lista_de_celebritati[new_celebrity]
    if new_celebrity == previous_celebrity:
        while new_celebrity == previous_celebrity:
            new_celebrity = random.choice(list(lista_de_celebritati))
    print(f"Compare A: {previous_celebrity}")
    print(vs)
    print(f"With B: {new_celebrity}")
    choice = input("Who has more followers? A or B\n").lower()
    if choice == 'a':
        if lista_de_celebritati[previous_celebrity] > lista_de_celebritati[new_celebrity]:
            score +=1
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n")
            game(previous_celebrity)

        else:
            print(f"Wrong. Your final score is {score}")

    elif choice == 'b':
        if lista_de_celebritati[previous_celebrity] < lista_de_celebritati[new_celebrity]:
            score += 1
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n")
            game(new_celebrity)

        else:
            print(f"Wrong. Your final score is {score}")

print(logo)
print("Welcome to HIGHER LOWER")
start = input("Type Y to start \n").lower()
while start != 'y':
    start = input("Type Y to start \n").lower()
first_celebrity = random.choice(list(lista_de_celebritati))
game(first_celebrity)