class Cells: 
    
    def __init__(self): 
        self.alive = False 
        self.neighbors = 0
        
        
        "Getter and Setter :"
        
        def is_alive(self):
            return self.alive
        
        def kill_cell(self):
            self.alive = False
            
        def rez_cell(self):
            self.alive = True
            
        def set_neighbors(self, n):
            self.neighbors = n
            
        def get_neighbors(self):
            return self.neighbors