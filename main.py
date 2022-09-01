# -*- coding: utf-8 -*-
from classes.menu import *
from classes.equipo import *
from classes.prestamo import *

if __name__=='__main__':
    menu = menu('Escuela de Ingeniería')
    op = menu.ver()
    while 1 < op and op > 3:
        print('No es una opción válida.')
        op = menu.ver() 
    if op == 1:
        menu2 = menuTecnicos('Escuela de Ingeniería')
        op2 = menu2.ver()
        while 1 < op2 and op2 > 4:
            print('No es una opción válida.')
            op2 = menu2.ver()   
        if op2 ==1:
            e = crearEquipo()
            e.save()
        elif op2==2:
            p=crearPrestamo()
            p.save()
        elif op2==3:
            registroEntrega()
        elif op2 ==4:
            registroMantenimiento()
            
    elif op == 2:
        menu2 = menuEstudiantes('Escuela de Ingeniería')
        op2 = menu2.ver()
        if op2 == 1:
            verPrestamos()
        elif op2==2:
            consularEquipo()
        
    

