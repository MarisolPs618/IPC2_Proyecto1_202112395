import xml.etree.ElementTree as ET
from Lista import LinkedList
from Lista import Node
from Muestras import muestra
import graphviz


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
        celdas_vivas = LinkedList()
        for celda_viva in sample.findall('listadoCeldasVivas/celdaViva'):
            fila = int(celda_viva.find('fila').text)
            columna = int(celda_viva.find('columna').text)
            codigo_organismo = celda_viva.find('codigoOrganismo').text
            organismo = organismos[codigo_organismo]
            celdas_vivas.add_node((fila, columna, organismo))
        newMuestra=muestra(codigo, descripcion, filas, columnas, celdas_vivas)
        muestras.append(newMuestra)
    return muestras
    


muestras = leer_archivo_xml('archivo.xml')
codigo_muestra=input("Ingrese el codigo de la muestra: ")
for recorrido_muestra in muestras:
   if codigo_muestra==recorrido_muestra.codigo:
        muestraA_codigo=recorrido_muestra.codigo
        muestraA_descripcion=recorrido_muestra.descripcion
        muestraA_filas=recorrido_muestra.filas
        muestraA_columnas=recorrido_muestra.columnas
        muestraA_celdasVivas=recorrido_muestra.celdas_vivas

