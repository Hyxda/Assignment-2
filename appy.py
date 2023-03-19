import random

class Product():
    def __init__(self):
        self.product_code = self.get_product_code()
        self.product_name = self.get_product_name()
        self.product_price = self.get_product_price()
        self.product_manuf = self.get_product_manuf()
        self.stock_level = self.get_stock_level()
        self.monthly_est = self.get_monthly_est()
        self.total_product_manuf = 0
        self.total_units_sold = 0

    def get_product_code(self):
        while True:
            product_code = input("Enter the product code (between 100 and 1000): ")
            if product_code.isdigit() and 100 <= int(product_code) <= 1000:
                return int(product_code)
            else:
                print("Incorrect input, please re-enter Product Code: ")

    def get_product_name(self):
        while True:
            product_name = input("Enter Product Name: ")
            if product_name.isalpha():
                return product_name
            else:
                print("Incorrect input, please re-enter Product Name: ")

    def get_product_price(self):
        while True:
            product_price_str = input("Enter Product Price: ")
            if product_price_str.replace('.', '', 1).isdigit():
                product_price = float(product_price_str)
                if product_price > 0:
                    return product_price
            else:
                print("Incorrect input, please re-enter Product Price: ")
    
    def get_product_manuf(self):
        while True:
            product_manuf_str = input("Enter Product Manufacturing Cost: ")
            if product_manuf_str.replace('.', '', 1).isdigit():
                product_manuf = float(product_manuf_str)
                if product_manuf > 0:
                    return product_manuf
            else:
                print("Incorrect input, please re-enter Product Manufacturing Cost: ")
        
    def get_stock_level(self):
        while True:
            stock_level = input("Enter the Stock Level: ")
            if stock_level.isdigit():
                return int(stock_level)
            else:
                print("Incorrect input, please re-enter Stock Level: ")
    
    def get_monthly_est(self):
        while True:
            monthly_est = input("Enter Estimated Monthly Units: ")
            if monthly_est.isdigit():
                return(int(monthly_est))
            else:
                print("Incorrect input, please re-enter Estimated Monthly Units: ")

    def simulate_monthly_production(self, months = 12):
        unfulfilled_sales = 0
        net_profit = 0
        for month in range(1, months + 1):
            product_manuf = random.randint(self.monthly_est - 10, self.monthly_est + 10)
            self.total_product_manuf += product_manuf
            units_sold = random.randint(self.total_product_manuf - self.stock_level - 10, self.total_product_manuf - self.stock_level + 10)
            
            if units_sold < 0:
                units_sold = 0

            if units_sold > self.stock_level:
                unfulfilled_sales += units_sold - self.stock_level
                units_sold = self.stock_level

            self.total_units_sold += units_sold
            self.stock_level = self.total_product_manuf - self.total_units_sold
            net_profit = self.total_units_sold * self.product_price - self.total_product_manuf * self.product_manuf

            print("Month {}: Units Manufactured = {}, Units Sold = {}, Stock Level = {}, Net Profit = {}".format(month, product_manuf, units_sold, self.stock_level, net_profit))

product = Product()
product.simulate_monthly_production()
#print(product.product_code, product.product_name, product.product_price, product.product_manuf, product.stock_level, product.monthly_est)