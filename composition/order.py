from product import Product


class Order:
    """
    An order class has an id and a list of products. It
    is like a receipt.

    Member variables: id(string), products(Product[])

    Methods: get_subtotal(), get_tax(), get_total(), add_product(), display_receipt() 
    """

    def __init__(self):
        """
        id is initially set to a blank string
        products is initially an empty array
        """
        self.id = ''
        self.products = []

    def get_subtotal(self):
        """
        Iterates through the products array and adds their price
        to the subtotal. The subtotal is returned.

        Arguments: none

        Return: subtotal(float)
        """
        subtotal = 0
        for product in self.products:
            subtotal += product.get_total_price()

        return subtotal

    def get_tax(self):
        """
        Calculates the tax that will be charged on the subtotal
        at a rate of 6.5%. Returns the amount to be added as taxes

        Arguments: none

        Return: tax(float)
        """
        return self.get_subtotal() * .065

    def get_total(self):
        """
        Adds the subtotal and the tax and then returns that value.

        Arguments: none

        Return: total(float)
        """
        return self.get_subtotal() + self.get_tax()

    def add_product(self, product):
        """
        Appends a product object to the products array.

        Arguments: product(Product)

        Return: none
        """
        self.products.append(product)

    def display_receipt(self):
        """
        Prints the order information as follows:
        Order: order id
        product name (product quantity) - product price <- This will be displayed for each product in the array
        Subtotal: $xx.xx
        Tax: $xx.xx
        Total: $xxx.xx

        Arguments: none

        Return: none
        """
        print(f'Order: {self.id}')
        for product in self.products:
            product.display()
        print(f'Subtotal: ${self.get_subtotal():0.2f}')
        print(f'Tax: ${self.get_tax():0.2f}')
        print(f'Total: ${self.get_total():0.2f}')
