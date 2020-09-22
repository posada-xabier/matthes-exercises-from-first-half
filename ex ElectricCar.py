
class Car():
    def __init__(self,marca,modelo,year):

        self.marca  = marca
        self.modelo  = modelo
        self.year  = year
        self.kms = 100_500
       

    def describe(self):
        # I'll use:    p_ = f"\n   "    p = p1+p2+p3
        p1 = f"\n Este bolido ha sido disenhado por la prestigiosa marca "
        p2 = f"\n {self.marca} bajo la denominacion de turbo {self.modelo} durante "
        p3 = f"\n el anho {self.year}. A dia de hoy tiene {self.kms} kilometros .\n"
        
        parrafo = p1+p2+p3
        return parrafo

    

class Battery():
    def __init__(self, batt_size = 75):

        self.batt_size = batt_size
        self.batt_color = 'black'
        self.batt_weigth = 90
        self.batt_price = 7000

    def describe_batt(self):
        text = f"\n Esta bateria tiene {self.batt_size} kWh de capacidad. "
        return text
        

       


class ECar(Car):
    def __init__ (self,marca,modelo,year):

        super(). __init__(marca, modelo,year)

        self.acumulador = Battery

    def describe_batt(self):
        text = f"this battery has a {self.acumulador.batt_size} kWh capacity"
        print(text)



print("\n CREAR INSTANCIA DE ECAR  ")
my_tesla = ECar('Tesla','Pig', 1900)

print("\n DESCRIBIR CAR  ")
print(my_tesla.describe())

print("\n  DESCRIBE BATT ")
print(my_tesla.acumulator.describe_batt())

print("\n TAMANHO BATT  ")
my_tesla.batt_size = 225

print("\n CAPACIDAD  BATT  ")
print(f"Su capacidad es de: {my_tesla.batt_size}.")

print("\n  DESCRIBE  BATT ")
my_tesla.describe_batt()

