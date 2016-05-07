class Alumnos:

	nombre = ""

	def __init__(self, nombre): 
        self.nombre = nombre


    def getFullDates(self):
        return "{0}".format(self.nombre)	
