# -*- coding: utf-8 -*-

class menu:
    def __init__(self, laboratorio):
        self.laboratorio = laboratorio
    def ver(self):
        print('BIENVENIDO AL SISTEMA'.center(25,'*'))
        print('Laboratorio: ' + self.laboratorio)
        print('1. Tecnicos')
        print('2. Estudiantes')
        print('3. Salir')
        op = int(input())
        return op
class menuTecnicos:
    def __init__(self, laboratorio):
        self.laboratorio = laboratorio
    def ver(self):
        print('Menu de tecnicos'.center(25,'*'))
        print('Laboratorio: ' + self.laboratorio)
        print('1. Registrar equipos')
        print('2. Ver datos')
        print('3. Consultar mantenimiento de equipos en un rango de fecha')
        print('4. Registrar prestamo')
        print('5. Registrar entrega')
        print('6. Registrar mantenimiento')
        op = int(input())
        return op
class menuEstudiantes:
    def __init__(self, laboratorio):
        self.laboratorio = laboratorio
    def ver(self):
        print('Menu de estudiantes'.center(25,'*'))
        print('Laboratorio: ' + self.laboratorio)
        print('1. Equipos en prestamo')
        print('2. Disponibilidad')
        op = int(input())
        while 1 < op and op > 2:
            op = int(input('No es una opción válida, pruebe de nuevo: '))
        return op