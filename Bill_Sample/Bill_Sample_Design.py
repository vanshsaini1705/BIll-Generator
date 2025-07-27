# importing datetime module to get current date and time for the bill
# This will be used to print the date and time on the bill
import datetime as dt

Date = dt.datetime.now().strftime("%d/%m/%Y")
Time = dt.datetime.now().strftime("%H:%M:%S")

# Function to print the bill
# This function will print a formatted bill with the current date and time

def Bill():
    """This is a function to print the basic bill
      created by the user without any input"""

    # Print the formatted bill
    # Start of the bill
    # GSTIN, Food License, Cash/Bill, Table, No., Date

    print(f"|{'-'*50}|")
    print(f"|{'GSTIN-08BWHIPS7357H1ZV':^50}|")
    print(f"|{'FOOD LIC-12215039000640':^50}|")
    print(f"|{'.  .  .  .  .  .  .  CASH/BILL .  .  .  .  .  .  .':^50}|")
    print(f"|{'  TABLE    0000':<25}{'CVR 01   WAITER  00  ':>25}|")
    print(f"|{'  NO.000708':<25}{'DATE: '+Date :>23}{' ':>2}|")
    print(f"|{'-'*50}|")

    # Description, Quantity, Rate, Amount
    print(f"|{'  DESCRIPTION':<20}{'QTY ':>10}{'RATE  ':>10}{'AMOUNT ':>10}|")
    print(f"|{'-'*50}|")

    # Sample items
    print(f"|{'  CHAT SAMOSA':<20}{'1.000':>10}{'35.00 ':>10}{'35.00  ':>10}|")
    print(f"|{'  SAMOSA':<20}{'2.000':>10}{'20.00 ':>10}{'40.00  ':>10}|")
    print(f"|{'  CHOLA BHATURA':<20}{'1.000':>10}{'130.00':>10}{'130.00 ':>10}|")
    print(f"|{'  sub_tot':<20}{'ITM= 3':>10}{'Q=4.000':>10}{'205.00 ':>10}|")
    print(f"|{'-'*50}|")

    # Total Cash
    print(f"|{'      CASH     ':<35}{'   205.00      ':>10}|")
    print(f"|{' '*50}|")
    print(f"|{'  C 6':<10}{Time:<25}{'M/C NO ':>5}{'13  ':>8}|")
    print(f"|{' '*50}|")
    print(f"|{' '*50}|")
    print(f"|{' '*50}|")

    # Name of restaurant
    print(f"|{'SHREE SHYAM SWEETS':^50}|")
    print(f"|{'KHATUSHYAM JI':^50}|")
    print(f"|{'-'*50}|")

    # End of the bill

# This is the main function that will call the Bill function
# It will print the bill when the script is run

if __name__ == "__main__":
    Bill()
    print(" "*50)
    print("Thank you for visiting us!".center(50))
    print("Please visit again!".center(50))
