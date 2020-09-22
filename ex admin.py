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

class Privileges():
    def __init__(self):

        self.privileges = ['read', 'write', 'delete']

    def show_privileges(self):
        for x in self.privileges:
            print(x)


class Admin(User):

    def __init__(self, name, apelido, age, oficio):

        super().__init__(name, apelido, age, oficio)

        self.privileges = Privileges()

    

jesus = Admin('Suso','Comesanha', 45, 'gaitero')

print(jesus.apelido)

jesus.privileges.show_privileges()
    
    
