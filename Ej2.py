def obtener_calificaciones():
    while True:
        try:
            input_calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")
            calificaciones = [int(cal) for cal in input_calificaciones.split(',')]
            return calificaciones
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros separados por comas. Vuelva a intentar.")

if __name__ == "__main__":
    calificaciones_usuario = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones_usuario)
