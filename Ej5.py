class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        if self.notas:
            print(f"Notas: {', '.join(map(str, self.notas))}")
        else:
            print("Notas: No asignadas")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

if __name__ == "__main__":
    # Ejemplo de uso
    nombre_usuario = input("Ingrese el nombre del estudiante: ")
    numero_registro_usuario = input("Ingrese el número de registro del estudiante: ")

    alumno1 = Alumno(nombre_usuario, numero_registro_usuario)
    
    edad_usuario = input("Ingrese la edad del estudiante: ")
    try:
        alumno1.set_age(int(edad_usuario))
    except ValueError:
        print("Error: La edad debe ser un valor numérico.")

    notas_usuario = input("Ingrese las notas del estudiante separadas por comas: ").split(',')
    try:
        alumno1.set_notas([float(nota) for nota in notas_usuario])
    except ValueError:
        print("Error: Las notas deben ser valores numéricos.")

    alumno1.display()
