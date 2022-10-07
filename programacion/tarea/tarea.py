from dataclasses import dataclass


@dataclass
class contenedor:
    nombre:str
    tipo:str
    cantidad:int
    hola = 2
    def mostrarc(self):
        print('========================================================')
        print('El nombre del vehiculo es : ', self.nombre)
        print('El tipo es de : ', self.tipo)
        print('La cantidad  es de : ', self.cantidad)
        print('========================================================')
    def cambiarcantidad(self,nueva):
        self.cantidad = nueva

@dataclass
class vehiculo:
    nombre:str
    costo:int
    capacidad:int
    contenedores:list
    holi = 2
    def mostrarv(self):
        print('========================================================')
        print('El nombre del vehiculo es : ', self.nombre)
        print('El costo es de : ', self.costo)
        print('La capacidad  es de : ', self.capacidad)
        print('Los contenedores son : ', self.contenedores)
        print('========================================================')
    def cambiarnombre(self,nuevonombre):
        self.nombre = nuevonombre


@dataclass
class contenedorliquido(contenedor):
    hola = 0

@dataclass
class vehiculocamion(vehiculo):
    holi = 0

el1 = contenedor('mariposa', 'voladora', 420)

el1.mostrarc()
el1.cambiarcantidad(144)
el1.mostrarc()
print('hola vale : ',el1.hola)



el2 = vehiculo('lancha', 1000, 3, ['hola','profe',':D'])

el2.mostrarv()
el2.cambiarnombre('helicoptero apache de combate')
el2.mostrarv()
print('holi vale : ',el2.holi)



conten = contenedorliquido("contenedor liquido", "solido", 1000)
cam = vehiculocamion('camion', 10, 23, [1,2,3])

cam.mostrarv()
cam.cambiarnombre('perro')
cam.mostrarv()
print('holi vale : ',cam.holi)


conten.mostrarc()
conten.cambiarcantidad(20)
conten.mostrarc()
print('hola vale : ',conten.hola)

