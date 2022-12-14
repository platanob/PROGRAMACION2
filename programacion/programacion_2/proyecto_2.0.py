from dataclasses import dataclass
import pygame as py
import pymysql


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
                    if self.capacidad >= 1:
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
    nombre:str = "camion"
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

"""funcion para sacar la cantidad de contenedores que tiene que llevar cada vehiculo segun el precio"""
def  mejoropcionvei(precios,lcon):
    n = [0,0,0,0]
    for o in range(len(precios) - 1 ):
        while (precios[o] * n[o] < precios[o+1]):
            n[o] += 1
        n[o] -= 1
    return veiculo_mete(lcon,n)

def veiculo_mete(contenedores,pre):
    lis_veiculos = []
    c_g , c_p =separa_conte(contenedores)
    tamaño = len(c_g) + (len(c_p)/2)
    while tamaño > 0 :
        elimina = []
        if tamaño <= 1*pre[0]:
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
        elif tamaño > 1*pre[0] and tamaño <= 10*pre[1]:
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
        elif tamaño > 10*pre[1] and tamaño < 250*pre[2] :
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
        elif tamaño >= 250*pre[2] :
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
        if c_g == None  and c_p == None:
            tamaño = 0
        elif c_g == None :
            tamaño = len(c_p)/2
        elif c_p == None:
            tamaño = len(c_g)
        else:
            tamaño = len(c_g) + (len(c_p)/2)

    for pesoss in lis_veiculos:
        pesoss.sacarpeso()
    return lis_veiculos

''' conectar a la base de datos'''

def crear_tabla(datoss):
    try:
        conec = pymysql.connect(host="db.inf.uct.cl",user="A2022_bcarrasco",password="A2022_bcarrasco",db="A2022_bcarrasco")
        cursor = conec.cursor()
        for da in datoss :
            sql = """INSERT INTO productos_py (id_producto, nombre_producto, tipo, masa,peso) VALUES (%s,%s,%s,%s,%s)"""           
            vals = (da[0], da[1], da[2], da[3], da[4])
            cursor.execute(sql, vals)
        conec.commit()
    except conec.Error as error:
        print(error)
    finally:
        cursor.close()

def sacardatos():
    try:
        conec = pymysql.connect(host="db.inf.uct.cl",user="A2022_bcarrasco",password="A2022_bcarrasco",db="A2022_bcarrasco")
        cursor = conec.cursor()
        sql = """SELECT *  from productos_py """
        cursor.execute(sql)
    except conec.Error as error:
        print(error)
    finally:
        resultado = cursor.fetchall()
        return resultado


""" crear_tabla(datos("MOCK_DATA.csv")) """


productos = sacardatos()





lista_productos=[]


for pro in productos:
    lista_productos.append(producto(int(pro[0]),str(pro[1]),str(pro[2]),str(pro[3]),float(pro[4])))

for k in lista_productos:
    k.toneladas()


lista_con = meter_productos(lista_productos)



"""for vei in lista_vehiculos:
    vei.imprimir()"""



def botones():
    smallfont = py.font.SysFont('Corbel',30) 
    pantalla.blit(smallfont.render("1.ver cantidad total de vehiculos ",True,blanco ), (20,40))
    pantalla.blit(smallfont.render("2.ver cantidad total de cada tipo de vehiculo ",True,blanco ), (20,80))
    pantalla.blit(smallfont.render("3.ver conteneidos de los vehiculos ",True,blanco ), (20,120))
    pantalla.blit(smallfont.render("4.costo de transporte ",True,blanco ), (20,160))
    pantalla.blit(smallfont.render("5.salir ",True,blanco ), (20,200))
    pantalla.blit(smallfont.render("ESC.menu ",True,blanco ), (0,450))

def can_vei(lisve):
    smallfont = py.font.SysFont('Corbel',50) 
    pantalla.blit(smallfont.render("vehiculos",True,blanco ), (160,120))
    pantalla.blit(smallfont.render(str(len(lisve)),True,blanco ), (220,200))

def contipovei(lisve):
    global im_avion , im_barco ,im_camion ,im_tren
    c = 0
    a = 0
    t = 0
    b = 0
    for el in lisve:
        if el.nombre == 'camion':
            c += 1
        elif el.nombre == 'avion':
            a += 1
        elif el.nombre == 'tren':
            t += 1
        elif el.nombre == 'barco':
            b += 1
    pantalla.blit(im_avion , (250,0))
    pantalla.blit(im_camion , (0,0))
    pantalla.blit(im_tren , (250,250))
    pantalla.blit(im_barco , (0,250))

    smallfont = py.font.SysFont('Corbel',50) 
    pantalla.blit(smallfont.render(str(c),True,rojo ), (100,100))
    pantalla.blit(smallfont.render(str(a),True,rojo ), (350,100))
    pantalla.blit(smallfont.render(str(t),True,rojo ), (350,350))
    pantalla.blit(smallfont.render(str(b),True,rojo ), (100,350))

def mostrar():
    smallfont = py.font.SysFont('Corbel',30) 
    pantalla.blit(smallfont.render('digite el numero del vehiculo',True,blanco ), (100,100))
    pantalla.blit(txt_surface, (input_box.x+5, input_box.y+5))
    py.draw.rect(pantalla, color, input_box, 2)



def preciovei():
    nombrev = ['camion','avion','tren','barco']
    smallfont = py.font.SysFont('Corbel',30) 
    pantalla.blit(smallfont.render('digite el precio del '+ nombrev[nnombrev],True,blanco ), (100,100))
    pantalla.blit(txt_surface, (input_box.x+5, input_box.y+5))
    py.draw.rect(pantalla, color, input_box, 2)

def mosdavei(num , lisve ):
    try:
        global o
        numero = num -1
        posy = 0
        smallfont = py.font.SysFont('Corbel',15) 
        smallfont2 = py.font.SysFont('Corbel',30) 
        pantalla.fill(negro)
        con_nor = 0
        con_re = 0
        con_in = 0
        p_nor = 0
        p_re = 0
        p_in = 0
        p_so = 0
        p_li = 0
        p_ga = 0
        for con in lisve[numero].l_contenedores:
            pantalla.blit(smallfont.render(str(con),True,rojo ), (0,posy))
            posy += 20
            if con.tipo_carga == 'normal':
                con_nor += 1
                p_nor += con.peso
            elif con.tipo_carga == 'refrigerada':
                con_re += 1
                p_re += con.peso
            elif con.tipo_carga == 'inflamable':
                con_in += 1
                p_in += con.peso
            if con.masa == 'solida' :
                p_so += con.peso
            elif con.masa == 'liquido' :
                p_li += con.peso
            elif con.masa== 'gas':
                p_ga += con.peso
        py.display.update()
        py.time.wait(3000)
        pantalla.fill(negro)
        pantalla.blit(smallfont2.render(('contenedores de tipo nomrla : '+str(con_nor)),True,rojo ), (0,100))
        pantalla.blit(smallfont2.render(('contenedore de tipo refrigerado : '+str(con_re)),True,rojo ), (0,160))
        pantalla.blit(smallfont2.render(('contenedores de tipo inflamable : '+str(con_in)),True,rojo ), (0,230))
        py.display.update()
        py.time.wait(3000)
        pantalla.fill(negro)
        pantalla.blit(smallfont2.render(('toneladas total de los productos :'+str(lisve[numero].peso)),True,rojo ), (0,100))
        py.display.update()
        py.time.wait(3000)
        pantalla.fill(negro)
        pantalla.blit(smallfont2.render(('toneladas de contenedores normal: '+str(p_nor)),True,rojo ), (0,100))
        pantalla.blit(smallfont2.render(('toneladas de contenedores refrigerados: '+str(p_re)),True,rojo ), (0,160))
        pantalla.blit(smallfont2.render(('toneladas de contenedores inflamable: '+str(p_in)),True,rojo ), (0,230))
        py.display.update()
        py.time.wait(3000)
        pantalla.fill(negro)
        pantalla.blit(smallfont2.render(('toneladas de masa solida: '+str(p_so)),True,rojo ), (0,100))
        pantalla.blit(smallfont2.render(('toneladas de masa liquida: '+str(p_li)),True,rojo ), (0,160))
        pantalla.blit(smallfont2.render(('toneladas de masa gas: '+str(p_ga)),True,rojo ), (0,230))
        py.display.update()
        py.time.wait(3000)
        o = 3 
    except : 
        pantalla.fill(negro)
        smallfont2 = py.font.SysFont('Corbel',50) 
        pantalla.blit(smallfont2.render(('numero no encontrado'),True,rojo ), (20,160))
        py.display.update()
        py.time.wait(3000)
        o = 3
def ptrans(lisve):
    pt = 0
    p_c = 0
    p_a = 0
    p_t = 0
    p_b = 0
    for ko in lisve:
        pt = ko.costo
        if ko.nombre == 'camion':
            p_c += ko.costo
        elif ko.nombre == 'avion':
            p_a += ko.costo
        elif ko.nombre == 'tren':
            p_t += ko.costo
        elif ko.nombre == 'barco':
            p_b += ko.costo
    smallfont = py.font.SysFont('Corbel',30) 
    pantalla.blit(smallfont.render(('costo de camiones : '+ str(p_c)),True,blanco ), (0,100))
    pantalla.blit(smallfont.render(('costo de avion : '+ str(p_a)),True,blanco ), (0,150))
    pantalla.blit(smallfont.render(('costo de tren : '+ str(p_t)),True,blanco ), (0,200))
    pantalla.blit(smallfont.render(('costo de barco : '+ str(p_b)),True,blanco ), (0,250))
    pantalla.blit(smallfont.render(('costo total : '+ str(pt)),True,blanco ), (0,300))

py.init()
resolucion = (500,500)
pantalla = py.display.set_mode(resolucion)
negro = (0,0,0)
blanco = (255,255,255)
amarrilo = (255,255,0)
rojo = (255,0,0)
numero = 0
o = 6
im_camion = py.transform.scale(py.image.load("camion.jpg"),(250,250))
im_avion = py.transform.scale(py.image.load('avion.jpg'),(250,250))
im_tren = py.transform.scale(py.image.load('tre.jpg'),(250,250))
im_barco = py.transform.scale(py.image.load('barco.jpg'),(250,250))



input_box = py.Rect(100, 200, 140, 32)
color_inactive = py.Color('lightskyblue3')
color_active = py.Color('dodgerblue2')
reloj = py.time.Clock()
color = color_inactive
text = ''
active = False
font = py.font.Font(None, 32)
nnombrev = 0
precioveiculos= []

while True :
    for ev in py.event.get():
        if ev.type == py.MOUSEBUTTONDOWN:
            if input_box.collidepoint(ev.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if ev.type == py.QUIT:
            py.quit()
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_1:
                if o == 0:
                    o = 1
            if ev.key == py.K_2 :
                if o == 0:
                    o = 2
            if ev.key == py.K_3:
                if o == 0 :
                    o= 3
                    text = ""
            if ev.key == py.K_4:
                if o == 0:
                    o = 4
            if ev.key == py.K_5:
                if o == 0:
                    py.quit()
            if ev.key == py.K_ESCAPE:
                    o=0
            if active:
                if ev.key == py.K_RETURN:
                    if o == 3:
                        print(text)
                        text = int(text)
                        mosdavei(text, lista_vehiculos)
                        text = ''
                    elif o == 6:
                        print(text)
                        precioveiculos.append(int(text))
                        text = ''
                        if nnombrev < 3 :
                            nnombrev += 1
                        else :
                            o = 0
                            lista_vehiculos = mejoropcionvei(precioveiculos,lista_con)
                elif ev.key == py.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += ev.unicode


    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    pantalla.fill(negro)
    if o == 0 :
        botones()
    elif o == 1:
        can_vei(lista_vehiculos)
    elif o == 2:
        contipovei(lista_vehiculos)
    elif o == 3 :
        mostrar()
    elif o == 4:
        ptrans(lista_vehiculos)
    elif o == 6 :
        preciovei()
    py.display.flip()
    reloj.tick(60)