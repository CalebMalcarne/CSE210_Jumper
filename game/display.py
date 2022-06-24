# Written by Michael Darling.

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

    def split_word(word):
        # Split up the word and display it.
        print(" ".join(word))