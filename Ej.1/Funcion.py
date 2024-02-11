from porcentaje import obtener_porcentaje

def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y: ")
        resultado = obtener_porcentaje(fraction)
        if resultado:
            print("Cantidad de combustible en el tanque:", resultado)
            break

if __name__ == "__main__":
    main()