import streamlit as st

import analisis.ratios as rt
import utils.funciones as ut
import utils.graficas as gr

import pandas as pd
import analisis.fuente as ex
from styles.style_utils import aplicar_estilos, h3_especial,tabla_2,tabla_22,tabla_222



# Comprobar que la hoja "balance" está cargada
if "hojas" in st.session_state and "balance" in st.session_state.hojas:
    df_balance = st.session_state.hojas["balance"]

# Comprobar que la hoja "resultado" está cargada
if "hojas" in st.session_state and "resultado" in st.session_state.hojas:
    df_resultado = st.session_state.hojas["resultado"]


# Comprobar que la hoja "resultado" está cargada
if "hojas" in st.session_state and "flujo" in st.session_state.hojas:
    df_flujo = st.session_state.hojas["flujo"]



aplicar_estilos()




st.markdown(
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Valoraciones</h1>',
    unsafe_allow_html=True
)

años=df_resultado.columns.tolist()
años=ut.procesar_array (años)


#*************************************************************************************************************
#***************************************************** Intereses / Ebit ************************************
#*************************************************************************************************************


h3_especial("Ratio de cobertura( ebit/ intereses)")

ebit=ex.beneficio_operativo(df_resultado)
intereses=ex.intereses(df_resultado)
intereses= [round(-x,2) if isinstance(x, (int, float)) else x for x in intereses]




gr.graficar_2barras (ebit, intereses, 
                     color1="#43CF5A", color2="#EE6259",
                     eje_x=años,
                     etiquetas=("ebit","intereses"),
                     eje_y="Valores")


ratio_intereses_ebit=ut.divide_listas(intereses, ebit)
#ratio_intereses_ebit= [ round(100*x,2) if isinstance(x, (int, float)) else x for x in ratio_intereses_ebit]





ut.mostrar_tres_arrays (años,ebit,intereses,"ebit","intereses")
años=años[1:]





ratio_intereses_ebit = [
    f"{x*100:.2f} %" if isinstance(x, (int, float)) and x is not None else "-"
    for x in ratio_intereses_ebit
]


ut.mostrar_dos_arrays_texto (años,ratio_intereses_ebit,"% intereses/ebit")






#*****************************************************Patrimonio neto **********************************************

h3_especial("Patrimonio Neto")

fila=ut.buscar_fila(df_balance, "Shareholders' Equity")

patrimonio = ut.fila_a_array(df_balance, fila+1)
patrimonio = [float(x) for x in patrimonio]


gr.grafica_columnas(años,patrimonio,"Años","Patrimonio (m)","#DEB887")


ut.mostrar_dos_arrays_texto(años, patrimonio,"Patrimonio")

cagr=rt.calcular_cagr(patrimonio)
ut.mostrar_tabla_tres_celdas("CAGR", "Patrimonio", cagr)

st.write("")


#******************************************************Retained Earnings**********************************************

h3_especial("Retained Earnings")

fila=ut.buscar_fila(df_balance, "Retained Earnings")

retained = ut.fila_a_array(df_balance, fila+1)
retained = [float(x) for x in retained]


gr.grafica_columnas(años,retained,"Años","Retained Earnings (m)","#BDB76B")


ut.mostrar_dos_arrays_texto(años, retained ,"Retained earnings")

cagr=rt.calcular_cagr(retained)
ut.mostrar_tabla_tres_celdas("CAGR", "Retained earnings", cagr)



#****************************************************** Intagibles **********************************************

h3_especial("Intangibles")

goodwill=ex.goodwill(df_balance)
intangible=ex.intangibles(df_balance)
activos_intagibles=ut.suma_listas (goodwill,intangible)




activos=ex.activos(df_balance)
porcen_godwill= ut.divide_listas (goodwill,activos)
porcen_intangibles=ut.divide_listas (intangible,activos)
porcen_total_intagibles=ut.divide_listas(activos_intagibles,activos)

porcen_godwill = [round(x*100,2) for x in porcen_godwill]
porcen_intangibles = [round(x*100,2) for x in porcen_intangibles]
porcen_total_intagibles = [round(x*100,2) for x in porcen_total_intagibles]


gr.graficar_tres_lineas(porcen_godwill, porcen_intangibles, porcen_total_intagibles,"#7EC5E6", "#2F7392","#02354D", eje_x=años, etiquetas=("Goodwill", "Otros intangibles" , "Total intangibles"), eje_y=" intangibles/activos %")









