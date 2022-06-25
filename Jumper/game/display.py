# Written by Michael Darling
import os
import sys

class Display:
    
    def __init__(self):
        self.body = []
        self.danger_floor = ""

    def create_jumper(self):
        # Set up jumper man.
        self.body = []
        self.body.append("  ___  ")
        self.body.append(" /___\ ")
        self.body.append(" \   / ")
        self.body.append("  \ /  ")
        self.body.append("   0   ")
        self.body.append("  /|\  ")
        self.body.append("  / \  ")
        # Set up the floor under the guy, seperated
        # so that it doesn't mess up the counter.
        self.danger_floor = "^^^^^^^"

    def lose(self):
        
        self.body[0]= ("   X   ")
        self.display_jumper(self)

    def display_jumper(self):
        # Display the jumper.
        print()
        for i in range(len(self.body)):
            print(self.body[i])
        print()
        print(self.danger_floor)

    def update_jumper(self):
        # Remove body parts.
        self.body.pop(0)

    def split_word(self, word, answers):
        my_os=sys.platform
        if my_os == "win32":
            os.system('cls')
        else:
            os.system('clear')
        #checks to see which correct answers have been guessed
        #if it has it prints the letter otherwise is pritns '_'
        word_State = ""       
        for letter in word:
            if letter in answers:
                word_State += letter + ' '
            else:
                word_State += '_ '
        print(word_State)
        if self.get_Status(self) == 3:
            print("To many faild guess's!, You Lose!")
        elif ''.join(answers) == word:
            print("Correct!, You Win!")


    def get_Status(self):
        return len(self.body)
    
