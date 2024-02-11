import random

def generar_numeros_aleatorios():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista generada:")
    print(lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
import sebastian_esquivel

if __name__ == "__main__":
    # Ejemplo de uso del módulo
    lista_aleatoria = sebastian_esquivel.generar_numeros_aleatorios()
    sebastian_esquivel.mostrar_lista(lista_aleatoria)
    sebastian_esquivel.ordenar_y_mostrar(lista_aleatoria)

