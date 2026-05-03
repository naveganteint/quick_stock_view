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
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Otros ratios</h1>',
    unsafe_allow_html=True
)

años=df_resultado.columns.tolist()
años=ut.procesar_array (años)



#***************************************************** Current ratio **********************************************

h3_especial("current Ratio")

activo_cp=ex.activo_cp(df_balance)
pasivos_cp=ex.pasivos_cp(df_balance)

ratio_corrientes= rt.dividir_y_convertir_a_porcentaje(activo_cp,pasivos_cp)
ratio_corrientes= [round(x/100,2) if isinstance(x, (int, float)) else x for x in ratio_corrientes]

lim_sup = 10*[1.5]
lim_inf=10*[1]


gr.graficar_tres_lineas(ratio_corrientes, lim_sup, lim_inf,"olive","lightgreen","coral", eje_x=años, etiquetas=("ratio corrientes","limite_sano","limite_no aceptable"), eje_y="solvencia corrientes")


ut.mostrar_dos_arrays_texto(años, ratio_corrientes ,"ratio corrientes")







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



#******************************************************Asignacion de capital **********************************************

h3_especial("Asignacion de capital")

fco=ex.FCO(df_flujo)
dividendos=ex.dividendos(df_flujo)
capex=ex.capex(df_resultado)


fcf1=ut.resta_listas(fco,capex)
fco_div_capex=ut.resta_listas(fcf1,dividendos)


recompras=ex.recompras(df_flujo)
adquisiciones=ex.adquisiciones(df_flujo)
deuda_emitida=ex.pago_deuda(df_flujo)


aux1=ut.suma_listas(recompras,adquisiciones)
aux1=ut.suma_listas(aux1,deuda_emitida)
aux1=[-x for x in aux1]


listas=[fco_div_capex,aux1, adquisiciones,recompras,deuda_emitida]   
etiquetas= ["FCO_div_capex","RE+adq+Deuda","Aquisiciones","Recompras","Deuda emitida"]
colores=["#52815D","#8DF16E","#351D03","#C46807","#EC4D42"]



gr.graficar_n_barras(listas, 
                     colores=colores,
                     eje_x=años,
                     etiquetas=etiquetas,
                     eje_y="Valores")


deuda_neta=ex.deuda_neta(df_balance)

gr.grafica_columnas(años,deuda_neta,"Años","Deuda neta","#CE5B5B")
cagr=rt.calcular_cagr(deuda_neta)
ut.mostrar_tabla_tres_celdas("CAGR", "Deuda neta", cagr)




st.write("")



#************************************************************NET CASH **********************************
h3_especial("Net cash")

fco=fco
cash_from_inversion=ex.cash_inversion(df_flujo)
cash_from_finacing=ex.cash_financing(df_flujo)

resultado=ut.suma_listas(fco,cash_from_inversion)
net_cash=ut.suma_listas(resultado,cash_from_finacing)

cash_from_inversion2 = [round (float(-x),2) for x in cash_from_inversion]
cash_from_finacing2 = [round (float(-x),2) for x in cash_from_finacing]

gr.graficar_barras_apiladas_y_linea(fco, cash_from_inversion2, cash_from_finacing2, net_cash,
                                    "#F3B890","#318DB8", "#89A064", 'blue',
                                    eje_x=años,
                                    etiquetas=("fco","cash from inversion","cash from financing","net cash"),
                                    eje_y_izq="Millones",
                                    eje_y_der="Millones")

caja=ex.caja(df_balance)

ut.crear_tabla_5_listas (años, fco,  cash_from_inversion, cash_from_finacing,net_cash,"FCO","cash from inversion","cash from financing","Net Cash")

gr.grafica_columnas(años,caja,"Años","Caja","#83F068")
cagr=rt.calcular_cagr(caja)
ut.mostrar_tabla_tres_celdas("CAGR", "Caja", cagr)


activos=ex.activos(df_balance)
por_activos=ut.divide_listas(caja,activos)
por_activos=[round (x*100,0) for x in por_activos]
por_activos=[f"{x:.0f} %" for x in por_activos]


ut.mostrar_tres_arrays_texto(años,  caja ,por_activos,"Caja","Porcentaje de los activos")






