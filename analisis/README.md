# Análisis del Proyecto ERP

#ntroducción

Este proyecto consiste en un sistema ERP básico desarrollado en Python utilizando Programación Orientada a Objetos (POO).

El sistema fue creado con el objetivo de administrar productos, ventas y reportes dentro de un negocio de manera sencilla.

Además, permite guardar la información en archivos JSON para que los datos no se pierdan al cerrar el programa.

# Objetivos

#Objetivo general

Desarrollar un sistema ERP en Python aplicando conceptos de Programación Orientada a Objetos.

#Objetivos específicos

* Implementar herencia, encapsulamiento y polimorfismo.
* Gestionar productos y ventas.
* Controlar el stock del inventario.
* Guardar información en archivos JSON.
* Generar reportes de ventas.

#Descripción del sistema

El sistema funciona mediante un login de usuarios.

Dependiendo del rol:

* Administrador
* Cajero

el sistema muestra diferentes opciones del menú.

El administrador puede:

* Agregar productos
* Vender
* Ver reportes

El cajero puede:

* Buscar productos
* Vender
* Ver reportes

Cuando se realiza una venta:

* Se descuenta el stock.
* Se guarda la venta.
* Se genera una factura.

#Conceptos POO utilizados

#Herencia

Las clases Administrador y Cajero heredan de Usuario.
Usuario hereda de Persona.

#Encapsulamiento

Se utilizaron atributos privados con doble guion bajo (__).

#Polimorfismo

Cada usuario implementa su propio método mostrar_menu().

#Validaciones

Se validó:
* Precio mayor a 0.
* Stock no negativo.
  
#Tecnologías utilizadas

* Python
* JSON
* Programación Orientada a Objetos

#Conclusión

El proyecto permitió aplicar los conceptos fundamentales de Programación Orientada a Objetos mediante el desarrollo de un sistema ERP funcional capaz de gestionar productos, ventas y reportes.
