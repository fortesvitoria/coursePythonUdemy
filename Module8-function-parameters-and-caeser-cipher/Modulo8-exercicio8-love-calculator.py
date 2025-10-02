'''
Love Calculator
💪 This is a difficult challenge! 💪
You are going to write a function called calculate_love_score() that tests the compatibility between two names.
To work out the love score between two people:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number and print it out.

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

Love Score = 53


Example Input

calculate_love_score("Kanye West", "Kim Kardashian")

Example Output
42



How to test your code and see your output?

Udemy coding exercises do not have a console, so you cannot use the input() function.
You will need to call your function with hard-coded values like so:

    def calculate_love_score(name1, name2):
      # your code here

    # Call your function with hard coded values
    calculate_love_score("Kanye West", "Kim Kardashian")
'''

#cria função
def calculate_love_score(name1, name2):
    soma1 = 0
    soma2 = 0
    for i in name1.lower():
        if i == 't':
            soma1 += 1
        elif i == 'r':
            soma1 += 1
        elif i == 'u':
            soma1 += 1
        elif i == 'e':
            soma1 += 1

    for i in name2.lower():
        if i == 't':
            soma1 += 1
        elif i == 'r':
            soma1 += 1
        elif i == 'u':
            soma1 += 1
        elif i == 'e':
            soma1 += 1

    for i in name1.lower():
        if i == 'l':
            soma2 += 1
        elif i == 'o':
            soma2 += 1
        elif i == 'v':
            soma2 += 1
        elif i == 'e':
            soma2 += 1
    for i in name2.lower():
        if i == 'l':
            soma2 += 1
        elif i == 'o':
            soma2 += 1
        elif i == 'v':
            soma2 += 1
        elif i == 'e':
            soma2 += 1

    print(f'{soma1}{soma2}')
calculate_love_score('Vitoria','Eduardo')