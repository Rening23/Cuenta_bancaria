'''Codigo básico para crear una cuenta bancaria, o como sería el funcionamiento de la misma
parte de formaciones realizadas en mi proceso de aprendizaje de programación usando el lenguaje Python'''


class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre,apellido,numero_Cuenta, Balance=0):
        super().__init__(nombre,apellido)
        self.numero_Cuenta=numero_Cuenta
        self.Balance=Balance

    def __str__(self):
        return f"El cliente cuyo nobre es {self.nombre} {self.apellido} \n numero de cuenta {self.numero_Cuenta} tiene un total de $ {self.Balance} en su cuenta"

    def __len__(self):
        return self.Balance

    def depositar(self,cantidad):
        self.Balance+=cantidad
        print("Deposito aceptado")

    def retirar(self, valor):
        if self.Balance >= valor:
            self.Balance -= valor
            print("Retira realizado")
        else:
            print("Fondos insuficientes")


def crear_cliente():
    nombre_cliente=input("Ingrese su nombre: ")
    apellido_cliente=input("Ingrese su apellido: ")
    numero_cuenta=input("Ingrese su numero de cuenta ")
    cliente=Cliente(nombre_cliente,apellido_cliente,numero_cuenta)
    return cliente


def inicio():
    mi_cliente=crear_cliente()
    print(mi_cliente)
    opcion=0

    while opcion != 5:
        print(""" ******Escoge una opción******
        Menu
        1) Datos de la cuenta
        2) Balance
        3) Depositar
        4) Retirar
        5) Salir""")
        opcion = int(input("Opcion: "))

        if opcion == 1:
            print(mi_cliente)
        elif opcion==2:
            print("Su saldo actual es: ")
            print(len(mi_cliente))
        elif opcion == 3:
            monto_dep = int(input("Ingrese monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 4:
            monto_ret = int(input("Ingrese monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print("Gracias por operar en el banco Python")
inicio()


