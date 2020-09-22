class User():
    def __init__(self, nome, apelido,year,city):
        self.nome = nome
        self.apelido = apelido
        self.year = year
        self.city = city
    def describe(self):
        print(f"Esta persoa chamase {self.nome} e da familia dos {self.apelido} e naceu no anno {self.year} en {self.city} ")
    def greet(self):
        print(f"Hola {self.nome} de  {self.city}")
xabier = User('Javier', 'Posada',1985, 'Vigo')
suso = User('Jesus', 'Comesanha', 1992, 'Coruxo')
patricia = User('patricia', 'amiga', 1999, 'Celanova')

xabier.describe()
suso.describe()
patricia.describe()


