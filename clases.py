class Sensei:

   name = ""
   lastname = ""

   def __init__(self, name, lastname): #init es el constructor
       self.name = name
       self.lastname = lastname

   def getFullName(self):
       return "{0} {1}".format(self.name, self.lastname)	