# Importing datetime module to get current date and time for the bill
# This will be used to print the date and time on the bill
import datetime as dt 

def input_bill_basic_data():  # this function is to take user input of the basic details for the bill i.e. GST No., Food No., Table No., Date, Time, Place, Slogan
    """This function is to take user input for the bill"""
    Gst_No = input("Enter GST No. : ")
    Food_No = input("Enter Food No. : ")
    Table_No = input("Enter Table No. : ")
    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%H:%M:%S")
    Place = input("Enter Name of Place: ")
    Slogan = input("Enter Slogan: ")
    return Gst_No, Food_No, Table_No, date, time, Place, Slogan

def item_details():   # This function is to take user input for item details (name, quantity, rate) and calculate the amount
    """
    This function takes user input for item details (name, quantity, rate)
    and calculates the amount. It can be used to input a single item or multiple items,
    returning a list of tuples, where each tuple represents an item.
    """
    items = []    # List to store item details as tuples (item_name, quantity, rate, amount)
    while True:   # Loop to allow multiple item entries
        item_name = input("Enter Item Name: ")
        # Input validation for quantity
        while True:  
            try:    
                quantity = float(input("Enter Quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input for quantity. Please enter a number.")

        # Input validation for rate
        while True:
            try:
                rate = float(input("Enter Rate: "))
                if rate < 0:
                    print("Rate cannot be negative. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input for rate. Please enter a number.")

        amount = quantity * rate
        items.append((item_name, quantity, rate, amount))

        more_items = input("Do you want to add more items? (yes/no): ").lower()
        if more_items != 'yes':
            break
    
    return items

# This function is to print the bill with the items and their details
# It takes the list of items and other details as input and prints a formatted bill

def print_bill(items, gst_no, food_no, table_no, date, time, place, Slogan):
    """This function is to print the bill"""
    print(f"|{'-'*50}|")
    print(f"|{'GSTIN-'+gst_no:^50}|")
    print(f"|{'FOOD LIC-'+food_no:^50}|")
    print(f"|{'.  .  .  .  .  .  .  CASH/BILL .  .  .  .  .  .  .':^50}|")
    print(f"|{'  TABLE '+table_no:<25}{'CVR 01   WAITER  00  ':>25}|")
    print(f"|{'  NO.000708':<25}{'DATE: '+date :>23}{' ':>2}|")
    print(f"|{'-'*50}|")
    print(f"|{'  DESCRIPTION':<20}{'QTY ':>10}{'RATE  ':>10}{'AMOUNT  ':>10}|")
    print(f"|{'-'*50}|")

    # Getting the total amount and printing each item
    total_amount = 0
    for item in items:
        item_name, quantity, rate, amount = item
        total_amount += amount
        print(f"|{'  '}{item_name:<17}{quantity:>10.3f}{rate:>9.2f}{amount:>10.2f}{'  ':>2}|")

    # Print the subtotal
    print(f"|{'  SUB TOTAL':<15}{'ITM= '+str(len(items)):>10}{'Q= '+str(sum(item[1] for item in items)):>13}{total_amount:>10.2f}{' ':>2}|")

    # Print the total cash

    print(f"|{'-'*50}|")
    print(f"|{'      CASH':<35}{total_amount:>10.2f}{' ':>5}|")
    print(f"|{' '*50}|")

    # Print the C 6 line with time and M/C NO

    print(f"|{'  C 6':<10}{time:<25}{'M/C NO ':>5}{'13':>6}{' ':>2}|")
    print(f"|{' '*50}|")
    print(f"|{' '*50}|")
    print(f"|{' '*50}|")

    # Print the name of the restaurant

    print(f"|{place:^50}|")
    print(f"|{Slogan:^50}|")
    print(f"|{'-'*50}|")

    # End of the bill

# This is the main function that will call the input_bill_basic_data and item_details functions
# It will print the bill when the script is run

if __name__ == "__main__":
    print("Welcome to the Bill Generator!".center(50))

    #  Get the return values from the function
    Gst_No, Food_No, Table_No, date, time, Place, Slogan = input_bill_basic_data()

    print("Please enter the item details:".center(50))

    #  Get the list of items
    items_list = item_details()

    #  Pass the  variables to the print_bill function
    print_bill(items_list, Gst_No, Food_No, Table_No, date, time, Place, Slogan)
   
    print(" "*50)
    print("Thank you for visiting us!".center(50))
    print("Please visit again!".center(50))