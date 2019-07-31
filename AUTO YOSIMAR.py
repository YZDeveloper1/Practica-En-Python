
import time 
class ferrari():    
    def __init__(self, velocidad = 0):
        self.velocidad = velocidad
        self.accion=9
    def mostrar(self):
        print(f" 1: Acelerar", "2: Frenar", "3: crucero")
        print(f"Velocidad actual : ", self.velocidad)
    def acelerar(self):
        while True:
            self.mostrar()
            accion = int(input("Que desea hacer :"))
            if(accion == 1):
                self.velocidad+=5   
            if(self.velocidad >0 and accion==2):  
                while(accion != 5 and self.velocidad >= 5):
                    self.velocidad-=5   
                    print(f"La velocidad actual del auto es: ", self.velocidad)
                    accion = int(input("Quieres que el auto siga frenando? 4: SI  5: NO  "))
            if(accion == 3):
                while(self.velocidad != 60): 
                    time.sleep(0.25)   
                    if(self.velocidad > 60):
                        self.velocidad-=5  
                    else:
                        self.velocidad+=5   
                    print(f"Velocidad crucero :", self.velocidad)

auto=ferrari()
auto.acelerar()







