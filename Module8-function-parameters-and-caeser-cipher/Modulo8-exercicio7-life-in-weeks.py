'''
Life in Weeks
Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Example Input
56
Example Output
You have 1768 weeks left.
'''
#Create a function called life_in_weeks()
def life_in_weeks(age):
    weeks_lived = (age * 365) / 7
    #print(weeks_lived)
    weeks_life = (90 * 365) / 7
    weeks_left = weeks_life - weeks_lived
    print(f'You got {weeks_left} weeks left!')

life_in_weeks(56)