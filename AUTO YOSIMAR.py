# -*- coding: utf-8
import time #  importamos el packe de time
class ferrari():    #  Se crea la clase con nombre mi_auto
    def __init__(self, velocidad = 0):
        self.velocidad = velocidad
        self.accion=9
    def mostrar(self):
        print(f" 1: Acelerar", "2: Frenar", "3: crucero")
        print(f"Velocidad actual : ", self.velocidad)
    def acelerar(self):
        while True:
            self.mostrar()
            accion = int(input("Que desea hacer :"))#  Lectura en mayuscula
            if(accion == 1):
                self.velocidad+=5   #  Aumenta la velocidad del auto de 5 en 5
            if(self.velocidad >0 and accion==2):    #  pregunta si desea seguir frenando
                while(accion != 5 and self.velocidad >= 5):
                    self.velocidad-=5   #  Frena el auto de 5 en 5
                    print(f"La velocidad actual del auto es: ", self.velocidad)
                    accion = int(input("Quieres que el auto siga frenando? 4: SI  5: NO  "))
            if(accion == 3):
                while(self.velocidad != 60):  # la velociad crucero llega a 60Km/h frenando o acelerando
                    time.sleep(0.25)    #  Crea un efecto para realentizar cada segundo
                    if(self.velocidad > 60):
                        self.velocidad-=5   #  debe frenar el auto
                    else:
                        self.velocidad+=5   #  debe acelerar el auto
                    print(f"Velocidad crucero :", self.velocidad)

auto=ferrari()
auto.acelerar()







