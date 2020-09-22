class Restaurant():
    def __init__(self, name, pais):
        self.name = name
        self.pais = pais
        self.orders = 0

    def describe(self):
        p1 = f"\n Este restaurante se llama  {self.name}  y la cocina"
        p2 = f"\n es de  {self.pais}."
        print(p1+p2)

    def set_orders(self,pedidos):
        self.orders = pedidos

    def increment(self,days):
        self.orders += 31


class IceCreamStand(Restaurant):
    def __init__(self,name,pais):
        super().__init__(name,pais)

        self.flavors = ['fresa','vainilla','chocolate']

    def describe_flavors(self):
        for x in self.flavors:
            print(x)

roco = IceCreamStand('Rock&Roll', 'Italia')

print(roco.name)
roco.describe()
roco.describe_flavors()
            
