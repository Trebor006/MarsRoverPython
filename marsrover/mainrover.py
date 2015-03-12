'''
Created on 12/3/2015

@author: Robert
'''

from marsrover.rover import Rover

class RoverMain(object):
      
    def __init__(self):  
        self.maxX = 0
        self.maxY = 0
        self.pos_rover_x = 0
        self.pos_rover_y = 0
        self.direccion_rover = 0
        self.movimientos = ""
        self.cont = 0        
        self.inicio = True
        self.movimientos=""
        
    def ejecutar(self,directorio_archivo):
        px=Rover(0,0)    
        f = open(directorio_archivo)   
        for linea in f:
 #           print(linea)
            if self.inicio==True:
                linea_array = linea.split(" ")
                maxX = linea_array[0]
                maxYLetra= linea_array[1]               
                msplit = maxYLetra.split("\n")
                maxY=msplit[0]
                self.inicio = False;
                px = Rover(int(maxX), int(maxY))
            else:
                if self.cont==0:
                    linea_array = linea.split(" ")                    
                    self.pos_rover_x = linea_array[0]
                    self.pos_rover_y = linea_array[1]
                    letrax=linea_array[2]                    
                    self.direccion_rover =letrax[0]                     
                    #print("%d %d %c" % (int(self.pos_rover_x), int(self.pos_rover_y), self.direccion_rover))
                    px.establecerPosicionRoverInicial(int(self.pos_rover_x), int(self.pos_rover_y), self.direccion_rover)
                    self.cont = 1
                else:
                    linea_leida = linea.split("\n")
                    self.movimientos = linea_leida[0]
                    px.establecerMovimientosRover(self.movimientos)
                    print(px.obtenerDireccionFinal())
                    self.cont = 0
            
        f.close()
                
objeto = RoverMain()
objeto.ejecutar("EntradaDeDatos.txt")