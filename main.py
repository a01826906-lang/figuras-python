# Cálculo de figuras
import math
import csv  

# ===========================

# Triángulo
def triangulo(base, altura):
    """Calcula el área y perímetro del triángulo (rectángulo)"""
    area = (base * altura) / 2
    hipotenusa = math.sqrt(base ** 2 + altura ** 2)
    perimetro = base + altura + hipotenusa
    return area, perimetro

# Círculo
def circulo(radio):
    """Calcula el área y perímetro del círculo"""
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

# Rectángulo
def rectangulo(base, altura):
    """Calcula el área y perímetro del rectángulo"""
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro


# ===========================

with open("../figuras/figuras.csv", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        figura = fila["FIGURA"]
        medida1 = float(fila["MEDIDA1"])
        medida2 = float(fila["MEDIDA2"])

        if figura == "t":
            area, perimetro = triangulo(medida1, medida2)
            print(f"Triángulo (base={medida1}, altura={medida2}) → Área: {area:.2f}, Perímetro: {perimetro:.2f}")

        elif figura == "r":
            area, perimetro = rectangulo(medida1, medida2)
            print(f"Rectángulo (base={medida1}, altura={medida2}) → Área: {area:.2f}, Perímetro: {perimetro:.2f}")

        elif figura == "c":
            area, perimetro = circulo(medida1)
            print(f"Círculo (radio={medida1}) → Área: {area:.2f}, Perímetro: {perimetro:.2f}")
