class Producto:

    def __init__(self):
        self.codigo = ""
        self.tamaño = 0
        self.descripcion = ""

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setTamaño(self, tamaño):
        self.tamaño = tamaño

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getCodigo(self):
        return self.codigo

    def getTamaño(self):
        return self.tamaño

    def getDescripcion(self):
        return self.descripcion

    def __str__(self):
        return self.codigo+" "+self.tamaño+" "+self.descripcion