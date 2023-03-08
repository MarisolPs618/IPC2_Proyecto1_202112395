import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from Muestras import muestra
from Muestras import celdasV
from matriz import Matriz



muestras = []
def leer_archivo_xml(nombre_archivo):
    # Parsear el archivo XML
    tree = ET.parse(nombre_archivo)
    root = tree.getroot()

    # Crear una lista de organismos
    organismos = {}
    i=0
    for organismo in root.find('listaOrganismos'):
        i=i+1
        codigo = organismo.find('codigo').text
        nombre = organismo.find('nombre').text
        organismos[i] = {'codigo': codigo, 'nombre': nombre, 'contador': i}

    # Crear una lista de muestras, cada una con su respectiva lista enlazada de celdas vivas

    for sample in root.findall('listadoMuestras/muestra'):
        codigo=str(sample.find('codigo').text)
        descripcion = str(sample.find('descripcion').text)
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
    return muestras,organismos

menu="""
    Menú Principal
***********************
1. Carga de archivo
2. Manejo de muestras
3. Retornar XML
4. Salir
***********************
"""
menu2="""
         MANEJO DE MUESTRAS
******************************************
    1. Graficar
    2. Insertar organismo
    3. Identificacion de prosperidad
    4. Estado de muestra
    5. Regresar
******************************************
    """


menu_principal=True
while menu_principal==True:
    print(menu)
    opcion_menuPrincipal=int(input("Seleccione una opcion: "))
    if opcion_menuPrincipal==1:
        print("CARGAR ARCHIVO")
        archivo=input("Ingrese la ruta del archivo: ")
        ruta_archivo = archivo.replace('\u202a', '')
        ruta_archivo = r"{}".format(ruta_archivo)
        muestras,organismos=leer_archivo_xml(ruta_archivo)

    elif opcion_menuPrincipal==2:

        if muestras==[]:
           print("ERROR: No se localizó el archivo de entrada")
           continue
        contador=0
        for muestra_recorrido in muestras:
            contador=contador+1
            print(str(contador)+". "+muestra_recorrido.codigo)

        muestra_trabajar=int(input("Ingrese el numero de la muestra a trabajar: "))
        codigo_muestra=muestras[muestra_trabajar-1].codigo

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
                for codigo, organismo in organismos.items():
                    print(str(organismo['contador'])+". "+f"Nombre: {organismo['nombre']} "+ f"Codigo: {organismo['codigo']}")
                numero_organismo=int(input("Ingrese el codigo del organismo a buscar: "))
                codigo_insertar=organismos[numero_organismo]['codigo']
                fila=int(input("ingrese fila: "))
                columna=int(input("ingrese columna: "))
                insertado = matriz.buscar(fila,columna)
                if insertado.valor==None:
                    print("Ya hay un organismo en esta celda")
                else:
                    prosperidad= matriz.insertar_organismo(fila, columna, codigo_insertar)
                    if prosperidad==False:
                        print("El organismo no puede prosperar")
                    else: 
                        print("prospera")
                        muestraActual.celdas_vivas.append(celdasV(fila, columna, codigo_insertar))
                

            elif opcion_Menu2==3:
                print("IDENTIFICACION DE PROSPERIDAD")
                print("********************************")
                print("LISTADO DE ORGANISMO")
                for codigo, organismo in organismos.items():
                    print(str(organismo['contador'])+". "+f"Nombre: {organismo['nombre']} "+ f"Codigo: {organismo['codigo']}")
                numero_organismo=int(input("Ingrese el codigo del organismo a buscar: "))
                codigo_organismo=organismos[numero_organismo]['codigo']
                celdas_prospera=matriz.verificacion_prosperidad(codigo_organismo)

                if celdas_prospera==[]:
                    print("No existen celdas donde el organismo pueda prosperar")
                else:
                    print("El organismo "+organismos[numero_organismo]['nombre']+" prospera en las siguientes celdas: ")
                    for celdas in celdas_prospera:
                        print(celdas)
                input()

            elif opcion_Menu2==4:

                print("ESTADO DE MUESTRA")
                for codigo, organismo in organismos.items():
                    print("El organismo "f"Nombre: {organismo['nombre']} "+ f"Codigo: {organismo['codigo']}")
                    codigo_organismo=organismo['codigo']
                    celdas_prosperar=matriz.verificacion_prosperidad(codigo_organismo)
                    if celdas_prosperar==[]:
                        print("No existen celdas donde el organismo pueda prosperar")
                    else:
                        print(" Prospera en las siguientes celdas: ")
                        for celdas in celdas_prosperar:
                            print(celdas)
                input()


            elif opcion_Menu2==5:
                menu_secundario=False
            else:
                print("Opcion invalida")

    elif opcion_menuPrincipal==3:
        print("Devolver XML")
        new_root = ET.Element("datosMarte")
        tree = ET.ElementTree(new_root)
        # Agregar los organismos al nuevo documento
        lista_organismos = ET.SubElement(new_root, "listaOrganismos")
        muestras[0].celdas_vivas[0].codigo_organismo = "#33FF44"  # Cambiar el código de la primera celda viva de la primera muestra
        for codigo, organismo in organismos.items():
            org = ET.SubElement(lista_organismos, "organismo")
            codigo = ET.SubElement(org, "codigo")
            codigo.text = organismo['codigo']
            nombre = ET.SubElement(org, "nombre")
            nombre.text = organismo['nombre']

        # Agregar las muestras al nuevo documento
        listado_muestras = ET.SubElement(new_root, "listadoMuestras")
        for muestra in muestras:
            m = ET.SubElement(listado_muestras, "muestra")
            ET.SubElement(m, "codigo").text = muestra.codigo
            ET.SubElement(m, "descripcion").text = muestra.descripcion
            ET.SubElement(m, "filas").text = str(muestra.filas)
            ET.SubElement(m, "columnas").text = str(muestra.columnas)
            listado_celdas_vivas = ET.SubElement(m, "listadoCeldasVivas")
            for celda_viva in muestra.celdas_vivas:
                cv = ET.SubElement(listado_celdas_vivas, "celdaViva")
                ET.SubElement(cv, "fila").text = str(celda_viva.fila)
                ET.SubElement(cv, "columna").text = str(celda_viva.columna)
                ET.SubElement(cv, "codigoOrganismo").text = str(celda_viva.codigo_organismo)
        xml_string = minidom.parseString(ET.tostring(new_root)).toprettyxml(indent="\t")
        with open("nuevo_archivo.xml", "w") as file:
            file.write(xml_string)

       



    elif opcion_menuPrincipal==4:
        menu_principal=False
    else:
        print("Opcion invalida")


