class Customer:
    def __init__(self, name):
        self.name = name
        self._orders=[]
        self._coffees=[]
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance (name,str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order,Order):
            self._orders.append(new_order)
        return self._orders

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee not in self._coffees and isinstance(new_coffee,Coffee):
            self._coffees.append(new_coffee)
        return self._coffees

    def create_order(coffee, price):
        if isinstance(coffee, Coffee) and isinstance(price,int):
            return Order(self,coffee,price)
        else:
            raise Exception("Inputs must be Coffee and integer types")
    
