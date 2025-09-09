def factorial(n):
    if n == 0 or n == 1:   # Caso base
        return 1
    else:
        return n * factorial(n - 1)

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


