provicen = input('What province do you live in? ')
tax = 0

# if provicen == 'Alberta':
#     tax = 0.5
# if provicen == 'Nenavut':
#     tax = 0.5
# if provicen == 'Onatairo':
#     tax = 0.13
# print(tax)

#if provicen == 'Alberta' or provicen == 'Nenavut':
if provicen in('Alberta', 'Nenavut'):
    tax = 0.05
elif provicen == 'Onatairo':
    tax = 0.13
else:
    tax = 0.15
print(tax)
