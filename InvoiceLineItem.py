#CIS 261
#Jasmine Bumbray
#Invoice Line Item

def get_price():
    while True:
        try:
            price = float(input("Please enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Sorry! Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Please enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Sorry! Please try again.")

def main():
    print("The Invoice Line Item Calculator\n")

    answer = "y"
    while answer.lower() == "y":
        #price and quantity
        price = get_price()
        quantity = get_quantity()
    
        # calculate the total
        total = price * quantity

        # results
        print()
        print("PRICE:    ", f"{price: .2f}")
        print("QUANTITY: ", quantity)
        print("TOTAL:    ", f"{total: .2f}")
        answer = input("Enter another line item? (y/n): ")
        print()
        
    print("See ya!")


if __name__ == "__main__":
    main()
