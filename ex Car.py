class Car():
    def __init__(self,marca,modelo,year):

        self.marca  = marca
        self.modelo  = modelo
        self.year  = year
        self.kms = 100_500

    def describe(self):
        # I'll use:    p_ = f"\n   "    p = p1+p2+p3
        p1 = f"\n Este bolido ha sido disenhado por la prestigiosa marca "
        p2 = f"\n {self.marca} bajo la denominacion de turbo {self.modelo} "
        p3 = f"\n el anho {self.year}. a dia de hoy tiene {self.kms} kilometros .\n"
        parrafo = p1+p2+p3
        return parrafo

javier = Car('Seat', 'Panda', 1992)

javier.kms = 300_600

print(javier.describe())

p = "45"
q = "67"
print(p+q+"simbolo +")
print(p,q, "separados por coma sin espacios")
print(p,   q,   "separado por comas y espacios")
