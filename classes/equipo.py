# -*- coding: utf-8 -*-
from tabulate import tabulate
from datetime import datetime
from datetime import timedelta
class Equipo:
    file = 'database/equipos.csv'
    def __init__(self, nombre,provedor,cantidad, referencia,ciclo,fum='' ):
        self.nombre = nombre
        self.provedor = provedor
        self.cantidad = cantidad
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum        
    def save(self):
        f = open('database/equipos.csv','a')
        Linea = ';'.join([self.nombre,self.provedor,self.cantidad,self.referencia,self.ciclo,self.fum])
        f.write(Linea+'\n')
        f.close()
def consultadisponibilidad():
    listaEquipos = getAllEquipos()
    listaPrestamo = getAllPrestamos()
    equipo = input('Nombre del equipo: ')
    datos = [['Equipo', 'Disponibilidad']]
    ban = 0
    for p in listaPrestamo:#Cuenta los que están en prestamo y se los resta al total registrados
        if equipo in p:
            ban = ban+1
    for e in listaEquipos:
        if equipo in e:
            datoe = e.split(';')
            new = [datoe[0], int(datoe[2])-ban] 
            datos.append(new)
    print(tabulate(datos,headers="firstrow", tablefmt='github'))
def crearEquipo():
    print('Registrar equipo nuevo')
    nombre = input('Nombre: ')
    provedor = input('Provedor: ')
    cantidad = input('Cantidad : ')
    referencia = input('Referencia: ')
    ciclo = input('Ciclo de mantenimiento (días): ')
    fum = input ('Fecha del último mantenimiento (yyy-mm-dd): ')
    e = Equipo(nombre, provedor, cantidad, referencia, ciclo, fum)
    return e
def verDatosEquipos():
    datos = [['Nombre', 'Referencia', 'Cantidad', 'Provedor', 'Ciclo', 'Fum']]
    listaEquipos = getAllEquipos()
    for e in listaEquipos:
        datoe = e.split(';')
        datos.append(datoe)
    print(tabulate(datos,headers="firstrow", tablefmt='github'))
def registroMantenimiento():
    listaEquipos = getAllEquipos()
    equipo = input('Equipo: ')
    fum = input('Fecha último mantenimiento: ')
    pos = 0
    for e in listaEquipos:
        if equipo in e:
            datosEquipo = e.split(';')
            datosEquipo[5] = fum + '\n'
            listaEquipos[pos] =';'.join(datosEquipo)    
        pos+=1
    print('Fecha de mantenimiento actualizada'.center(25,'*'))
    saveAllEquipos(listaEquipos)
def mantenimiento():
    listaEquipos = getAllEquipos()
    datos = [['Equipo','Fecha mantenimiento']]
    characters = '\n'
    fechaI = input('Diga la fecha inicial (yyy-mm-dd): ')
    fechaI = datetime.strptime(fechaI,'%Y/%m/%d')
    fechaF = input('Diga la fecha final (yyy-mm-dd): ')
    fechaF = datetime.strptime(fechaF,'%Y/%m/%d')
    for e in listaEquipos:
        datosEquipo = e.split(';')
        fechaM = datosEquipo[5]
        for x in range(len(characters)):
            fechaM = fechaM.replace(characters[x],"")
        fechaM = datetime.strptime(fechaM,'%Y/%m/%d')
        fechaM = fechaM + timedelta(days=int(datosEquipo[4]))
        if fechaM >= fechaI and fechaF >= fechaM: #Se incluyen los limites
            new = [datosEquipo[0], fechaM.strftime('%Y/%m/%d')]
            datos.append(new)
    print(tabulate(datos,headers="firstrow", tablefmt='github'))
def saveAllEquipos(equipos):
    a = open('database/equipos.csv','w')
    for e in equipos:
        a.write(e)
    a.close()
def getAllEquipos():
    a = open('database/equipos.csv','r')
    datos = a.readlines()
    return datos
def getAllPrestamos():
    a = open('database/prestamo.csv','r')
    datos = a.readlines()
    return datos 