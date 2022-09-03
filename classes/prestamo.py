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
    equipos = getAllEquipos()
    listaPrestamo = getAllPrestamos()
    equipo = input('Equipo: ')
    ban = 0
    for p in listaPrestamo:
        if equipo in p:
            ban = ban+1
    band = 0
    for P in equipos: ## Verifica que el equipo esté disponible.
        if equipo in P:
            datoP = P.split(';')
            disp = int(datoP[2])-ban 
            if disp > 0:
                nombre = input('Nombre: ')
                carnet = input('Carnet: ')
                fechap = input('Fecha de prestamo (yyy-mm-dd): ')
                fechae = input('Fecha de entrega (yyy-mm-dd): ')
                P = Prestamo(nombre, carnet, equipo, fechap, fechae)
                band = 1
                P.save()
                print('Prestamo registrado'.center(25,'*'))
    if band == 0:
        print('Equipo no disponible'.center(25,'*'))
def verPrestamos():
    datos = [['Nombre', 'Carnet', 'Equipo', 'Fecha Prestamo', 'Fecha Entrega']]
    listaprestamo = getAllPrestamos()
    carnet = input('¿Cuál es el número del carnet?: ')
    for p in listaprestamo:
        if carnet in p:
            datop = p.split(';')
            datos.append(datop)
    print(tabulate(datos,headers="firstrow", tablefmt='github'))
    return datos
def registroEntrega():
    listaPrestamos = getAllPrestamos()
    carnet = input('¿Cuál es el número del carnet?: ')
    equipo = input('¿Qué equipo va a entregar?: ')
    pos = 0
    for p in listaPrestamos:
        if carnet in p and equipo in p:
            listaPrestamos.pop(pos)
            print('Entrega realizada'.center(25,'*'))
        pos = pos+1
    saveAllPrestamos(listaPrestamos)
def getAllPrestamos():
    a = open('database/prestamo.csv','r')
    datos = a.readlines()
    return datos
def getAllEquipos():
    a = open('database/equipos.csv','r')
    datos = a.readlines()
    return datos
def saveAllPrestamos(prestamos):
    a = open('database/prestamo.csv','w')
    for p in prestamos:
        a.write(p)
    a.close()
