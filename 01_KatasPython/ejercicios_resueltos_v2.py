"""
Proyecto Lógica: Katas de Python
Cada ejercicio se encuentra precedido de su enunciado (como comentario) y cuenta con explicaciones
para reforzar los conocimientos básicos en Python.
"""

import math
from functools import reduce

#===============================================================
# PROYECTO LÓGICA: Katas de Python 1
#===============================================================

# Ejercicio 1.1
# ===================== 
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_letras(texto):
    """
    Recibe una cadena de texto y devuelve un diccionario con la frecuencia de cada letra, ignorando los espacios.
    """
    # Eliminar espacios del texto
    texto = texto.replace(" ", "")
    frecuencias = {}
    for letra in texto:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias
# Llamada a la función para prueba
print("Ejercicio 1.1 - Frecuencia de letras:")
print(frecuencia_letras("hola mundo"))

# Ejercicio 1.2
# ===================== 
# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def duplicar_valores(lista_numeros):
    """
    Recibe una lista de números y devuelve una nueva lista con el doble de cada valor utilizando map().
    """
    return list(map(lambda x: x * 2, lista_numeros))
# Llamada a la función para prueba
print("\nEjercicio 1.2 - Duplicar valores:")
print(duplicar_valores([1, 2, 3, 4]))

# Ejercicio 1.3
# ===================== 
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def filtrar_palabras(lista_palabras, objetivo):
    """
    Recibe una lista de palabras y una palabra objetivo.
    Retorna una lista con las palabras que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista_palabras if objetivo in palabra]
# Llamada a la función para prueba
print("\nEjercicio 1.3 - Filtrar palabras que contengan 'an':")
print(filtrar_palabras(["manzana", "banana", "pera", "análisis"], "an"))

# Ejercicio 1.4
# ===================== 
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas(lista1, lista2):
    """
    Recibe dos listas de números de igual longitud y devuelve una lista con la diferencia
    elemento a elemento (lista1 - lista2) usando map().
    """
    return list(map(lambda a, b: a - b, lista1, lista2))
# Llamada a la función para prueba
print("\nEjercicio 1.4 - Diferencia entre listas:")
print(diferencia_listas([10, 20, 30], [1, 2, 3]))

# Ejercicio 1.5
# ===================== 
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5.
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado.
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga
# la media y el estado.
def evaluar_nota(numeros, nota_aprobado=5):
    """
    Calcula la media de la lista de números y devuelve una tupla (media, estado),
    donde estado es "aprobado" si la media >= nota_aprobado, de lo contrario "suspenso".
    """
    if not numeros:
        return (0, "suspenso")
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)
# Llamada a la función para prueba
print("\nEjercicio 1.5 - Evaluar nota:")
print(evaluar_nota([4, 6, 8]))

# Ejercicio 1.6
# ===================== 
# Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    """
    Calcula el factorial de un número n de forma recursiva.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# Llamada a la función para prueba
print("\nEjercicio 1.6 - Factorial de 5:")
print(factorial(5))

# Ejercicio 1.7
# ===================== 
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_strings(lista_tuplas):
    """
    Convierte cada tupla de la lista en un string concatenando sus elementos.
    """
    return list(map(lambda t: ''.join(map(str, t)), lista_tuplas))
# Llamada a la función para prueba
print("\nEjercicio 1.7 - Convertir tuplas a strings:")
print(tuplas_a_strings([('h', 'o', 'l', 'a'), ('m', 'u', 'n', 'd', 'o')]))

# Ejercicio 1.8
# ===================== 
# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o
# intenta dividir por cero, maneja esas excepciones de manera adecuada.
def dividir_numeros():
    """
    Solicita dos números al usuario e intenta dividirlos, manejando errores de entrada y división por cero.
    """
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print("La división fue exitosa. Resultado:", resultado)
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
# Llamada a la función para prueba
print("\nEjercicio 1.8 - División de números:")
dividir_numeros()

# Ejercicio 1.9
# ===================== 
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo
# ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter()
def filtrar_mascotas(lista_mascotas):
    """
    Filtra de la lista las mascotas prohibidas en España usando filter().
    """
    mascotas_prohibidas = {"Mapache", "Tigre", "Serpiente", "Cocodrilo", "Oso"}
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))
# Llamada a la función para prueba
print("\nEjercicio 1.9 - Filtrar mascotas:")
print(filtrar_mascotas(["Perro", "Gato", "Mapache", "Loro", "Oso"]))

# Ejercicio 1.10
# ===================== 
# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción
# personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    """Excepción personalizada para lista vacía."""
    pass

def promedio(lista):
    """
    Calcula el promedio de una lista de números.
    Lanza ListaVaciaError si la lista está vacía.
    """
    if not lista:
        raise ListaVaciaError("La lista está vacía.")
    return sum(lista) / len(lista)
# Llamada a la función para prueba
print("\nEjercicio 1.10 - Promedio de lista:")
try:
    print(promedio([10, 20, 30]))
except ListaVaciaError as e:
    print("Error:", e)

# Ejercicio 1.11
# ===================== 
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera
# del rango esperado (menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def solicitar_edad():
    """
    Solicita al usuario su edad y verifica que sea un número entre 0 y 120.
    """
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango esperado.")
        print("Edad válida:", edad)
    except ValueError as e:
        print("Error:", e)
# Llamada a la función para prueba
print("\nEjercicio 1.11 - Solicitar edad")
solicitar_edad()

# Ejercicio 1.12
# ===================== 
# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitudes_palabras(frase):
    """
    Devuelve una lista con la longitud de cada palabra en la frase usando map().
    """
    palabras = frase.split()
    return list(map(lambda palabra: len(palabra), palabras))
# Llamada a la función para prueba
print("\nEjercicio 1.12 - Longitudes de palabras:")
print(longitudes_palabras("El perro de san roque no tiene rabo"))

# Ejercicio 1.13
# ===================== 
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
# Las letras no pueden estar repetidas. Usa la función map()
def letras_mayus_minus(caracteres):
    """
    Recibe una cadena de caracteres y devuelve una lista de tuplas (letra en mayúscula, letra en minúscula)
    para cada letra única usando map().
    """
    unicas = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), unicas))
# Llamada a la función para prueba
print("\nEjercicio 1.13 - Letras mayúsculas y minúsculas:")
print(letras_mayus_minus("Python"))

# Ejercicio 1.14
# ===================== 
# Crea una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Usa la función filter()
def filtrar_por_letra(lista_palabras, letra):
    """
    Filtra y retorna las palabras que comienzan con la letra especificada.
    """
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))
# Llamada a la función para prueba
print("\nEjercicio 1.14 - Filtrar palabras que empiezan con 'p':")
print(filtrar_por_letra(["python", "java", "perl", "ruby"], "p"))

# Ejercicio 1.15
# ===================== 
# Crea una función lambda que sume 3 a cada número de una lista dada.
suma_tres = lambda lista: list(map(lambda x: x + 3, lista))
# Llamada a la función para prueba
print("\nEjercicio 1.15 - Sumar 3 a cada número:")
print(suma_tres([1, 2, 3]))

# Ejercicio 1.16
# ===================== 
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras
# que sean más largas que n. Usa la función filter()
def palabras_mas_largas(texto, n):
    """
    Devuelve una lista de palabras del texto que tengan más de n caracteres utilizando filter().
    """
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))
# Llamada a la función para prueba
print("\nEjercicio 1.16 - Palabras más largas que 3 caracteres:")
print(palabras_mas_largas("este es un ejemplo de filtrado", 3))

# Ejercicio 1.17
# ===================== 
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce()
def lista_a_numero(digitos):
    """
    Convierte una lista de dígitos en el número que representan, usando reduce().
    """
    return reduce(lambda acc, d: acc * 10 + d, digitos, 0)
# Llamada a la función para prueba
print("\nEjercicio 1.17 - Convertir lista de dígitos a número:")
print(lista_a_numero([5, 7, 2]))

# Ejercicio 1.18
# ===================== 
# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.
def filtrar_estudiantes(estudiantes):
    """
    Filtra y retorna los estudiantes (diccionarios) que tengan una calificación mayor o igual a 90.
    """
    return list(filter(lambda estudiante: estudiante.get('calificacion', 0) >= 90, estudiantes))

# Llamada a la función para prueba
print("\nEjercicio 1.18 - Filtrar estudiantes con calificación >= 90:")
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 92},
    {"nombre": "Marta", "edad": 19, "calificacion": 88}
]
print(filtrar_estudiantes(estudiantes))

# Ejercicio 1.19
# ===================== 
# Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
# Llamada a la función para prueba
print("\nEjercicio 1.19 - Filtrar números impares:")
print(filtrar_impares([1, 2, 3, 4, 5]))

# Ejercicio 1.20
# ===================== 
# Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def filtrar_integers(lista):
    """
    Devuelve una nueva lista que contiene solo los elementos de tipo int de la lista original.
    """
    return list(filter(lambda x: isinstance(x, int), lista))
# Llamada a la función para prueba
print("\nEjercicio 1.20 - Filtrar sólo valores enteros:")
print(filtrar_integers([1, "dos", 3, "cuatro"]))

# Ejercicio 1.21
# ===================== 
# Crea una función que calcule el cubo de un número dado mediante una función lambda.
cubo = lambda x: x ** 3
# Llamada a la función para prueba
print("\nEjercicio 1.21 - Cubo de 3:")
print(cubo(3))

# Ejercicio 1.22
# ===================== 
# Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().
def producto_total(lista):
    """
    Calcula el producto total de los números de la lista usando reduce().
    """
    return reduce(lambda acc, x: acc * x, lista, 1)
# Llamada a la función para prueba
print("\nEjercicio 1.22 - Producto total de una lista:")
print(producto_total([1, 2, 3, 4]))

# Ejercicio 1.23
# ===================== 
# Concatena una lista de palabras. Usa la función reduce().
def concatenar_palabras(lista):
    """
    Concatena todos los elementos de la lista (palabras) en una sola cadena usando reduce().
    """
    return reduce(lambda acc, palabra: acc + palabra, lista, "")
# Llamada a la función para prueba
print("\nEjercicio 1.23 - Concatenar palabras:")
print(concatenar_palabras(["Hola", " ", "mundo"]))

# Ejercicio 1.24
# ===================== 
# Calcula la diferencia total en los valores de una lista. Usa la función reduce().
def diferencia_total(lista):
    """
    Calcula la diferencia total de los elementos de la lista, restándolos secuencialmente, usando reduce().
    """
    if not lista:
        return 0
    elif len(lista) == 1:
        return lista[0]
    return reduce(lambda acc, x: acc - x, lista[1:], lista[0])
# Llamada a la función para prueba
print("\nEjercicio 1.24 - Diferencia total de una lista:")
print(diferencia_total([100, 20, 30]))

# Ejercicio 1.25
# ===================== 
# Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(texto):
    """
    Devuelve el número total de caracteres en la cadena de texto.
    """
    return len(texto)
# Llamada a la función para prueba
print("\nEjercicio 1.25 - Contar caracteres:")
print(contar_caracteres("hola mundo"))

# Ejercicio 1.26
# ===================== 
# Crea una función lambda que calcule el resto de la división entre dos números dados.
resto_division = lambda a, b: a % b
# Llamada a la función para prueba
print("\nEjercicio 1.26 - Resto de la división (7 % 3):")
print(resto_division(7, 3))

# Ejercicio 1.27
# ===================== 
# Crea una función que calcule el promedio de una lista de números.
def promedio_numeros(lista):
    """
    Calcula y devuelve el promedio de una lista de números.
    """
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)
# Llamada a la función para prueba
print("\nEjercicio 1.27 - Promedio de números:")
print(promedio_numeros([10, 20, 30, 40]))

# Ejercicio 1.28
# ===================== 
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    """
    Retorna el primer elemento duplicado en la lista. Si no hay duplicados, retorna None.
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None
# Llamada a la función para prueba
print("\nEjercicio 1.28 - Primer duplicado:")
print(primer_duplicado([1, 2, 3, 2, 4]))

# Ejercicio 1.29
# ===================== 
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#',
# excepto los últimos cuatro.
def enmascarar_variable(variable):
    """
    Convierte la variable a cadena y reemplaza todos sus caracteres por '#' excepto los últimos cuatro.
    """
    s = str(variable)
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]
# Llamada a la función para prueba
print("\nEjercicio 1.29 - Enmascarar variable:")
print(enmascarar_variable("123456789"))

# Ejercicio 1.30
# ===================== 
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en
# diferente orden.
def son_anagramas(palabra1, palabra2):
    """
    Retorna True si palabra1 y palabra2 son anagramas (ignorando mayúsculas y minúsculas), de lo contrario False.
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
# Llamada a la función para prueba
print("\nEjercicio 1.30 - Verificar anagramas ('roma' y 'amor'):")
print(son_anagramas("roma", "amor"))

# Ejercicio 1.31
# ===================== 
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    """
    Solicita al usuario una lista de nombres y luego un nombre para buscar.
    Imprime si el nombre fue encontrado; si no, lanza una excepción.
    """
    nombres = input("Ingresa una lista de nombres separados por comas: ").strip()
    if not nombres:
        raise Exception("La lista de nombres está vacía.")

    lista_nombres = [nombre.strip() for nombre in nombres.split(',') if nombre.strip()]
    if not lista_nombres:
        raise Exception("No se ingresaron nombres válidos.")

    nombre_buscar = input("Ingresa el nombre a buscar: ").strip()
    if nombre_buscar in lista_nombres:
        print(f"{nombre_buscar} fue encontrado en la lista.")
    else:
        raise Exception(f"{nombre_buscar} no se encuentra en la lista.")
# Llamada a la función para prueba
print("\nEjercicio 1.31 - Buscar nombre:")
buscar_nombre()

# Ejercicio 1.32
# ===================== 
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.
def buscar_empleado(nombre_completo, lista_empleados):
    """
    Busca en la lista de empleados (cada uno representado por un diccionario) el empleado cuyo 'nombre' coincide
    con nombre_completo y retorna su 'puesto'. Si no se encuentra, retorna un mensaje.
    """
    for empleado in lista_empleados:
        if empleado.get('nombre') == nombre_completo:
            return empleado.get('puesto')
    return f"{nombre_completo} no trabaja aquí."
# Llamada a la función para prueba
print("\nEjercicio 1.32 - Buscar empleado:")
empleados = [
    {"nombre": "Carlos", "puesto": "Gerente"},
    {"nombre": "Lucía", "puesto": "Analista"}
]
print(buscar_empleado("Lucía", empleados))
print(buscar_empleado("Pedro", empleados))

# Ejercicio 1.33
# ===================== 
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_listas = lambda lista1, lista2: list(map(lambda pair: pair[0] + pair[1], zip(lista1, lista2)))
# Llamada a la función para prueba
print("\nEjercicio 1.33 - Sumar listas:")
print(sumar_listas([1, 2, 3], [4, 5, 6]))

# Ejercicio 1.34
# ===================== 
# Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. 
class Arbol:
    """
    Clase que representa un árbol con un tronco y una lista de ramas.
    """
    def __init__(self):
        self.tronco = 1
        self.ramas = []  # Lista que guarda las longitudes de las ramas
    
    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en una unidad.
        """
        self.tronco += 1
    
    def nueva_rama(self):
        """
        Agrega una nueva rama de longitud 1.
        """
        self.ramas.append(1)
    
    def crecer_ramas(self):
        """
        Incrementa en una unidad la longitud de cada rama existente.
        """
        self.ramas = [rama + 1 for rama in self.ramas]
    
    def quitar_rama(self, posicion):
        """
        Elimina la rama en la posición dada si existe.
        """
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida para quitar una rama.")
    
    def info_arbol(self):
        """
        Devuelve un diccionario con la información del árbol: longitud del tronco, número de ramas y sus longitudes.
        """
        return {
            "tronco": self.tronco,
            "numero_de_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Caso de uso de la clase Arbol:
def caso_uso_arbol():
    """
    Caso de uso:
      1. Crear un árbol.
      2. Hacer crecer el tronco una unidad.
      3. Añadir una nueva rama.
      4. Hacer crecer todas las ramas una unidad.
      5. Añadir dos nuevas ramas.
      6. Retirar la rama situada en la posición 2.
      7. Mostrar la información del árbol.
    """
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    info = arbol.info_arbol()
    print("Información del árbol:", info)
# Llamada a la función para prueba
print("\nEjercicio 1.34 - Caso de uso de la clase Arbol:")
caso_uso_arbol()

# Ejercicio 1.36
# ===================== 
# Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Proporciona métodos para retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
class UsuarioBanco:
    """
    Representa a un usuario de un banco.
    """
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    def retirar_dinero(self, cantidad):
        """
        Retira una cantidad del saldo. Lanza un error si la cantidad es mayor al saldo disponible.
        """
        if cantidad > self.saldo:
            raise Exception("Fondos insuficientes para retirar.")
        self.saldo -= cantidad
    
    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transfiere dinero desde otro usuario al usuario actual. Lanza un error si el otro usuario no tiene fondos suficientes.
        """
        if cantidad > otro_usuario.saldo:
            raise Exception(f"{otro_usuario.nombre} no tiene fondos suficientes para transferir.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
    
    def agregar_dinero(self, cantidad):
        """
        Agrega una cantidad al saldo.
        """
        self.saldo += cantidad

# Caso de uso de la clase UsuarioBanco:
def caso_uso_usuario_banco():
    """
    Caso de uso:
      1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    """
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    print(f"Saldo inicial - Alicia: {alicia.saldo}, Bob: {bob.saldo}")
    return alicia, bob
# Llamada a la función para prueba
print("\nEjercicio 1.35 - Caso de uso de la clase UsuarioBanco:")
alicia, bob = caso_uso_usuario_banco()

# Agregar 20 unidades de saldo de "Bob".
def agregar_saldo_bob(bob):
    """
    Agrega 20 unidades al saldo de Bob.
    """
    bob.agregar_dinero(20)
    print(f"Nuevo saldo de Bob: {bob.saldo}")
# Llamada a la función para prueba
print("\nEjercicio 1.36 - Agregar saldo a Bob:")
agregar_saldo_bob(bob)

# Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
def transferencia_bob_a_alicia(bob, alicia):
    """
    Intenta transferir 80 unidades desde Bob a Alicia. Se maneja la excepción si Bob no tiene fondos suficientes.
    """
    try:
        alicia.transferir_dinero(bob, 80)
        print("Transferencia exitosa.")
    except Exception as e:
        print("Error en la transferencia:", e)
# Llamada a la función para prueba
print("\nEjercicio 1.37 - Transferencia de Bob a Alicia (80 unidades):")
transferencia_bob_a_alicia(bob, alicia)

# Retirar 50 unidades de saldo a "Alicia".
def retirar_saldo_alicia(alicia):
    """
    Retira 50 unidades del saldo de Alicia, manejando posibles errores.
    """
    try:
        alicia.retirar_dinero(50)
        print(f"Nuevo saldo de Alicia: {alicia.saldo}")
    except Exception as e:
        print("Error al retirar saldo de Alicia:", e)
# Llamada a la función para prueba
print("\nEjercicio 1.38 - Retirar 50 unidades de Alicia:")
retirar_saldo_alicia(alicia)

# Ejercicio 1.37
# ===================== 
# Crea una función llamada procesar_texto que procese un texto según la opción especificada:
# contar_palabras, reemplazar_palabras, eliminar_palabra. Primero define las funciones auxiliares.
def contar_palabras(texto):
    """
    Cuenta la cantidad de veces que aparece cada palabra en el texto y devuelve un diccionario.
    """
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza todas las ocurrencias de palabra_original por palabra_nueva en el texto.
    """
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    """
    Elimina la palabra especificada del texto.
    """
    palabras = texto.split()
    palabras_filtradas = list(filter(lambda p: p != palabra, palabras))
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    """
    Procesa el texto según la opción:
      - "contar": cuenta las palabras.
      - "reemplazar": reemplaza una palabra (requiere palabra_original y palabra_nueva).
      - "eliminar": elimina una palabra (requiere la palabra a eliminar).
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise Exception("Se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise Exception("Se requiere un argumento: la palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise Exception("Opción no válida.")

# Caso de uso de procesar_texto:
def caso_uso_procesar_texto():
    """
    Prueba la función procesar_texto con las tres opciones.
    """
    texto = "hola mundo hola a todos"
    print("Contar palabras:", procesar_texto(texto, "contar"))
    print("Reemplazar 'hola' por 'adiós':", procesar_texto(texto, "reemplazar", "hola", "adiós"))
    print("Eliminar 'a':", procesar_texto(texto, "eliminar", "a"))

# Llamada a la función para prueba
print("\nEjercicio 1.39 - Caso de uso de procesar_texto:")
caso_uso_procesar_texto()

# Ejercicio 1.38
# ===================== 
# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def determinar_periodo():
    """
    Solicita la hora (0-23) al usuario y determina si es de día, tarde o noche.
    """
    try:
        hora = int(input("Ingresa la hora (0-23): "))
        if hora < 0 or hora > 23:
            raise ValueError("Hora fuera de rango.")
        if 6 <= hora < 12:
            print("Es de día.")
        elif 12 <= hora < 20:
            print("Es de tarde.")
        else:
            print("Es de noche.")
    except ValueError as e:
        print("Error:", e)

# Llamada a la función para prueba
print("\nEjercicio 1.40 - Determinar periodo del día:")
determinar_periodo()

# Ejercicio 1.39
# ===================== 
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Reglas:
#   0-69: insuficiente
#   70-79: bien
#   80-89: muy bien
#   90-100: excelente
def calificacion_alumno():
    """
    Solicita la calificación numérica al usuario y muestra la calificación en texto correspondiente.
    """
    try:
        nota = float(input("Ingresa la calificación numérica (0-100): "))
        if nota < 0 or nota > 100:
            raise ValueError("Calificación fuera de rango.")
        if nota < 70:
            print("Insuficiente")
        elif nota < 80:
            print("Bien")
        elif nota < 90:
            print("Muy bien")
        else:
            print("Excelente")
    except ValueError as e:
        print("Error:", e)

# Llamada a la función para prueba
print("\nEjercicio 1.41 - Calificación del alumno:")
calificacion_alumno()

# Ejercicio 1.40
# ===================== 
# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo")
# y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area(figura, datos):
    """
    Calcula y retorna el área de la figura indicada:
      - 'rectangulo': datos = (base, altura) -> área = base * altura.
      - 'circulo': datos = (radio,) -> área = pi * radio^2.
      - 'triangulo': datos = (base, altura) -> área = (base * altura) / 2.
    """
    if figura.lower() == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura.lower() == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura.lower() == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise Exception("Figura no reconocida.")

# Llamada a la función para prueba
print("\nEjercicio 1.42 - Calcular área de figuras:")
print("Área del rectángulo (base=5, altura=3):", calcular_area("rectangulo", (5, 3)))
print("Área del círculo (radio=4):", calcular_area("circulo", (4,)))
print("Área del triángulo (base=6, altura=4):", calcular_area("triangulo", (6, 4)))

# Ejercicio 1.41
# ===================== 
# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea,
# después de aplicar un descuento.
# Pasos:
#   1. Solicita el precio original.
#   2. Pregunta si tiene cupón (sí/no).
#   3. Si tiene cupón, solicita el valor del cupón.
#   4. Aplica el descuento si es válido (valor > 0).
#   5. Muestra el precio final.
def compra_con_descuento():
    """
    Calcula el monto final de una compra aplicando descuento si se posee cupón.
    """
    try:
        precio_original = float(input("Ingresa el precio original del artículo: "))
        if precio_original < 0:
            raise ValueError("El precio original no puede ser negativo.")
        tiene_cupon = input("¿Tienes cupón de descuento? (sí/no): ").strip().lower()
        respuestas_positivas = {"sí", "si", "s", "y", "SÍ", "SI", "S", "Y"}
        if tiene_cupon in respuestas_positivas:
            valor_cupon = float(input("Ingresa el valor del cupón de descuento: "))
            if valor_cupon > 0:
                precio_final = max(0, precio_original - valor_cupon)
            else:
                precio_final = precio_original
        else:
            precio_final = precio_original
        print("El precio final es:", precio_final)
    except ValueError as e:
        print("Error en la entrada de datos:", e)
# Llamada a la función para prueba
print("\nEjercicio 1.43 - Compra con descuento:")
compra_con_descuento()
