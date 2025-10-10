beers = 1
water = 2 #for testing

def more_beers(beer):
    print(f'Beers inside function: {beers}')
    return beer + 1

beers = more_beers(beers)
print(f"Beers outside function: {beers}")
print(f"\n {'-' * 20}\n")

#Global scope can be useful in:
#Global Constants - variables that never changes:
#for conventions the name ll be all uppercase
PI = 3.14159

print(f"\n {'-' * 20}\n")


