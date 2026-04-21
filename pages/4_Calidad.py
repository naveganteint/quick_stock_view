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


#*********************************************** Margenes *****************

h3_especial("Margenes")

ventas=ex.ventas(df_resultado)
beneficio_bruto=ex.beneficio_bruto(df_resultado)
beneficio_operativo=ex.beneficio_operativo(df_resultado)
beneficio_neto=ex.beneficio(df_resultado)

margen_bruto=ut.divide_listas (beneficio_bruto,ventas)
margen_operativo=ut.divide_listas(beneficio_operativo,ventas)
margen_neto=ut.divide_listas(beneficio_neto,ventas)

margen_bruto=[round (x*100,0) for x in margen_bruto]
margen_operativo=[round (x*100,0) for x in margen_operativo]
margen_neto=[round (x*100,0) for x in margen_neto]



gr.graficar_tres_lineas(margen_bruto, margen_operativo, margen_neto,"#0A44E6","#8A1717","#219E1C", eje_x=años, etiquetas=("Margen bruto","Margen operativo","Margen neto"), eje_y="Margenes %")


ut.mostrar_cuatro_arrays(años,margen_bruto,margen_operativo,margen_neto,"Margen bruto","Margen operativo","Margen neto")
años=años[1:]



#*********************************************** ROE Y ROIC *****************

h3_especial("ROE Y ROIC")

beneficio_neto=beneficio_neto
patrimonio=ex.patrimonio(df_balance)

roe=ut.divide_listas(beneficio_neto,patrimonio)


deuda_cp=ex.deuda_cp(df_balance)
deuda_lp=ex.deuda_lp(df_balance)
deuda=ut.suma_listas(deuda_cp,deuda_lp)
capital_invertido=ut.suma_listas(deuda,patrimonio)


beneficio_operativo=ex.beneficio_operativo(df_resultado)
beneficios_antes_impuestos=ex.pretax_income(df_resultado)
impuestos_sobre_beneficios=ex.income_tax(df_resultado)





tax_rate=rt.calculo_tasa(beneficios_antes_impuestos,impuestos_sobre_beneficios)


nopat=rt.calcular_nopat(beneficio_operativo, tax_rate)



roic=ut.divide_listas(nopat,capital_invertido)


linea15=10*[15]
roe=[round (x*100,0) for x in roe]
roic=[round (x*100,0) for x in roic]


gr.graficar_tres_lineas(roe,roic,linea15,"#8287CE","#C7D31A","#F74444", eje_x=años, etiquetas=("Roe","Roic","15%"), eje_y="Rentabilidad")