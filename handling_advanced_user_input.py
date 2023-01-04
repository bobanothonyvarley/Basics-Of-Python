#this program will scan user input, and primitively sort them into different types of words, ie, nouns, verbs, etc.
#It doesn't apply these new meanings to anything, it just catagorises your words

#In the Lexicon class is all the words that this program can identify

class Lexicon:
    direction_words = {'north': 'north', 'south': 'south', 'east': 'east', 'west': 'west', 
    'left': 'left', 'right': 'right', 'up': 'up', 'down': 'down', 'forward': 'forward', 'back':'back', 
    'word_type': 'DIRECTION'}                                                                          #do I need to have a value if the key is identical?
    verbs = {'go': 'go', 'stop': 'stop', 'kill': 'kill', 'eat': 'eat', 'word_type': 'VERB'}
    stop_words = {'the': 'the', 'in': 'in', 'of': 'of', 'from':'from', 'at': 'at', 'it':'it', 'and': 'and', 'word_type': 'STOP_WORD'}
    nouns = {'door': 'door', 'bear': 'bear', 'princess': 'princess', 'cabinet': 'cabinet', 'word_type': 'NOUNS'}
    types_of_words = [direction_words, verbs, stop_words, nouns]
    
    def convert_string_to_number(number):
        try:
            return int(number)
        except ValueError:
            return None



def input_scanner(input):
    list = input.casefold()  #change string to lowercase
    list = list.replace((',', '.', '\'', '\"'), '')
    sentence = list.split(' ')
    count = 0 #used to index into list

    for i in sentence: #this compares the current (user input) word to every word in the Lexicon
        current_element_is_in_Lexicon = False #used for error handling
        for current_type_of_word in Lexicon.types_of_words:
            for word in current_type_of_word:
                if (word==i):
                    #sentence[i] = ('direction', word) #doesn't work, because i is string, and for index I need integer
                    
                    sentence[count] = (current_type_of_word['word_type'], word)
                    current_element_is_in_Lexicon = True
        
        #checking if i is a number, or not in lexicon
        if (current_element_is_in_Lexicon==False):
            current_element = Lexicon.convert_string_to_number(i)
            if (current_element==None):
                sentence[count] = ('ERROR', i)
            else:
                sentence[count] = ('NUMBER', i)
        else:
            pass
        
        count += 1 #used to change current element of sentence[]
    return sentence
    
    
def convert_user_input():
    finished = False
    while (not finished):
        user_input = input('Enter your next action, or type \'finished\' to stop\n>')
        if (user_input=='finished'):
            finished = True
        else:
            sentence = input_scanner(user_input)
            print (sentence)
    



convert_user_input()


# py __init__.py

