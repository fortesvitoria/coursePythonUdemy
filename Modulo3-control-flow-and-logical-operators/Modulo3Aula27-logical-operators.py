'''
Logical operators
A and B --- A^B
C or D --- C v D
not E --- ¬D
'''

a = 12
print('Operator E - ^')
if a > 10 and a <13:
    print(True)
    #both true
else:
    print(False)

print('*' * 15)
print('Operator OR - v')

if a > 10 or a >13:
    print(True)
    #at list one true
else:
    print(False)

print('*' * 15)
print('Operator NOT - ¬')

if not a < 0:
    print(True)
    #reverse, if true become false, if false become true
else:
    print(False)