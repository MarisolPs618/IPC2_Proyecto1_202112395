class muestra:
    def __init__(self, codigo, descripcion, filas, columnas, celdas_vivas):
        self.codigo = codigo
        self.descripcion = descripcion
        self.filas = filas
        self.columnas=columnas
        self.celdas_vivas=celdas_vivas
        
class celdasV:
    def __init__(self, fila, columna, codigo_organismo):
        self.fila = fila
        self.columna=columna
        self.codigo_organismo = codigo_organismo

    
   