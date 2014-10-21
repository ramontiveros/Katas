# coding: utf8
template = " {0} │ {1} │ {2} \n───┼───┼───\n {3} │ {4} │ {5} \n───┼───┼───\n {6} │ {7} │ {8} "

def GetTablero():
    """
        Esta funcion debe regresar el tablero en forma de cadena
        Nota: Usar el template de arriva
    """
    raise NotImplementedError

def JuegoContinua():
    """
        Debe de regresar verdadero si el juego continua o false si ha terminado
    """
    raise NotImplementedError

def IntentarTirada(casilla):
    """
        Esta funcion recibe el intento del jugador por ocupar una casilla
        y regresa una cadena segun los siguientes criterios:
        Si esta fuera de rango: "La tirada debe de estar entre 1 y 9"
        Si la casilla esta ocupada: "La casilla ya esta ocupada"
        Si x a ganado: "Felicidades X as ganado. weeee"
        Si o a ganado: "Felicidades O as ganado. weeee"
        Si el juego a quedado empatado: "Juego empatado. :("
        Ninguna de las anteriores: "" (cadena vacia)
    """
    raise NotImplementedError

def IniciaJuego():
    """
        Esta function se puede utilizar para re iniciar variables.
        Si no se usa se puede dejar vacia
    """
    return None

if __name__ == '__main__':
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        msg = ""
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        if msg != "":
            print(msg)