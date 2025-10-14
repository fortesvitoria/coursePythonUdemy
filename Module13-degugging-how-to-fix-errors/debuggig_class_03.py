'''
Playing computer is an important skill in debugging. You need to be able to go through your code line by line as if you were the computer to help you figure out what is going wrong.

PAUSE 1
Play computer and go through the code line by line as if you were executing the code to figure out why 1994 does not work as expected. Then go ahead and fix the code.
'''
year = int(input("What's your year of birth?\n"))

#the problem is that it never gets 1994, so we need to add a <= 1994 to the millenials
# if year > 1980 and year < 1994:
if year > 1980 and year <= 1994: #fixed
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
