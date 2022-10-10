from dataclasses import dataclass


@dataclass
class vehiculo:
    nombre : str

@dataclass
class producto:
    id_producto :int
    nombre:str
    tipo:str
    masa:str
    peso:float


    def quitarpeso(self,menos):
        self.peso -= menos


@dataclass
class contenedor:
    masa : str
    tipo:str
    tamano:str
    peso :float = 0
    tipo_carga :str = ''
    lista_productos = []
    capacidad: float = 0 


    def imprimir(self):
        print("su tipo de carga es : " , self.tipo_carga)
        print("su masa es : ",self.masa)
        print("su tamaño es : " ,self.peso)
        print("su tipo es : " , self.tipo)
        print("su tipo es : " , self.lista_productos)
        print('su capacidad es de : ',self.capacidad)


    def tiene_espacio(self):
        if self.capacidad > 0 :
            return True
        else:
            return False


    def con_producto(self,producto):
        self.lista_productos.append(producto)
        self.capacidad -= producto.peso
        self.peso += producto.peso





class contenedor_normal(contenedor):
    tipo_carga:str = "normal"

    def tamano_contenedor(self):
        if self.tamano == "grande":
            self.capacidad=24
        elif self.tamano == "pequeño":
            self.capacidad=12  


class contenedor_refrigerado(contenedor):
    tipo_carga:str="refrigerada"

    def tamano_contenedor(self):
        if self.tamano == "grande":
            self.capacidad=20
        elif self.tamano == "pequeño":
            self.capacidad

class contenedor_inflamable(contenedor):
    tipo_carga:str="inflamable"

    def tamano_contenedor(self):
        if self.tamano == "grande":
            capacidad=22
        elif self.tamano == "pequeño":
            capacidad=11  







def datos(archivo):
    datos =[]
    with open(archivo , 'r') as fichero:
        next(fichero)
        for linea in fichero:
            linea = linea.strip('\n')
            datos.append(linea.split(','))
    fichero.close()
    return datos

def tiene_espacio(tipo,lista):
    try:
        for contenedor in lista:
            if contenedor.tipo == tipo:
                if contenedor.capacidad > 0 :
                    pass
    except:
            pass




def meter_productos(productos):
    lista_contenedores=[]
    for producto in productos:
        if producto.tipo=="normal":
            if len(lista_contenedores)==0:
                if producto.peso <= 12 :
                    conte_momentanio = contenedor_normal(producto.masa,producto.tipo,"pequeño")
                    conte_momentanio.tamano_contenedor()
                    conte_momentanio.con_producto(producto)
                    lista_contenedores.append(conte_momentanio)
                elif producto.peso >= 24 :
                    conte_momentanio = contenedor_normal(producto.masa,producto.tipo,"grande")
                    conte_momentanio.con_producto(producto)
                    lista_contenedores.append(conte_momentanio)
                elif producto.peso > 24 :
                    conte_momentanio = contenedor_normal(producto.masa,producto.tipo,"grande")
                    conte_momentanio.con_producto(producto)
                    lista_contenedores.append(conte_momentanio)

    return lista_contenedores











"""productos =datos("ejemplo_lista.csv")


lista_productos=[]

for pro in productos:
    lista_productos.append(producto(int(pro[0]),pro[1],pro[2],pro[3],float(pro[4])))




meter_productos(lista_productos)



a = contenedor_inflamable("normal","solida",23,"hiku")
a.imprimir()"""

j = producto(2, 'papas', 'normal', 'solido', 7)
k = producto(6, 'berengena', 'normal', 'solido', 5)
kl = []
kl.append(j)
kl.append(k)
ol = meter_productos(kl)
print(ol[0].lista_productos)