# 🐾 Sistema de Gestión de Hospital Veterinario

## Descripción

Este proyecto desarrolla un sistema básico para la gestión de un hospital veterinario usando **Python** y **Programación Orientada a Objetos (POO)**.

El sistema permite gestionar:

- Personas
- Clientes
- Mascotas
- Consultas
- Tratamientos
- Facturación
- Métodos de pago

El objetivo principal es aplicar correctamente los conceptos fundamentales de POO en un caso práctico sencillo y fácil de entender.

---

## Objetivo del ejercicio

Diseñar e implementar un sistema en Python que modele el funcionamiento básico de un hospital veterinario, aplicando relaciones entre clases y principios de POO.

---

## Conceptos de POO aplicados

### 1. Abstracción
Se usan dos clases abstractas:

- `Persona`
- `MetodoPago`

### 2. Herencia
De la clase `Persona` heredan:

- `Veterinario`
- `Recepcionista`
- `Cliente`

De la clase `MetodoPago` heredan:

- `PagoEfectivo`
- `PagoTarjeta`
- `PagoTransferencia`

### 3. Agregación
Existe una relación de agregación entre:

- `Cliente` y `Mascota`

Un cliente tiene una lista de mascotas, pero la mascota puede seguir existiendo aunque el cliente se elimine del sistema.

### 4. Asociación
Existe una relación de asociación entre:

- `Veterinario` y `Mascota`

Esta relación se refleja en la clase `Consulta`, donde se conecta el veterinario con la mascota atendida.

### 5. Composición
Existe una relación de composición entre:

- `Consulta` y `Tratamiento`

Los tratamientos nacen dentro de la consulta mediante el método `crear_tratamiento()`.

### 6. Polimorfismo
La clase `Factura` puede usar distintos métodos de pago mediante el método:

- `pagar(metodo_pago)`

Esto permite procesar pagos con diferentes clases hijas de `MetodoPago`.

---

## Clases implementadas

- `Persona` (abstracta)
- `Veterinario`
- `Recepcionista`
- `Cliente`
- `Mascota`
- `Consulta`
- `Tratamiento`
- `Factura`
- `MetodoPago` (abstracta)
- `PagoEfectivo`
- `PagoTarjeta`
- `PagoTransferencia`

---

## Funcionalidades del sistema

El código permite como mínimo:

- Crear un cliente
- Agregar una o más mascotas al cliente
- Crear un veterinario
- Registrar una consulta para una mascota
- Crear uno o más tratamientos dentro de la consulta
- Generar una factura
- Pagar la factura con distintos métodos de pago

---

## Prueba del sistema

La ejecución incluida en `main.py` muestra lo siguiente:

1. Se crea un cliente
2. Se registran dos mascotas
3. Un veterinario atiende una de las mascotas
4. Se crea una consulta
5. La consulta genera dos tratamientos
6. Se calcula el costo total
7. Se paga con un método de pago
8. Se cambia el método de pago y se prueba nuevamente

---

## Estructura del proyecto

```bash
hospital-veterinario/
│
├── main.py
├── README.md
└── diagrama_uml.png   # opcional