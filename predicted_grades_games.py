#In this game, you must travel from teacher to teacher to try to make a joke to them, and get your predicted grade increased


class Scene:
    def enter(self):
        print ('The scene isn\'t configured yet.')
        exit(1)
    
    
    
    def correct_answer(self): #this should be a staticmethod
        print ('Teacher: You been listening to my jokes in class! A H1 for you!')
        print ('\nCleared\n*************')
        if Map.list_of_scenes_for_display==[]:
            print ('Congradulations, you won!\nThese jokes do not reflect my former teachers in real life, all of whom I was very fortunate to obtain.')
            exit(0)
        
        Corridor.list_remaining_teachers()
        
    def incorrect_answer(self):
        print ('Teacher: I never particularly liked you anyway. Go to the principal\'s office!')
        print ('\n\n\n-------------\nYou have failed.')
        exit(0)
        
class English(Scene):
    def enter(self):
        print ('Teacher: What is one thing children and my English teacher don\'t like?\n') #don't judge me
        print ('a. Sibilance!\nb. The patriarchy!\nc. Online school!\n')
        action = input('>')
        
        if action=='a':
            self.correct_answer()
        else:
            self.incorrect_answer()
            
        

class Irish(Scene):
   def enter(self):
        print ('Teacher: What did the husband say to his wife in the poem \'Scaradar?\'\n') #don't judge me
        print ('a. Nothing - it\'s a trick question!\nb. That she could lose a few pounds of weight, and not money for once!')
        print ('c. I don\'t know, I\'ve never done any work in your classes\n')
        action = input('>')
        
        if action=='a': #this may be factually incorrect, I never actually read the poem
            self.correct_answer()
        else:
            self.incorrect_answer()
   
    
    
class Maths(Scene):
   def enter(self):
        print ('Teacher: Why was the Maths book sad?\n') #don't judge me
        print ('a. Because you were relying on it to do your job for you!\nb. Because it had too many problems!\nc. Because it was trying to teach me!\n')
        action = input('>')
        
        if action=='b' or action=='c':
            self.correct_answer()
        else:
            self.incorrect_answer()

class French(Scene):
   def enter(self):
        print ('Teacher: Who did I want to win the 2022 French Presidential election?\n') #don't judge me
        print ('a. Eric Zemmour!\nb. Emmanuel Macron!\nc. Neither!\n')
        action = input('>')
        
        if action=='c':
            self.correct_answer()
        else:
            self.incorrect_answer()

class Business(Scene):
   def enter(self):
        print ('Teacher: What message did I send to my friend who was on a yacht off the coast of Spain?\n') #don't judge me
        print ('a. I hope you have a lovely time!\nb. Bring some of the women home!\nc. I would probably break some guideline by repeating that joke.\n')
        action = input('>')
        
        if action=='c':
            self.correct_answer()
        else:
            self.incorrect_answer()

class Biology(Scene):
   def enter(self):
        print ('Teacher: What did the medicine student do over Christmas?\n') #don't judge me
        print ('a. Study.\nb. Enjoy the company of their family!\nc. Socialise over a drink with friends!\n')
        action = input('>')
        
        if action=='a':
            self.correct_answer()
        else:
            self.incorrect_answer()

class History(Scene):
   def enter(self):
        print ('Teacher: As Josef Stalin once said, dark humour is...?\n') #don't judge me
        print ('a. inappropriate.\nb. funny!\nc. like food - not many people get it\n')
        action = input('>')
        
        if action=='c':
            self.correct_answer()
        else:
            self.incorrect_answer()

class Art(Scene):
   def enter(self):
        print ('Teacher: Why couldn\'t the artist get a loan?\n') #don't judge me
        print ('a. He was always drawing a blank!\nb. He was bad at his job!\nc. You would not appreciate my answer.\n')
        action = input('>')
        
        if action=='a':
            self.correct_answer()
        else:
            self.incorrect_answer()




class Corridor(Scene):
    def list_remaining_teachers():
        print ('Teachers remaining:')
        for teacher in Map.list_of_scenes_for_display:
            if (teacher==Map.list_of_scenes_for_display[len(Map.list_of_scenes_for_display)-1]): #if it's the last entry, finish with a . instead of a ,
                print ('%s.' % teacher)
            else:
                print ('%s,' % teacher)
        
        Corridor.enter_next_scene() #I split them up into two functions just for clarity, although it's not necessary
    
    def enter_next_scene():
        next_scene_name = input('What teacher would you like to befriend next?\n>')
        print ('\n')
        current_scene = Map.scenes[next_scene_name]
        Map.list_of_scenes_for_display.remove(next_scene_name)  #I have two lists, one for accessing and one for display
        current_scene.enter()                                   #Since the value of the key-value pair in Map.scenes is a class, I can't just delete it using del() or pop()

class Map:
    scenes = {'English': English(), 'Irish':Irish(), 'Maths': Maths(), 'French': French(), 
    'Business': Business(), 'Biology': Biology(), 'History': History(), 'Art': Art()} #not gonna name my teachers, just in case this ever finds its way to them
    
    list_of_scenes_for_display = ['English', 'Irish', 'Maths', 'French', 
    'Business', 'Biology', 'History', 'Art'] #I have two lists, one for accessing and one for display
    #                                         Since the value of the key-value pair in Map.scenes is a class, I can't just delete it using del() or pop()


print ('''\n\nHello, this is a game I made to teach myself class inheritance. I know some of the jokes are very one-dimensional, 
but that is the extent of my humour and wit, resign yourself to it, I did long ago.
In this game, you must go to teachers, listen to their jokes and pick the right answer to prove that you\'ve been
listening to their jokes. You are doing this because you are receiving predicted grades this year, and you need
to be on your teachers\' good side.

To answer, enter the letter assigned to the option on the left hand side, ie, 
Why did the chicken cross the road?

a. *An answer*

Here, you should enter:
>a

When it asks you to enter a teacher, use CamelCase, ie, 'Art, Business, Maths' etc
I did not have the time for proper error handling, if you give an answer like 'd', it will just abort the program
Thanks for playing, and (please try to) enjoy:
\n\n\n-------------\n''')

Corridor.list_remaining_teachers()




#   python predicted_grades_games.py
        
    