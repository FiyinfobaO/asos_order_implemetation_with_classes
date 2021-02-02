import pandas as pd


class Order:
    def __init__(self, loc):
        self.cart = []  # cart that stores all items about to be purchased
        # list of items with prices in the store
        self.items = {'bag': 10.03, 'brogues': 51.48, 'loafers': 31.27,
                      'plainTees': 10.03, 'shirt': 20.84, 'sneakers': 21.63,
                      'glasses': 13, 'chain': 9.5, 'derby': 48.32}
        self.location = loc
        self.cost = 0

    def add_items(self, item):  # to add items to the cart
        self.cart.append(item)

    def remove_items(self, item):  # to remove items from the cart
        self.cart.remove(item)

    def s_cost(self, item):  # gets the cost for a particular item
        return self.items[item]

    def get_cost(self):  # gets the cost of all items in the cart
        for item in self.cart:
            self.cost += self.items[item]
        return self.cost

    def place_order(self):  # places the order
        if self.location == 'Nigeria' and self.cost > 100:
            return False
        return True


# initializes the class with Nigeria as the location
order = Order(loc='Nigeria')
store = pd.DataFrame({'Items': ['bag',
                                'brogues',
                                'loafers',
                                'plainTees',
                                'shirt',
                                'sneakers',
                                'glasses',
                                'chain',
                                'derby'],
                      'Price ($)': [10.03,
                                    51.48,
                                    31.27,
                                    10.03,
                                    20.84,
                                    21.63,
                                    13,
                                    9.5,
                                    48.32]})
print(store, '\n')

try:
    items = input(
        'Welcome to FOBZ STORE. Please select what you would like to order? ').split()
    for i in items:
        order.add_items(i)
        print(f'Added {i} which cost {order.s_cost(i)} dollars')
except KeyError:
    print('Error with spelling')
    order.cart.clear()  # clears the cart
    items = input('Please reselect what you would like to order ').split()
    for i in items:
        order.add_items(i)
        print(f'Added {i} which cost {order.s_cost(i)} dollars')


def plac_ord(answer):
    if answer.lower() == 'yes' or answer.lower() == 'yeah' or answer.lower() == 'yup' or \
            answer.lower() == 'yh' or 'ye' in answer.lower() or 'yu' in answer.lower():
        # get the total cost of all the items
        cost = order.get_cost()
        print(
            f'The total cost of all the items for this order is {cost} dollars')
        val = input('Should i proceed with the order? ')
        if val.lower() == 'yes' or val.lower() == 'yeah' or val.lower() == 'yup' or \
                val.lower() == 'yh' or 'ye' in val.lower() or 'yu' in val.lower():
            success = order.place_order()
            if success:
                print(
                    f'Order Successful. You have ordered {len(order.cart)} item namely, '
                    f'{str(order.cart)} with a total cost of ${cost}')
            else:
                print('Order Unsuccessful.')
        else:
            print('Okay. Have a great day 😒😑')

    elif answer.lower() == 'no' or answer.lower() == 'nope' or answer.lower() == 'naa' or \
            answer.lower() == 'atall' or 'no' in answer.lower() or 'na' in answer.lower():
        k = input(
            'Do you want to add or remove items or you wish to cancel the order? ')
        if 'remove' in k:
            h = input('What items do you want to remove? ').split()
            for n in h:
                order.remove_items(n)
                print(f'Removed {n} which cost {order.s_cost(n)} dollars')
            asd = input(
                f'Removed {len(h)} items from cart. Are you ready to place the order now? ')
            plac_ord(asd)
        elif 'add' in k:
            h = input('What items do you want to add? ').split()
            for n in h:
                order.add_items(n)
                print(f'Added {n} which cost {order.s_cost(n)} dollars')
            asd = input(
                f'Added {len(h)} items to cart. Are you ready to place the order now? ')
            plac_ord(asd)
        elif 'cancel' in k:
            print('Alright! Have a nice day')
    else:
        print('Please enter a valid answer')


answer = input('Are you ready to place your order? ')
plac_ord(answer)
