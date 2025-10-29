##Ejercicio1
# Funcion recursiva que calcula el factorial de un numero
def factorial(n):
    if n == 0 or n == 1:  # Caso base: factorial de 0 o 1 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Solicitar al usuario un numero entero
num = int(input("Ingrese un numero entero: "))

# Mostrar los factoriales desde 1 hasta el numero ingresado
print(f"\nFactoriales del 1 al {num}:")
for i in range(1, num + 1):
    print(f"{i} = {factorial(i)}")  # Calcular y mostrar factorial de i


##Ejercicio2
# Funcion recursiva que calcula el valor de Fibonacci en la posicion n
def fibonacci(n):
    if n <= 1:  # Caso base: Fibonacci de 0 es 0 y de 1 es 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva

# Solicitar al usuario la posicion hasta donde desea ver la serie
num = int(input("Ingrese la posicion hasta la que desea ver la serie de Fibonacci: "))

# Mostrar la serie de Fibonacci desde la posicion 0 hasta la indicada
print(f"\nSerie de Fibonacci hasta la posicion {num}:")
for i in range(num):
    print(fibonacci(i), end=" ")  # Calcular y mostrar Fibonacci de cada posicion


##Ejercicio3
# Funcion recursiva que calcula la potencia de un numero
def potencia(base, exponente):
    if exponente == 0:  # Caso base: cualquier numero elevado a 0 es 1
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Llamada recursiva

# Solicitar al usuario la base y el exponente
b = float(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))

# Calcular la potencia y mostrar el resultado
resultado = potencia(b, e)
print(f"{b} elevado a la {e} es {resultado}")


##Ejercicio4
# Funcion recursiva que convierte un numero decimal a binario
def decimal_a_binario(n):
    if n == 0:  # Caso base: si el numero es 0, retornar cadena vacia
        return ""
    else:
        # Llamada recursiva con el cociente de n entre 2 y concatenar el resto
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar al usuario un numero entero positivo
num = int(input("Ingrese un numero entero positivo: "))

# Mostrar el resultado en binario
if num == 0:
    print("0")
else:
    print(f"El numero {num} en binario es {decimal_a_binario(num)}")


##Ejercicio5
# Funcion recursiva que verifica si una palabra es palindromo
def es_palindromo(palabra):
    if len(palabra) <= 1:  # Caso base: una letra o cadena vacia es palindromo
        return True
    if palabra[0] != palabra[-1]:  # Si los extremos no coinciden, no es palindromo
        return False
    # Llamada recursiva eliminando el primer y ultimo caracter
    return es_palindromo(palabra[1:-1])

# Solicitar al usuario una palabra
texto = input("Ingrese una palabra: ")

# Verificar y mostrar el resultado
if es_palindromo(texto.lower()):
    print("Es palindromo")
else:
    print("No es palindromo")


##Ejercicio6
# Funcion recursiva que calcula la suma de los digitos de un numero
def suma_digitos(n):
    if n < 10:  # Caso base: si el numero es de un solo digito, retornar el mismo numero
        return n
    else:
        # Sumar el ultimo digito (n % 10) y llamar recursivamente con el resto del numero (n // 10)
        return n % 10 + suma_digitos(n // 10)

# Solicitar al usuario un numero entero positivo
num = int(input("Ingrese un numero entero positivo: "))

# Mostrar la suma de los digitos
print(f"La suma de los digitos de {num} es {suma_digitos(num)}")


##Ejercicio7
# Funcion recursiva que calcula el total de bloques necesarios para una piramide
def contar_bloques(n):
    if n == 1:  # Caso base: si solo hay un bloque, retornar 1
        return 1
    else:
        # Sumar el numero de bloques del nivel actual y llamar recursivamente con n-1
        return n + contar_bloques(n - 1)

# Solicitar al usuario el numero de bloques del nivel mas bajo
num = int(input("Ingrese el numero de bloques del nivel mas bajo: "))

# Mostrar el total de bloques necesarios
print(f"Total de bloques necesarios: {contar_bloques(num)}")


##Ejercicio8
# Funcion recursiva que cuenta cuantas veces aparece un digito en un numero
def contar_digito(numero, digito):
    if numero == 0:  # Caso base: si el numero es 0, retornar 0
        return 0
    elif numero % 10 == digito:  # Si el ultimo digito coincide, sumar 1
        return 1 + contar_digito(numero // 10, digito)
    else:
        # Llamada recursiva eliminando el ultimo digito
        return contar_digito(numero // 10, digito)

# Solicitar al usuario un numero entero positivo y el digito a contar
num = int(input("Ingrese un numero entero positivo: "))
d = int(input("Ingrese el digito a contar: "))

# Mostrar cuantas veces aparece el digito en el numero
print(f"El digito {d} aparece {contar_digito(num, d)} veces en {num}")
