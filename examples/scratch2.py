# print("Hello")

# class Student:
#     def __init__(self, name):
#         self.name = name

# class Graduate(Student):
#     def __init__(self, name, graduation_date):
#         super().__init__(name)
#         self.graduation_date = graduation_date


# class Duck:
#     def __init__(self, name, bill_description, tail_length):
#         self.name = name
#         self.bill_description = bill_description



# class Product:
#     def __init__(self, name, price, description, brand_name, sku, on_sale=False):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.brand_name = brand_name
#         self.sku = sku
#         self.on_sale = on_sale

#     def __str__(self):
#         return self.name + "\t$" + str(self.price)


# product = Product('baseball', 4, 'lame', 'wilson', '1234', 'false')


# print(product)


# class Clothing(Product):
#     def __init__(self, name, price, description, brand_name, sku, color, size, on_sale):
#         super().__init__(self, name, price, description, brand_name, sku, color, size, on_sale)
#         self.color = color
#         self.size = size

people = ["Abe", "Bill", "Charles", "Dolly", "Evelyn", "Frank", "Gunther"]
# comp for names that start with D

a = [name.lower() for name in people if name[0]=="D" ]
print(a)
# comp for names that end in Y

a = [name for name in people if name.endswith("y")]
print(a)


# comp for names that start with B through D
a = [name for name in people if name.startswith("B") or name.startswith("C") or name.startswith("D")]
print(a)



## names in uppercase

upper = [name.upper() for name in people]
print(upper)




import csv

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price



products = []


def product_reader(products=[]):
    