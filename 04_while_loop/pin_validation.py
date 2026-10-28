pin=1234
i=0
while(i<3):
  num=int(input("Enter pin:"))
  i=i+1
  if num==pin:
    print("Transaction Allowed")
  else:
    print("Card Blocked")
