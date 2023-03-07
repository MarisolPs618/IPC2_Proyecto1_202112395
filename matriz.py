from Listas import NodoEncabezado
from Listas import ListaEncabezado
from Listas import NodoInterno
from Muestras import celdasV
import os

class Matriz:
    def __init__(self) -> None:
        self.filas = ListaEncabezado()
        self.columnas = ListaEncabezado()

    def insertar(self, pfila, pcol, valor):
        nuevo = NodoInterno(pfila, pcol, valor)

        if self.filas.buscar(pfila) == None:
            self.filas.insertar(NodoEncabezado(pfila))

        if self.columnas.buscar(pcol) == None:
            self.columnas.insertar(NodoEncabezado(pcol))

        fila = self.filas.buscar(pfila)
        col = self.columnas.buscar(pcol)

        if fila.acceso == None:
            fila.acceso = nuevo
        else:
            if nuevo.col < fila.acceso.col:
                nuevo.derecha = fila.acceso
                fila.acceso.izquierda = nuevo
                fila.acceso = nuevo
            elif nuevo.col > fila.acceso.col:
                actual = fila.acceso
                while actual.derecha != None:
                    actual = actual.derecha
                actual.derecha = nuevo
                nuevo.izquierda = actual
            else:
                actual = fila.acceso
                while actual.derecha != None:
                    if nuevo.col < actual.derecha.col:
                        nuevo.derecha = actual.derecha
                        nuevo.izquierda = actual
                        actual.derecha.izquierda = nuevo
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha

        if col.acceso == None:
            col.acceso = nuevo
        else:
            if nuevo.fila < col.acceso.fila:
                nuevo.abajo = col.acceso
                col.acceso.arriba = nuevo
                col.acceso = nuevo
            elif nuevo.fila > col.acceso.fila:
                actual = col.acceso
                while actual.abajo != None:
                    actual = actual.abajo
                actual.abajo = nuevo
                nuevo.arriba = actual
            else:
                actual = col.acceso
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        nuevo.arriba = actual
                        actual.abajo.arriba = nuevo
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
    
    def buscar(self, fila, columna):
        encabezado_fila = self.filas.buscar(fila)
        if encabezado_fila is None:
            return None
        nodo_actual = encabezado_fila.acceso
        while nodo_actual is not None and nodo_actual.col != columna:
            nodo_actual = nodo_actual.derecha
        return nodo_actual
    
    def es_valida(self, fila, columna):
        return self.buscar(fila, columna) is not None
    
    def buscar_adyacentes(self, fila, columna):
        celdas = []
        for i in range(fila-1, fila+2):
            for j in range(columna-1, columna+2):
                if self.es_valida(i, j) and (i, j) != (fila, columna):
                    valor_celda = self.buscar(i, j).valor
                    if valor_celda != "":
                        celdas_ady = celdasV(i, j, valor_celda)
                        celdas.append(celdas_ady)
        return celdas
    
    def get_dimensiones(self):
        num_filas = len(self.filas)
        num_columnas = len(self.columnas)
        return (num_filas, num_columnas)
    
    def insertar_organismo(self, fila, columna,valor_encerrar):
        celdas_adyacentes=self.buscar_adyacentes(fila, columna)
        if celdas_adyacentes==[]:
            print("El organismo no prospera")
            
        celdas_diferentes=[]
        for celda in celdas_adyacentes:
            if celda.codigo_organismo!=valor_encerrar:
                celdas_diferentes.append(celda)
        filas_matriz, columnas_matriz=self.get_dimensiones()
        
        for organismo in celdas_diferentes:
            encerradas=[]
         
            valor_encerrado=organismo.codigo_organismo
            direccion_fila=organismo.fila-fila
            direccion_col=organismo.columna-columna
            i = fila
            j = columna
            while i >= 0 and i < filas_matriz and j >= 0 and j <columnas_matriz :
                # Hacer algo con la celda (i, j)
                i += direccion_fila
                j += direccion_col
                valor_celda=self.buscar(i, j).valor
                if valor_celda==None: 
                    print("El organismo no prospera")
                    break
                elif valor_celda==valor_encerrado:
                    celdas_encerradas=celdasV(i, j, valor_celda)
                    encerradas.append(celdas_encerradas)
                elif valor_celda==valor_encerrar:
                    for encerrada in encerradas:
                        insertada=self.buscar(fila,columna)
                        insertada.valor=valor_encerrar
                        nodo = self.buscar(encerrada.fila,encerrada.columna)
                        nodo.valor = valor_encerrar
                    break
                else:
                    print("El organismo no prospera")
                    break
           
    def verificar_insercion(self, fila, columna,valor_encerrar):
        prospera=False
        celdas_adyacentes=self.buscar_adyacentes(fila, columna)
        if celdas_adyacentes==[]:
            prospera=False
            
        celdas_diferentes=[]
        for celda in celdas_adyacentes:
            if celda.codigo_organismo!=valor_encerrar:
                celdas_diferentes.append(celda)
        filas_matriz, columnas_matriz=self.get_dimensiones()
        
        for organismo in celdas_diferentes:
            encerradas=[]
            valor_encerrado=organismo.codigo_organismo
            direccion_fila=organismo.fila-fila
            direccion_col=organismo.columna-columna
            i = fila
            j = columna
            while i >= 0 and i < filas_matriz and j >= 0 and j <columnas_matriz :
                # Hacer algo con la celda (i, j)
                i += direccion_fila
                j += direccion_col
                valor_celda=self.buscar(i, j).valor
                if valor_celda==None: 
                    prospera=False
                    break
                elif valor_celda==valor_encerrado:
                    celdas_encerradas=celdasV(i, j, valor_celda)
                    encerradas.append(celdas_encerradas)
                elif valor_celda==valor_encerrar:
                    prospera=True
                    break
                else:
                    prospera=False
                    break
        return prospera
    def verificacion_prosperidad(self,codigo_organismo):
        filas_matriz, columnas_matriz=self.get_dimensiones()
        celdas_prospera=[]
        for fila in range(filas_matriz):
            for columna in range(columnas_matriz):   
                prospera=self.verificar_insercion(fila,columna,codigo_organismo)
                if prospera==True and self.buscar(fila,columna).valor=="":
                    celdasP=fila,columna
                    celdas_prospera.append(celdasP)
        return celdas_prospera

    def graficar(self):
        if self.filas.primero == None:
            return
        if self.columnas.primero == None:
            return

        file = open("Matriz.dot", "w")
        file.write("digraph G{\n")
        file.write("node [shape=plaintext];\n")
        file.write("rankdir=LR;\n")
        file.write("Matriz [\n")
        file.write("label=<<table border='0' cellborder='1' cellspacing='0'> \n")

        file.write("<tr>\n")
        file.write("<td></td>\n")

        actual = self.columnas.primero
        while actual != None:
            file.write("<td bgcolor=\"#DE0039\">" + str(actual.id) + "</td>\n")
            actual = actual.siguiente
        file.write("</tr>\n")

        actual = self.filas.primero
        while actual != None:
            file.write("<tr>\n")
            file.write("<td bgcolor=\"#0062DE\">" + str(actual.id) + "</td>\n")

            aux = actual.acceso
            actual_col = self.columnas.primero
            while actual_col != None:
                if aux != None and aux.col == actual_col.id:
                    if aux.valor == "":
                        file.write("<td bgcolor=\"white\"></td>\n")
                    else:
                        file.write("<td bgcolor=\"" + aux.valor + "\"></td>\n")
                    aux = aux.derecha
                else:
                    file.write("<td></td>\n")
                actual_col = actual_col.siguiente

            file.write("</tr>\n")
            actual = actual.siguiente

        file.write("</table>>];\n")
        file.write("}")
        file.close()
        os.system("dot -Tpng Matriz.dot -o Matriz.png")
