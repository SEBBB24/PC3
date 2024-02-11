class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

if __name__ == "__main__":
    # Ejemplo de uso
    try:
        largo_usuario = float(input("Ingrese el largo del rectángulo: "))
        ancho_usuario = float(input("Ingrese el ancho del rectángulo: "))
        mi_rectangulo = Rectangulo(largo_usuario, ancho_usuario)
        area_rectangulo = mi_rectangulo.calcular_area()
        print(f"El área del rectángulo con largo {largo_usuario} y ancho {ancho_usuario} es: {area_rectangulo:.2f}")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos para el largo y el ancho.")
