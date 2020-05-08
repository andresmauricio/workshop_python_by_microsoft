price = input('how much did you pay? ')
price = float(price)

if price  >= 1.00:
    tax = .70
else:
    tax = 0
print(f'Tac rate is: {tax}')

#compare string 
conuntry = input('Enter the name of your home conuntry: ')

if conuntry.lower() == 'canada':
    print('So you must like hockey')
else:
    print('You are not from Canada')

