# Resolvemos los ejercicios 1 al 16 en un solo script de Python

# Ejercicio 1
def contar_caracteres(texto):
    return len(texto)

# Ejercicio 2
def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0

# Ejercicio 3
def encontrar_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# Ejercicio 4
def enmascarado_datos(dato):
    dato_str = str(dato)
    return '#' * (len(dato_str) - 4) + dato_str[-4:]

# Ejercicio 5
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

# Ejercicio 6
def buscar_nombre():
    nombres = ["Jaime", "Silvia", "Ana"]
    nombre = input("Introduce un nombre para buscar: ")
    if nombre in nombres:
        print(f"{nombre} fue encontrado en la lista.")
    else:
        raise ValueError(f"{nombre} no se encuentra en la lista.")

# Ejercicio 7
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ejercicio 8
def encontrar_puesto_empleado(nombre_completo, empleados):
    for emp in empleados:
        if f"{emp['nombre']} {emp['apellido']}" == nombre_completo:
            return emp['puesto']
    return "La persona no trabaja aquí."

# Ejercicio 9
cubo_numero = lambda x: x**3

# Ejercicio 10
resto_division = lambda x, y: x % y

# Ejercicio 11
numeros_pares = lambda lista: list(filter(lambda x: isinstance(x, int) and x % 2 == 0, lista))

# Ejercicio 12
numeros_suma = lambda lista: list(map(lambda x: x + 3, lista))

# Ejercicio 13
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

# Ejercicio 14
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, pos):
        if 0 <= pos < len(self.ramas):
            self.ramas.pop(pos)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Ejercicio 15
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError("El otro usuario no tiene suficiente saldo.")
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# Ejercicio 16
def contar_palabras(texto):
    palabras = texto.lower().replace('.', '').split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    return ' '.join([p for p in texto.split() if p != palabra])

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida")
