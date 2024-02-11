import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio**2
        return area

if __name__ == "__main__":
    # Ejemplo de uso
    try:
        radio_usuario = float(input("Ingrese el radio del círculo: "))
        mi_circulo = Circulo(radio_usuario)
        area_circulo = mi_circulo.calcular_area()
        print(f"El área del círculo con radio {radio_usuario} es: {area_circulo:.2f}")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico para el radio.")
