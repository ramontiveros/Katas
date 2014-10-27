def GetRankedGame(hands):
    """
        Esta funcion recibe las manos y se encarga de determinar 
        que juego tiene cada mano, darles puntajes y determinar cual gana
        (regresa una cadena con el formato indicado) 
    """
    raise NotImplementedError
    
if __name__ == '__main__':
    print("Captura un mano por linea y una linea en blanco para terminar:")
    hands = ""
    line = input()
    while(line != ""):
        hands += line + "\n"
        line = input()
    print(GetRankedGame(hands))