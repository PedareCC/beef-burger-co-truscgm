beef_burgers = {'Cheeseburger': 12.50, 'Beef Burger': 16.50, 'Schlumberger': 17.60, 'Triple Bacon Artery Clogger': 19.99}
drinks = {'Large Coca Cola': }

cheeseburger = ['Cheese', 'Pickles', 'Onion', 'Ketchup']
schlumberger = ['']

customer_order = []

def order():
    print('')
    print('--- Beef Burger Menu ---')
    print('1. Burger')
    print('2. Drink')
    print('3. View/edit order')
    print('4. Checkout')
    print('')
    user_input = input('What would customer like to do? ')
    if user_input == '1':
        for burger in beef_burgers:
            print(f'{burger}: ${beef_burgers[burger]:.2f}')
    elif user_input == '2':
        print('2')
    elif user_input == '3':
        print('3')
    elif user_input == '4':
        print('4')
    else:
        print('Invalid input')
        order()
order()



'''
total_order = []      
total_order_prices = []   

def menu():
    print('--- Beef Burger Menu ---')
    print(f"1. Cheeseburger for ${beef_burgers['Cheeseburger']}")
    print('2. Go to checkout.')


def customer_order():
        order = input('Select what you would like to order: ')
  
        if order == 1:

        elif

        else 

def check_out():
    print('\n--- Your Order Summary ---')


print('Welcome to the Beef Burger Co. menu!')
menu()
customer_order()
check_out()
'''