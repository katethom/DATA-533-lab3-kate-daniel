class objectprice():
    def __init__(self, name, price, prov):
        self.name = name
        self.price = price
        self.prov = prov

    def getprice(self):
        return calctax.tax(self)

class calctax():
    def __init__(self, name, price, prov):
            objectprice.__init__(self, name, price, prov)

    def tax(self):

        if self.prov == 'bc':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.12 + self.price))
        if self.prov == 'alb':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
        if self.prov == 'sas':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.11 + self.price))
        if self.prov == 'man':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.13 + self.price))
        if self.prov == 'ont':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.13 + self.price))
        if self.prov == 'que':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.14975 + self.price))
        if self.prov == 'nb':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'pei':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'ns':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'nal':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'yuk':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
        if self.prov == 'nwt':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
        if self.prov == 'nun':
            return print("The total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
