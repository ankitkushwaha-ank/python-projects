import random

you = 0
computer = 0
while True:
    n = int(input('''
1 play game 
2 Exit
press 1 for play or 2 for exit:- 
    '''))
    l = ['Rock','Paper','Scissor']
    if n == 1:
        print('lets play the game')
        for a in range(1, 6):
            print('''
        1. Rock
        2. Paper
        3. Scissor
            ''')

            user = int(input('select one option to play the game...'))
            if user == 1:
                uchoice = "Rock"
            elif user == 2:
                uchoice = "Paper"
            elif user == 3:
                uchoice = "Scissor"
            else:
                print('❌ invalid option choose between 1,2 or 3:)')
                continue

            cchoice = random.choice(l)
            if cchoice==uchoice:
                print('your input:' ,uchoice)
                print("computer choice:",cchoice)
                print('-'*25)
                print('🙂game draw')
                print('-' * 25)
                you = you + 1
                computer = computer + 1
            elif (uchoice =='Rock' and cchoice =='Scissor') or (uchoice == 'Paper' and cchoice == 'Rock') or (uchoice =='Scissor' and cchoice == 'Paper'):

                print('your input:',uchoice)
                print("computer choice:", cchoice)
                print('-' * 25)
                print('🥳you win')
                print('-' * 25)
                you = you + 1
            else:
                print('your input:',uchoice)
                print("computer choice:", cchoice)
                print('-' * 25)
                print('🥲Computer win')
                print('-' * 25)
                computer = computer + 1

        print('~'*25)
        print('Round over')
        print('your score is:', you)
        print('Computer score is:', computer)
        print('-' * 25)
        if you == computer:
            print('game draw your both point is same ')
        elif you > computer:
            print('🥳🥳you won the game')
        else:
            print('🥲🥲Computer won the game')
        print('-' * 25)
    elif n == 2:
        break
    else:
        print('❌ invalid option')


import panda