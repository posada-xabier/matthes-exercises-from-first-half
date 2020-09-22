class Restaurant():
    def __init__(self, name, pais):
        self.name = name
        self.pais = pais
        self.orders = 0

    def describe(self):
        print (f" \n\t Este restaurante se llama  {self.name}  y la cocina es de  {self.pais}.")

    def set_orders(self,pedidos):
        self.orders = pedidos

    def increment(self,days):
        self.orders += 31
        

papote = Restaurant('"Papo\'s"', 'Vigo')
mosquito = Restaurant('"el mosquito"', 'Coruxo')
soria = Restaurant('"El Soriano"', 'Mos')

print(f"\n {papote.orders} orders yesterday")
papote.orders = 99
print(f"\n {papote.orders} orders today\n")
print (papote.name)
papote.set_orders(501)
print(f"\n {papote.orders} orders this week")
papote.increment(40)
print(f"\n {papote.orders} orders after 40 days")
papote.describe()
mosquito.describe()
soria.describe()

    
