# Import the random module
import random

# Define Product class
class Product():
    # Define the class constructor
    def __init__(self):
        # Initialize class attributes using respective methods
        self.product_code = self.get_product_code()
        self.product_name = self.get_product_name()
        self.product_price = self.get_product_price()
        self.product_manuf = self.get_product_manuf()
        self.stock_level = self.get_stock_level()
        self.monthly_est = self.get_monthly_est()
        self.total_product_manuf = 0
        self.total_units_sold = 0

    # Define method to get product code from user
    def get_product_code(self):
        # Initialize while loop to validate user input
        while True:
            # Prompt user to enter the product code
            product_code = input("Enter the product code (between 100 and 1000): ")
            # Check if the input is a number between 100 and 1000
            if product_code.isdigit() and 100 <= int(product_code) <= 1000:
                return int(product_code)
            else:
                # Print an error message and prompt the user to enter the product code again
                print("Incorrect input, please re-enter Product Code: ")

    # Define method to get product name from user
    def get_product_name(self):
        while True:
            product_name = input("Enter Product Name: ")
            # Check if input only contains alphabetic characters
            if product_name.isalpha():
                return product_name
            else:
                print("Incorrect input, please re-enter Product Name: ")

    # Define method to get product price from user
    def get_product_price(self):
        while True:
            product_price_str = input("Enter Product Price: ")
            # Check if the input is valid (a positive floating point number)
            if product_price_str.replace('.', '', 1).isdigit():
                product_price = float(product_price_str)
                if product_price > 0:
                    return product_price
            else:
                print("Incorrect input, please re-enter Product Price: ")

    # Define method to get product manufacturing cost from user
    def get_product_manuf(self):
        while True:
            product_manuf_str = input("Enter Product Manufacturing Cost: ")
            # Check if the input is valid (a positive floating point number)
            if product_manuf_str.replace('.', '', 1).isdigit():
                product_manuf = float(product_manuf_str)
                if product_manuf > 0:
                    return product_manuf
            else:
                print("Incorrect input, please re-enter Product Manufacturing Cost: ")
    
    # Define method to get stock level from user
    def get_stock_level(self):
        while True:
            stock_level = input("Enter the Stock Level: ")
            # Check if the input is valid (a positive integer)
            if stock_level.isdigit():
                return int(stock_level)
            else:
                print("Incorrect input, please re-enter Stock Level: ")

    # Define method to get monthly production estimate from user
    def get_monthly_est(self):
        while True:
            monthly_est = input("Enter Estimated Monthly Units: ")
            # Check if the input is valid (a positive integer)
            if monthly_est.isdigit():
                return(int(monthly_est))
            else:
                print("Incorrect input, please re-enter Estimated Monthly Units: ")

    # Define a function named "simulate_monthly_production" that takes "months" as a parameter with a default value of 12
    def simulate_monthly_production(self, months = 12):
        # Initialize some variables to keep track of
        unfulfilled_sales = 0
        net_profit = 0
        total_net = 0
        total_product_manuf = self.monthly_est  # set initial value
        total_units_sold = 0

        # Update the current stock level of the product based on the total product manufactured and total units sold
        self.stock_level = total_product_manuf - total_units_sold

        # Print a statement about the current stock of the product
        print("\n********Programming Principles Sample Stock Statement********")
        print("\nProduct Code: {} \nProduct Name: {} \n\nSale Price: ${} CAD \nManufacture Cost: {} \nMonthly Production: {} (Approx.)\n".format(self.product_code, self.product_name, self.product_price, self.product_manuf, self.monthly_est))
        
        # Loop through each month specified, generating a prediction for the stock statement for each month
        for month in range(1, months + 1):

            # Generate a prediction for the product manufacturing for the current month
            product_manuf = self.monthly_est

            # Add the product manufacturing for the current month to the total product manufactured
            total_product_manuf += product_manuf

            # Generate a random number of units sold for the current month based on the product manufacturing for the month
            units_sold = random.randint(product_manuf - 10, product_manuf + 10)

            # Limit the number of units sold to the range [product_manuf - 10, product_manuf + 10]
            units_sold = max(product_manuf - 10, min(units_sold, product_manuf + 10))

            # Ensure that the number of units sold is not negative
            if units_sold < 0:
                units_sold = 0
            
            # Check if there are enough units in stock to fulfill the sales for the month, and update the stock level accordingly
            if units_sold > self.stock_level:
                unfulfilled_sales += units_sold - self.stock_level
                units_sold = self.stock_level
            
            # Add the units sold for the current month to the total units sold
            total_units_sold += units_sold

            # Update the current stock level of the product based on the total product manufactured and total units sold
            self.stock_level = total_product_manuf - total_units_sold

            # Ensure that the stock level is not negative
            if self.stock_level < 0:
                self.stock_level = 0
            
            # Calculate the net profit for the current month and add it to the total net profit
            net_profit += (total_units_sold * self.product_price) - (total_product_manuf * self.product_manuf)
            total_net += net_profit

            # Generate a predicted stock statement for the current month
            self.generate_predicted_stock_statement(month, product_manuf, units_sold, self.stock_level)

        # If there were any unfulfilled sales for the entire simulation, print a message about it
        if unfulfilled_sales > 0:
            print("\n{} units could not be sold due to insufficient stock.".format(unfulfilled_sales))
        
        # Calculate and print the total profit or loss for the entire simulation
        product.profit_losses(total_net)

    # Define a function named "generate_predicted_stock_statement" that displays monthly information for product manufactured, units sold, & stock level 
    def generate_predicted_stock_statement(self, month, product_manuf, units_sold, stock_level):
        print("Month {} \n-\tManufactured: {} units \n-\tUnits Sold: {} units \n-\tStock: {}".format(month, product_manuf, units_sold, stock_level))

    # Define a function named "profit_losses" that displays net profit or incurred losses
    def profit_losses(self, total_net):
        if total_net > 0:
            print("\nNet Profit: ${} CAD".format(total_net))
        else:
            print("\nIncurred Loss: ${} CAD".format(total_net))


product = Product()
product.simulate_monthly_production()