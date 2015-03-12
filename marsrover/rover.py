'''
Created on 12/3/2015

@author: Robert
'''
#Modulo rover.py

class Rover(object):
    maxX = 0
    maxY = 0
    direction = 0
    rover_pos_x = 0
    rover_pos_y = 0
    opciones_movimientos = {}
    definicion_movimientos = {}
    options = {}
    options_inv = {}    
        
    def __init__(self, xi, yi):
        self.maxX = xi
        self.maxY = yi
        self.opciones_movimientos = {'M' : self.move, 'R' : self.toRight, 'L' : self.toLeft, }
        self.definicion_movimientos = {0 : self.avanzararriba, 1 : self.avanzarderecha, 2 : self.avanzarabajo, 3:self.avanzarizquierda, }
        self.options = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3, }
        self.options_inv = {0:'N', 1:'E', 2:'S', 3:'W', }

    def establecerPosicionRoverInicial(self, x, y, direccionx):
        self.rover_pos_x = x
        self.rover_pos_y = y        
        self.direction = self.options[direccionx]

    def obtenerDireccionFinal(self):                
        punto_cardinal = self.options_inv[self.direction]    
        return "%d %d %c" % (self.rover_pos_x, self.rover_pos_y, punto_cardinal)

    def toLeft(self):        
        self.direction = self.direction - 1
        if self.direction < 0 :
            self.direction = 3

    def toRight(self):
        self.direction = self.direction + 1
        if self.direction > 3 :
            self.direction = 0

    def avanzararriba(self):    
        if self.rover_pos_y <= self.maxY - 1:
            self.rover_pos_y = self.rover_pos_y + 1

    def avanzarderecha(self):        
        if self.rover_pos_x <= self.maxX - 1:
            self.rover_pos_x = self.rover_pos_x + 1

    def avanzarabajo(self):        
        if self.rover_pos_y >= 1:
            self.rover_pos_y = self.rover_pos_y - 1

    def avanzarizquierda(self):        
        if self.rover_pos_x >= 1:
            self.rover_pos_x = self.rover_pos_x - 1

    def move(self):        
        self.definicion_movimientos[self.direction]()

    def establecerMovimientosRover(self, movimientos):        
        for comando in movimientos:
            self.opciones_movimientos[comando]()

#rover = Rover(5, 5)
#rover.establecerPosicionRoverInicial(1, 2, "N")
#rover.establecerMovimientosRover("LMLMLMLMM")
#print(rover.obtenerDireccionFinal())

#rover.establecerPosicionRoverInicial(3,3,"E")
#rover.establecerMovimientosRover("MMRMMRMRRM")
#print(rover.obtenerDireccionFinal())

#rover.establecerPosicionRoverInicial(2, 3, "W")
#rover.establecerMovimientosRover("MRMRMRMMLMR")
#print(rover.obtenerDireccionFinal())
