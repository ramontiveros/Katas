def NextOfspring(u):
    """
        Esta funcion recibe un universo y regresa la siguiente generacion segun las reglas
        Nota: La funcion recibe la cadena el el formato establecido y lo regresa en el mismo formato
    """
    raise NotImplementedError

def GetUniverse(u):
    """
        Esta funcion debe de regresar el universo en el formato establecido 
        pero regresa el universo sin el renglon de las dimenciones y con los saltos
        de linea correspondientes
    """
    raise NotImplementedError

if __name__ == '__main__':
    print("Captura un universo (Linea por linea segun el formato y vacio para terminar)")
    u = ""
    line = input()
    while(line != ""):
        u += line
        line = input()
    option = input("Teclee n para ver la siguiente generacion y s para deter la simulacion")
    while(option == "n"):
        u = NextOfspring(u)
        print(GetUniverse(u))
        option = input()
    