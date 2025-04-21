import random
user_input =""
while True:
    user = input('press enter for play or q for quit...')
    if user == 'q':
        break
    else:

        coin = 0
        computer = 0

        for a in range(1,51):

                input('''
        roll a dice...''')
                # this is for you
                dice = random.randint(1, 6)
                coin = coin + dice
                dice2 = random.randint(1, 6)
                computer = computer + dice2

                # for snake biting computer
                if coin  == 10 or coin  == 16 or coin  ==25 or coin  ==79 :
                    coin = coin - 4

                    print('🐍snake bite you lose 4 you are on:' ,coin)
                elif coin  == 32 or coin  == 16 or coin  ==39 or coin  ==87:
                    coin = coin - 7

                    print('🐍snake bite you you lose 7 you are on:' ,coin)
                elif coin  == 50 or coin  == 16 or coin  ==58 or coin  ==99:
                    coin = coin - 10
                    print(f'''
           round no  {a}
        you got {dice}  coputer  {dice2}
                                                ''')
                    print('🐍snake bite you you lose 10 you are on:' ,coin)

                # for snake biting computer
                elif coin  == 10 or coin  == 16 or coin  ==25 or coin  ==79 :
                    computer = computer - 4

                    print('🐍snake bite computer lose 4 computer are on:' ,computer)
                elif computer  == 32 or computer  == 16 or computer  ==39 or computer  ==87:
                    computer = computer - 7

                    print('🐍snake bite computer computer lose 7 computer are on:' ,computer)
                elif computer  == 50 or computer  == 16 or computer  ==58 or computer  ==99:
                    computer = computer - 10
                    print('🐍snake bite computer computer lose 10 computer are on:' ,computer)
                elif coin > 100:
                    coin = coin - dice
                elif computer > 100:
                    computer = computer - dice2
                else:


                    print(f'''
           round no  {a}
        you got {dice}  coputer  {dice2}
                                               ''')
                    print('you', 'computer')
                    print('------------')
                    print(f'| {coin}   |  {computer} |')
                    print('------------')

                #for wining the game
                if coin ==100:
                    print('''
           🥳hurrey you won the game''')
                    break
                elif computer == 100:
                    print('''
           computer won the game''')
                    break
    print('round over game pls restart')
    break
