class Resto():
    def __init__(self, name, pays):
        self.name = name
        self.pays = pays
    def describe(self):
        print(f"Este resto se llama {self.name} y ofrece recetas de {self.pays}")
    def open(self):
        print("The resto is open all day")

tokio = Resto('Tokio Best food', 'Japon')

print(tokio.name)
print(tokio.pays)

tokio.open()
tokio.describe()

# instancia.metodo()
# print(   f " {self.name} .... " )