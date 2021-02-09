from order import Order


class Customer:
    """
    A Customer object has an id, name, and an array of orders. This can be used
    to keep track of customer purchases.

    Member Variables: id(string), name(string), orders(Order[])

    Methods: get_order_count(), get_total(), add_order(), display_summary(), display_receipts()
    """

    def __init__(self):
        """
        Initializes all member variables to empty values.
        id = empty string
        name = empty string
        orders = empty Order array
        """
        self.id = ''
        self.name = ''
        self.orders = []

    def get_order_count(self):
        """
        Uses the len() function to returnt he length of the orders array.

        Arguments: none

        Return: orders length (int)
        """
        return len(self.orders)

    def get_total(self):
        """
        Iterates through the orders array and calls the get_total method for
        each order. The returned value is added the the total local variable.
        The total is returned.

        Arguments: none

        Return: Total(float)
        """
        total = 0
        for order in self.orders:
            total += order.get_total()

        return total

    def add_order(self, order):
        """
        Appends an order object to the orders array.

        Arguments: order(Order)

        Return: none
        """
        self.orders.append(order)

    def display_summary(self):
        """
        Prints a summary for the customer in this format:
        Summary for customer id:
        Name: name
        Orders: total orders
        Total: total spent on orders

        Arguments: none

        Return: none
        """
        print(f'Summary for customer \'{self.id}\':')
        print(f'Name: {self.name}')
        print(f'Orders: {self.get_order_count()}')
        print(f'Total: {self.get_total():.02f}')

    def display_receipts(self):
        """
        Iterates through the orders and calls display_receipt() on
        each order.
        Prints the receipts for a customer in this format:

        Detailed receipts for customer id:
        Name: name

        Order: order id
        product name (product quantity) - product price <- This will be displayed for each product in the array
        Subtotal: $xx.xx
        Tax: $xx.xx
        Total: $xxx.xx

        Arguments: none

        Return: none
        """
        print(f'Detailed receipts for customer \'{self.id}\':')
        print(f'Name: {self.name}')
        for order in self.orders:
            print()
            order.display_receipt()
