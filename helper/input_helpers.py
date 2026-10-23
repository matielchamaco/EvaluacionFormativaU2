def leer_entero(mensaje: str, minimo: int = None) -> int:
    """Solicita un número entero por consola de forma segura con try-except."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error de entrada: Por favor, ingresa un número entero válido.")

def leer_flotante(mensaje: str, minimo: float = 0.0) -> float:
    """Solicita un número decimal de forma segura, validando un mínimo permitido."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo:
                print(f"Error: El monto no puede ser inferior a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error de entrada: Por favor, ingresa un número decimal válido.")

def leer_texto(mensaje: str) -> str:
    """Solicita un texto asegurando que no quede vacío ni compuesto solo por espacios."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: Este campo no puede quedar vacío.")