play = True

while play:
    # The below section is used to import the python modules into our code
    import time
    import os
    import random
    import sys
    # The vairables are defined as 0 or nothing so that they can be operated with straight aaway
    player_1_life = 0
    player_2_life = 0
    loop = int(0)
    wordbank = []
    contents = ""
    hidden = ""
    underscores = "".join(hidden)
    # The code below defines the list with the different hangman images so that they can easily be printed out later
    hangmanpics = [
     '''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''','''
        ▄██████████████▄▐█▄▄▄▄█▌
██████▌▄▌▄▐▐▌███▌▀▀██▀▀
████▄█▌▄▌▄▐▐▌▀███▄▄█▌
▄▄▄▄▄██████████████▀''','''
░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████'''
    ]
    hangmanpicsfor2player = [
     '''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''','''
        ▄██████████████▄▐█▄▄▄▄█▌
██████▌▄▌▄▐▐▌███▌▀▀██▀▀
████▄█▌▄▌▄▐▐▌▀███▄▄█▌
▄▄▄▄▄██████████████▀''','''
░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████'''
    ]
    # Welcomes the player to the game and asks them in which way they want to select the word
    print('''
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''' " to Hangman!")
    time.sleep(1.5)
    input_type = input("Do you want to input a word or have a word selected randomly from a word bank txt file? Answer '1' for the first option of '2' for the second option. ")
    # If the player chosces option one they are required to input a word
    if input_type == "1":
        print("You have selected to input a word.")
        time.sleep(1)
        print("Tip! Have a third party input the word so no player is aware of the answer.")
        time.sleep(1.5)
        ans = input("Input a word! ")
    # If the player chosces option two they are required to input a txt file. The word will be randonmly selected from the txt file
    elif input_type == "2":
        print("You have selected to input a randomn word from a txt file!")
        time.sleep(1.5)
        file_name = input("Input a txt file located in the same folder as this program (I have included some demos with this submission). Remeber to include '.txt' at the end of the name. ")
        # The below step imports the txt file into the code so it can be interpreted
        with open(os.path.join(sys.path[0], f"{file_name}"), "r") as f:
            contents = f.read()
            #The below step of the code turns the txt file into a list (The txt file has to be turned into the list so that the random choice module captures an entire word and not just a character)
            wordbank = contents.split()
            # By using the randomn choice vairable, the code randomly chosces a word from the list
            ans = random.choice(wordbank)

    # After the answer is chosen, the hidden vairable can be defined
    hidden = ['-'] * len(ans)

    players = int(input("How many players do you have? 1/2 ? "))

    if players == 1:
        name = input ("Ok then, what is your name? ")
        print(f"Hello {name}!")
        time.sleep(0.5)
        print(f"The answer has {len(ans)} letters!")
        time.sleep(0.5)
        print("Let's begin, start guessing!")
        time.sleep(0.5)
        while loop <= 6:
            guess = input("Guess? ")
            if guess.lower() in ans.lower():
                print(f"Correct")
                if len(guess) == 1:
                    for char in range(0, len(ans)):
                        if ans.lower()[char] == guess.lower():
                            hidden[char] = guess.upper()
                            underscores = "".join(hidden)
                            print(underscores)
                elif guess.lower() == ans.lower():
                    hidden = ans
                else:
                    print("That was not the word!")
                    loop = loop + 1
            else:
                print("That was incorrect!")
                loop = loop + 1
            if "-" not in hidden:
                print("You won!")
                loop = 8
            if loop > 0:
                print(hangmanpics[loop - 1])
        if "-" in hidden:
            print("What a shame you failed!")
            print(f"The word was {ans}")
    elif players == 2:
        name1 = input("Player 1, what is your name? ")
        name2 = input("Player 2, what is your name? ")
        print(f"Hello {name1} and {name2}!")
        while player_1_life + player_2_life <=6:
            if player_1_life <= 3:
                guess = input(f"Input a Guess {name1}! ")
                if guess.lower() in ans.lower():
                    print(f"Correct")
                    if len(guess) == 1:
                        for char in range(0, len(ans)):
                            if ans.lower()[char] == guess.lower():
                                hidden[char] = guess.upper()
                                underscores = "".join(hidden)
                                print(underscores)
                    elif guess.lower() == ans.lower():
                        hidden = ans
                    else:
                        print(f"That was not the word {name1}!")
                        player_1_life = player_1_life + 1
                        if player_1_life == 4:
                            print(f"What a shame {name1} has failed!")
                else:
                    print(f"That was incorrect {name1}!")
                    player_1_life = player_1_life + 1
                    if player_1_life == 4:
                        print(f"What a shame {name1} has failed!")
                if "-" not in hidden:
                    print(f"You won {name1}!")
                    loop = 9
                    player_1_life = 5
                if player_1_life > 0:
                    print(hangmanpicsfor2player[player_1_life - 1])
            if loop <= 6:
                if player_2_life <= 3:
                    guess = input(f"Input a Guess {name2}! ")
                    if guess.lower() in ans.lower():
                        print(f"Correct")
                        if len(guess) == 1:
                            for char in range(0, len(ans)):
                                if ans.lower()[char] == guess.lower():
                                    hidden[char] = guess.upper()
                                    underscores = "".join(hidden)
                                    print(underscores)
                        elif guess.lower() == ans.lower():
                            hidden = ans
                        else:
                            print(f"That was not the word {name2}!")
                            player_2_life = player_2_life + 1
                            if player_2_life == 4:
                                print(f"What a shame {name2} has failed!")
                    else:
                        print(f"That was incorrect {name2}!")
                        player_2_life = player_2_life + 1
                        if player_2_life == 4:
                            print(f"What a shame {name2} has failed!")
                    if "-" not in hidden:
                        print(f"You won {name2}!")
                        loop = 9
                        player_2_life = 5
                    if player_2_life > 0:
                        print(hangmanpicsfor2player[player_2_life - 1])
        if "-" in hidden:
            print("What a shame you both failed!")
            print(hangmanpicsfor2player[3])
            print(f"The word was {ans}")
    else:
        print("Looks like you have inputed an unsupported value. Please load the game again!")
    play = input("Want to play again (Y/N)? ")
    if play == "y" or "Y":
        continue
    else:
        play = False
        break



