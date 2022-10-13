from dataclasses import dataclass


@dataclass
class vehiculo:
    nombre = ''
    costo = 0
    capacidad = 0
    l_contenedores = []
    peso = 0

    def meter_contenedores(self,losconte):
        ol = []
        if losconte == None:
            return []
        elif len(losconte) == 1:
            ol.append(losconte[0])
        else :
            for conte in losconte:
                if self.capacidad > 0 :
                    if self.capacidad > 1:
                        self.l_contenedores.append(conte)
                        ol.append(conte)
                        if conte.tamano == "grande" :
                            self.capacidad -= 1
                        elif conte.tamano == "pequeño":
                            self.capacidad -= 0.5
                    elif self.capacidad == 0.5:
                        self.l_contenedores.append(conte)
                        ol.append(conte)
                        self.capacidad -= 0.5
        return ol
    def imprimir(self):
        print('su nombre es  : ',self.nombre)
        print('su costo es de : ' ,self.costo)
        print('su capacidad es de : ', self.capacidad)
        print('su peso es de  : ', self.peso)
        print('sus contenedores son : ', self.l_contenedores)


    def sacarpeso(self):
        l = 0
        for k in self.l_contenedores:
            l +=k.peso
        self.peso = l
    def tiene_espacio(self):
        if self.capacidad > 0 :
            return True
        else:
            return False
class camion(vehiculo):
    nombre:str = "avion"
    costo:int = 500000
    capacidad:int = 1
    l_contenedores = []

class avion(vehiculo):
    nombre:str  = 'avion'
    costo:int = 1000000
    capacidad:int = 10
    l_contenedores = []

class tren(vehiculo):
    nombre:str = 'tren'
    costo = 10000000
    capacidad = 250
    l_contenedores = []

class barco(vehiculo):
    nombre = 'barco'
    costo = 1000000000
    capacidad = 24000
    l_contenedores = []



@dataclass
class producto:
    id_producto :int
    nombre:str
    tipo:str
    masa:str
    peso:float



    def quitarpeso(self,menos):
        self.peso -= menos

    def pesomaximo(self,pes):
        self.peso = pes

    def toneladas(self):
        self.peso= self.peso/1000
@dataclass
class contenedor:
    masa : str
    tipo:str
    tamano:str
    peso :float = 0
    tipo_carga  = ''
    lista_productos = []
    capacidad: float = 0 


    def imprimir(self):
        print('===============================================================')
        print("su tipo de carga es : " , self.tipo_carga)
        print("su masa es : ",self.masa)
        print("su peso es : " ,self.peso)
        print("su tipo es : " , self.tipo)
        print("sus productos son es : " , self.lista_productos)
        print('su capacidad es de : ',self.capacidad)
        print('su tamaño es : ' , self.tamano)
        print('===============================================================')
    def tiene_espacio(self):
        if self.capacidad > 0 :
            return True
        else:
            return False


    def con_producto(self,produ):
        self.lista_productos.append(produ)
        self.capacidad -= produ.peso
        self.peso += produ.peso
    





class contenedor_normal(contenedor):
    tipo_carga:str= "normal"

    def tamano_contenedor(self):
        self.lista_productos=[]
        if self.tamano == "grande":
            self.capacidad=24
        elif self.tamano == "pequeño":
            self.capacidad=12  


class contenedor_refrigerado(contenedor):
    tipo_carga:str="refrigerada"
    def tamano_contenedor(self):
        self.lista_productos=[]
        if self.tamano == "grande":
            self.capacidad=20
        elif self.tamano == "pequeño":
            self.capacidad=10

class contenedor_inflamable(contenedor):
    tipo_carga:str="inflamable"
    def tamano_contenedor(self):
        self.lista_productos=[]
        if self.tamano == "grande":
            self.capacidad=22
        elif self.tamano == "pequeño":
            self.capacidad=11  




def datos(archivo):
    datos =[]
    with open(archivo , 'r') as fichero:
        next(fichero)
        for linea in fichero:
            linea = linea.strip('\n')
            datos.append(linea.split(','))
    fichero.close()
    return datos




def pasoelmaximo(produr,maximo):
    lisa = []
    while produr.peso > 0 :
        if produr.peso > maximo : 
            lisa.append(producto(produr.id_producto,produr.nombre,produr.tipo,
            produr.masa,maximo))
            produr.quitarpeso(maximo)
        else :   
            lisa.append(producto(produr.id_producto,produr.nombre,produr.tipo,
            produr.masa,produr.peso))
            produr.quitarpeso(produr.peso)
    return lisa

def maxdeconte(produ,maxi):
    li = []
    li.append(producto(produ.id_producto, produ.nombre, produ.tipo,
    produ.masa, maxi))
    k = produ.peso-maxi
    li.append(producto(produ.id_producto, produ.nombre, produ.tipo,
    produ.masa, k))
    return li
def sacarcontenedores(nume,liscon):
    loscontenedores = []
    k = len(liscon)
    for con in liscon :
        loscontenedores.append(con)
        nume -= 1
        k -= 1
        if nume <= 0 or k <= 0:
            return loscontenedores
def creatonte(produkl,tama):
    if produkl.masa == 'solida':
        conte_momentanio = contenedor_normal(produkl.masa,'contenedor',tama)
    conte_momentanio.tamano_contenedor()
    conte_momentanio.con_producto(produkl)
    return conte_momentanio

def maximosdeproductos(productoss):
    lispro=[]
    for p in productoss:
        
        if p.tipo == "normal":
            if p.peso > 24 :
                k = pasoelmaximo(p, 24)
                for lk in k:
                    lispro.append(lk)
            else: 
                lispro.append(p)
        elif p.tipo == "refrigerado":
            if p.peso > 20:
                k =(pasoelmaximo(p, 20))
                for lk in k:
                    lispro.append(lk)
            else :
                lispro.append(p)
        elif p.tipo == "inflamable":
            if p.peso > 22:
                k =(pasoelmaximo(p, 22))
                for lk in k:
                    lispro.append(lk)
            else : 
                lispro.append(p)
    
    return lispro
def meter_productos(productos):
    
    lista_contenedores=[]
    productos = maximosdeproductos(productos)
    for producto2 in productos:
        oscar = True
        if producto2.tipo=="normal":
            if len(lista_contenedores)==0:
                if producto2.masa == "solida":
                    if producto2.peso <= 24 and producto2.peso > 12:
                        conte_momentanio = contenedor_normal(producto2.masa,'contenedor',"grande")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                    elif producto2.peso <= 12 and producto2.peso > 0:
                        conte_momentanio = contenedor_normal(producto2.masa,'contenedor',"pequeño")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                elif producto2.masa == 'liquida' or producto2.masa == 'gas':
                    if producto2.peso <= 24 and producto2.peso > 12:
                        conte_momentanio = contenedor_normal(producto2.masa,'estanque',"grande")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                    elif producto2.peso <= 12 and producto2.peso > 0:
                        conte_momentanio = contenedor_normal(producto2.masa,'estanque',"pequeño")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
            elif len(lista_contenedores) > 0 : 
                    for cont in lista_contenedores:
                        if cont.tipo_carga == 'normal':
                            if cont.tiene_espacio() :
                                if producto2.masa == cont.masa:
                                    if cont.capacidad >= producto2.peso:
                                        cont.con_producto(producto2)
                                        oscar = False
                                        break
                                    else :
                                        wakanda = maxdeconte(producto2, cont.capacidad)
                                        cont.con_producto(wakanda[0])
                                        productos.append(wakanda[1])
                                        oscar = False
                                        break
                    if oscar :
                        if producto2.masa == 'solida':
                            if producto2.peso <= 24 and producto2.peso > 12:
                                conte_momentanio = contenedor_normal(producto2.masa,'contenedor',"grande")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                            elif producto2.peso <= 12 and producto2.peso > 0:
                                conte_momentanio = contenedor_normal(producto2.masa,'contenedor',"pequeño")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                        elif producto2.masa == 'liquida' or producto2.masa == 'gas':
                            if producto2.peso <= 24 and producto2.peso > 12:
                                conte_momentanio = contenedor_normal(producto2.masa,'estanque',"grande")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                            elif producto2.peso <= 12 and producto2.peso > 0:
                                conte_momentanio = contenedor_normal(producto2.masa,'estanque',"pequeño")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
        elif producto2.tipo == 'refrigerado':
            if len(lista_contenedores)==0:
                if producto2.masa == "solida":
                    if producto2.peso <= 20 and producto2.peso > 10:
                        conte_momentanio = contenedor_refrigerado(producto2.masa,'contenedor',"grande")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                    elif producto2.peso <= 10 and producto2.peso > 0:
                        conte_momentanio = contenedor_refrigerado(producto2.masa,'contenedor',"pequeño")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                elif producto2.masa == 'liquida' or producto2.masa == 'gas':
                    if producto2.peso <= 20 and producto2.peso > 10:
                        conte_momentanio = contenedor_refrigerado(producto2.masa,'estanque',"grande")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                    elif producto2.peso <= 10 and producto2.peso > 0:
                        conte_momentanio = contenedor_refrigerado(producto2.masa,'estanque',"pequeño")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
            elif len(lista_contenedores) > 0 : 
                    for cont in lista_contenedores:
                        if cont.tipo_carga == 'refrigerada':
                            if cont.tiene_espacio() :
                                if producto2.masa == cont.masa:
                                    if cont.capacidad >= producto2.peso:
                                        cont.con_producto(producto2)
                                        oscar = False
                                        break
                                    else :
                                        wakanda = maxdeconte(producto2, cont.capacidad)
                                        cont.con_producto(wakanda[0])
                                        productos.append(wakanda[1])
                                        oscar = False
                                        break
                    if oscar : 
                        if producto2.masa == 'solida':
                            if producto2.peso <= 20 and producto2.peso > 10:
                                conte_momentanio = contenedor_refrigerado(producto2.masa,'contenedor',"grande")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                            elif producto2.peso <= 10 and producto2.peso > 0:
                                conte_momentanio = contenedor_refrigerado(producto2.masa,'contenedor',"pequeño")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                        elif producto2.masa == 'liquida' or producto2.masa == 'gas':
                            if producto2.peso <= 20 and producto2.peso > 10:
                                conte_momentanio = contenedor_refrigerado(producto2.masa,'estanque',"grande")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                            elif producto2.peso <= 10 and producto2.peso > 0:
                                conte_momentanio = contenedor_refrigerado(producto2.masa,'estanque',"pequeño")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
        elif producto2.tipo == 'inflamable':
            if len(lista_contenedores)==0:
                if producto2.masa == "solida":
                    if producto2.peso <= 22 and producto2.peso > 11:
                        conte_momentanio = contenedor_inflamable(producto2.masa,'contenedor',"grande")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                    elif producto2.peso <= 11 and producto2.peso > 0:
                        conte_momentanio = contenedor_inflamable(producto2.masa,'contenedor',"pequeño")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                elif producto2.masa == 'liquida' or producto2.masa == 'gas':
                    if producto2.peso <= 22 and producto2.peso > 11:
                        conte_momentanio = contenedor_inflamable(producto2.masa,'estanque',"grande")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
                    elif producto2.peso <= 11 and producto2.peso > 0:
                        conte_momentanio = contenedor_inflamable(producto2.masa,'estanque',"pequeño")
                        conte_momentanio.tamano_contenedor()
                        conte_momentanio.con_producto(producto2)
                        lista_contenedores.append(conte_momentanio)
            elif len(lista_contenedores) > 0 : 
                    for cont in lista_contenedores:
                        if cont.tipo_carga == 'inflamable':
                            if cont.tiene_espacio() :
                                if producto2.masa == cont.masa:
                                    if cont.capacidad >= producto2.peso:
                                        cont.con_producto(producto2)
                                        oscar = False
                                        break
                                    else :
                                        wakanda = maxdeconte(producto2, cont.capacidad)
                                        cont.con_producto(wakanda[0])
                                        productos.append(wakanda[1])
                                        oscar = False
                                        break
                                
                    if oscar :
                        if producto2.masa == 'solida':
                            if producto2.peso <= 22 and producto2.peso > 11:
                                conte_momentanio = contenedor_inflamable(producto2.masa,'contenedor',"grande")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                            elif producto2.peso <= 11 and producto2.peso > 0:
                                conte_momentanio = contenedor_inflamable(producto2.masa,'contenedor',"pequeño")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                        elif producto2.masa == 'liquida' or producto2.masa == 'gas':
                            if producto2.peso <= 22 and producto2.peso > 11:
                                conte_momentanio = contenedor_inflamable(producto2.masa,'estanque',"grande")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
                            elif producto2.peso <= 11 and producto2.peso > 0:
                                conte_momentanio = contenedor_inflamable(producto2.masa,'estanque',"pequeño")
                                conte_momentanio.tamano_contenedor()
                                conte_momentanio.con_producto(producto2)
                                lista_contenedores.append(conte_momentanio)
    return lista_contenedores

def separa_conte(contenedores):
    contenedores_grandes = []
    contenedores_pequeños = []
    for hola in contenedores:
        if hola.tamano == 'grande':
            contenedores_grandes.append(hola)
        else:
            contenedores_pequeños.append(hola) 

    return contenedores_grandes , contenedores_pequeños


def veiculo_mete(contenedores):
    lis_veiculos = []
    
    c_g , c_p =separa_conte(contenedores)
    tamaño = len(c_g) + (len(c_p)/2)
    while tamaño > 0 :
        elimina = []
        if tamaño <= 2:
            conetes = sacarcontenedores(2, c_p)
            conetes2 = sacarcontenedores(1, c_g)
            ve = camion()

            elimina = ve.meter_contenedores(conetes)
            for kaka in elimina:
                c_p.remove(kaka)
            
            elimina = ve.meter_contenedores(conetes2)
            for kaka in elimina:
                c_g.remove(kaka)
            lis_veiculos.append(ve)
        elif tamaño > 2 and tamaño <= 100:
            conetes = []
            conetes = sacarcontenedores(20, c_p)
            conetes2 = sacarcontenedores(10, c_g)
            ve = avion()
            elimina = ve.meter_contenedores(conetes)
            for kaka in elimina:
                c_p.remove(kaka)
            elimina = ve.meter_contenedores(conetes2)
            for kaka in elimina:
                c_g.remove(kaka)
            lis_veiculos.append(ve)
        elif tamaño > 100 and tamaño <24000 :
            conetes = []
            conetes = sacarcontenedores(500, c_p)
            conetes2 = sacarcontenedores(250, c_g)
            ve = tren()
            elimina = ve.meter_contenedores(conetes)
            for kaka in elimina:
                c_p.remove(kaka)
            elimina = ve.meter_contenedores(conetes2)
            for kaka in elimina:
                c_g.remove(kaka)
            lis_veiculos.append(ve)
        elif tamaño >= 24000 :
            conetes = []
            conetes = sacarcontenedores(48000, c_p)
            conetes2 = sacarcontenedores(24000, c_g)
            ve = barco()
            elimina = ve.meter_contenedores(conetes)
            for kaka in elimina:
                c_p.remove(kaka)
            elimina = ve.meter_contenedores(conetes2)
            for kaka in elimina:
                c_g.remove(kaka)
            lis_veiculos.append(ve)
        tamaño = len(c_g) + (len(c_p)/2)

    for pesoss in lis_veiculos:
        pesoss.sacarpeso()
    return lis_veiculos






productos =datos("ejemplo_lista.csv")


lista_productos=[]


for pro in productos:
    lista_productos.append(producto(int(pro[0]),pro[1],pro[2],pro[3],float(pro[4])))

for k in lista_productos:
    k.toneladas()


lista_con = meter_productos(lista_productos)



lista_vehiculos = veiculo_mete(lista_con)
for vei in lista_vehiculos:
    vei.imprimir()
""" j = producto(2, 'papas', 'normal', 'solido', 22)
k = producto(6, 'berengena', 'normal', 'solido', 5)
kl = []
kl.append(j)
kl.append(k)
ol = meter_productos(kl)
for po in ol :
    print(po.imprimir()) """