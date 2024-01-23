import random
from Tablero import Tablero

class Menu:
    def __init__(self):
        pass
    def palabra_aleatoria(self):
        palabra = ['moñiga', 'puchero', 'paliza', 'croqueta', 'cazurro', 'calvo']
        return random.choice(palabra)

    def iniciar_juego(self):
        print("¡Bienvenido al Juego del Ahorcado!")
        print("Tienes que adivinar la palabra secreta antes de quedarte sin intentos.")
        print("Buena suerte... ¡y que comience el juego!")

        nuevoTablero = Tablero()
        palabra = self.palabra_aleatoria()
        letras_adivinadas = []
        numero_intentos = 0

        while True:
            nuevoTablero.mostrar_tablero(numero_intentos)

            estado = ''
            for letra in palabra:
                if letra in letras_adivinadas:
                    estado += letra + ' '
                else:
                    estado += '_ '
            print(estado)

            if estado.replace(" ", "") == palabra:
                print('¡Felicidades! ¡Has adivinado la palabra correctamente!')
                break

            if numero_intentos == len(nuevoTablero.figura) - 1:
                print('¡Oh no! Te has quedado sin intentos. La palabra era:', palabra)
                break

            letra = input('Ingresa una letra: ').lower()

            if len(letra) != 1 or not letra.isalpha():
                print('Por favor, ingresa una sola letra válida.')
                continue

            if letra in letras_adivinadas:
                print('Ya has ingresado esa letra antes. ¡Intenta con otra!')
                continue

            letras_adivinadas.append(letra)

            if letra not in palabra:
                numero_intentos += 1
                print('La letra', letra, 'no está en la palabra. ¡Te quedan', len(nuevoTablero.figura) - numero_intentos, 'intentos!')


