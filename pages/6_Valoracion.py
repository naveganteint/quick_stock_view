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
#***************************************************** Ratio deuda ebitda ************************************
#*************************************************************************************************************




#***************************************************** cotizacion *******************s**************************
#***************************************************************************************************************


h3_especial("Cotizacion accion")

st.markdown("""
<style>
div[data-testid="stNumberInput"] {
    max-width: 300px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

precio_accion = st.number_input("Introduce la Cotización:", value=50.0)





#***************************************************** EV/ebitda*********************************************
#***************************************************************************************************************


h3_especial("EV/ebitda")
st.write("")



#***************************************************** acciones*********************************************


fila=ut.buscar_fila(df_resultado, "Shares (Diluted)")
num_acciones=ut.fila_a_array (df_resultado,fila+1)
num_acciones_num=rt.convertir_a_numero(num_acciones)


valor_num_acciones=num_acciones_num[-1]



#***************************************************** market cap*********************************************

marketcap= round(precio_accion * valor_num_acciones,2)



#***************************************************** deuda neta*********************************************

deuda_neta=ex.deuda_neta(df_balance)
valor_deuda_neta= round(deuda_neta[-1],2)

EV= round((marketcap+valor_deuda_neta),2)


#***************************************************** ebitda*********************************************
ebitda=ex.ebitda(df_resultado)
valor_ebitda= round(ebitda[-1],2)




#***************************************************** ratio ev/ebitda*********************************************

ratio_EV_ebitda= round ((marketcap+valor_deuda_neta) /valor_ebitda,2)


#******************************************MOSTRAR DATOS****************

tabla_2("Cotizacion",precio_accion)
tabla_2( "Marketcap", marketcap)
tabla_2( "Deuda neta", valor_deuda_neta)

tabla_22 ("EV",round((EV),2))
tabla_22 ("Ebitda",valor_ebitda)

tabla_222 ("Mutiplo EV/ebitda",ratio_EV_ebitda)


st.write("")
st.write("")
st.write("")

#*************************************************************************************************************
#***************************************************** Per************************************
#*************************************************************************************************************
h3_especial("PER")
st.write("")

marketcap=marketcap
beneficio=ex.beneficio(df_resultado)
valor_beneficio=beneficio[-1]

per= (marketcap/valor_beneficio)


tabla_2 ("marketcap",marketcap)
tabla_2 ("Beneficio",valor_beneficio)

tabla_222 ("PER",per)




#*************************************************************************************************************
#***************************************************** FCF yield ************************************
#*************************************************************************************************************

h3_especial("FCF yield")
st.write("")
st.write("")

EV=EV
fcf=ex.FCF(años,df_flujo,0)
valor_fcf=fcf[-1]




fcf_yield=round ((valor_fcf/EV)*100,2)

tabla_2 ("fcf",valor_fcf)
tabla_2 ("EV",EV)

tabla_222 ("fcf_yield",fcf_yield)
st.write("")
tabla_222 ("Mutiplo EV/fcf",100/fcf_yield)

st.write("")



h3_especial("Book value")

st.write("")
patrimonio=ex.patrimonio(df_balance)
valor_patrimonio=patrimonio[-1]
marketcap=marketcap

Price_to_book_value=round ((marketcap/valor_patrimonio),2)

tabla_2 ("Marketcap",marketcap)
tabla_2 ("Patrimonio",valor_patrimonio)
tabla_222 ("Mutiplo Price-to-book-value",Price_to_book_value)

st.write("")




fco= ex.FCO(df_flujo)
fcf=ex.FCF(años,df_flujo,0)
beneficio= ex.beneficio(df_resultado)

