import random
from Tablero import Tablero

class Menu:
    def __init__(self):
        self.nuevoTablero = Tablero()
        self.palabra = self.palabra_aleatoria()
        self.letras_adivinadas = []
        self.numero_intentos = 0

    # Método para agregar nuestras palabras dentro del atributo palabra y que te devuelva de forma
    # aleatoria una de ellas a palabra_aleatoria
    def palabra_aleatoria(self):
        palabra = ['moñiga', 'puchero', 'paliza', 'croqueta', 'cazurro', 'calvo']
        return random.choice(palabra)

    # Este método contiene la lógica para iniciar el juego, en el va a estar el bucle que va a
    # recorrer el tablero según las letras que pongamos, también irá rellenado posiciones, comparando si la letra
    # ha sido ya introducida, si es un caracter válido y si no se encuentra dentro de la palabra
    def iniciar_juego(self):
        print("¡Bienvenido al Juego del Ahorcado!")
        print("Tienes que adivinar la palabra secreta antes de quedarte sin intentos.")
        print("Buena suerte... ¡y que comience el juego!")



        while True:
            self.nuevoTablero.mostrar_tablero(self.numero_intentos)

            estado = ''
            for letra in self.palabra:
                if letra in self.letras_adivinadas:
                    estado += letra + ' '
                else:
                    estado += '_ '
            print(estado)
            # Si la representación de la palabra oculta coincide con la palabra secreta, el jugador ha ganado.
            if estado.replace(" ", "") == self.palabra:
                print('¡Felicidades! ¡Has adivinado la palabra correctamente!')
                break
            # Si el número de intentos alcanza el límite (longitud máxima de la lista figura), el jugador ha perdido.
            if self.numero_intentos == len(self.nuevoTablero.figura) - 1:
                print('¡Oh no! Te has quedado sin intentos. La palabra era:', self.palabra)
                break

            letra = input('Ingresa una letra: ').lower()
            # Verifica si la entrada del jugador no es una sola letra válida.
            if len(letra) != 1 or not letra.isalpha():
                print('Mete una letra válida cohone!.')
                continue
            # Verifica si la letra ya ha sido ingresada antes.
            if letra in self.letras_adivinadas:
                print('Ya pusiste esa letra antes abuel@')
                continue

            self.letras_adivinadas.append(letra)
            # Verifica si la letra está en la palabra y te dice el número de intentos que te quedan
            if letra not in self.palabra:
                self.numero_intentos += 1
                print('La letra', letra, 'no está en la palabra. ¡Te quedan', len(self.nuevoTablero.figura) - self.numero_intentos, 'intentos!')
                continue

