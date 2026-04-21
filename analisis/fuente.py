import numpy as np
import streamlit as st
import pandas as pd
import analisis.ratios as rt
import utils.funciones as ut



# ******************************************extrae años *********************************
def años(df):
    años=df.columns.tolist()
    años=ut.procesar_array (años)
    
    return años

# ******************************************Cuenta de resultados*********************************
# ************************************************************* *********************************

def ventas(df):

    fila=ut.buscar_fila(df, "Revenue")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista



def beneficio_bruto(df):

    fila=ut.buscar_fila(df, "Gross Profit")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista



def beneficio_operativo(df):

    fila=ut.buscar_fila(df, "Operating Profit")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista




def beneficio(df):

    fila=ut.buscar_fila(df, "Net Income")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def pretax_income(df):

    fila=ut.buscar_fila(df, "Pre-Tax Income")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def income_tax(df):

    fila=ut.buscar_fila(df, "Income Tax")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def intereses(df):

    fila=ut.buscar_fila(df, "Net Interest Income")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista









#********************************** num acciones *********************

def num_acciones(df):

    fila=ut.buscar_fila(df, "Shares (Diluted)")

    
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]


   
    
    lista=ut.convertir_a_numero(lista)
    lista= [int(x) for x in lista ]
    


    return lista







def ingresos_operativos(df):

    fila=ut.buscar_fila(df, "Operating Profit")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista



def ebitda(df):

    fila=ut.buscar_fila(df, "Operating Profit")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    fila2=ut.buscar_fila(df, "Depreciation & Amortization")
    try:
        lista2=ut.fila_a_array (df,fila2+1)
    except :
        lista2= 10* [0]

    lista2=ut.limpiar_a_numeros(lista2)


    lista=ut.suma_listas (lista,lista2)

    return lista







# ******************************************Balance*********************************
# ************************************************************* *********************************
def activos(df):

    fila=ut.buscar_fila(df, "Total Assets")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista




def activo_cp(df):

    fila=ut.buscar_fila(df, "Total Current Assets")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista

def inventarios(df):

    fila=ut.buscar_fila(df, "Inventories")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def caja(df):

    fila=ut.buscar_fila(df, "Cash & Equivalents")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista




def goodwill(df):

    fila=ut.buscar_fila(df, "Goodwill")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def intangibles(df):

    fila=ut.buscar_fila(df, "Other Intangible Assets")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista






def long_debt(df):

    fila=ut.buscar_fila(df, "Long-Term Debt")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def long_lease(df):

    fila=ut.buscar_fila(df, "Capital Leases (Non-Current)")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista






def patrimonio(df):

    fila=ut.buscar_fila(df, "Shareholders' Equity")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista






# ******************************************pasivos*********************************

def pasivos(df):

    fila=ut.buscar_fila(df, "Total Liabilities")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista




def pasivos_cp(df):

    fila=ut.buscar_fila(df, "Total Current Liabilities")
    try:
        current_debt=ut.fila_a_array (df,fila+1)
    except :
        current_debt= 10* [0]

    current_debt=ut.limpiar_a_numeros(current_debt)

    return current_debt


def deuda_neta(df):

    cp= deuda_cp(df)
    lp= deuda_lp(df)
    ca= caja(df)


    deuda_neta = [
    (a if isinstance(a, (int, float)) else 0) +
    (b if isinstance(b, (int, float)) else 0)
    for a, b in zip(cp, lp) ]

   

    deuda_neta = [
    (a if isinstance(a, (int, float)) else 0) -
    (b if isinstance(b, (int, float)) else 0)
    for a, b in zip(deuda_neta, ca) ]


    



    return deuda_neta





def deuda_cp(df):

    fila=ut.buscar_fila(df, "Short-Term Debt")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    fila2=ut.buscar_fila(df, "Capital Leases (Current)")
    try:
        lista2=ut.fila_a_array (df,fila2+1)
    except :
        lista2= 10* [0]

    lista2=ut.limpiar_a_numeros(lista2)

    lista=ut.suma_listas (lista,lista2)

    return lista



def deuda_lp(df):

    fila=ut.buscar_fila(df, "Long-Term Debt")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    fila2=ut.buscar_fila(df, "Capital Leases (Non-Current)")
    try:
        lista2=ut.fila_a_array (df,fila2+1)
    except :
        lista2= 10* [0]

    lista2=ut.limpiar_a_numeros(lista2)

    lista=ut.suma_listas (lista,lista2)

    return lista














# ******************************************Flujo de caja*********************************
# ************************************************************* *********************************

def FCO(df):

    fila=ut.buscar_fila(df, "Cash From Operations")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista







def FCF(años,df_flujo,bandera):
    fila=ut.buscar_fila(df_flujo, "Cash From Operations")
    flujo_operativo=ut.fila_a_array (df_flujo,fila+1)

    if (bandera):
        st.markdown(
            '<div style="text-align: center; font-size: 16px;"><br><b>Flujo operativo</b></div>',
            unsafe_allow_html=True)

        ut.mostrar_dos_arrays(años, flujo_operativo)


    #··························capex promedio******************************


    fila=ut.buscar_fila(df_flujo, "Depreciation & Amortization")
    depreciacion=ut.fila_a_array (df_flujo,fila+1)
    
    if (bandera):
        st.markdown(
            '<div style="text-align: center; font-size: 16px;"><b>Depreciacion</b></div>',
            unsafe_allow_html=True)
        ut.mostrar_dos_arrays(años, depreciacion)




    fila=ut.buscar_fila(df_flujo, "Property, Plant, & Equipment")
    capex=ut.fila_a_array (df_flujo,fila+1)
    
    if (bandera):
        st.markdown(
            '<div style="text-align: center; font-size: 16px;"><b>Capex total</b></div>',
            unsafe_allow_html=True)
        ut.mostrar_dos_arrays(años, capex)

    if (bandera):
        st.markdown(
            '<div style="text-align: center; font-size: 16px;"><b>Ratio depreciacion / capex </b></div>',
            unsafe_allow_html=True)

    lista_promedio=rt.dividir_listas(depreciacion, capex)
    
    if (bandera):
        ut.mostrar_dos_arrays(años, lista_promedio)

    promedio_capex=rt.promedio(lista_promedio)


    capex_mantenimiento = [-promedio_capex * x for x in capex]


    capex_mantenimiento= [round(x, 2) if isinstance(x, (int, float)) else x for x in capex_mantenimiento]

    if (bandera):
        st.markdown(
            f'<div style="text-align: center; font-size: 16px;"><b>Capex mantenimiento calculado</b> (ratio medio <b>{round(promedio_capex,2)}</b>) </div>',
            unsafe_allow_html=True)
        ut.mostrar_dos_arrays(años, capex_mantenimiento)


        st.markdown(
            '''
            <div style="text-align: center; font-size: 18px;">
                <b>FCF</b> (Flujo de caja operativo − CAPEX mantenimiento)<br>
                <span style="font-size:14px;">(capex mantenimiento tomado como promedio depreciación/capex 10 años)</span>
            </div>
            ''',
            unsafe_allow_html=True
        )



    FCF= [
        round((a if isinstance(a, (int, float)) else 0) +
        (b if isinstance(b, (int, float)) else 0),2)
        for a, b in zip(flujo_operativo, capex_mantenimiento)
    ]

    return FCF

#*********************************************************************



def capex(df):

    fila=ut.buscar_fila(df, "Property, Plant, & Equipment")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def capex_mantenimiento(df):

    fila=ut.buscar_fila(df, "Property, Plant, & Equipment")

    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    capex=ut.limpiar_a_numeros(lista)


    fila2=ut.buscar_fila(df, "Depreciation & Amortization")

    try:
        lista2=ut.fila_a_array (df,fila2+1)
    except :
        lista2= 10* [0]

    depreciacion=ut.limpiar_a_numeros(lista2)

    lista_promedio=rt.dividir_listas(depreciacion, capex)
    promedio_capex=rt.promedio(lista_promedio)
    capex_mantenimiento = [-promedio_capex * x for x in capex]


    return capex_mantenimiento


def depreciacion(df):

    fila=ut.buscar_fila(df, "Depreciation & Amortization")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista


def recompras(df):

    fila=ut.buscar_fila(df, "Net Issuance of Common Stock")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista




def dividendos(df):

    fila=ut.buscar_fila(df, "Cash Paid for Dividends")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista




def adquisiciones(df):

    fila=ut.buscar_fila(df, "Acquisitions")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista



def pago_deuda(df):

    fila=ut.buscar_fila(df, "Net Issuance of Debt")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista





def inversiones_varias(df):

    fila=ut.buscar_fila(df, "Investments")

    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    inversiones=ut.limpiar_a_numeros(lista)


    fila2=fila+1
    valor = df.iloc[fila2, 0]
  

    if (valor == "Other"):
        try:
            lista2=ut.fila_a_array (df,fila2+1)
        except :
            lista2= 10* [0]
    else:
        lista2= 10* [0]
    


    other=ut.limpiar_a_numeros(lista2)
     
    inversion_total=ut.suma_listas(inversiones,other)

    return inversion_total


def dividendos(df):

    fila=ut.buscar_fila(df, "Cash Paid for Dividends")
    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)

    return lista






def financiacion(df):

    fila=ut.buscar_fila(df, "Cash Paid for Dividends")
    valor = df.iloc[fila+1, 0]

    try:
        lista=ut.fila_a_array (df,fila+2)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)


    return lista,valor



def cash_inversion(df):

    fila=ut.buscar_fila(df, "Cash From Investing")
   

    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)
  

    return lista



def cash_financing(df):

    fila=ut.buscar_fila(df, "Cash From Financing")
  

    try:
        lista=ut.fila_a_array (df,fila+1)
    except :
        lista= 10* [0]

    lista=ut.limpiar_a_numeros(lista)
  

    return lista