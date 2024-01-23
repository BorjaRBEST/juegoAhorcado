
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
    def mostrar_tablero(self, intentos):
        if 0 <= intentos < len(self.figura):
            print(self.figura[intentos])
        else:
            print('Te has pasado de intentos compadre')
