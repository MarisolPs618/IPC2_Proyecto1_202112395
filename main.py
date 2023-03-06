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

menu="""
    Menú Principal
***********************
1. Carga de archivo
2. Manejo de muestras
3. Retornar XML
4. Salir
"""
menu2="""
    1. Graficar 
    2. Insertar organismo 
    3. Identificacion de prosperidad
    4. Estado de muestra
    5. Limpiar muestra?
    6. Regresar
    """


menu_principal=True
while menu_principal==True:
    print(menu)
    opcion_menuPrincipal=int(input("Seleccione una opcion: "))
    if opcion_menuPrincipal==1:
        print("CARGAR ARCHIVO")
         ## archivo=input("Ingrese la ruta del archivo: ")
        archivo='archivo.xml'
        ruta_archivo = archivo.replace('\u202a', '')
        ruta_archivo = r"{}".format(ruta_archivo)
        muestras=leer_archivo_xml(ruta_archivo)
    elif opcion_menuPrincipal==2:

        if muestras==[]:
           print("ERROR: No se localizó el archivo de entrada")
           continue

        ##codigo_muestra=input("Ingrese el codigo de la muestra a trabajar: ")
        codigo_muestra="A3"
        for muestra in muestras:
            if muestra.codigo == codigo_muestra:
                muestraActual=muestra
        matriz = Matriz()
        tamaño_filas=muestraActual.filas
        tamaño_columnas=muestraActual.columnas
        for fila in range(tamaño_filas+1):
            for columna in range(tamaño_columnas+1):
                matriz.insertar(fila, columna, "")
        for celda_viva in muestraActual.celdas_vivas:
            fila=int(celda_viva.fila)
            columna=int(celda_viva.columna)
            codigo=celda_viva.codigo_organismo
            nodo = matriz.buscar(fila,columna)
            nodo.valor = codigo
       

        menu_secundario=True
        while menu_secundario==True:
            print(menu2)
            opcion_Menu2=int(input("Seleccione una opcion: "))
            if opcion_Menu2==1:
                print("GRAFICAR")
                matriz.graficar()

            elif opcion_Menu2==2:
                print("INSERTAR ORGANISMO")
                codigo_insertar="#33FF44"
                # fila=int(input("ingrese fila: "))
                # columna=int(input("ingrese columna: "))
                matriz.insertar_organismo(5,5,"#33FF44")

                

            elif opcion_Menu2==3:
                print("IDENTIFICACION DE PROSPERIDAD")
            elif opcion_Menu2==4:
                print("ESTADO DE MUESTRA")
            elif opcion_Menu2==6:
                menu_secundario=False
                




    elif opcion_menuPrincipal==3:
        print("Devolver XML")
    else: 
        opcion_menuPrincipal=False
    
