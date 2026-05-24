import streamlit as st

import analisis.ratios as rt
import utils.funciones as ut
import utils.graficas as gr

import pandas as pd
import analisis.fuente as ex
from styles.style_utils import aplicar_estilos, h3_especial


st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)




aplicar_estilos()



st.markdown(
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Datos Financieros</h1>',
    unsafe_allow_html=True
)

# Comprobar que la hoja "resultado" está cargada


# Comprobar que la hoja "balance" está cargada
if "hojas" in st.session_state and "balance" in st.session_state.hojas:
    df_balance = st.session_state.hojas["balance"]

# Comprobar que la hoja "resultado" está cargada
if "hojas" in st.session_state and "resultado" in st.session_state.hojas:
    df_resultado = st.session_state.hojas["resultado"]


# Comprobar que la hoja "resultado" está cargada
if "hojas" in st.session_state and "flujo" in st.session_state.hojas:
    df_flujo = st.session_state.hojas["flujo"]


años=df_resultado.columns.tolist()
años=ut.procesar_array (años)


#***********************************************Ventas - Beneficio *****************

h3_especial("Ventas - Beneficio neto")


ventas = ex.ventas(df_resultado)
beneficio=ex.beneficio(df_resultado)

margen_neto=ut.divide_listas(beneficio,ventas)
margen_neto= [round(100*x,2) for x in margen_neto]
margen_neto_texto = [f"{x} %" for x in margen_neto]

gr.graficar_2barras (ventas, beneficio, 
                     color1="#4AB0F0", color2="#F59556",
                     eje_x=años,
                     etiquetas=("ventas","beneficio"),
                     eje_y="Valores")

ut.mostrar_tabla_4_listas(años,ventas,beneficio,margen_neto_texto,"Ventas","Beneficio","Margen neto %")



gr.grafica_columnas(años,ventas,"Años","Ventas","#4AB0F0")
cagr=rt.calcular_cagr(ventas)
ut.mostrar_tabla_tres_celdas("CAGR", "Ventas", cagr)


gr.grafica_columnas(años,beneficio,"Años","Beneficio","#F59556")
cagr=rt.calcular_cagr(beneficio)
ut.mostrar_tabla_tres_celdas("CAGR", "Beneficio", cagr)


st.write("")





#***********************************************FCF *****************

h3_especial("Free cash Flow")


fcf=ex.FCF(años,df_flujo,0)
gr.grafica_columnas(años,fcf,"Años","FCF","#628585")

ut.mostrar_dos_arrays_texto (años,fcf,"Free Cash Flow")




#*********************************************** Recompras *****************

h3_especial("Recompras")
recompras=ex.recompras(df_flujo)



gr.grafica_columnas(años,recompras,"Años","Recompras","#86B18E")

ut.mostrar_dos_arrays_texto (años,recompras,"Recompras")


acciones=ex.num_acciones(df_resultado)

st.write("")
gr.graficar_una_linea (acciones, '#20B2AA', eje_x=años, etiqueta="numº de acciones", eje_y="Billones")



ut.mostrar_dos_arrays_texto (años,acciones,"Numº de acciones")
cagr=rt.calcular_cagr(acciones)
ut.mostrar_tabla_tres_celdas("CAGR", "Acciones", cagr)


