class Product:
    """
    The Product class is used to create an object with 
    an id, name, price, and quantity. These are all initialized 
    when the object is created.

    Member variables: id(string), name(string), price(float), quantity(int)

    Methods: get_total_price() - Returns product price * product quantity
                      display() - Prints product details like: name (quantity) - price 
    """

    def __init__(self, id, name, price, quantity):
        """
        Initializing memebr variables at object instantiation
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        """
        Retursn the total price of the product multiplied by its quantity

        Arguments: none

        Returns: total price (float)
        """
        return self.price * self.quantity

    def display(self):
        """
        Prints the product details in this format:
        Pencil (10) - $12.90
        Name (quantity) - price
        """
        print(f'{self.name} ({self.quantity}) - ${self.get_total_price():0.2f}')
