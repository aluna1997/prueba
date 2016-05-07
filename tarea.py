
class Alumnos:
    cinta = ""
    nombre = ""
    apellido = ""
    edad = ""
    def __init__(self, nombre, apellido, edad, cinta): 
        self.nombre = nombre
        self.apellido = apellido
        self.cinta = cinta
        self.edad = edad

    def getFullDates(self):
        return "{0} {1} {2} {3}".format(self.nombre, self.apellido, self.edad, self.cinta)	