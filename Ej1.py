def obtener_porcentaje_combustible():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            numerador, denominador = map(int, fraccion.split('/'))

            if denominador == 0 or numerador > denominador or denominador < 0:
                raise ValueError("Error: X debe ser menor o igual a Y, y Y debe ser diferente de 0")

            porcentaje = (numerador / denominador) * 100

            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{round(porcentaje)}%"

        except ValueError as ve:
            print(f"Error: {ve}. Vuelva a intentar.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Vuelva a intentar.")

if __name__ == "__main__":
    resultado = obtener_porcentaje_combustible()
    print("Resultado:", resultado)
