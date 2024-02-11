def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero.")
        resultado = a / b
        return resultado
    except (TypeError, ZeroDivisionError) as e:
        return f"Error: {str(e)}"

import operaciones

if __name__ == "__main__":
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")

    try:
        num1 = float(num1)
        num2 = float(num2)

        resultado_suma = operaciones.suma(num1, num2)
        print(f"Suma: {resultado_suma}")

        resultado_resta = operaciones.resta(num1, num2)
        print(f"Resta: {resultado_resta}")

        resultado_producto = operaciones.producto(num1, num2)
        print(f"Producto: {resultado_producto}")

        resultado_division = operaciones.division(num1, num2)
        print(f"División: {resultado_division}")

    except ValueError:
        print("Error: Tipo de dato no válido. Asegúrese de ingresar números.")
