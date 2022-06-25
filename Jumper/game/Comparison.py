
class comparison():
#Check if the user input matches the letter of the word
    def compare(word,user_input):
        list_of_text = list(word)
        #_user_letter = user_input

        if user_input in word:
            return True
        else:
            return False