'''
# Create a function that determines if a function is odd or even.
def odd_or_even(num):
    print(f'{num} is odd!' if num % 2 != 0 else f'{num} is even!')

num = int(input('Enter a number: '))
odd_or_even(num)
'''

'''
# Create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was bad, okay, good, or great.
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
'''

'''
# Create a function that accepts an input and determines all factors of the number.
def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(str(i))
    
    print(f'The factors of {num} are: {', '.join(factors)}.')

factor(1000)
'''

# Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.
def gcf(num1, num2):
    pass

'''
# MadLibs
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
'''