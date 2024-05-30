import random
class bank():
    def __init__(self):
        self.data = [["Suresh",123,2000,5000],["Raina",124,400,1000],["Virat",125,6000,2000]]
        
    def chkbal(self,accno):
        for i in self.data[1]:
            if i[1]==accno:
                print("Your Bal: ",i[1])
            else:
                print("Invalid AccNO")


    def create(self,name,bal,fd):
        accno = self.data[len(self.data)-1][1] + 1
        new = [name,accno,bal,fd]
        self.data.append(new)
        print("Name: ",name)
        print("AccNo: ",accno)
        print("Balance: ",bal)
        print("Fixed Dep: ",fd)
        print("Your Account Created")


    def deposit(self,accno,depamt):
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        if depamt > 100000:
            pan = input("Enter Pan No.: ")
            if len(pan) != 5:
                print("Ivalid Pan")
            else:
                self.data[idx][2] += depamt
                print("Your Balance: ",self.data[idx][2])
        else:
            self.data[idx][2] += depamt
            print("Your Balance: ",self.data[idx][2])


    def withdraw(self,accno,witamt):
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        if witamt > self.data[idx][2]:
            print("Insufficiant Fund.")
        else:
            self.data[idx][2] -= witamt
            print("Your Balance: ",self.data[idx][2])

    def fd(self,accno,fdamt,yrs):
        rtn = 0
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        if fdamt > 50000:
            rtn = (10000 * yrs) + self.data[idx][3]
            print("Your Return is: ",rtn)
        else:
            print ("FD should be above Rs.50000.")
                     
