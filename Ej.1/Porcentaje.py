def obtener_porcentaje(fraction):
    try:
        numerador, denominador = map(int, fraction.split('/'))
        if denominador == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        if numerador > denominador:
            raise ValueError("El numerador debe ser menor o igual al denominador.")
        
        porcentaje = numerador/denominador * 100

        if porcentaje < 1:
            return "E"
        elif porcentaje > 99:
            return "F"
        else:
            return f"{round(porcentaje)}%"
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese una fracción válida con números enteros.")
        return None
    except ZeroDivisionError as e:
        print(f"Error: {e}. Por favor, ingrese una fracción válida con denominador diferente de cero.")
        return None