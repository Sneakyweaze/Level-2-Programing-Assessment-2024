import time
# This is the list of pizzas that the shop sells
pizzas_ = [[1, "Pepperoni", "$13.50", 13.50],
           [2, "Meat Lovers","$13.50", 13.50],
           [3, "Margherita","$13.50",13.50],
           [4, "BBQ Chicken","$13.50",13.50],
           [5, "Chicken Bacon & Aioli","$13.50",13.50],
           [6, "Veggie","$8.50",8.50],
           [7, "Hawaiian","$8.50",8.50],
           [8, "Plain Cheese", "$8.50",8.50], 
           [9, "Greek Lamb", "$8.50",8.50],
           [10, "Garlic Prawn","$8.50",8.50],
           [11, "Spicy Pepper","$8.50",8.50],
           [12, "Ham & Cheese","$8.50",8.50]]

# This is the list of chosen pizzas added to your order
pizza_chosen = []
global pizza_price

# this varible sets the code to loop or not
loop = True

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
  user_pizza = input("What pizza would you like to order?")
  for pizza in pizzas_:
    if user_pizza.lower() == pizza[1].lower():
      time.sleep(0.75)
      global pizza_price
      print(f"Added a {pizza[1]} pizza to your order.")
      pizza_chosen.append(pizza[1:3])
      if pizza[0] == 1 or pizza[0] == 2 or pizza[0] == 3 or pizza[0] == 4 or pizza[0] ==5:
        pizza_price += 13.50
        break
      else:
        pizza_price += 8.50
        break

    elif user_pizza.lower() not in pizza[1].lower():
      time.sleep(0.75)
      print("Sorry, we don't have that pizza here.")
      break
    else:
      time.sleep(0.75)
      print("Sorry, we don't have that pizza here.")
      break


def pizza_checkout():
  for pizza in pizza_chosen:
    print(pizza[0],'-' ,' - '.join(pizza[1:3]))
    time.sleep(0.75)
  print("These Are All Of The Pizzas You have on your Order")
  time.sleep(0.75)
  # this is the price of all the pizzas added to your order
  print("The Total Price of Your Order is: $", pizza_price)
  print("Would you like to checkout?")

def pizza_payment():
  time.sleep(0.75)
  print("test")

# this is the main code block
pizza_price = 0.0
print("Welcome to the Pizza Shop")
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
    print("Thank you for visiting the Pizza Shop.")
    loop = False
  else:
    print("\n")
    time.sleep(0.75)
    print("Please Select a Valid Option")
    print("\n")