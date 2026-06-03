
import streamlit as st
import analisis.ratios as rt
import utils.funciones as ut
import utils.graficas as gr
import analisis.fuente as ex

import pandas as pd
from styles.style_utils import aplicar_estilos, h3_especial,tabla_2,tabla_22,tabla_222,h2_especial,tabla_2_1

def app(df_resultado,df_balance,df_flujo,años):
    st.header("📊 Valoración General")
    st.write("Aquí va el análisis de valoracion General")



    precio_accion = st.number_input("Precio", value=50.0)

    #***************************************************** acciones*********************************************


    fila=ut.buscar_fila(df_resultado, "Shares (Diluted)")
    num_acciones=ut.fila_a_array (df_resultado,fila+1)
    num_acciones_num=rt.convertir_a_numero(num_acciones)


    valor_num_acciones=num_acciones_num[-1]





    #***************************************************** EV/ebitda*********************************************
    #***************************************************************************************************************


    h3_especial("EV/ebitda")
    st.write("")






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
    beneficio=ex.beneficio(df_resultado)
    marketcap=marketcap

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

    #**********************************************************Book value*******************

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



    #*************************************************************************************************************
    #***************************************************** Valoracion *********************************************
    #*************************************************************************************************************


    st.markdown("""
    <style>
    div[data-testid="stNumberInput"] {
        max-width: 200px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)




