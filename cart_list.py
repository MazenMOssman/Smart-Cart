# This file will be used to count number of products based on the neural network predictions.
class Cart:
    def __init__(self):
# Initialize price, the list of products, and number of products in the cart to 0 
        self.price = 0
        self.count = 0
        self.list = []

# This method modify the price based on the product predicted.
    def Quantaty(self, id, num = 1 ):
        self.count = self.count + num
        for i in range(0,num):
            if id == 0:
               self.price = self.price + 20
               self.list.append(0)
            elif id == 1:
               self.price = self.price + 5
               self.list.append(1)
            elif id == 2:
                self.price = self.price + 10
                self.list.append(2)
            elif id == 3:
                self.list.append(3)
                self.price = self.price + 3
            elif id == 4:
                self.price = self.price + 8
                self.list.append(4)
            else:
                print("we don't have the product please contact the manager for more info")
                return 0

# This function deletes the item if there are no item, it will print you don't have any prouct
    def Delete_item(self, id):
        if self.count <= 0 or self.price <= 0:
            print("You don't have any product in the cart")
            return 0
        elif id == 0:
            if 0 not in self.list:
                print("sorry you don't have the product")
                return 0
            else:
               for i in range (0,len(self.list)):
                   if self.list[i] == 0:
                      self.list.remove(0)
                      self.price = self.price - 20
                      self.count = self.count - 1
                      break
        elif id == 1 :
            if id not in self.list:
                print("sorry you don't have the product")
                return 0
            else:
                for i in range (0,len(self.list)):
                    if self.list[i] == 1:
                       self.price = self.price - 5
                       self.count = self.count - 1
                       self.list.remove(1)
                       break
        elif id == 2:
            if id not in self.list:
                print("sorry you don't have the product")
                return 0
            else:
                for i in range (0,len(self.list)):
                    if self.list[i] == 2:
                       self.list.remove(2)
                       self.price = self.price -10
                       self.count = self.count -1
                       break

        elif id == 3:
            if id not in self.list:
                print("sorry you don't have the product")
                return 0
            else:
                for i in range (0,len(self.list)):
                    if self.list[i] == 3:
                       self.list.remove(3)
                       self.price = self.price -3
                       self.count = self.count -1
                       break
        elif id == 4 :
            if ud not in self.list:
                print("sorry you don't have the product")
                return 0
            else:
                for i in range (0,len(self.list)):
                    if self.list[i] == 4:
                        self.list.remove(4)
                        self.price = self.price -8
                        self.count = self.count -1
                        break
        else:
            print("we don't have the product please contact the manager for more info")

# this function is performs checkout once the user pays using the app.
    def checkout(self):
        self.price = 0
        self.count = 0
        self.list.clear()
        print("Thank you for your visit your current price is ",self.price)
    
# A, Ce, Co, Da, Sa prints the products quantity in the cart.
    def Get_products(self):
        self.A = 0
        self.Ce = 0
        self.Co = 0
        self.Da = 0
        self.Sa = 0
        if self.count <= 0 or self.price <= 0:
            return "you don't have any product in the cart"
        for i in range(0,len(self.list)):
            if self.list[i] == 0:
                self.A = self.A +1
            elif self.list[i] == 1:
                self.Ce = self.Ce + 1
            elif self.list[i] == 2:
                self.Co = self.Co + 1
            elif self.list[i] == 3:
                self.Da = self.Da + 1
            elif self.list[i] == 4:
                self.Sa = self.Sa + 1
        return self.A,self.Ce,self.Co,self.Da,self.Sa,self.price

