import numpy as np
import streamlit as st
import pandas as pd
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import re



######################################################### grafica de dos barras ************************************************

def graficar_2barras(lista1, lista2, 
                     color1="blue", color2="orange",
                     eje_x=None,
                     etiquetas=None,
                     eje_y="Valores"):

    # Validar longitud
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud")

    n = len(lista1)

    # Eje X
    if eje_x is None:
        eje_x = list(range(n))

    if len(eje_x) != n:
        raise ValueError("El eje X debe tener la misma longitud")

    # Etiquetas
    if etiquetas is None:
        etiquetas = ["Serie 1", "Serie 2"]

    # Crear figura
    fig, ax = plt.subplots(figsize=(7, 4))

    x = range(n)
    width = 0.35

    # Barras
    ax.bar([i - width/2 for i in x], lista1,
           width=width, label=etiquetas[0], color=color1)

    ax.bar([i + width/2 for i in x], lista2,
           width=width, label=etiquetas[1], color=color2)

    # Eje X
    ax.set_xticks(list(x))
    ax.set_xticklabels(eje_x)

    # Estilo limpio
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Etiquetas
    ax.set_xlabel("Años", fontsize=12, color='gray')
    ax.set_ylabel(eje_y, fontsize=12, color='gray')

    # Grid
    ax.yaxis.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)
    ax.axhline(y=0, linewidth=1)
    ax.set_axisbelow(True)

    # Leyenda (corregida)
    ax.legend()

    plt.tight_layout()

    # Exportar a imagen
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)

    img_base64 = base64.b64encode(buf.read()).decode()

    # Mostrar en Streamlit
    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <img src="data:image/png;base64,{img_base64}" width="700px">
    </div>
    """, unsafe_allow_html=True)




    #**************************graficar una linea ********************************************


def graficar_una_linea (lista, color, eje_x=None, etiqueta="Línea", eje_y="Valores"):
        """
        Genera una gráfica de una sola línea con Matplotlib y la muestra en Streamlit.
        
        Parámetros:
        - lista: lista de valores numéricos
        - eje_x: lista de valores para el eje X (por ejemplo años). Por defecto 1..n
        - etiqueta: nombre de la línea
        - eje_y: nombre del eje Y
        """

        n = len(lista)

        # Eje X por defecto
        if eje_x is None:
            eje_x = list(range(1, n+1))

        if len(eje_x) != n:
            raise ValueError("La lista del eje X debe tener la misma longitud que la lista de valores")

        # Crear figura
        fig, ax = plt.subplots(figsize=(7,4))

        # Graficar línea
        ax.plot(eje_x, lista, label=etiqueta, color=color)

        # Eliminar bordes
        for spine in ax.spines.values():
            spine.set_visible(False)

        # Etiquetas
        ax.set_xlabel("Año" if eje_x else "Índice", fontsize=12, color='gray')
        ax.set_ylabel(eje_y, fontsize=12, color='gray')

        ax.tick_params(axis='x', colors='gray', length=5, width=1)
        ax.tick_params(axis='y', colors='gray', length=5, width=1)

        # Leyenda y grid
        ax.legend()
        ax.yaxis.grid(True, color='gray', linestyle='-', linewidth=1)
        ax.axhline(y=0, color='black', linewidth=2, linestyle='-')

        plt.tight_layout()

        # Guardar figura
        buf = BytesIO()
        fig.savefig(buf, format="png", bbox_inches='tight')
        buf.seek(0)

        img_base64 = base64.b64encode(buf.read()).decode()

        # Mostrar centrada en Streamlit
        st.markdown(f"""
        <div style="display:flex; justify-content:center;">
            <img src="data:image/png;base64,{img_base64}" width="700px">
        </div>
        """, unsafe_allow_html=True)




        #Funcion para introducir una grafica de barras*********************************************************************************


def grafica_columnas(arr1, arr2,eje_x,eje_y,color_barras):
    

    df = pd.DataFrame({'x':arr1, 'y':arr2})

    # Crear figura Matplotlib
    fig, ax = plt.subplots(figsize=(7,4))  # tamaño relativo
    ax.bar(df['x'], df['y'], color=color_barras)
    ax.set_xlabel(eje_x,color='gray',fontsize=12, labelpad=15)
    ax.set_ylabel(eje_y,color='gray',fontsize=12, labelpad=15)
    #ax.set_title('Gráfico de Barras con Matplotlib')
    ax.set_xticks(df['x'])

    ax.tick_params(axis='x', colors='gray', length=5, width=1)  # ticks eje X
    ax.tick_params(axis='y', colors='gray', length=5, width=1)  # ticks eje Y

    # Líneas horizontales de fondo (gridlines)
    ax.yaxis.grid(True, color='gray', linestyle='-', linewidth=1)  # gris claro y punteado
    ax.set_axisbelow(True)  # asegura que las líneas queden debajo de las barras


    # Eliminar todos los spines (bordes de la gráfica)
    for spine in ax.spines.values():
        spine.set_visible(False)


    # Guardar figura en buffer
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')  # bbox_inches evita recorte de etiquetas
    buf.seek(0)

    # Convertir a base64 para incrustar en HTML
    img_base64 = base64.b64encode(buf.read()).decode()

    # HTML para centrar imagen con ancho fijo de 700px
    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <img src="data:image/png;base64,{img_base64}" width="700px">
    </div>
    """, unsafe_allow_html=True)








    #************************ graficar tres lineas ***********************************

def graficar_tres_lineas(lista1, lista2, lista3,color1,color2,color3, eje_x=None, etiquetas=None, eje_y="margenes %"):
        """
        Genera una gráfica de líneas con tres listas de valores usando Matplotlib y la muestra en Streamlit.
        
        Parámetros:
        - lista1, lista2, lista3: listas de valores numéricos (misma longitud)
        - eje_x: lista de valores para el eje X (por ejemplo años). Por defecto 1..n
        - etiquetas: lista de 3 strings para la leyenda de cada línea (opcional)
        - titulo: título de la gráfica
        - eje_y: nombre del eje Y (por defecto "Valores")
        """
        # Validar longitud
        n = len(lista1)
        if len(lista2) != n or len(lista3) != n:
            raise ValueError("Todas las listas deben tener la misma longitud")
        
        # Eje X por defecto
        if eje_x is None:
            eje_x = list(range(1, n+1))
        
        if len(eje_x) != n:
            raise ValueError("La lista del eje X debe tener la misma longitud que las listas de valores")
        
        # Etiquetas por defecto
        if etiquetas is None:
            etiquetas = ["Línea 1", "Línea 2", "Línea 3"]
        
        # Crear figura
        fig, ax = plt.subplots(figsize=(7,4))                             
        
        # Graficar líneas
        ax.plot(eje_x, lista1,  label=etiquetas[0], color=color1)
        ax.plot(eje_x, lista2,  label=etiquetas[1], color=color2)
        ax.plot(eje_x, lista3,  label=etiquetas[2], color=color3)
        

        # Eliminar todos los spines (bordes de la gráfica)
        for spine in ax.spines.values():
            spine.set_visible(False)


        # Títulos y etiquetas
        #ax.set_title(titulo, fontsize=14)
        ax.set_xlabel("Año" if eje_x else "Índice", fontsize=12, color='gray')
        ax.set_ylabel(eje_y, fontsize=12, color='gray')

        
        ax.tick_params(axis='x', colors='gray', length=5, width=1)  # ticks eje X
        ax.tick_params(axis='y', colors='gray', length=5, width=1)  # ticks eje Y

        
        # Leyenda y cuadrícula
        ax.legend()
     
        
        ax.yaxis.grid(True, color='gray', linestyle='-', linewidth=1)  # gris claro y punteado
        ax.axhline(y=0, color='black', linewidth=2, linestyle='-')

        plt.tight_layout()
        
        
        # Guardar figura en buffer
        buf = BytesIO()
        fig.savefig(buf, format="png", bbox_inches='tight')  # bbox_inches evita recorte de etiquetas
        buf.seek(0)

        # Convertir a base64 para incrustar en HTML
        img_base64 = base64.b64encode(buf.read()).decode()

        # HTML para centrar imagen con ancho fijo de 700px
        st.markdown(f"""
        <div style="display:flex; justify-content:center;">
            <img src="data:image/png;base64,{img_base64}" width="700px">
        </div>
        """, unsafe_allow_html=True)





######################################################### grafica N barras ************************************************


def graficar_n_barras(listas, 
                     colores=None,
                     eje_x=None,
                     etiquetas=None,
                     eje_y="Valores"):

    n_series = len(listas)   # número de barras (ej: 9)
    n = len(listas[0])       # número de categorías

    # Validar que todas las listas tengan la misma longitud
    for lista in listas:
        if len(lista) != n:
            raise ValueError("Todas las listas deben tener la misma longitud")

    # Eje X
    if eje_x is None:
        eje_x = list(range(n))

    if len(eje_x) != n:
        raise ValueError("El eje X debe tener la misma longitud")

    # Etiquetas
    if etiquetas is None:
        etiquetas = [f"Serie {i+1}" for i in range(n_series)]

    # Colores
    if colores is None:
        colores = plt.cm.tab10.colors[:n_series]

    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 5))

    x = list(range(n))
    width = 0.8 / n_series   # 👈 clave: repartir espacio

    # Dibujar barras
    for i, lista in enumerate(listas):
        desplazamiento = (i - n_series/2) * width + width/2

        ax.bar([xi + desplazamiento for xi in x],
               lista,
               width=width,
               label=etiquetas[i],
               color=colores[i])

    # Eje X
    ax.set_xticks(x)
    ax.set_xticklabels(eje_x)
    ax.set_axisbelow(True)

    # Estilo
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel("Año", fontsize=12, color='gray')
    ax.set_ylabel(eje_y, fontsize=12, color='gray')

    ax.yaxis.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)
    ax.axhline(y=0, linewidth=1)

    ax.legend(ncol=3)  # 👈 útil cuando hay muchas series

    plt.tight_layout()

    # Exportar a imagen
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)

    img_base64 = base64.b64encode(buf.read()).decode()

    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <img src="data:image/png;base64,{img_base64}" width="900px">
    </div>
    """, unsafe_allow_html=True) 









#··········································graficas de barras 1+ 2 en 1 y con linea



def graficar_barras_apiladas_y_linea(lista1, lista2, lista3, lista4,
                                    color1, color2, color3, color4,
                                    eje_x=None,
                                    etiquetas=None,
                                    eje_y_izq="Valores",
                                    eje_y_der="Ratio (%)"):

    # Validar longitud
    n = len(lista1)
    if not (len(lista2) == len(lista3) == len(lista4) == n):
        raise ValueError("Todas las listas deben tener la misma longitud")

    # Eje X
    if eje_x is None:
        eje_x = list(range(n))

    if len(eje_x) != n:
        raise ValueError("El eje X debe tener la misma longitud")

    # Etiquetas
    if etiquetas is None:
        etiquetas = ["Barra 1", "Parte 1", "Parte 2", "Línea"]

    # Figura
    fig, ax = plt.subplots(figsize=(7,4))

    x = range(n)
    width = 0.35

    # 🔵 Barra individual (izquierda)
    ax.bar([i - width/2 for i in x], lista1,
           width=width, label=etiquetas[0], color=color1)

    # 🟢 Barras apiladas (derecha)
    ax.bar([i + width/2 for i in x], lista2,
           width=width, label=etiquetas[1], color=color2)

    ax.bar([i + width/2 for i in x], lista3,
           width=width, bottom=lista2,
           label=etiquetas[2], color=color3)

    # 🔴 Línea (eje secundario)
    ax2 = ax.twinx()
    ax2.plot(x, lista4,
             label=etiquetas[3],
             color=color4,
             marker='o',
             linewidth=2)

    # Eje X
    ax.set_xticks(x)
    ax.set_xticklabels(eje_x)

    # Estilo
    for spine in ax.spines.values():
        spine.set_visible(False)
    for spine in ax2.spines.values():
        spine.set_visible(False)

    ax.set_xlabel("Año", fontsize=12, color='gray')
    ax.set_ylabel(eje_y_izq, fontsize=12, color='gray')
    ax2.set_ylabel(eje_y_der, fontsize=12, color='gray')

    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')
    ax2.tick_params(axis='y', colors='gray')

    ax.yaxis.grid(True, color='gray', linestyle='-', linewidth=1)
    ax.axhline(y=0, color='black', linewidth=2)
    ax.set_axisbelow(True)

    # 🔥 Leyenda combinada
    lines_1, labels_1 = ax.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax.legend(lines_1 + lines_2, labels_1 + labels_2)

    plt.tight_layout()

    # Exportar
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)

    img_base64 = base64.b64encode(buf.read()).decode()

    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <img src="data:image/png;base64,{img_base64}" width="700px">
    </div>
    """, unsafe_allow_html=True)



    

