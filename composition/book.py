class Book:
    def __init__(self):
        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"

    def display(self):
        print(
            f'{self.title}\nPublisher:\n{self.publisher}\nAuthor:\n{self.author.display()}')


class Person:
    def __init__(self):
        self.name = "anonymous"
        self.birth_year = "unknown"

    def display(self):
        return f'{self.name} (b. {self.birth_year})'


def main():
    book = Book()
    book.display()
    print("\nPlease enter the following:")
    book.author.name = input("Name: ")
    book.author.birth_year = input("Year: ")
    book.title = input("Title: ")
    book.publisher = input("Publisher: ")
    print()
    book.display()


if __name__ == "__main__":
    main()


class Order:
    def __init__(self):
        self.products = []
        self.subtotal = 0

    def get_subtotal(self):
        for product in self.products:
            self.subtotal += product.price

        return self.subtotal

# class Product:
#     def __init__(self):
#         self.price = 10
#         self.name = "item"

# def main():
#     item1 = Product()
#     item2 = Product()
#     item3 = Product()

#     items = [item1, item2, item3]

#     order = Order()

#     order.products = items

#     print(order.get_subtotal())

#     # Alternitively

#     print(item1.price + item2.price + item3.price)
