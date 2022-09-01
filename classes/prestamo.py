from tabulate import tabulate
class Prestamo: 
    file = 'database/prestamo.csv'
    def __init__(self, nombre, carnet, equipo, fechap, fechae):
        self.nombre = nombre
        self.carnet = carnet
        self.equipo = equipo
        self.fechap = fechap
        self.fechae = fechae
        
    def save(self):
        f = open(self.file,'a')
        linea = ';'.join([self.nombre, self.carnet, self.equipo, self.fechap, self.fechae])
        f.write(linea+'\n')
        f.close() 
def crearPrestamo():
    print('REGISTRAR PRESTAMO')
    nombre = input('Nombre: ')
    carnet = input('Carnet: ')
    equipo = input('Equipo: ')
    fechap = input('Fecha de prestamo (yyy-mm-dd): ')
    fechae = input('Fecha de entrega (yyy-mm-dd): ')
    P = Prestamo(nombre, carnet, equipo, fechap, fechae)
    return P
def verPrestamos():
    listaprestamo = getAllPrestamos()

    carnet = input('¿Cuál es el numero del carnet?: ')
    pos = 0
    datosPrestamo = []
    for p in listaprestamo:
        if carnet in p:
            datosPrestamo = p.split(';')
            print(datosPrestamo)
            #datosPrestamo[5] = fechae + '\n'
        pos+=1
    verDatos(datosPrestamo)
def getAllPrestamos():
    a = open('database/prestamo.csv','r')
    datos = a.readlines()
    return datos

def verDatos(datosPrestamo):
    header = ['Nombre', 'Carnet', 'Equipo', 'Fecha Prestamo', 'Fecha Entrega']
    print(tabulate(datosPrestamo,header))