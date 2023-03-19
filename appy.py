import random

class Product():
    def __init__(self):
        self.product_code = self.get_product_code()
        # self.product_name = self.get_product_name()
        # self.product_price = self.get_product_price()
        # self.product_manuf = self.get_product_manuf()
        # self.stock_level = self.get_stock_level()
        # self.monthly_est = self.get_monthly_est()

    # def get_product_code(self):
    #     while True:
    #         product_code = int(input("Enter the product code (between 100 and 1000): "))
    #         if product_code < 100 or product_code > 1000:
    #             print("Product code must be between 100 and 1000.")
    #         else:
    #             return product_code

#     def get_product_name(self):
#         while True:
#             product_name = input("Enter Product Name: ")
#             if product_name.isalpha() == False:
#                 product_name = input("Incorrect input, please re-enter Product Name:")
#             else:
#                 return product_name
    
#     def get_product_price(self):
#         pass

# product = Product()

# print(product.product_name)