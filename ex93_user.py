class User:
    def __init__ (self, name, apelido, age, oficio):

        self.name = name
        self.apelido = apelido
        self.age = age
        self.oficio = oficio
        self.login_nb = 7

    def describe(self):
        f"\n  "
        p1 = f"\n Esta persona se llama {self.name}, e da familia dos {self.apelido},"
        p2 = f"\n ten {self.age} anos, e o seu oficio e o de {self.oficio} "
        p3 = f"\n ."
        p = p1+p2+p3
        
        print(p)

    def login_increment(self):
        self.login_nb += 1

    def login_nb_reset(self):
        self.login_nb = 0

    
pedro = User('Pedro', 'Madruga',45, 'Marinheiro' )
lucas = User('Lucas', 'Grijander', 12, 'Paiaso')
juan = User('Juan', 'Novoa', 88, 'Vixilante e inspector ademais de fotografo')
mateo = User('Mateo', 'Topten', 6, 'Hip hop dancer')

pedro.describe()
lucas.describe()
juan.describe()
mateo.describe()

print(f"\n {mateo.login_nb } inicial")
mateo.login_nb_reset()
print(f"\n {mateo.login_nb } reset")

for x in range(5):
    
    mateo.login_increment()
    print(f"\n {mateo.login_nb } incremento")
