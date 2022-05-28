#Author: Joseph Carlson
#Purpose: Dune Adventure game.


import pygame




#Introduction
print('“God created Arrakis to train the faithful.”')

print('Welcome to Arrakis! Home of the Spice Melange. To get you started on your journey, we need to get to know you a little bit better..')


#Character Creation

#character_stats = 


name = input('What is your name? ')
gender = input('What gender do you identify yourself? ')

home = input('Is Arrakis your home world? ')

if home == "Yes":
    print('Ah, you must be a Fremen then')

else: input('What is your home world then? ')


# Do a little experimenting with this.  
if home != "Yes":
    
    character_class = ""
    while character_class != "Warrior" or character_class != 'Mentat':
        character_class = input('Are you a Warrior or a Mentat? ')


        if character_class == "Warrior":
            print('Arrakis always needs more Warriors.')
            break

        elif character_class == "Mentat":
            print('The wise always prevail on Arrakis.')
            break

        else: print(character_class + ' is not a valid input, please try again')


