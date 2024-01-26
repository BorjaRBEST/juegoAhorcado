# Creamos una clase Tablero que contendrá la figura representativa,
# está figura es un array de 7 posiciones en las cuales gracias a comentarios multilineas agregamos
# unos String que representará nuestro monigote en cada momento
class Tablero:
    def __init__(self):
        self.figura = [
               '''
               -----   
               |   |  
               |
               |
               |
               ========    
               ''',
                '''
               -----   
               |   |  
               |   0
               |
               |
               ========    
               ''',
                '''
               -----   
               |   |  
               |   0
               |   |
               |
               ========    
               ''',
                '''
               -----   
               |   |  
               |   0
               |  /| 
               |
               ========    
               ''',
                '''
               -----   
               |   |  
               |   0
               |  /|\\
               |
               ========    
               ''',
                '''
               -----   
               |   |  
               |   0
               |  /|\\
               |  /
               ========    
               ''',
                '''
               -----   
               |   |  
               |   0
               |  /|\\
               |  / \\
               ========    
               ''',
        ]
    # Método que compara y muestra según el número de intentos una posición u otra
    # de la figura dentro del Array, empezando por la posición 0
    def mostrar_tablero(self, intentos):
        if 0 <= intentos < len(self.figura):
            print(self.figura[intentos])
