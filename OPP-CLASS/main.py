import csv

class Item:
    #class atribute
    pay_rate = 0.8 #pay rate ate 20% discount 

    all = []

    def __init__(self, name:str, price:float, quantity:int):
        #run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Qdt {quantity} is not greater than zero!"
        
        #assign to self object - instance atributes
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        #we ll count out the floats that are point zero.
        # for i.e: 5.0 ,10.0
        if isinstance(num, float):
            #count out the floats that re decimal zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(7.5))


# Item.instanciate_from_csv()
# print(Item.all)

# for i in Item.all:
#     print(i.name)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.__dict__)

# item1.apply_discount()
# print(item1.price)

# print(item2.price)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)



#class from https://www.youtube.com/watch?v=Ej_02ICOIgs