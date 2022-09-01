# -*- coding: utf-8 -*-
from tabulate import tabulate
from datetime import datetime
class Equipo:
    file = 'database/equipos.csv' #Variables de clase
    def __init__(self, nombre,provedor,cantidad, referencia,ciclo,fum='' ):
        self.nombre = nombre
        self.provedor = provedor
        self.cantidad = cantidad
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum
    def verDatos(self):
        header = ['Nombre', 'Referencia', 'Cantidad', 'Provedor', 'Ciclo', 'Fum']
        datos = [self.nombre, self.referencia, self.cantidad, self.provedor, self.ciclo, self.fum]
        print[tabulate(datos,header, tablefmt='github')]
        
    def save(self):
        f = open('database/equipos.csv','a')
        Linea = ';'.join([self.nombre,self.provedor,self.cantidad,self.referencia,self.ciclo,self.fum])
        f.write(Linea+'\n')
        f.close()
    def consultar (self, nombre):
        pass
        
def crearEquipo():
    print('Registrar equipo nuevo')
    nombre = input('Nombre: ')
    provedor = input('Provedor: ')
    cantidad = input('Cantidad : ')
    referencia = input('Referencia: ')
    ciclo = input('Ciclo de mantenimiento (días): ')
    fum = input ('Fecha del último mantenimiento (yyy-mm-dd): ')
    print(fum)
    e = Equipo(nombre, provedor, cantidad, referencia, ciclo, fum)
    return e
def consultarEquipo():
    print('Consulta de equipos')
    nombre = input('Nombre del equipo')
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
    saveAllEquipos(listaEquipos)
    
def saveAllEquipos(equipos):
    a = open('database/equipos.csv','w')
    print (equipos)
    for e in equipos:
        a.write(e)
    a.close()
    
def getAllEquipos():
    a = open('database/equipos.csv','r')
    datos = a.readlines()
    return datos

def registroEntrega():
    pass