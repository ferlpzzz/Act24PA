def factorial(n):
    if n<0:
        return "No es un numero natural"
    elif n == 0 or n == 1:   # Caso base
        return 1
    else:
        return n * factorial(n - 1)
def natural(m):
    if m <0:
        print("No es un numero natural")
    elif m== 0:
        return 0
    else:
        return m + natural(m-1)
def fibonacci(o):
    if o <= 0:
        return 0
    elif o == 1:
        return 1
    elif o == 2:
        return 1
    else:
        return fibonacci(o-1) + fibonacci(o-2)


while True:
    print("1- Calcular el factorial de un numero")
    print("2- SUma de los primeros N numeros naturales")
    print("3- Calcular el n-ésimo número de Fibonacci")
    print("4- Contar cuántas veces aparece una letra en una palabra")
    print("5- Invertir una cadena de texto")
    print("6- Calcular la potencia de un número (base^exponente)")
    print("7- Salir")
    opcion = input("Ingrese su opcion: ")
    match opcion:
        case "1":
            numero = int(input("Ingrese un número: "))
            print(f"El factorial de {numero} es {factorial(numero)}")
        case "2":
            numero = int(input("Ingrese un numero: "))
            print(f"La suma de los primeros n numeros naturales es: {natural(numero)}")
        case "3":
            numero = int(input("Ingrese un numero: "))
            print(f"El numero de fibonacci es: {fibonacci(numero)}")

