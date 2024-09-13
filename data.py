import os

# Clear the console
os.system('cls')

# Request inputs
verb1 = input('Enter the first (present tense) verb: ')
verb2 = input('Enter the second (present tense) verb: ')
name = input('Enter the name of the main character: ')
possessive1 = input('Enter the possessive pronoun for your character: ')
noun = input('Enter a noun (animal): ')
holiday = input('Enter the name of a holiday: ')
number = input('Enter a number: ')
celeb_guest = input('Enter the name of a celebrity guest: ')

# Determine whether a/an should be used for the noun variable
x = 'a' if noun[0] != 'a' and noun[0] != 'e' and noun[0] != 'i' and noun[0] != 'o' and noun[0] != 'u' else 'an'

# Create the result
madlib = f'''
It was {holiday}, and {name}, along with {possessive1} seven other friends, were {verb1} merrily around the fireplace. Everything seemed to be going great. Candles were lit, lanterns were hung, and {holiday} lights were decoratively scattered around the house. Suddenly, {x} {noun} fell from the roof and onto the lawn, startling {name} and {possessive1} guests. They all stopped what they were doing to take a closer look at the seemingly dead animal, until out of nowhere, {number} more {noun}s began sliding from the roof of the house and out onto the ground. However, this time, the {noun}s were alive, and one of them began to scream "{celeb_guest}" distinctly. All of a sudden, {celeb_guest} dropped from the sky, pointing a machine gun at the people.

In the span of just ten minutes, the entire neighborhood had been destroyed. There was no sign of life remaining in the area. Since that horrific event, no one had ever been able to uncover what had happened, and I don't think they would ever be able to. I, {celeb_guest}, am currently {verb2} at my desk, planning an ultimate attack on my next fellow victims.
'''

print(madlib)