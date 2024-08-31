def add_chocolates(chocolates):
  name=input("enter name of the chocolate")
  amount=int(input("enter the amount:"))
  stock=int(input("enter the stocks: "))
  chocolate={"name":name,"amount":amount,"stock":stock}
  chocolates.append(chocolate)
  return chocolates

def remove_chocolates(chocolates):
  name=input("enter name of chocolate: ")
  for chocolate in chocolates:
    if chocolate['name']==name:
      chocolates.remove(chocolate)
  return chocolates

def update_amount(chocolates):
  name=input("enter the name of chocolate: ")
  amount=int(input("enter the amount: "))
  for chocolate in chocolates:
    if chocolate['name']==name:
      chocolates['amount']==amount
  return chocolates

def update_stock(chocolates):
  name=input("enter the name of chocolate: ")
  stock=int(input("enter the stock: "))
  for chocolate in chocolates:
    if chocolate['name']==name:
      chocolates['stock']==stock
  return chocolates

def buy(chocolates):
  name=input("enter name of chocolate: ")
  quantity=int(input("enter name of chocolate: "))
  amount=0
  for chocolate in chocolates:
    if chocolate['name']==name:
     if quantity<=chocolate['stock']:
      amount=quantity*chocolate['amount']
      chocolate['stock']-=quantity
    else:
      print("out of stock")
  return chocolates,amount

