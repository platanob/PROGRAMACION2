from dataclasses import dataclass
import matplotlib.pyplot as plot

@dataclass
class pedido:
    id_producto : int
    nombre_producto:str
    tipo:str
    masa : str 
    peso : int

@dataclass
class contenedor:
    nombre:str
    tipo:str
    cantidad:int

@dataclass
class vehiculo:
    nombre:str
    costo:int
    capacidad:int
    contenedores:list


#Funcion para meter los productos a los contenedores
def compro(cantidad, estado,tipo):
    listacontenedores =[]
    tone = cantidad/1000
    estado.lower()
    tipo.lower()
    if estado == 'liquido':
        if tipo == 'normal':
            while tone > 0 :
                if tone >= 24 :
                    listacontenedores.append(contenedor('contenedor_liquido',tipo,24))
                    tone -= 24 
                else :
                    listacontenedores.append(contenedor('contenedor_liquido',tipo,tone))
                    tone -= tone

        elif tipo == 'inflamable':
            while tone > 0:
                if tone >= 20 :
                    listacontenedores.append(contenedor('contenedor_liquido_inflamable',tipo,20))
                    tone -= 20 
                else :
                    listacontenedores.append(contenedor('contenedor_liquido_inflamable',tipo,tone))
                    tone -= tone

        elif tipo == 'refrigerado':
            while tone > 0 :
                if tone >= 20:
                    listacontenedores.append(contenedor('contenedor_liquido_refrigerado_grande',tipo,20))
                    tone -= 20 
                elif tone >= 10:
                    listacontenedores.append(contenedor('contenedor_liquido_refrigerado_pequeño',tipo,10))
                    tone -= 10
                else :
                    listacontenedores.append(contenedor('contenedor_liquido_refrigerado_pequeño',tipo,tone))
                    tone -= tone

    elif estado == 'solida':
        if tipo == 'normal':
            while tone > 0:
                if tone >= 24:
                    listacontenedores.append(contenedor('contenedor_normal_grande',tipo,24))
                    tone -= 24 
                elif tone >= 12:
                    listacontenedores.append(contenedor('contenedor_normal_pequeño',tipo,12))
                    tone -= 12
                else :
                    listacontenedores.append(contenedor('contenedor_normal_pequeño',tipo,tone))
                    tone -= tone

        elif tipo == 'refrigerado':
            while tone > 0 :
                if tone >= 20:
                    listacontenedores.append(contenedor('contenedor_refrigerado_grande',tipo,20))
                    tone -= 20 
                elif tone >= 10:
                    listacontenedores.append(contenedor('contenedor_refrigerado_pequeño',tipo,10))
                    tone -= 10
                else :
                    listacontenedores.append(contenedor('contenedor_refrigerado_pequeño',tipo,tone))
                    tone -= tone

    elif estado == 'gas':
        if tipo == 'normal':
            while tone > 0 :
                if tone >= 24:
                    listacontenedores.append(contenedor('contenedor_liquido_gas',tipo,24))
                    tone -= 24 
                else :
                    listacontenedores.append(contenedor('contenedor_liquido_gas',tipo,tone))
                    tone -= tone

        elif tipo == 'inflamable':
            while tone > 0 :
                if tone >= 20:
                    listacontenedores.append(contenedor('contenedor_liquido_inflamable_gas',tipo,20))
                    tone -= 20 
                else :
                    listacontenedores.append(contenedor('contenedor_liquido_inflamable_gas',tipo,tone))
                    tone -= tone

    return listacontenedores


def tansporte(contenedores):
    conteo = 0
    listaveiculos=[]
    contenedorchico=[]
    contenedornomarl=[]
    #contamos cuantos contenedores son para separarlos de la manera mas optima
    for j in range(0,len(contenedores)):
        for i in range(0,len(contenedores[j])):
            if contenedores[j][i].nombre == "contenedor_normal_grande" or contenedores[j][i].nombre== "contenedor_refrigerado_grande":
                conteo += 1
                contenedornomarl.append(contenedores[j][i])
            elif contenedores[j][i].nombre=="contenedor_normal_pequeño" or contenedores[j][i].nombre== "contenedor_refrigerado_pequeño" or contenedores[j][i].nombre == 'contenedor_liquido_refrigerado_pequeño':
                conteo += 0.5
                contenedorchico.append(contenedores[j][i])
            elif contenedores[j][i].nombre=='contenedor_liquido_inflamable' or contenedores[j][i].nombre=='contenedor_liquido' or contenedores[j][i].nombre == "contenedor_liquido_refrigerado_grande" or contenedores[j][i].nombre == 'contenedor_liquido_inflamable_gas' or contenedores[j][i].nombre == 'contenedor_liquido_gas':
                conteo +=1
                contenedornomarl.append(contenedores[j][i])
    #Empesamos a introducir los contenedores a los vehiculos
    while conteo > 0 :
        if conteo <= 2 :
            if conteo >= 1 :
                if len(contenedornomarl) >= 1 :
                    listaveiculos.append(vehiculo('camion',500000,1,contenedornomarl[0]))
                    contenedornomarl = contenedornomarl[1:]
                    conteo -= 1
                    
                elif len(contenedorchico) >= 2:
                    listaveiculos.append(vehiculo('camion',500000,1,contenedorchico[0:2]))
                    contenedorchico = contenedorchico[2:]
                    conteo -= 1
            elif conteo < 1 :
                listaveiculos.append(vehiculo('camion',500000,conteo,contenedorchico[0]))
                contenedorchico = []
                conteo -= conteo

        elif conteo <= 100  and conteo > 2:

            if conteo < 10  :
                if len(contenedornomarl)>0 and len(contenedorchico) > 0:
                    listaveiculos.append(vehiculo('avion',1000000,conteo,(contenedornomarl,contenedorchico)))
                    contenedornomarl = []
                    contenedorchico = []
                    conteo -= conteo
                elif len(contenedornomarl) > 0 :
                    listaveiculos.append(vehiculo('avion',1000000,conteo,contenedornomarl))
                    contenedornomarl = []
                    conteo -= conteo
                elif len(contenedorchico) > 0 :
                    listaveiculos.append(vehiculo('avion',1000000,conteo,contenedorchico))
                    contenedorchico = []
                    conteo -= conteo
            else :
                if len(contenedornomarl) >= 10 :
                    listaveiculos.append(vehiculo('avion',1000000,10,contenedornomarl[:10]))
                    contenedornomarl = contenedornomarl[10:]
                    conteo -= 10
                elif len(contenedorchico) >= 20 :
                    listaveiculos.append(vehiculo('avion',1000000,10,contenedorchico[:20]))
                    contenedorchico = contenedorchico[20:]
                    conteo-=10
                else : 
                    for i in range(len(contenedornomarl)):
                        for k in range(len(contenedorchico)):
                            if i + (k/2)== 10 :
                                listaveiculos.append(vehiculo('avion',1000000,10,(contenedorchico[:k],contenedornomarl[:i])))
                                contenedorchico = contenedorchico[k:]
                                contenedornomarl = contenedornomarl[i:]
                                conteo-=10
        elif conteo < 24000 and conteo > 100 :
            if conteo >= 250 :    
                if len(contenedornomarl) >= 250 :
                    listaveiculos.append(vehiculo('avion',1000000,10,contenedornomarl[:10]))
                    contenedornomarl = contenedornomarl[10:]
                    conteo -= 250
                elif len(contenedorchico) >= 500 :
                    listaveiculos.append(vehiculo('avion',1000000,10,contenedorchico[:20]))
                    contenedorchico = contenedorchico[20:]
                    conteo-=250
                else : 
                    for i in range(len(contenedornomarl)):
                        for k in range(len(contenedorchico)):
                            if i + (k/2)== 250 :
                                listaveiculos.append(listaveiculos.append(vehiculo('tren',10000000,250,(contenedorchico[:k],contenedornomarl[:i]))))
                                contenedorchico = contenedorchico[k:]
                                contenedornomarl = contenedornomarl[i:]
                                conteo -= 250
            elif conteo < 250 :
                if len(contenedorchico) > 0 and len(contenedornomarl) > 0 :
                    listaveiculos.append(vehiculo('tren',10000000,conteo,(contenedornomarl,contenedorchico)))
                    contenedornomarl = []
                    contenedorchico = []
                    conteo -= conteo
                elif len(contenedornomarl) > 0 :
                    listaveiculos.append(vehiculo('tren',10000000,conteo,contenedornomarl))
                    contenedornomarl = []
                    conteo -= conteo
                elif len(contenedorchico) > 0 :
                    listaveiculos.append(vehiculo('tren',10000000,conteo,contenedorchico))
                    contenedorchico = []
                    conteo -= conteo
        elif conteo >= 24000 :
                if len(contenedornomarl) >= 24000 :
                    listaveiculos.append(vehiculo("barco", 1000000000, 24000,contenedornomarl[:24000]))
                    contenedornomarl = contenedornomarl[24000:]
                    conteo -= 24000
                elif len(contenedorchico) >= 48000 :
                    listaveiculos.append(vehiculo("barco", 1000000000, 24000,contenedorchico[:48000]))
                    contenedorchico = contenedorchico[48000:]
                    conteo-=24000
                else : 
                    for i in range(len(contenedornomarl)):
                        for k in range(len(contenedorchico)):
                            if i + (k/2)== 24000 :
                                listaveiculos.append(listaveiculos.append(vehiculo("barco", 1000000000, 24000,(contenedorchico[:k],contenedornomarl[:i]))))
                                contenedorchico = contenedorchico[k:]
                                contenedornomarl = contenedornomarl[i:]
                                conteo -= 24000
    return listaveiculos

#funcion para leer los datos
def leerarchivo(archivo):
    datos =[]
    with open(archivo , 'r') as fichero:
        next(fichero)
        for linea in fichero:
            linea = linea.strip('\n')
            datos.append(linea.split(','))
    fichero.close()
    return datos

def contadorvei(listavei):
    contavion = 0
    conttren = 0
    contcamion = 0
    contbarco = 0
    #contamos cuantos vehiculos tenemos
    for a in listavei:
        if a.nombre == 'avion':
            contavion += 1
        elif a.nombre == 'camion':
            contcamion += 1
        elif a.nombre == 'barco':
            contbarco += 1
        elif a.nombre == 'tren':
            conttren += 1
    print('=========================================================================================================')    
    print('Cantidad total de vehiculos : ' ,len(veiculos))
    print('Cantidad total de camiones : ' , contcamion)
    print('Cantidad total de aviones : ' , contavion)
    print('Cantidad total de barcos : ' , contbarco)
    print('Cantidad total de trenes : ' , conttren)
    print('=========================================================================================================')  

def contcontenedores(listavei):
    contadorporveiculo = 0
    n = 1
    contiponormal= 0
    contiporefrigerado = 0
    contipoinflamable = 0
    peso = 0
    pesotiponormal = 0
    pesotiporefrigerado = 0
    pesotipoinflamable = 0
    pesomasasolida = 0
    pesomasaliquida = 0
    pesomasagas = 0
    costo = 0
    numda = 331
    listadetipos=[]
    lis = []
    #recorremos todos los vehiculos y vamos sacando sus datos como los contenedores que tienen su tipo  producto que llevan cuando peso llevan de ese producto
    for transporte in listavei :
        if len(transporte.contenedores) !=2 :
            for a in range(len(transporte.contenedores)):
                if transporte.contenedores[a].tipo == 'normal':
                    contiponormal += 1
                    pesotiponormal += transporte.contenedores[a].cantidad
                elif transporte.contenedores[a].tipo == 'inflamable':
                    contipoinflamable +=1
                    pesotipoinflamable += transporte.contenedores[a].cantidad
                elif transporte.contenedores[a].tipo == 'refrigerado':
                    contiporefrigerado += 1
                    pesotiporefrigerado += transporte.contenedores[a].cantidad

                if transporte.contenedores[a].nombre == 'contenedor_liquido_inflamable_gas' or transporte.contenedores[a].nombre == 'contenedor_liquido_gas':
                    pesomasagas += transporte.contenedores[a].cantidad
                elif transporte.contenedores[a].nombre == 'contenedor_normal_grande' or transporte.contenedores[a].nombre == 'contenedor_normal_pequeño' or transporte.contenedores[a].nombre=='contenedor_refrigerado_grande' or transporte.contenedores[a].nombre=='contenedor_refrigerado_pequeño':
                    pesomasasolida+= transporte.contenedores[a].cantidad
                elif transporte.contenedores[a].nombre=='contenedor_liquido'or transporte.contenedores[a].nombre=='contenedor_liquido_inflamable'or transporte.contenedores[a].nombre== 'contenedor_liquido_refrigerado_grande' or transporte.contenedores[a].nombre=='contenedor_liquido_refrigerado_pequeño':
                    pesomasaliquida+=transporte.contenedores[a].cantidad
                contadorporveiculo +=1

                peso +=  transporte.contenedores[a].cantidad
        elif len(transporte.contenedores) == 2 :
            for a in range(len(transporte.contenedores)):
                for k in range(len(transporte.contenedores[a])):
                    if transporte.contenedores[a][k].tipo == 'normal':
                        contiponormal += 1
                        pesotiponormal += transporte.contenedores[a][k].cantidad
                    elif transporte.contenedores[a][k].tipo == 'inflamable':
                        contipoinflamable +=1
                        pesotipoinflamable += transporte.contenedores[a][k].cantidad
                    elif transporte.contenedores[a][k].tipo == 'refrigerado':
                        contiporefrigerado += 1
                        pesotiporefrigerado += transporte.contenedores[a][k].cantidad
                
                    if transporte.contenedores[a][k].nombre == 'contenedor_liquido_inflamable_gas' or transporte.contenedores[a][k].nombre == 'contenedor_liquido_gas':
                        pesomasagas += transporte.contenedores[a][k].cantidad
                    elif transporte.contenedores[a][k].nombre == 'contenedor_normal_grande' or transporte.contenedores[a][k].nombre == 'contenedor_normal_pequeño' or transporte.contenedores[a][k].nombre=='contenedor_refrigerado_grande' or transporte.contenedores[a][k].nombre=='contenedor_refrigerado_pequeño':
                        pesomasasolida+= transporte.contenedores[a][k].cantidad
                    elif transporte.contenedores[a][k].nombre=='contenedor_liquido'or transporte.contenedores[a][k].nombre=='contenedor_liquido_inflamable'or transporte.contenedores[a][k].nombre== 'contenedor_liquido_refrigerado_grande' or transporte.contenedores[a][k].nombre=='contenedor_liquido_refrigerado_pequeño':
                        pesomasaliquida+=transporte.contenedores[a][k].cantidad
                    contadorporveiculo +=1
                    peso +=  transporte.contenedores[a][k].cantidad
        
        print('=========================================================================================================')
        print('Total de contenedores en el',transporte.nombre,n,' : ', contadorporveiculo)
        print('Contenedores de tipo normal : ', contiponormal)
        print('Contenedores de tipo refrigerado : ', contiporefrigerado)
        print('contenedores de tipo inflamable : ', contipoinflamable)
        print('-------------------------------------------------------------------------------------------------------------')
        print('Toneladas totales de todos los contenedores : ' , peso)
        print('El peso de los productos de tipo normal es de  : ' , pesotiponormal)
        print('El peso de los productos de tipo inflamble es de  : ' , pesotipoinflamable)
        print('El peso de los productos de tipo refrigerado es de  : ' , pesotiporefrigerado)
        print('-------------------------------------------------------------------------------------------------------------')
        print('El peso por masa solida es de  :',pesomasasolida)
        print('El peso por masa liquida es de :',pesomasaliquida)
        print('El peso por masa gas es de  :',pesomasagas)
        print('-------------------------------------------------------------------------------------------------------------')
        print('Costo del vehiculo : ' , transporte.costo)
        print('=========================================================================================================')

        datos= [pesotiponormal,pesotipoinflamable,pesotiporefrigerado]
        nombre = ['normal','inflamable','refrigerado']
        #graficamos el peso de cada tipo de producto que lleva cada vehiculo
        plot.subplot(numda)
        plot.title("vehiculo "+ str(n))
        plot.bar(nombre,datos)
        plot.ylabel('PESO')
        plot.xlabel('TIPO')
        plot.subplots_adjust(hspace=0.55)

        lis.append(contipoinflamable)
        lis.append(contiponormal)
        lis.append(contiporefrigerado)      
        listadetipos.append(lis)
        lis= []

        numda +=1
        contiponormal= 0
        contiporefrigerado = 0
        contipoinflamable = 0
        n +=1
        contadorporveiculo = 0
        peso = 0
        pesotiponormal = 0
        pesotiporefrigerado = 0
        pesotipoinflamable = 0
        pesomasasolida = 0
        pesomasaliquida = 0
        pesomasagas = 0
        costo += transporte.costo
    print('Costo total de todos los vehiculos : ' , costo)
    plot.show()
    return listadetipos



def graficocan(lista):
    numda = 331
    nombre = ['inflamable','normal','refrigerado']
    n = 1
    #graficamos todos que cantidad de tipo de contenedores lleva cada vehiculo
    for datos in lista:
        plot.subplot(numda)
        plot.title("vehiculo "+ str(n)+' Contenedores')
        plot.bar(nombre,datos)
        plot.ylabel('NUMERO')
        plot.xlabel('TIPO')
        plot.subplots_adjust(hspace=0.55)
        numda+=1
        n +=1
    plot.show()


#cambiar el nombre del archivo de ser necesario
h =  leerarchivo('ejemplo_lista.csv')

contenedores = []

#ingresamos los datos del archivo al objeto pedido 
for i in range(0,len(h)):
    a = pedido(int(h[i][0]),h[i][1],h[i][2],h[i][3],int(h[i][4]))
    contenedores.append(compro(a.peso,a.masa,a.tipo))

veiculos = tansporte(contenedores)

paragraficar = contcontenedores(veiculos)
contadorvei(veiculos)
graficocan(paragraficar)