chocolate=[   {"name":"choco","amount":20,"stock":"50"},
              {"name":"orange","amount":30,"stock":"120"},
              {"name":"mango","amount":40,"stock":"40"},
              {"name":"vanilla","amount":25,"stock":"100"},
              {"name":"almond","amount":10,"stock":"25"} ]

def display(chocolates):
  for chocolate in chocolates:
    print("Name: ",chocolate['name'],"Amount: ",chocolate['amount'],"stock: ",chocolate['stock'])

flag=True
while flag:
  print("-"*70)
  print("Chocolate Factory")
  print("-"*70)
  print("1. Shopkeeper")
  print("2. Customers")
  print("0. Exit")
  print("-"*70)
  choice=int(input("Enter the choice: "))
  if choice == 1:
    shopkeeper_flag=True
    while shopkeeper_flag:
      print("-"*70)
      print("Shopkeeper")
      print("-"*70)
      print("1. Add Chocolates")
      print("2. Remove Chocolates")
      print("3. Update amount")
      print("4. Update stock")
      print("5. Display chocolates")
      print("0. Back")
      print("-"*70)
      shopkeeper_choice=int(input("Enter the choice: "))
      if shopkeeper_choice == 1:
        print("-"*70)
        print("Add Chocolates")
        print("-"*70)
        chocolates=add_chocolates(chocolates)
      elif shopkeeper_choice == 2:
        print("-"*70)
        print("Remove Chocolates")
        print("-"*70)
        chocolates=remove_chocolates(chocolates)
      elif shopkeeper_choice == 3:
        print("-"*70)
        print("Update Amount")
        print("-"*70)
        chocolates=update_amount(chocolates)
      elif shopkeeper_choice == 4:
        print("-"*70)
        print("Update Stock")
        print("-"*70)
        chocolates=update_stock(chocolates)
      elif shopkeeper_choice == 5:
        print("-"*70)
        print("Display")
        display(chocolates)
        print("-"*70)
      elif shopkeeper_choice == 0:
        print("-"*70)
        print("Back to Main Menu")
        print("-"*70)
        shopkeeper_flag=False
      else:
        print("-"*70)
        print("Enter a valid number: ")
        print("-"*70)
  elif choice == 2:
    customer_flag=True
    while customer_flag:
      print("-"*70)
      print("Customer")
      print("-"*70)
      print("1. Buy Chocolates")
      print("2. Display")
      print("0. Back")
      print("-"*70)
      customer_choice=int(input("Enter the choice: "))
      if customer_choice == 1:
        print("-"*70)
        print("Buy Chocolates")
        print("-"*70)
        chocolates,amount=buy(chocolates)
        print("-"*70)
        print("Amount: ",amount)
        print("-"*70)
      elif customer_choice == 2:
        print("-"*70)
        print("Display")
        display(chocolates)
        print("-"*70)
      elif customer_choice == 0:
        print("-"*70)
        print("Back to Main Menu")
        print("-"*70)
        customer_flag=False
      else:
        print("-"*70)
        print("Enter a valid number: ")
        print("-"*70)
  elif choice == 0:
    print("-"*70)
    print("Exit")
    print("-"*70)
    flag=False
  else:
    print("-"*70)
    print("Enter a valid number: ")
    print("-"*70)
