from abc import ABC, abstractmethod

# CLASE ABSTRACTA: PERSONA

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

# CLASES HIJAS DE PERSONA

class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Veterinario - Especialidad: {self.especialidad}"

    def atender_mascota(self, mascota):
        print(f"El veterinario {self.nombre} está atendiendo a {mascota.nombre}.")


class Recepcionista(Persona):
    def mostrar_rol(self):
        return "Recepcionista"

    def registrar_cliente(self, cliente):
        print(f"Cliente {cliente.nombre} registrado correctamente.")


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []  # Agregación

    def mostrar_rol(self):
        return "Cliente"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        if not self.mascotas:
            print(f"{self.nombre} no tiene mascotas registradas.")
            return

        print(f"Mascotas de {self.nombre}:")
        for mascota in self.mascotas:
            print(f"- {mascota.mostrar_info()}")

# CLASE MASCOTA

class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return (
            f"Nombre: {self.nombre}, Especie: {self.especie}, "
            f"Edad: {self.edad} años, Peso: {self.peso} kg"
        )

# CLASE TRATAMIENTO

class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        return (
            f"Tratamiento: {self.nombre} | "
            f"Costo: ${self.costo:.2f} | "
            f"Duración: {self.duracion_dias} días"
        )

# CLASE CONSULTA
# Asociación: Mascota + Veterinario
# Composición: Tratamiento nace dentro de la consulta
class Consulta:
    COSTO_BASE_CONSULTA = 50000

    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []

    def crear_tratamiento(self, nombre, costo, duracion_dias):
        tratamiento = Tratamiento(nombre, costo, duracion_dias)
        self.tratamientos.append(tratamiento)

    def calcular_costo_consulta(self):
        total_tratamientos = sum(tratamiento.costo for tratamiento in self.tratamientos)
        return self.COSTO_BASE_CONSULTA + total_tratamientos

    def mostrar_resumen(self):
        print("\n========== RESUMEN DE LA CONSULTA ==========")
        print(f"Mascota: {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Motivo: {self.motivo}")
        print(f"Diagnóstico: {self.diagnostico}")
        print("Tratamientos:")

        if not self.tratamientos:
            print("- No hay tratamientos registrados.")
        else:
            for tratamiento in self.tratamientos:
                print(f"- {tratamiento.mostrar_tratamiento()}")

        print(f"Costo total de la consulta: ${self.calcular_costo_consulta():.2f}")
        print("============================================\n")

# CLASE ABSTRACTA: METODO DE PAGO

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago en efectivo realizado por ${monto:.2f}")


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago con tarjeta aprobado por ${monto:.2f}")


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago por transferencia realizado por ${monto:.2f}")

# CLASE FACTURA
# Polimorfismo: recibe cualquier objeto de tipo MetodoPago
class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = self.subtotal * 0.19
        self.total = self.subtotal + self.impuesto

    def calcular_total(self):
        return self.total

    def mostrar_factura(self):
        print("=============== FACTURA ===============")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Impuesto (19%): ${self.impuesto:.2f}")
        print(f"Total a pagar: ${self.total:.2f}")
        print("=======================================\n")

    def pagar(self, metodo_pago):
        metodo_pago.procesar_pago(self.total)

# PRUEBA DEL SISTEMA
def main():
    print("========== SISTEMA HOSPITAL VETERINARIO ==========\n")

    # 1. Crear un cliente
    cliente = Cliente("Carlos Pérez", "123456789", "3001234567")
    print(f"Cliente creado: {cliente.nombre} - {cliente.mostrar_rol()}")

    # 2. Registrar dos mascotas
    mascota1 = Mascota("Firulais", "Perro", 3, 10.5)
    mascota2 = Mascota("Misu", "Gato", 2, 4.2)

    cliente.agregar_mascota(mascota1)
    cliente.agregar_mascota(mascota2)

    print("\nSe registraron dos mascotas al cliente.")
    cliente.mostrar_mascotas()

    # 3. Crear un veterinario
    veterinario = Veterinario("Dr. Juan López", "987654321", "Medicina General")
    print(f"\nVeterinario creado: {veterinario.nombre} - {veterinario.mostrar_rol()}")

    # 4. El veterinario atiende una mascota
    print()
    veterinario.atender_mascota(mascota1)

    # 5. Crear una consulta
    consulta = Consulta(
        mascota=mascota1,
        veterinario=veterinario,
        motivo="Fiebre y decaimiento",
        diagnostico="Infección leve"
    )

    # 6. La consulta genera dos tratamientos
    consulta.crear_tratamiento("Antibiótico", 30000, 5)
    consulta.crear_tratamiento("Vitaminas", 20000, 7)

    # 7. Mostrar resumen y calcular costo
    consulta.mostrar_resumen()

    # 8. Generar factura
    factura = Factura(consulta)
    factura.mostrar_factura()

    # 9. Pagar con un método de pago
    print("Primer pago:")
    pago_efectivo = PagoEfectivo()
    factura.pagar(pago_efectivo)

    # 10. Cambiar método de pago y probar nuevamente
    print("\nSegundo pago:")
    pago_tarjeta = PagoTarjeta()
    factura.pagar(pago_tarjeta)

    print("\n========== PROCESO FINALIZADO ==========")


if __name__ == "__main__":
    main()