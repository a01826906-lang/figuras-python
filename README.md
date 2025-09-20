# Proyecto Individual: Cálculo de Figuras

Este proyecto calcula **área y perímetro** de círculos, triángulos y rectángulos usando Python.

## Estructura del proyecto

- `main/main.py`: archivo principal con funciones para calcular área y perímetro y que lee el archivo CSV.
- `figuras/figuras.csv`: archivo con la lista de figuras y sus medidas.

## Funcionalidad

- Funciones:
  - `triangulo(base, altura)`: devuelve área y perímetro de un triángulo rectángulo.
  - `rectangulo(base, altura)`: devuelve área y perímetro de un rectángulo.
  - `circulo(radio)`: devuelve área y perímetro de un círculo.

- El programa lee un archivo CSV con las columnas:
  - `FIGURA` → tipo de figura: `c` (círculo), `t` (triángulo), `r` (rectángulo)
  - `MEDIDA1` → radio o base
  - `MEDIDA2` → altura (para triángulo y rectángulo; 0 para círculos)

- Calcula automáticamente el **área y perímetro** de todas las figuras del CSV y las imprime en la terminal.

