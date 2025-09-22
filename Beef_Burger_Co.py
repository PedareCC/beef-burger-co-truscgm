import time
#Menu items
beef_burgers = {
    'cheeseburger': 
        {
            'price': 12.50, 
            'toppings': ['cheese', 'pickles', 'onion', 'ketchup', 'mustard', 'lettuce', 'tomato', 'mayo']
        }, 
    'beef burger': 
        {
            'price': 16.50,
            'toppings': ['cheese', 'beef patty', 'onion', 'ketchup', 'mustard', 'lettuce', 'tomato', 'mayo']
        },
    'schlumberger':
        {
            'price': 17.60,
            'toppings': ['cheese','beef patty', 'caramelized onions', 'mushrooms', 'lettuce', 'tomato', 'ketchup', 'mustard', 'mayo', 'barbeque sauce']
        },
    'triple bacon artery clogger':
        {
            'price': 19.99,
            'toppings': ['cheese', 'beef patty', 'bacon', 'lettuce', 'tomato', 'onion', 'ketchup', 'mustard', 'mayo']
        }
}
drinks = {
    'large coca cola':
    { 'price': 3.50 },
    'medium coca cola':
    { 'price': 2.50 },
    'small coca cola':
    { 'price': 1.50 },
    'large fanta':
    { 'price': 3.50 },
    'medium fanta':
    { 'price': 2.50 },
    'small fanta':
    { 'price': 1.50 }
}
chips = {
    'waffle fries': { 'price': 2.99 },
    'curly fries': { 'price': 3.40 },
    'shoestring': { 'price': 3.99 },
    'wedges': { 'price': 4.25 },
    'sweet potato': { 'price': 4.99 },
    'standard fries': { 'price': 2.50 }
}
bailey_burgers = list(beef_burgers.keys())
bailey_sides = list (chips.keys())
bailey_drinks = list(drinks.keys())
customer_order = []
credit_card_details = []

def order():
    print()
    print('--- Beef Burger Menu ---')
    print('1. Burger')
    print('2. Drink')
    print('3. Sides')
    print('4. View order')
    print('5. Checkout')
    print()
    user_input = input('What would customer like to do? ')
    if user_input == '1':
        print('--- Burger Menu ---')
        for i in range(len(bailey_burgers)): #Loops through the dictionary and prints the menu items with their prices
            print(f'{i + 1}. {bailey_burgers[i].title()}: ${beef_burgers[bailey_burgers[i]]['price']:.2f}') 
        burger_input = int(input('What does the customer want? '))
        print()
        burger_input = bailey_burgers[burger_input - 1]
        if burger_input in beef_burgers:
            print(f'You have selected a {burger_input} which costs ${beef_burgers[burger_input]["price"]:.2f}')
            time.sleep(1)
            print()
            print('Toppings include:')
            for topping in beef_burgers[burger_input]['toppings']:
                print(f'- {topping.title()}')
            time.sleep(1)
            user_input = input('Would you like to edit toppings? (y/n) ')
            burger = [burger_input, beef_burgers[burger_input]['price'], []]
            if user_input.lower() == 'y':
                toppings_edit = True
                while toppings_edit:
                    remove_ingredients = []
                    user_input = input('Enter toppings to remove, separated by commas: ').lower()
                    toppings_to_remove = [topping.strip() for topping in user_input.split(',')]
                    for topping in toppings_to_remove:
                        if topping in beef_burgers[burger_input]['toppings']:
                            remove_ingredients.append(topping)
                            print(f'Removed {topping}')
                        else:
                            print(f'{topping} not found in toppings')
                    burger[2] = remove_ingredients
                    toppings_edit = False
                customer_order.append([f'{burger[0]} - {burger[1]} - No {", ".join(burger[2])}', burger[1]])
            else:
                customer_order.append([f'{burger[0]} - ${burger[1]}', burger[1]])
            print('Item added to order')
            order()
        else:
            print('Invalid input')
            order()
    elif user_input == '2':
        print('--- Drinks Menu ---')
        for i in range(len(bailey_drinks)): #Loops through the dictionary and prints the menu items with their prices
            print(f'{i + 1}. {bailey_drinks[i].title()}: ${drinks[bailey_drinks[i]]['price']:.2f}') 
        drink_input = int(input('What does the customer want? '))
        drink_input = bailey_drinks[drink_input - 1]
        if drink_input in drinks:
            drink_order = (drink_input, drinks[drink_input]['price'])
            print(f'You have selected a {drink_input} which costs ${drinks[drink_input]['price']:.2f}')
            customer_order.append([f'{drink_order[0]} - ${drink_order[1]:.2f}', drink_order[1]])
            print('Item added to order.')
            order()
        else:
            print('Invalid input')
            order()
    elif user_input == '3':
        print('--- Sides Menu ---')
        for i in range(len(bailey_sides)): #Loops through the dictionary and prints the menu items with their prices
            print(f'{i + 1}. {bailey_sides[i].title()}: ${chips[bailey_sides[i]]['price']:.2f}') 
        sides_input = int(input('What does the customer want? '))
        sides_input = bailey_sides[sides_input - 1]
        if sides_input in chips:
            sides_order = [sides_input, chips[sides_input]['price']]
            print(f'You have selected a {sides_input} which costs ${chips[sides_input]['price']:.2f}')
            customer_order.append([f'{sides_input} - ${sides_order[1]:.2f}', sides_order[1]])
            print('Item added to order.')
            order()
    elif user_input == '4':
        print('--- Current Order ---')
        total = sum(item[1] for item in customer_order)
        for item in customer_order:
            print(item[0])
        print(f'Customer Total: ${total:.2f}')
    elif user_input == '5':
        print('--- Checkout ---')
        total = sum(item[1] for item in customer_order)
        for item in customer_order:
            print(item[0])
        print(f'Customer Total: ${total:.2f}')
        user_input = input('Please put in credit card details to pay: ')
        credit_card_details.append(user_input)
        print('Order successful')
        print('I stole your credit card details :)')
        print(credit_card_details)
    else:
        print('Invalid input')
        order()
while True: 
    order()