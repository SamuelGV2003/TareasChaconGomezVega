def separa_letras(cadena):
    """
    Separa una cadena en letras mayúsculas y minúsculas.
    Devuelve un código de error/éxito y las dos cadenas resultantes.
    """
    # Verificar que el parámetro sea un string
    if not isinstance(cadena, str):
        return -100, None, None  # Código de error: No es un string

    # Verificar que no sea un string vacío
    if cadena.strip() == "":
        return -300, None, None  # Código de error: String vacío

    # Verificar que solo contenga letras del abecedario
    if not cadena.isalpha():
        return -200, None, None
    # El anterior es el Código de error: Tiene caracteres no alfabéticos

    mayusculas = "".join([c for c in cadena if c.isupper()])
    minusculas = "".join([c for c in cadena if c.islower()])

    return 0, mayusculas, minusculas  # Código de éxito


if __name__ == "__main__":
    entrada = input("Ingrese una palabra: ").strip()
    resultado, mayusculas, minusculas = separa_letras(entrada)

    if resultado == 0:
        print(f"Éxito: Mayúsculas: {mayusculas}, Minúsculas: {minusculas}")
    else:
        print("Error: Entrada no válida.")


def potencia_manual(base, potencia):
    """
    Calcula la potencia de una base usando sumas,
    ciclos for y condiciones if/else.
    No se permite el uso de multiplicaciones o funciones de potencia de Python.

    Parámetros:
    - base: Número entero o flotante (no string).
    - potencia: Número entero o flotante (no string).

    Retorna:
    - Código de error/éxito (int).
    - Resultado de la operación (float o int) o None en caso de error.
    """

    # Verificar que los parámetros no sean de tipo string
    if isinstance(base, str) or isinstance(potencia, str):
        return -400, None  # Código de error: Parámetro es un string

    # Casos especiales:
    # Si la potencia es 0, el resultado es 1 (excepto cuando la base es 0)
    if potencia == 0:
        if base == 0:
            return 0, 0  # 0^0 es indefinido, pero aquí se retorna 0
        return 0, 1  # Cualquier número elevado a 0 es 1

    # Si la base es 0, el resultado es 0 (excepto cuando la potencia es 0)
    if base == 0:
        return 0, 0  # 0 elevado a cualquier potencia es 0

    # Si la potencia es negativa, se convierte en positiva y se invierte
    es_negativo = potencia < 0
    potencia = abs(potencia)  # Trabajamos con potencias positivas

    # Inicializar el resultado como la base
    resultado = base

    # Calcular la potencia usando sumas y ciclos for
    for _ in range(1, int(potencia)):
        temp = 0
        for _ in range(int(base)):
            temp += resultado
        resultado = temp

    # Si la potencia era negativa, calcular el inverso
    if es_negativo:
        resultado = 1 / resultado

    return 0, resultado  # Código de éxito y resultado de la operación


if __name__ == "__main__":
    base = float(input("Ingrese la base: "))
    potencia = float(input("Ingrese la potencia: "))

    estado, resultado = potencia_manual(base, potencia)

    if estado == 0:
        print(f"Éxito: Resultado = {resultado}")
    else:
        print(f"Error: Código = {estado}")
