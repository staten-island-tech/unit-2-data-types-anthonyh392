import os

# Clear the console
os.system('cls')

# Request inputs
verb1 = input('Enter the first (past tense) verb: ')
verb2 = input('Enter the second (present tense) verb: ')
name = input('Enter the name of the main character: ')
subject1 = input('Enter the subject pronoun for your character: ')
object1 = input('Enter the object pronoun for your character: ')
possessive1 = input('Enter the possessive pronoun for your character: ')
noun = input('Enter a noun (animal): ')
holiday = input('Enter the name of a holiday: ')
number = input('Enter a number: ')
celeb_guest = input('Enter the name of a celebrity guest: ')
subject2 = input('Enter the subject pronoun for your celebrity guest: ')
object2 = input('Enter the object pronoun for your celebrity guest: ')
possessive2 = input('Enter the possessive pronoun for your celebrity guest: ')

# Determine whether a/an should be used for the noun variable
x = 'a' if noun[0] != 'a' and noun[0] != 'e' and noun[0] != 'i' and noun[0] != 'o' and noun[0] != 'u' else 'an'

# Create the result
madlib = f'It was {holiday}, and {name}, along with {possessive1} seven other friends, were celebrating merrily around the fireplace. Everything seemed to be going great. Candles were lit, lanterns were hung, and {holiday} lights were chaotically scattered around the house. Suddenly, {x} {noun} fell from the roof and onto the lawn, startling {name} and {possessive1} guests. They all stopped what they were doing to take a closer look at the seemingly dead animal, until out of nowhere, hundreds of more {noun}s began sliding from the roof of the house and out onto the ground. However, this time, the {noun}s were alive, and one of them began to scream "{celeb_guest}" distinctly.'