def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it!")

my_function()

# TO-DO: Describe the Problem - Write your unsears as comments:
# 1. What is the looping doing?
# the loop goes from a range of number from 1 to 19
# 2. When is the function meanty to print "You got it"?
#The function should print "You got it" when it gets to the number 20
# 3. What are you assumpiuton about the value of i?
#i is a counter, thats goes from 1 to 19. 

#To fix we can change tha range to (1,21) or (1,20+1)