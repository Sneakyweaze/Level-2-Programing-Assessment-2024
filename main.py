#This is the list of pizzas that the shop sells
pizzas_ = [[1, "Pepperoni", "$8.50"],
           [2, "Meat Lovers", "$8.50"],
           [3, "Margherita","$8.50"],
           [4, "BBQ Chicken","$8.50"],
           [5, "Chicken Bacon & Aioli","$8.50"],
           [6, "Veggie","$8.50"],
           [7, "Hawaiian","$8.50"],
           [8, "Plain Cheese","$5"],
           [9, "Greek Lamb","$5"],
           [10, "Garlic Prawn","$5"],
           [11, "Spicy Pepper","$5"],
           [12, "Ham & Cheese","$5"]]

#this varible sets the code to loop or not
loop = True

#this is the funtion that prints of the list of pizzas that the shop sells. 
def pizza_menu():
  '''
  When the user selects the pizza menu, the program will print the menu. 
  
  The output will look like this for each line:
  1 - Pepperoni - $8.50
  2 - Meat Lovers - $8.50
  3 - Margherita - $8.50
  ect. until the 2D list is finished
  '''
  print("These Are the Pizzas we sell:")
  for pizza in pizzas_:
    print(pizza[0],'-','- '.join(pizza[1:3]))



def pizza_order():
  print("test")
def pizza_checkout():
  print("test")
def pizza_payment():
  print("test")

#this is the main code block
print("Welcome to the Pizza Shop")
while loop is True:
  menu_select = input("Please Select an Option:\n1 - Pizza Menu\n2 - Add Pizza To Order\n3 - Checkout\n4 - Exit\n-> ")
  if menu_select == "1":
    pizza_menu()
    print("\n")
    continue
  elif menu_select == "2":
    pizza_order()
    print("\n")
    continue
  elif menu_select == "3":
    pizza_checkout()
    print("\n")
    continue 
  elif menu_select == "4":
    print("Thank you for visiting the Pizza Shop.")
    loop = False
  else:
    print("Please Select a Valid Option")
    print("\n")