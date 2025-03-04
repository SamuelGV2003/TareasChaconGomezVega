# Este es un código hecho por un integrante del grupo para el curso de
# elementos de computación.

# Función principal es un menú del registro de la producción de arduinos.
# Va a tener opción 1, 2, 3, 4 y 0. Cada una realiza una función diferente
# y se va a trabajar llamando a funciones secundarias.

######################################################################
# Funciones Secundarias
######################################################################
# Aquí se va a extraer y guardar los datos del archivo, en caso de que
# no exista el archivo entonces se creará uno vacío.
def leer_diccionario():
    diccionario = {}
    try:
        archivo = open("produccion.dat", "r")
        string = archivo.read()
        archivo.close()
        # Está como un string, ocupa pasar a diccionario
        diccionario = eval(string)
    except:
        diccionario = {}
    return diccionario


def guardar_diccionario(diccionario):
    archivo = open("produccion.dat", "w")
    archivo.write(str(diccionario))
    archivo.close()


# Para validar entradas
def validar_arduino(arduino):
    if arduino in "Arduino UNO, Arduino TRE, Arduino Zero, Arduino Zero Pro, \
    Arduino BT, Arduino Mega, Arduino Ethernet, Arduino Pro, \
    Arduino Pro Mini, Arduino Micro, Arduino Primo, Arduino Nano, \
    Arduino Industrial 101, Arduino LilyPad, Arduino Esplora":
        return True
    else:
        print("ERROR: EL TIPO DE ARDUINO NO EXISTE")
        return False


def validar_cantidad(cantidad):
    if isinstance(cantidad, int):
        return True
    else:
        print("ERROR: LA CANTIDAD DEBE SER UN NÚMERO")
        return False


# Agregar unidades producidas
def agregar(diccionario):
    arduino = input("Indique el tipo de arduino que desea agregar:")
    if validar_arduino(arduino):
        valor = input("Indique el valor de unidades que desea agregar:")
        if validar_cantidad(valor):
            if arduino in diccionario:
                diccionario[arduino] =diccionario[arduino]+valor
            else:
                diccionario[arduino] = valor
            return diccionario


# Eliminar unidades de la producción
def eliminar(diccionario):
    arduino = input("Indique el tipo de arduino que desea eliminar:")
    if validar_arduino(arduino):
        valor = int(input("Indique el valor de unidades que desea eliminar:"))
        if validar_cantidad(valor):
            if arduino in diccionario and valor <= diccionario[arduino]:
                diccionario[arduino] = diccionario[arduino]-valor
                if diccionario[arduino] == 0:
                    del diccionario[arduino]
                return diccionario
            else:
                print("ERROR: EL VALOR DE UNIDADES A ELIMINAR ES MAYOR A LAS \
                EXISTENTES")


# Consultar producción
def consultar(diccionario):
    arduino = input("Indique el tipo de arduino que desea consultar o * si \
    desea consultar todos:")
    print("     PRODUCCIÓN DE ARDUINOS")
    print("TIPO DE ARDUINO          CANTIDAD")
    print("")
    if arduino == "*":
        for arduino in diccionario:
            print(arduino, "              ", diccionario[arduino])
    elif arduino not in diccionario:
        pass
    elif validar_arduino(arduino) and diccionario[arduino] != 0:
        print(arduino, "              ", diccionario[arduino])
    else:
        print("ERROR: EL TIPO DE ARDUINO NO EXISTE O LA CANTIDAD ES NULA")


# Consultar lista de arduinos que se pueden producir
def consultar_lista():
    print("Arduino UNO\nArduino TRE\nArduino Zero\nArduino Zero Pro\n\
    Arduino BT\nArduino Mega\nArduino Ethernet\nArduino Pro\n\
    Arduino Pro Mini\nArduino Micro\nArduino Primo\nArduino Nano\n\
    Arduino Industrial 101\nArduino LilyPad\nArduino Esplora")

######################################################################
# Funcion Primaria
######################################################################
diccionario = leer_diccionario()
while 1 < 2:
    print("          REGISTRO DE LA PRODUCCIÓN DE ARDUINOS")
    print("1-Agregar unidades producidas")
    print("2-Eliminar unidades de la producción")
    print("3-Consultar producción")
    print("4-Consultar lista de arduinos que se pueden producir")
    print("0-Fin")
    print("")
    opcion = int(input("Opción:"))
    print("")
    if opcion == 0:
        break
    elif opcion == 1:
        diccionario = agregar(diccionario)
    elif opcion == 2:
        diccionario = eliminar(diccionario)
    elif opcion == 3:
        consultar(diccionario)
    elif opcion == 4:
        consultar_lista()
    else:
        print("ERROR: NO ES UNA OPCIÓN VALIDA")
    print("")
    print("------------------------------------------------------")
    print("")
guardar_diccionario(diccionario)
