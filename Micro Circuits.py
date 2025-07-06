
# declaring the lists - 3 separate lists
stock_codes_list = [] # List to store stock codes
stock_prices_list = [] # List to store corresponding stock prices
stock_count_list = [] # List to store corresponding stock counts

# declaring the maximum values
max_types = 50 # Maximum number of stock types allowed
max_price = 1000.00 # Maximum price per item
max_count = 100 # Maximum number of items per stock type

def AddStockCode(): # this is function to add a new stock code together with its price
    if len(stock_codes_list) >= max_types:  # checks if the length of the stock code list is 50 or the max is reached
        print("Oops, Cannot add more stock codes, The maximum is reached!")
        return

    stock_code = input("Enter the stock code: ").strip().lower()
    while True:
        try:
         price = float(input("Enter the stock price (max 1000.00): "))
         if price > max_price:
             print(f"The price cannot exceed {max_price}!")
         else:
            break
        except ValueError:
         print("Invalid price. Please enter a number!")

    stock_codes_list.append(stock_code)
    stock_prices_list.append(price)
    stock_count_list.append(0) # new stock code starts with 0 stock
    print(f"Stock code '{stock_code}' successfully added.")


def SearchCode(stock_code): # this is a function to search for a stock code and return its index, if the code is not found it returns an error message
    for i in range(len(stock_codes_list)):
        if stock_codes_list[i] == stock_code:
            return i
        else:
            print(f"Stock code '{stock_code}' not found!")
            return -1


def AddStockItem(): # this is a function to add items to an existing stock code
    stock_code = input("Enter the stock code which you want to add the stock for: ")
    i = SearchCode(stock_code) # i - for index
    if i == -1:
        return

    num_of_items = int(input("Enter the number of items to add: "))

    if stock_count_list[i] + num_of_items > max_count:
        print(f"Stock level of {max_count} exceeded. Capping stock at {max_count}!")
    else:
        stock_count_list[i] += num_of_items
        print(f"Added {num_of_items} items to the stock code '{stock_code}'.")

def DisplayStockList(): # this is a function to display all stock information and total stock value
    print("Stock code, In stock, Price, Stock value")
    total_value = 0
    for i in range(len(stock_codes_list)):
        stock_code = stock_codes_list[i]
        count = stock_count_list[i]
        price = stock_prices_list[i]
        stock_value = price * count
        print(f"{stock_code},\t\t{count},\t\t{price},\t\t{stock_value}")
        total_value += stock_value
    print(f"Total,,{total_value}")

def menu(): # this is a function to display the menu and handle user choices
    while True:
        print("-----------Menu------------")
        print("1. Add Stock Code")
        print("2. Add Stock Item")
        print("3. Display Stock List")
        print("4. Exit")

        option = input("Select your option: ").strip()

        if option == "1":
            AddStockCode()
        elif option == "2":
            AddStockItem()
        elif option == "3":
            DisplayStockList()
        elif option == "4":
            print("Exiting Program...")
            break
        else:
            print("Invalid option, please choose from 1, 2, 3 or 4.")

menu()

