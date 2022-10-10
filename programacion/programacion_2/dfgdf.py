from dataclasses import dataclass

a = []
@dataclass
class perro():
    edad:int = 0

    def ladra(self):
        self.edad -= 3

@dataclass
class caca(perro):

    edad:int = 23


a = caca()
print(a.edad)

