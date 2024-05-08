import time
# This is the list of pizzas that the shop sells
pizzas_ = [[1, "Pepperoni", "$13.50", 13.50],
           [2, "Meat Lovers","$13.50", 13.50],
           [3, "Margherita","$13.50",13.50],
           [4, "BBQ Chicken","$13.50",13.50],
           [5, "Chicken Bacon And Aioli","$13.50",13.50],
           [6, "Veggie","$8.50",8.50],
           [7, "Hawaiian","$8.50",8.50],
           [8, "Plain Cheese", "$8.50",8.50], 
           [9, "Greek Lamb", "$8.50",8.50],
           [10, "Garlic Prawn","$8.50",8.50],
           [11, "Spicy Pepper","$8.50",8.50],
           [12, "Ham And Cheese","$8.50",8.50]]

# This is the list of chosen pizzas added to your order
pizza_chosen = []
# This the varible that the total price of the pizzas is stored
global pizza_price

# this varible sets the code to loop or not
global loop 

# this is the funtion that prints of the list of pizzas that the shop sells. 
def pizza_menu():
  '''
  When the user selects the pizza menu, the program will print the menu. 
  
  The output will look like this for each line:
  1 - Pepperoni - $8.50
  2 - Meat Lovers - $8.50
  3 - Margherita - $8.50
  ect. until the 2D list is finished, meaning that you can add and remove pizzas from the list.
  '''
  time.sleep(0.75)
  print("These Are the Pizzas we sell:")
  for pizza in pizzas_:
    time.sleep(0.25)
    print(pizza[0],'-' ,' - '.join(pizza[1:3]))


# This is the function that allows the user to choose a pizza they want to order.
def pizza_order():
  '''
  When the user selects pizza_order, the program will ask the user to input the number of the pizza they want to order.
  E.g below 
  Would you like to order a pizza?
  "Pepperoni"
  Added a Pepperoni pizza to your order.
  if the user inputs a pizza that is not in the list, the program will ask the user to input a valid one.
  E.g below 
  Would you like to order a pizza?
  "Beef And Herbs"
  Sorry, we don't have that pizza here.
  '''
  time.sleep(0.75)
  user_pizza = input("What pizza would you like to order? -> ")
  for pizza in pizzas_:
    if user_pizza.lower() == pizza[1].lower():
      time.sleep(0.75)
      global pizza_price
      print(f"Added a {pizza[1]} pizza to your order.")
      pizza_chosen.append(pizza[1:3])
      if pizza[0] == 1 or pizza[0] == 2 or pizza[0] == 3 or pizza[0] == 4 or pizza[0] == 5:
        pizza_price += 13.50 
        break
      else:
        pizza_price += 8.50
        break
    
  
    elif user_pizza.lower() not in pizza[1].lower():
      time.sleep(0.10)
    
  another = input("Do you want to order another pizza? Y/N -> ")
  if another.upper() == "Y":
    pizza_order()
  else: 
    print("\n")
    

# this function tells the user what pizzas they have chosen and the price of the pizzas they have chosen, and then asks if they want to continue to payment.
def pizza_checkout():
  '''
  When the user selects pizza_checkout, the program will print the pizzas that the user has chosen and the price of the pizzas indevidualy .
  E.g below

  These Are All Of The Pizzas You have on your Order
  Pepperoni - $13.50
  Meat Lovers - $13.50
  Plain Cheese - $8.50

  Afterwards, the program will tell the user how much their order is.
  E.g below
  The Total Price Of Your Order Is $32.50

  then the program will ask the user if they want to continue to payment. if they don't they will be returned to the main menu.
  
  '''
  print("These Are All Of The Pizzas You have on your Order")
  for pizza in pizza_chosen:
    print(pizza[0],'-' ,' - '.join(pizza[1:3]))
    time.sleep(0.75)
  time.sleep(0.75)
  # this is the price of all the pizzas added to your order
  print("The Total Price of Your Order is: $", pizza_price)
  checkout_yn = input("Would you like to checkout? Y/N (You Will Not Be Able To Exit-> ")
  if checkout_yn.upper() == "Y":
    time.sleep(0.75)
    pizza_payment()
  elif checkout_yn.upper() =="N":
    time.sleep(0.75)
    print("You will be return to the main menu")
  else:
   time.sleep(0.75)
   print("This isn't a valid option")
    
def pizza_payment():
  
  print("\n")
  deliver = input("Do You Want Your Pizza To Be delivered? Y/N -> ")
  if deliver.upper() == "Y":
    print("Please Enter The Required infomaction")
    time.sleep(0.75)
    name = str(input("Name -> "))
    time.sleep(0.50)
    phone_number = int(input("Phone Number -> "))
    time.sleep(0.50)
    address = input("Address -> ")
    time.sleep(0.50)
    print("\n")
    print("\n")
    print("Order Cost: $",pizza_price)
    time.sleep(0.25)
    print("Delivery Cost: $ 2.50")
    time.sleep(0.25)
    print("Total Cost: $",pizza_price + 2.50)
    time.sleep(0.25)
    print("\n")
    
  elif deliver.upper() == "N":
    address = None
    print("Please Enter The Required infomaction")
    time.sleep(0.75)
    name = input("Name -> ")
    time.sleep(0.50)
    print("\n")
    print("Total Cost: $",pizza_price)
    time.sleep(0.25)
    print("\n")
  
  else:
    print("This isn't a valid option")
    pizza_payment()
  order_complete =input("Finish Order? Y/N -> ")
  if order_complete.upper() =="Y":
    print("Thank You For Ordering")
    time.sleep(0.75)
    
    if deliver.upper() == "Y":
      print("Your Pizza Will Be Delivered To", address)
      print("\n\n\n\n\n\n\n\n\n\n\n")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("Name:",name)
      print("Address:",address)
      print("Phone Number:",phone_number)
      for pizza in pizza_chosen:
        print(pizza[0],'-' ,' - '.join(pizza[1:3]))
      print("Order Cost: $",pizza_price)
      print("Delivery Cost: $ 2.50")
      print("Total Cost: $",pizza_price + 2.50)
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("\n\n\n\n\n\n\n\n\n\n\n")

    elif deliver.upper() == "N":
 
      print("\n\n\n\n\n\n\n\n\n\n\n")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("Name:",name)
      for pizza in pizza_chosen:
        print(pizza[0],'-' ,' - '.join(pizza[1:3]))
      print("Total Cost: $",pizza_price)
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("\n\n\n\n\n\n\n\n\n\n\n")
    loop = False
  elif order_complete.upper() =="N":
    print("You will be return to the main menu")
    
  else:
    print("This isn't a valid option")
  
      
    
 

# this is the main code block
pizza_price = 0.0
print("Welcome to Crusty's Pizza Shop")
pizza_chosen = []
name = None
phone_number = None
address = None
loop = True
while loop is True:
  time.sleep(0.75)
  menu_select = input("Please Select an Option:\n1 - Pizza Menu\n2 - Add Pizza To Order\n3 - Checkout\n4 - Exit\n-> ")
  if menu_select == "1":
    print("\n")
    pizza_menu()
    print("\n")
    continue
  elif menu_select == "2":
    print("\n")
    pizza_order()
    print("\n")
    continue
  elif menu_select == "3":
    print("\n")
    pizza_checkout()
    print("\n")
    continue 
  elif menu_select == "4":
    time.sleep(0.75)
    print("Thank you for visiting Crusty's Pizza Shop.")
    loop = False
  else:
    print("\n")
    time.sleep(0.75)
    print("Please Select a Valid Option")
    print("\n")