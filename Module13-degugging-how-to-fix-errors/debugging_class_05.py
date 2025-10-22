'''
print() is your friend. It can help expose hidden values while your code is running. In a for loop, the loop will follow some rules to perform a repeated block of code. But during the loop it's difficult to see the intermediate values, that's a perfect example of how you can use print to expose those intermediate values and help you debug your code.

PAUSE 1
The code is supposed to calculate the total number of words given the number pages and the word per page. But it's not currently giving any output. Diagnose the problem using print() statements.

PAUSE 2
Fix the code.

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) #fixed here, instead of '==' use the assignment operator '='
total_words = pages * word_per_page
print(total_words)


'''

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
