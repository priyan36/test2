from module import bank

bank = bank()


print(bank.data)

while True:
  serv = int(input("Service Provided:\n1.Acc Cretion\n2.Deposit\n3.Withdraw\n4.Fixed Deposit\n5.Exit\n"))
      
  if serv == 1:
    name = input("Enter Name: ")
    bal = int(input("Enter Deposit Amt: "))
    fd = int(input("Enter FD Amt: "))
    bank.create(name,bal,fd)
      
            #bank.create()
  if serv == 2:
    accno =int(input("Enter Accno: "))
    depamt =int(input("Enter Deposit Amount: "))
    bank.deposit(accno,depamt)  
  if serv == 3:
    accno =int(input("Enter Accno: "))
    witamt =int(input("Enter Withdraw Amount: "))
    bank.withdraw(accno,witamt)  
  if serv == 4:
    accno =int(input("Enter Accno: "))
    fdamt =int(input("Enter FD Amount: "))
    yrs = input("Enter FD Years: ")
    bank.fd(accno,fdamt,yrs)  
  if serv == 5:
    print("Thank You!!!") 
    break 
   
  