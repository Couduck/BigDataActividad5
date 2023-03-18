import math

# Archivo main de la actividad

# Ejercicio 1
def ejercicio1():
    print("---------------")
    input("Ejercicio 1: Calcular el area de un triangulo equilatero con base y altura definidos (4 y 6 respectivamente)\n\nPRESIONE ENTER...")
    print("---------------\n")

    # Definición de variables
    base = 4
    altura = 6

    # Efectuar cálculos
    area = base*altura/2

    # Imprimir resultados
    print(f"Resultados:\n\n\tBase = {base}\n\tAltura = {altura}\n\n\tArea = {base}*{altura}/2 = {area}")
    input("\n\nPRESIONE ENTER...")

def ejercicio2():
    print("---------------")
    input("Ejercicio 2: Determinar la hipotenusa de un triangulo con catetos ya definidos (4.56 y 5.67 respectivamente)\n\nPRESIONE ENTER...")
    print("---------------\n")

    # Definición de variables
    C1 = 4.56
    C2 = 5.67

    # Efectuar cálculos
    H = round(math.sqrt(math.pow(C1,2) + math.pow(C2,2)),2)

    # Imprimir resultados
    print(f"Resultados:\n\n\tCateto 1 = {C1}\n\tCateto 2 = {C2}\n\n\tHipotenusa = √(C1^2 + C2^2) = {H}")
    input("\n\nPRESIONE ENTER...")

def ejercicio3():
    print("---------------")
    input("Ejercicio 3: Usar los valores del triangulo anterior para calcular su semiperimetro\n\nPRESIONE ENTER...")
    print("---------------\n")

    # Definición de variables
    C1 = 4.56
    C2 = 5.67
    H = round(math.sqrt(math.pow(C1, 2) + math.pow(C2, 2)), 2)

    # Efectuar cálculos
    semiperimetro = round((C1 + C2 + H)/2,2)

    # Imprimir resultados
    print(f"Resultados:\n\n\tCateto 1 = {C1}\n\tCateto 2 = {C2}\n\tHipotenusa = {H}\n\n\tSemiperimetro = (C1 + C2 + H)/2 = {semiperimetro}")
    input("\n\nPRESIONE ENTER...")

def ejercicio4():
    print("---------------")
    input("Ejercicio 4: Calcular el seno, coseno y tangente de un triangulo al igual que uno de sus ángulos (en grados) teniendo en cuenta la medida de su cateto adyacente (X = 12.3) y su cateto opuesto (Y = 11)\n\nPRESIONE ENTER...")
    print("---------------\n")

    # Definición de variables
    X = 12.3
    Y = 11
    Z = round(math.sqrt(math.pow(X,2) + math.pow(Y,2)),1)

    # Efectuar cálculos
    trianguloSen = round(Y/Z,4)
    trianguloCos = round(X/Z,4)
    trianguloTan = round(Y/X,4)

    angulo = round(math.asin(trianguloSen) * 180/math.pi,2)

    # Imprimir resultados
    print(f"Resultados:\n\n\tCateto Opuesto = {Y}\n\tCateto Adyacente = {X}\n\tHipotenusa = {Z}\n\n\tseno = (O/H) = {trianguloSen}\n\tcoseno = (A/H) = {trianguloCos}\n\ttangente = (O/A) = {trianguloTan}\n\n\tangulo (°) = arcsin({trianguloSen}) * 180/π = {angulo}")
    input("\n\nPRESIONE ENTER...")

# Ejecución de main
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
