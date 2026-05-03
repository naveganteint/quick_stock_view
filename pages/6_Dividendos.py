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
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Dividendos</h1>',
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


#*********************************************** Dividendos *****************

h3_especial("Dividendos")

dividendos=ex.dividendos(df_flujo)
dividendos=[round (-x,2) for x in dividendos]



gr.grafica_columnas(años,dividendos,"Años","Dividendos","#E78D43")

variacion=ut.variacion_porcentual(dividendos)



ut.mostrar_tres_arrays_texto(años, dividendos,variacion ,"Dividendos","Variacion Dividendos")


cagr=rt.calcular_cagr(dividendos)
ut.mostrar_tabla_tres_celdas("CAGR", "Dividendos", cagr)







#*********************************************** Dividendos por accion *****************

h3_especial("Dividendos por accion")

dividendos=dividendos
acciones=ex.num_acciones(df_resultado)

dividendo_accion=ut.divide_listas(dividendos,acciones)

gr.grafica_columnas(años,dividendo_accion,"Años","Dividendos accion","#E73D12")


variacion=ut.variacion_porcentual(dividendo_accion)

ut.mostrar_tres_arrays_texto(años, dividendo_accion,variacion ,"Dividendos por accion","Variacion Div por accion")



cagr=rt.calcular_cagr(dividendo_accion)
ut.mostrar_tabla_tres_celdas("CAGR", "Dividendo accion", cagr)


#*********************************************** Pay out *****************

h3_especial("Dividendos por accion")

dividendos=dividendos
beneficio=ex.beneficio(df_resultado)
fcf=ex.FCF(años,df_flujo,0)
acciones=acciones

pay_out=ut.divide_listas(dividendos,beneficio)
pay_out=[round (x*100,0) for x in pay_out]
pay_out_fcf=ut.divide_listas(dividendos,fcf)
pay_out_fcf=[round (x*100,0) for x in pay_out_fcf]
lim_sup=10*[85]

gr.graficar_tres_lineas(pay_out, pay_out_fcf, lim_sup,"#F06616","#AA7EF0","#FF0000", eje_x=años, etiquetas=("Pay out beneficio neto","Pay out FCF","Limite recomendable"), eje_y="Margenes %")

ut.mostrar_tres_arrays_texto(años,pay_out,pay_out_fcf,"pay_out sobre beneficio", "pay_out sobre FCF")