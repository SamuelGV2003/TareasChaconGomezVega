def separa_letras(cadena):
    """
    Separa una cadena en letras mayúsculas y minúsculas.
    Devuelve un código de error/éxito y las dos cadenas resultantes.
    """
    # Verificar que el parámetro sea un string
    if not isinstance(cadena, str):
        return "Error", None, None  # Código de error: No es un string
    
    # Verificar que no sea un string vacío
    if cadena.strip() == "":
        return "Error", None, None  # Código de error: String vacío
    
    # Verificar que solo contenga letras del abecedario
    if not cadena.isalpha():
        return "Error", None, None  # Código de error: Contiene caracteres no alfabéticos
    
    mayusculas = "".join([c for c in cadena if c.isupper()])
    minusculas = "".join([c for c in cadena if c.islower()])
    
    return "Éxito", mayusculas, minusculas  # Código de éxito

if __name__ == "__main__":
    entrada = input("Ingrese una palabra: ").strip()
    resultado, mayusculas, minusculas = separa_letras(entrada)
    
    if resultado == "Éxito":
        print(f"Éxito: Mayúsculas: {mayusculas}, Minúsculas: {minusculas}")
    else:
        print("Error: Entrada no válida.")

