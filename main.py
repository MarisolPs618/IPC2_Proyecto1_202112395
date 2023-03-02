import xml.etree.ElementTree as ET
from Muestras import muestra
from Muestras import celdasV
from matriz import Matriz



def leer_archivo_xml(nombre_archivo):
    # Parsear el archivo XML
    tree = ET.parse(nombre_archivo)
    root = tree.getroot()
    
    # Crear una lista de organismos
    organismos = {}
    for organismo in root.find('listaOrganismos'):
        codigo = organismo.find('codigo').text
        nombre = organismo.find('nombre').text
        organismos[codigo] = nombre
        
    # Crear una lista de muestras, cada una con su respectiva lista enlazada de celdas vivas
    muestras = []
 
    for sample in root.findall('listadoMuestras/muestra'):
        codigo=str(sample.find('codigo').text)
        descripcion = eval(sample.find('descripcion').text)
        filas = int(sample.find('filas').text)
        columnas = int(sample.find('columnas').text)
        celdas_vivas = []
        for celda_viva in sample.findall('listadoCeldasVivas/celdaViva'):
            fila = int(celda_viva.find('fila').text)
            columna = int(celda_viva.find('columna').text)
            codigo_organismo = celda_viva.find('codigoOrganismo').text
            celda_viva_ob = celdasV(fila, columna, codigo_organismo)
            celdas_vivas.append(celda_viva_ob)
        newMuestra=muestra(codigo, descripcion, filas, columnas, celdas_vivas)
        muestras.append(newMuestra)
    return muestras

muestras = leer_archivo_xml('archivo.xml')
codigo_muestra=input("Ingrese el codigo de la muestra: ")
matriz = Matriz()
for muestra in muestras:
    if muestra.codigo == codigo_muestra:
        tamaño_filas=muestra.filas
        tamaño_columnas=muestra.columnas
        for fila in range(tamaño_filas+1):
            for columna in range(tamaño_columnas+1):
                matriz.insertar(fila, columna, "")

        for celda_viva in muestra.celdas_vivas:
            fila=int(celda_viva.fila)
            columna=int(celda_viva.columna)
            codigo=celda_viva.codigo_organismo
            nodo = matriz.buscar(fila,columna)
            nodo.valor = codigo
                


matriz.graficar()