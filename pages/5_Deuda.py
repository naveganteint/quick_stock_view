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
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Deuda</h1>',
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







#***********************************************Deuda neta- Ebitda *****************

h3_especial("Deuda neta - Ebitda")



deuda_neta= ex.deuda_neta(df_balance)


ebitda=ex.ebitda(df_resultado)


gr.graficar_2barras (deuda_neta, ebitda, 
                     color1="#B43838", color2="#52923E",
                     eje_x=años,
                     etiquetas=("deuda neta","ebitda"),
                     eje_y="Valores")



ratio=ut.divide_listas(deuda_neta,ebitda)


ut.mostrar_tabla_4_listas (años, deuda_neta, ebitda, ratio, "Deuda neta","Ebitda","Ratio Deuda neta/Ebitda")
gr.graficar_una_linea (ratio, "#B43838", eje_x=años, etiqueta="Ratio Deuda neta/Ebitda", eje_y="Ratio")



#***********************************************Deuda neta - cfo *****************

h3_especial("Deuda neta- Flujo de caja operativo")


fco=ex.FCO(df_flujo)
ratio=ut.divide_listas(deuda_neta,fco)


gr.graficar_2barras (deuda_neta, fco, 
                     color1="#B43838", color2="#C296C4",
                     eje_x=años,
                     etiquetas=("deuda","fco"),
                     eje_y="Valores")


ut.mostrar_tabla_4_listas (años, deuda_neta, fco, ratio, "Deuda neta","fco","Ratio Deuda neta/fco")
gr.graficar_una_linea (ratio, "#B43838", eje_x=años, etiqueta="Ratio Deuda/Ebitda", eje_y="Ratio")




#*********************************************** Deuda neta *****************

h3_especial("Deuda neta")

fila=ut.buscar_fila(df_balance, "Short-Term Debt")
try:
    current_debt=ut.fila_a_array (df_balance,fila+1)
except :
    current_debt= 10* [0]

current_debt=ut.limpiar_a_numeros(current_debt)



fila=ut.buscar_fila(df_balance, "Capital Leases (Current)")
try:
    current_lease=ut.fila_a_array (df_balance,fila+1)
except :   
    current_lease= 10* [0]

current_lease=ut.limpiar_a_numeros(current_lease)


fila=ut.buscar_fila(df_balance, "Long-Term Debt")
long_debt=ut.fila_a_array (df_balance,fila+1)
long_debt=ut.limpiar_a_numeros(long_debt)




long_lease=ex.long_lease(df_balance)



fila=ut.buscar_fila(df_balance, "Cash & Equivalents")
caja=ut.fila_a_array (df_balance,fila+1)
caja=ut.limpiar_a_numeros(caja)

cero = [0] * 10

#ut.mostrar_dos_arrays(años, current_debt)
#ut.mostrar_dos_arrays(años, current_lease)
#ut.mostrar_dos_arrays(años, long_debt)
#ut.mostrar_dos_arrays(años, long_lease)



deuda =ut.sumar_cinco_listas(current_debt, current_lease, long_debt, long_lease, cero)
deuda_neta = [
    (a if isinstance(a, (int, float)) else 0) -
    (b if isinstance(b, (int, float)) else 0)
    for a, b in zip(deuda, caja) ]



gr.graficar_tres_lineas(deuda, caja, deuda_neta,"pink","lightgreen","red", eje_x=años, etiquetas=("Deuda","Caja","Deuda_neta"), eje_y="Deuda neta")

ut.crear_tabla_4_listas(años, deuda, caja, deuda_neta, "Deuda","Caja","Deuda neta")

st.write("")


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


















#****************************************************** Coste de la deuda **********************************************
h3_especial(" Coste de la deuda")





try:
    coste_deuda= [
        round((a if isinstance(a, (int, float)) else 0) /
        (b if isinstance(b, (int, float)) else 0),4)
        for a, b in zip(intereses, deuda)
    ]
except:
    coste_deuda=10*[1]

coste_deuda = [round(100*x,2) if isinstance(x, (int, float)) else x for x in coste_deuda]

lim_sup= 10 * [6]
lim_inf= 10 * [4]
gr.graficar_tres_lineas(coste_deuda, lim_sup, lim_inf,"#3B3C42","coral","lightgreen", eje_x=años, etiquetas=("tipo interes medio deuda %","limite con riesgo","limite_sano"), eje_y="Coste de la deuda")

ut.crear_tabla_4_listas(años, intereses, deuda, coste_deuda, "Intereses","Deuda","Coste deuda %")
st.write("")
