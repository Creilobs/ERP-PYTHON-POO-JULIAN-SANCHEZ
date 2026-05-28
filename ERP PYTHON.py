#PASO A PASO DE MI ERP
#El usuario inicia sesion
#El sistema valida credenciales.
#Dependiendo del rol muestra un menu
#El administrador puede agregar productos.
#El cajero puede vender.
#Las ventas actualizan el stock.
#Todo se guarda en JSON.
#El sistema genera reportes.
import json
from datetime import datetime
#Json se utiliza para guardar informacion permanente
#Datetime se utiliza pa guardar las fechas de las ventas

# CLASE PERSONA 
#HERENCIA: hereda atributos de persona 
#Clase padre del sistema
class Persona:

    def __init__(self, nombre, usuario, contraseña):
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contraseña = contraseña

    # Getters
    def get_nombre(self):
        return self.__nombre


    def get_usuario(self):
        return self.__usuario

    def get_contraseña(self):
        return self.__contraseña
#Use encapsulamiento para evitar que se modifiquen desde afuera

# CLASE USUARIO
#Hereda de la clase persona
class Usuario(Persona):

    def __init__(self, nombre, usuario, contraseña, rol):
        super().__init__(nombre, usuario, contraseña)
        self.__rol = rol

    def get_rol(self):
        return self.__rol

    # POLIMORFISMO
    #Cada usuario tiene un comportamiento diferente
    def mostrar_menu(self):
        print("Menú general")


# ADMINISTRADOR
#Tiene los permisos completos, agrega, vende y ve reportes.
class Administrador(Usuario):

    def __init__(self, nombre, usuario, contraseña):
        super().__init__(nombre, usuario, contraseña, "Administrador")

    def mostrar_menu(self):
        print("\n===== MENÚ ADMINISTRADOR =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Vender producto")
        print("5. Ver reportes")
        print("6. Salir")


# CAJERO
#Usuario limitado a ver, vender y buscar productos 
class Cajero(Usuario):

    def __init__(self, nombre, usuario, contraseña):
        super().__init__(nombre, usuario, contraseña, "Cajero")

    def mostrar_menu(self):
        print("\n===== MENÚ CAJERO =====")
        print("1. Mostrar productos")
        print("2. Buscar producto")
        print("3. Vender producto")
        print("4. Ver reportes")
        print("5. Salir")


# CLASE PRODUCTO
#Representa cada producto del inventario
class Producto:

    def __init__(self, codigo, nombre, precio, stock):

        # VALIDACIONES
        #Estas dos validaciones se colocan para evitar errores en el sistema 
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # Setter stock
    def set_stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    # Mostrar información
    def mostrar_info(self):

        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: $ {self.__precio}")
        print(f"Stock: {self.__stock}")

        if self.__stock <= 3:
            print("⚠ STOCK BAJO")

        print("-" * 40)


# SISTEMA ERP
#La clase principal controla productos, usuarios, ventas y reportes
class SistemaERP:

    def __init__(self):

        self.productos = []
        self.ventas = []

        self.usuarios = [
            Administrador("Julian", "admin", "123"),
            Cajero("Carlos", "cajero", "123")
        ]

    # LOGIN
    #implemente un login basico, se pide el usuario y contraseña, ahi se ve si esta registrado
    def login(self):

        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        for u in self.usuarios:

            if u.get_usuario() == usuario and u.get_contraseña() == contraseña:
                print(f"\n✅ Bienvenido {u.get_nombre()}")
                return u

        print("❌ Usuario incorrecto")
        return None

    # GUARDAR PRODUCTOS JSON
    def guardar_productos(self):

        datos = []

        for p in self.productos:

            datos.append({
                "codigo": p.get_codigo(),
                "nombre": p.get_nombre(),
                "precio": p.get_precio(),
                "stock": p.get_stock()
            })

        with open("productos.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

    # CARGAR PRODUCTOS JSON
    #permite que los productos y las ventas no se pierdan si cierro el programa
    def cargar_productos(self):

        try:

            with open("productos.json", "r") as archivo:

                datos = json.load(archivo)

                for d in datos:

                    producto = Producto(
                        d["codigo"],
                        d["nombre"],
                        d["precio"],
                        d["stock"]
                    )

                    self.productos.append(producto)

        except:
            pass

    # GUARDAR VENTAS JSON

    def guardar_ventas(self):

        with open("ventas.json", "w") as archivo:
            json.dump(self.ventas, archivo, indent=4)

    # CARGAR VENTAS JSON
    
    def cargar_ventas(self):

        try:

            with open("ventas.json", "r") as archivo:
                self.ventas = json.load(archivo)

        except:
            pass

    # AGREGAR PRODUCTO
    def agregar_producto(self):

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        producto = Producto(codigo, nombre, precio, stock)

        self.productos.append(producto)

        self.guardar_productos()

        print("✅ Producto agregado")

    # MOSTRAR PRODUCTOS
    
    def mostrar_productos(self):

        print("\n===== PRODUCTOS =====")

        for p in self.productos:
            p.mostrar_info()

    # BUSCAR PRODUCTO
    def buscar_producto(self):

        codigo = input("Ingrese código: ")

        encontrado = False

        for p in self.productos:

            if p.get_codigo() == codigo:

                print("\n✅ PRODUCTO ENCONTRADO")
                p.mostrar_info()
                encontrado = True

        if not encontrado:
            print("❌ Producto no encontrado")

    # VENDER PRODUCTO
    #Aqui el sistema busca, valida, descuenta las unidades, guarda la venta y genera una factura
    def vender_producto(self):

        codigo = input("Código producto: ")
        cantidad = int(input("Cantidad: "))

        for p in self.productos:

            if p.get_codigo() == codigo:

                if p.get_stock() >= cantidad:

                    nuevo_stock = p.get_stock() - cantidad
                    p.set_stock(nuevo_stock)

                    total = p.get_precio() * cantidad

                    venta = {
                        "producto": p.get_nombre(),
                        "cantidad": cantidad,
                        "total": total,
                        "fecha": str(datetime.now())
                    }

                    self.ventas.append(venta)

                    self.guardar_productos()
                    self.guardar_ventas()

                    # FACTURA
                    #Fac muestra producto, cantidad, precio, total y fecha
                    print("\n" + "="*40)
                    print("           FACTURA")
                    print("="*40)
                    print("Producto:", p.get_nombre())
                    print("Cantidad:", cantidad)
                    print("Precio:", p.get_precio())
                    print("TOTAL: $", total)
                    print("Fecha:", venta["fecha"])
                    print("="*40)

                    return

                else:
                    print("❌ Stock insuficiente")
                    return

        print("❌ Producto no encontrado")

    
    # REPORTES
    # este permite visualizar ventas realizadas y total vendido 
    def reportes(self):

        print("\n===== REPORTES =====")

        total_general = 0

        for v in self.ventas:

            print(
                f"{v['producto']} | "
                f"Cantidad: {v['cantidad']} | "
                f"Total: $ {v['total']}"
            )

            total_general += v["total"]

        print("-" * 40)
        print(f"TOTAL VENDIDO: $ {total_general}")
        print("-" * 40)



# MENÚ PRINCIPAL-Funcion principal
#Aqui inicia el sistema, carga Json, ejecuta el login y muestra el menu
def main():

    sistema = SistemaERP()

    sistema.cargar_productos()
    sistema.cargar_ventas()

    usuario = None

    while usuario is None:
        usuario = sistema.login()

    while True:

        # POLIMORFISMO
        usuario.mostrar_menu()

        opcion = input("Seleccione una opción: ")

        # ADMIN
        if usuario.get_rol() == "Administrador":

            if opcion == "1":
                sistema.agregar_producto()

            elif opcion == "2":
                sistema.mostrar_productos()

            elif opcion == "3":
                sistema.buscar_producto()

            elif opcion == "4":
                sistema.vender_producto()

            elif opcion == "5":
                sistema.reportes()

            elif opcion == "6":
                print("👋 Saliendo...")
                break

            else:
                print("❌ Opción inválida")

        # CAJERO
        elif usuario.get_rol() == "Cajero":

            if opcion == "1":
                sistema.mostrar_productos()

            elif opcion == "2":
                sistema.buscar_producto()

            elif opcion == "3":
                sistema.vender_producto()

            elif opcion == "4":
                sistema.reportes()

            elif opcion == "5":
                print("👋 Saliendo...")
                break

            else:
                print("❌ Opción inválida")



# EJECUTAR

main()