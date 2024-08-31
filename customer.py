def buy(chocolates):
  name=input("Enter name of chocolate: ")
  quantity=int(input("Enter the quantity: "))
  amount=0
  for chocolate in chocolates:
    if chocolate['name'] == name:
      if quantity<=chocolate['stock']:
        amount=quantity*chocolate['amount']
        chocolate['stock']-=quantity
      else:
        print("Out of stock")
  return chocolates,amount