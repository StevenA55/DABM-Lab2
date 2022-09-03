# -*- coding: utf-8 -*-
from classes.menu import *
from classes.equipo import *
from classes.prestamo import *

if __name__=='__main__':
    menu = menu('Escuela de Ingeniería')
    op = menu.ver()
    while 1 < op and op > 3:
        print('No es una opción válida'.center(25,'*'))
        op = menu.ver() 
    if op == 1: # INICIO MENU TECNICOS
        menu2 = menuTecnicos('Escuela de Ingeniería')
        op2 = menu2.ver()
        while 1 < op2 and op2 > 7:
            print('No es una opción válida'.center(25,'*'))
            op2 = menu2.ver()   
        if op2 ==1:
            e = crearEquipo()
            e.save()
            print('Equipo creado'.center(25,'*'))
        elif op2==2:
            verDatosEquipos() 
        elif op2 == 3:
            mantenimiento()
        elif op2==4:
            p=crearPrestamo()
        elif op2==5:
            registroEntrega()
        elif op2 ==6:
            registroMantenimiento()
    # FIN MENU TECNICOS 
    elif op == 2: # INICIO MENU ESTUDIANTES
        menu2 = menuEstudiantes('Escuela de Ingeniería')
        op2 = menu2.ver()
        if op2 == 1:
            verPrestamos()
        elif op2==2:
            consultadisponibilidad()
        while 1 < op2 and op2 > 2:
            print('No es una opción válida'.center(25,'*'))
            op2 = menu2.ver()     
    # FIN MENU ESTUDIANTES

