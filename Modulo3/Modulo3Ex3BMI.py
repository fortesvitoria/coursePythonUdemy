#BMI Calculator with Interpretations
#Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
#If the bmi is under 18.5 (not including), print out "underweight"
#If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
#If the bmi is 25 (including) or over, print out "overweight"
name = input('Digite seu nome: ')
weight = float(input(f'{name} digite seu peso: '))
height = float(input(f'{name} digite sua altura: '))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f'{name} your weight is {weight:.2f}, your height is {height:.2f} and your BMI is {bmi:.2f}. You are underweight!')
elif bmi >= 18.5 and bmi < 25:
    print(f'{name} your weight is {weight:.2f}, your height is {height:.2f} and your BMI is {bmi:.2f}. You are ate a normal weight')
else:
    print(f'{name} your weight is {weight:.2f}, your height is {height:.2f} and your BMI is {bmi:.2f}. You are overweight!')