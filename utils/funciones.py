import numpy as np
import streamlit as st
import pandas as pd
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import re






#**************************************mostrar dos array con titulo

    
def mostrar_dos_arrays_texto(lista1, lista2 ,texto):
        # Validar longitudes
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud")

    # Crear encabezado (años)
    columnas = ["años"] + lista1

    # Crear fila de datos
    fila = [texto] + lista2

    # Crear DataFrame
    df = pd.DataFrame([fila], columns=columnas)
    
    # Convertir DataFrame a HTML
    html_table = df.to_html(index=False, header=True,table_id="tabla_2lista",escape=False,)
    
    css ="""
    <style>
    table.dataframe#tabla_2lista {
      
        width: auto;            /* ancho automático según contenido */
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto;     /* centra la tabla */
}

  

    table.dataframe#tabla_2lista tbody tr{
        background-color: white;
        text-align: center;
        padding: 2px;
    }

    
    table#tabla_2lista thead th {
        background-color: #D9E6E7;   
        text-align: center;
        padding: 1px;
    }
    






    /* Opcional: bordes de celdas */
    table.dataframe td {
        border: 1px solid #ccc;
    }
    </style>
    """
    

  
    
    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)


#******************************************************procesar array**************************************

def procesar_array(arr):
    """
    Toma un array o lista, elimina los dos primeros elementos
    y luego invierte el orden del resto.
    
    Parámetros:
    - arr: lista o array
    
    Retorna:
    - array procesado
    """
    if arr is None or len(arr) <= 2:
        return []  # No hay suficientes elementos
    
    # Eliminar los dos primeros elementos y voltear el resto
    arr_procesado = arr[2:][::-1]
    
    return arr_procesado



#******************************************************* buscar filar en df ********************************

def buscar_fila(df, texto):
    """
    Busca una cadena en la primera columna de un DataFrame
    y devuelve el número de la fila donde aparece.
    """
    
    col = df.iloc[:, 0]  # primera columna
    
    filas = col[col == texto].index
    
    if len(filas) > 0:
        return filas[0]   # devuelve la primera coincidencia
    else:
        return None






#****************************************** limpiar lista a solo numeros ***************************

def limpiar_a_numeros(lista):
    """
    Convierte los elementos de una lista a número.
    Si no se pueden convertir, los reemplaza por 0.
    """
    resultado = []

    for x in lista:
        try:
            num = int(x)
            resultado.append(num)
        except (ValueError, TypeError):
            resultado.append(0)

    return resultado


#***************************fila a array *******************************

def fila_a_array(df, numero_fila, humana=True):
    """
    Devuelve la fila indicada como array de numpy, eliminando los dos primeros elementos
    y reordenando el resto en orden invertido (primero → último, segundo → penúltimo, ...).

    Parámetros:
    - df : DataFrame
    - numero_fila : número de fila
    - humana=True → la fila empieza en 1
      humana=False → la fila empieza en 0
    """
    try:
        # Seleccionar fila
        if humana:
            fila = df.iloc[numero_fila - 1]
        else:
            fila = df.iloc[numero_fila]

        # Convertir a array numpy
        arr = fila.to_numpy()

        # 1️⃣ eliminar los dos primeros elementos
        arr = arr[2:]

        # 2️⃣ invertir el orden de los elementos restantes
        arr = arr[::-1]

        return arr

    except IndexError:
        return None
    




#**************************************mostrar tres array con titulo

    
def mostrar_tres_arrays_texto(lista1, lista2, lista3, texto1, texto2):
    # Validar longitudes
    if len(lista1) != len(lista2) or len(lista1) != len(lista3):
        raise ValueError("Todas las listas deben tener la misma longitud")

    # Columnas (años)
    columnas = ["años"] + lista1

    # Filas
    fila1 = [texto1] + lista2
    fila2 = [texto2] + lista3

    # DataFrame con DOS filas
    df = pd.DataFrame([fila1, fila2], columns=columnas)
    
    # Convertir DataFrame a HTML
    html_table = df.to_html(index=False, header=True,table_id="tabla_2lista",escape=False,)
    
    css ="""
    <style>
    table.dataframe#tabla_2lista {
      
        width: auto;            /* ancho automático según contenido */
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto;     /* centra la tabla */
}

  

    table.dataframe#tabla_2lista tbody tr{
        background-color: white;
        text-align: center;
        padding: 2px;
    }

    
    table#tabla_2lista thead th {
        background-color: #D9E6E7;   
        text-align: center;
        padding: 1px;
    }
    






    /* Opcional: bordes de celdas */
    table.dataframe td {
        border: 1px solid #ccc;
    }
    </style>
    """
    

  
    
    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)




    #*********************************************suma listas ******************

def suma_listas (lista1,lista2):
    
    lista3=[(a if isinstance(a, (int, float)) else 0) +
    (b if isinstance(b, (int, float)) else 0)
    for a, b in zip(lista1, lista2) ]

    return lista3

#*********************************************resta listas ******************

def resta_listas (lista1,lista2):
    
    lista3=[(a if isinstance(a, (int, float)) else 0) -
    (b if isinstance(b, (int, float)) else 0)
    for a, b in zip(lista1, lista2) ]
    return lista3


#*********************************************dividir listas ******************

def divide_listas (lista1,lista2):
    
    try:
        lista3=[ round((a if isinstance(a, (int, float)) else 0) /
        (b if isinstance(b, (int, float)) else 0),2)
        for a, b in zip(lista1, lista2) ]
    except:
        lista3= 10 * [1]  

    return lista3

#******************************************mostrar tabla 4 listas *****************************************

def mostrar_tabla_4_listas(lista1, lista2, lista3, lista4, texto1, texto2, texto3):
        """
        Crea una tabla de 4 filas:
        
        - Fila 1: "años" + lista1
        - Fila 2: texto1 + lista2
        - Fila 3: texto2 + lista3
        - Fila 4: texto3 + lista4
        """

        # Validar longitudes
        n = len(lista1)
        if not (len(lista2) == len(lista3) == len(lista4) == n):
            raise ValueError("Todas las listas deben tener la misma longitud")



        # Crear DataFrame
        df = pd.DataFrame(
            [lista2, lista3, lista4],
            columns=lista1  # 👈 los años como columnas
        )

        # Añadir primera columna con etiquetas
        df.insert(0, "años", [texto1, texto2, texto3])

      

        # Convertir DataFrame a HTML
        html_table = df.to_html(index=False, header=True,table_id="tabla_2lista",escape=False,)
        
        css ="""
        <style>
        table.dataframe#tabla_2lista {
        
            width: auto;            /* ancho automático según contenido */
            border-collapse: collapse;
            margin-left: auto;
            margin-right: auto;     /* centra la tabla */
        }
    
        table.dataframe#tabla_2lista tbody tr{
           
            text-align: center;
  
        }

      
        table#tabla_2lista thead th {
            background-color: #D9E6E7;   
            text-align: center;
    
        }
        



        /* Opcional: bordes de celdas */
        table.dataframe td {
            border: 1px solid #ccc;
        }


        table#tabla_2lista tbody tr:nth-child(3) {
        background-color: #E7D6FC !important;
        }
        table.dataframe#tabla_2lista tbody td:first-child {
            font-weight: bold;
        }
        
        table#tabla_2lista td {
        line-height: 1.2; /* más compacto */

        </style>




        """
        

    
        
        # Mostrar CSS y tabla
        st.markdown(css, unsafe_allow_html=True)
        st.markdown(html_table, unsafe_allow_html=True)


        

#************************** convertir a numero B o M ************************************************************


def convertir_a_numero(lista):
    """
    Convierte valores tipo '1.7B', '500M', etc. a números reales.
    B = miles de millones
    M = millones
    """
    
    resultado = []

    for x in lista:
        if isinstance(x, str):

            if x.endswith("B"):
                valor = float(x[:-1]) * 1_000

            elif x.endswith("M"):
                valor = float(x[:-1]) * 1

            else:
                valor = float(x)

        else:
            valor = x

        resultado.append(valor)

    return resultado

#************************************************************************



def mostrar_tabla_tres_celdas(texto1, texto2,valor):
        # Validar longitudes



    # Crear fila de datos
    fila = [texto1] + [texto2] + [valor]

    # Crear DataFrame
    df = pd.DataFrame([fila])
    
    # Convertir DataFrame a HTML
    html_table = df.to_html(index=False, header=False,table_id="tabla_2lista",escape=False,)
    
    css ="""
    <style>
    table.dataframe#tabla_2lista {
      
        width: auto;            /* ancho automático según contenido */
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto;     /* centra la tabla */
}

  

    table.dataframe#tabla_2lista tbody tr{
        background-color: white;
        text-align: center;
        padding: 2px;
    }

    
    table#tabla_2lista thead th {
        background-color: #D9E6E7;   
        text-align: center;
        padding: 1px;
    }
    






    /* Opcional: bordes de celdas */
    table.dataframe td {
        border: 1px solid #ccc;
    }
    </style>
    """
    

  
    
    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)





#******************************mostrar cuatro arrays ***********************************

def mostrar_cuatro_arrays(arr1, arr2, arr3, arr4,texto1,texto2,texto3):
    """
    Muestra una tabla en Streamlit con 4 listas:
    - arr1: encabezado de la tabla
    - arr2, arr3, arr4: filas de datos
    Las celdas están centradas y no se colorean los valores.
    
    Parámetros:
    - arr1: lista de nombres de columnas
    - arr2, arr3, arr4: listas de datos (misma longitud que arr1)
    """
    # Convertir a listas normales si son NumPy arrays
    for i, arr in enumerate([arr1, arr2, arr3, arr4]):
        if isinstance(arr, np.ndarray):
            if i == 0:
                arr1 = arr.tolist()
            elif i == 1:
                arr2 = arr.tolist()
            elif i == 2:
                arr3 = arr.tolist()
            elif i == 3:
                arr4 = arr.tolist()

    # Verificar que todas las listas tengan la misma longitud
    n = len(arr1)
    if not all(len(lst) == n for lst in [arr2, arr3, arr4]):
        st.error("Todas las listas deben tener la misma longitud que el encabezado")
        return

    datos1=[]
    datos2=[]
    datos3=[]    


    def cambia_celda (lista,datos):
        for x in lista:
                
                if pd.isna(x):
                    datos.append("-")
                
                elif x < 0:
                    datos.append(f'<span style="color:red;">{x}</span>')
                
            
                else:
                    datos.append(f"{x}")

    




    cambia_celda(arr2,datos1)
    cambia_celda(arr3,datos2)
    cambia_celda(arr4,datos3)
    

    arr1.insert(0, "Años")
    datos1.insert(0, texto1)
    datos2.insert(0, texto2)
    datos3.insert(0, texto3)

    # Crear DataFrame con arr1 como columnas y arr2, arr3, arr4 como filas
    df = pd.DataFrame([datos1, datos2, datos3], columns=arr1)

    # Convertir DataFrame a HTML
    html_table = df.to_html(index=False, header=True, table_id="tabla_4listas", escape=False)

    # CSS para centrar celdas y encabezado
    css = """
    <style>
    table.dataframe#tabla_4listas {
        width: auto;
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto; /* centra la tabla */
    }

    table.dataframe#tabla_4listas tbody tr{
        background-color: white;
        text-align: center;
        padding: 4px;
    }

    table#tabla_4listas thead th {
        background-color: #D9E6E7;
        text-align: center;
        padding: 4px;
    }

    table.dataframe#tabla_4listas td {
        border: 1px solid #ccc;
    }
    </style>
    """

    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)





#******************************mostrar tres arrays ***********************************

def mostrar_tres_arrays(arr1, arr2, arr3,texto1,texto2):
    """
    Muestra una tabla en Streamlit con 4 listas:
    - arr1: encabezado de la tabla
    - arr2, arr3, arr4: filas de datos
    Las celdas están centradas y no se colorean los valores.
    
    Parámetros:
    - arr1: lista de nombres de columnas
    - arr2, arr3, arr4: listas de datos (misma longitud que arr1)
    """
    # Convertir a listas normales si son NumPy arrays
    for i, arr in enumerate([arr1, arr2, arr3]):
        if isinstance(arr, np.ndarray):
            if i == 0:
                arr1 = arr.tolist()
            elif i == 1:
                arr2 = arr.tolist()
            elif i == 2:
                arr3 = arr.tolist()
            elif i == 3:
                arr4 = arr.tolist()

    # Verificar que todas las listas tengan la misma longitud
    n = len(arr1)
    if not all(len(lst) == n for lst in [arr2, arr3]):
        st.error("Todas las listas deben tener la misma longitud que el encabezado")
        return

    datos1=[]
    datos2=[]
      


    def cambia_celda (lista,datos):
        for x in lista:
                
                if pd.isna(x):
                    datos.append("-")
                
                elif x < 0:
                    datos.append(f'<span style="color:red;">{x}</span>')
                
            
                else:
                    datos.append(f"{x}")

    




    cambia_celda(arr2,datos1)
    cambia_celda(arr3,datos2)

    

    arr1.insert(0, "Años")
    datos1.insert(0, texto1)
    datos2.insert(0, texto2)


    # Crear DataFrame con arr1 como columnas y arr2, arr3 como filas
    df = pd.DataFrame([datos1, datos2], columns=arr1)

    # Convertir DataFrame a HTML
    html_table = df.to_html(index=False, header=True, table_id="tabla_4listas", escape=False)

    # CSS para centrar celdas y encabezado
    css = """
    <style>
    table.dataframe#tabla_4listas {
        width: auto;
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto; /* centra la tabla */
    }

    table.dataframe#tabla_4listas tbody tr{
        background-color: white;
        text-align: center;
        padding: 4px;
    }

    table#tabla_4listas thead th {
        background-color: #D9E6E7;
        text-align: center;
        padding: 4px;
    }

    table.dataframe#tabla_4listas td {
        border: 1px solid #ccc;
    }
    </style>
    """

    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)


# variacion lista
def variacion_porcentual(lista):
    resultado = ["-"]  # primer elemento

    for i in range(1, len(lista)):
        anterior = lista[i-1]
        actual = lista[i]

        if (
            isinstance(anterior, (int, float)) and
            isinstance(actual, (int, float)) and
            anterior != 0
        ):
            variacion = (actual - anterior) / anterior
            resultado.append(f"{variacion*100:.2f} %")
        else:
            resultado.append("-")

    return resultado



#################################crear tabla 5 listas *********************************


def crear_tabla_5_listas(lista1, lista2, lista3, lista4,lista5, texto1, texto2, texto3,texto4):
        """
        Crea una tabla de 4 filas:
        
        - Fila 1: "años" + lista1
        - Fila 2: texto1 + lista2
        - Fila 3: texto2 + lista3
        - Fila 4: texto3 + lista4
        """

        # Validar longitudes
        n = len(lista1)
        if not (len(lista2) == len(lista3) == len(lista4) == len (lista5) ):
            raise ValueError("Todas las listas deben tener la misma longitud")



        # Crear DataFrame
        df = pd.DataFrame(
            [lista2, lista3, lista4,lista5],
            columns=lista1  # 👈 los años como columnas
        )

        # Añadir primera columna con etiquetas
        df.insert(0, "años", [texto1, texto2, texto3,texto4])

      

        # Convertir DataFrame a HTML
        html_table = df.to_html(index=False, header=True,table_id="tabla_5lista",escape=False,)
        
        css ="""
        <style>
        table.dataframe#tabla_5lista {
        
            width: auto;            /* ancho automático según contenido */
            border-collapse: collapse;
            margin-left: auto;
            margin-right: auto;     /* centra la tabla */
        }
    
        table.dataframe#tabla_5lista tbody tr{
           
            text-align: center;
  
        }

      
        table#tabla_5lista thead th {
            background-color: #D9E6E7;   
            text-align: center;
    
        }
        



        /* Opcional: bordes de celdas */
        table.dataframe td {
            border: 1px solid #ccc;
        }

        table.dataframe#tabla_5lista tbody tr:nth-child(4) td {
        background-color: #E7D6FC !important;
        }

        table.dataframe#tabla_5lista tbody td:first-child {
            font-weight: bold;
        }
        
        table#tabla_5lista td {
        line-height: 1.2; /* más compacto */

        </style>




        """
        

    
        
        # Mostrar CSS y tabla
        st.markdown(css, unsafe_allow_html=True)
        st.markdown(html_table, unsafe_allow_html=True)    



