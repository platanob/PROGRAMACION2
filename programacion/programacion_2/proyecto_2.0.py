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

@dataclass
class contenedor:
    carga:str
    masa : str
    peso:int
    tipo:str
    tamano:str
    capacidad=0
    def imprimir(self):
        print("su tipo de carga es : " , self.tipo_carga)
        print("su carga es : ", self.carga)
        print("su masa es : ",self.masa)
        print("su tamaño es : " ,self.peso)
        print("su tipo es : " , self.tipo)




@dataclass
class contenedor_normal(contenedor):
    tipo_carga = "normal"

    if self.tamano == "grande":
        capacidad=24
    elif self.tamano == "pequeño":
        capacidad=12  

@dataclass
class contenedor_refrigerado(contenedor):
    tipo_carga="refrigerada"

    if self.tamano == "grande":
        capacidad=20
    elif self.tamano == "pequeño":
        capacidad=10  

@dataclass
class contenedor_inflamable(contenedor):
    tipo_carga="inflamable"

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
            contenedor_normal













productos =datos("ejemplo_lista.csv")


lista_productos=[]

for pro in productos:
    lista_productos.append(producto(int(pro[0]),pro[1],pro[2],pro[3],float(pro[4])))




meter_productos(lista_productos)



a = contenedor_inflamable("normal","solida",23,"hiku")
a.imprimir()