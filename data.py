import os
import time

os.system('cls')

# Tip calculator
print('TIP CALCULATOR\n')
bill = float(input('What is the bill? '))
tip = int(int(input('What is the tip (as a percentage)? ')) / 100 * bill)
total_amount = bill + tip
print(f'Your total is ${total_amount}.')

time.sleep(3)
os.system('cls')

# Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. First write out your plan using comments. Then craft the function.
# Set the variable "sentence" to an input
# Split the sentence into an array using a whitespace as a separator
# Count the length of the array and print the length
print('WORDS COUNTER\n')
sentence = input('Enter a sentence: ')
words = sentence.split(' ')
length = len(words)
print(f'Your sentence has {length} word(s).')

time.sleep(3)
os.system('cls')

# Create a function that determines if a function is odd or even.
print('EVEN OR ODD\n')
def odd_or_even(num):
    print(f'{num} is odd!' if num % 2 != 0 else f'{num} is even!')

num = int(input('Enter a number: '))
odd_or_even(num)

time.sleep(3)
os.system('cls')

# Create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was bad, okay, good, or great.
print('SERVICE CALCULATOR\n')
def tip(bill, service):
    service = service.lower()

    if service == 'bad':
        tip = '0%'
    elif service == 'okay':
        tip = '15%'
        bill *= 1.15
    elif service == 'good':
        tip = '20%'
        bill *= 1.2
    elif service == 'great':
        tip = '25%'
        bill *= 1.25
    else:
        print('Invalid bill!')
        return
    
    print(f'You tipped {tip}! Your bill is now {bill}.')

tip(81.00, 'great')

time.sleep(3)
os.system('cls')

# Create a function that accepts an input and determines all factors of the number.
print('FACTORS OF A NUMBER\n')
def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(str(i))
    
    print(f'The factors of {num} are: {', '.join(factors)}.')

factor(1000)

time.sleep(3)
os.system('cls')

# Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.
print('GCF CALCULATOR\n')
def gcf(first_number, second_number):
    minimum = min(first_number, second_number)
    factors = []
    for number in range(1, minimum + 1):
        if first_number % number == 0 and second_number % number == 0:
            factors.append(number)
    print(factors[len(factors) - 1])

gcf(20, 50)

time.sleep(3)
os.system('cls')

# MadLibs
print('MADLIBS PROJECT\n')
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
madlib = f"""
It was {holiday}, and {name}, along with {possessive1} seven other friends, were {verb1} merrily around the fireplace. Everything seemed to be going great. Candles were lit, lanterns were hung, and {holiday} lights were decoratively scattered around the house. Suddenly, {x} {noun} fell from the roof and onto the lawn, startling {name} and {possessive1} guests. They all stopped what they were doing to take a closer look at the seemingly dead animal, until out of nowhere, {number} more {noun}s began sliding from the roof of the house and out onto the ground. However, this time, the {noun}s were alive, and one of them began to scream "{celeb_guest}" distinctly. All of a sudden, {celeb_guest} dropped from the sky, pointing a machine gun at the people.

In the span of just ten minutes, the entire neighborhood had been destroyed. There was no sign of life remaining in the area. Since that horrific event, no one had ever been able to uncover what had happened, and I don't think they would ever be able to. I, {celeb_guest}, am currently {verb2} at my desk, planning an ultimate attack on my next fellow victims.
"""

print(madlib)