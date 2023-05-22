"""
Student: Juan Plasencia
*Showing Creativity:
-Added an "invalid option" option when entering a value outside of 1-5, when choosing which action the program should perform.
-Added the quantity of the items in the list.
-Addes better formatting aligning the prices.
"""
#welcome
print("Welcome to the Shopping Cart Program!")
#variables that we are going to use during program execution
menu = ["1. Add item", "2. View cart", "3. Remove item", "4. Compute total", "5. Quit"]
run = True
cart = []
price = []
quantity = []
#Loop that displays the user options until you choose exit
while run == True:
    #Display the options and ask
    print("\nPlease select one of the following:")
    for option in menu:
        print(option)
    item = input("Please enter an action: ")
    #Add an item to cart
    if item == "1":
        cart_item = input("What item would you like to add?: ").capitalize()
        cart.append(cart_item)
        price_item = round(float(input(f"What is the price of '{cart_item}'? ")),2)
        price.append(price_item)
        quantity_item = int(input(f"How many items of '{cart_item}' will you add? "))
        quantity.append(quantity_item)
        print(f"'{cart_item}' has been added to the cart.")
    #shows the contents of the cart
    elif item == "2":
        print("The contents of the shopping cart are: ")
        if cart == []:
            print("The car is empty")
        else:
            cart_width = max(len(x) for x in cart)
            price_width = max(len(f"{x:,.2f}") for x in price)
            quantity_width = max(len(str(x)) for x in quantity)
            for i in range(len(cart)):
                print(f"{i+1}. {cart[i].center(cart_width)} - $ {price[i]:>{price_width},.2f} - {quantity[i]:>{quantity_width}} units") 
    #nothing for the moment, display an apology message
    elif item == "3":
        removed = int(input("Which item would like to remove? " )) - 1
        cart.pop(removed)
        price.pop(removed)
        quantity.pop(removed)
        print("Item removed.")
    #nothing for the moment, display an apology message.
    elif item == "4":
        partial = []
        for i in range(len(cart)):
            multiply = price[i] * quantity[i]
            partial.append(multiply)
        total = 0.00
        for i in range(len(cart)):
            total += partial[i]
        print(f"The total price of the items in the shopping cart is ${total}")
    #Goodbye
    elif item == "5":
        print("Thank you. Goodbye.")
        run = False
    #Only if in case the user gets confused or chooses something outside the options 
    else:
        print("This is not a valid option, try 1 to 5, please.")