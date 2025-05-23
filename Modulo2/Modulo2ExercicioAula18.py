print('Welcome to the tip calculator!')

totalBill = float(input('What was the total bill? '))
percentageTip = int(input('How much tip would you like to give? 10, 12 or 15? '))
split = int(input('How many people to split the bill? '))
tip = percentageTip / 100
bill = totalBill * (1+tip) / split

print(f'The total bill as {totalBill}, the tip percentage was {percentageTip}% splited by {split} people. ')
print(f'Each person should pay {bill:.2f}')