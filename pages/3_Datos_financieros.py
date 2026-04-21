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


#***********************************************Deuda - Ebitda *****************

h3_especial("Deuda - Ebitda")






deuda_cp=ex.deuda_cp(df_balance)
deuda_lp=ex.deuda_lp(df_balance)

deuda=ut.suma_listas(deuda_cp,deuda_lp)





ebitda=ex.ebitda(df_resultado)


gr.graficar_2barras (deuda, ebitda, 
                     color1="#B43838", color2="#52923E",
                     eje_x=años,
                     etiquetas=("deuda","ebitda"),
                     eje_y="Valores")



ratio=ut.divide_listas(deuda,ebitda)


ut.mostrar_tabla_4_listas (años, deuda, ebitda, ratio, "Deuda","Ebitda","Ratio Deuda/Ebitda")
gr.graficar_una_linea (ratio, "#B43838", eje_x=años, etiqueta="Ratio Deuda/Ebitada", eje_y="Ratio")



#***********************************************Deuda - cfo *****************

h3_especial("Deuda - Flujo de caja operativo")

deuda=deuda
fco=ex.FCO(df_flujo)
ratio=ut.divide_listas(deuda,fco)


gr.graficar_2barras (deuda, fco, 
                     color1="#B43838", color2="#C296C4",
                     eje_x=años,
                     etiquetas=("deuda","fco"),
                     eje_y="Valores")


ut.mostrar_tabla_4_listas (años, deuda, fco, ratio, "Deuda","fco","Ratio Deuda/fco")
gr.graficar_una_linea (ratio, "#B43838", eje_x=años, etiqueta="Ratio Deuda/Ebitada", eje_y="Ratio")


#***********************************************cfo - capex *****************

h3_especial("Flujo de caja operativo - capex")

fco=fco
capex=ex.capex(df_flujo)
capex_positivo = [-x for x in capex]

ratio=ut.divide_listas(capex_positivo,fco)
ratio = [round(x*100,2) for x in ratio]
ratio_texto = [f"{x:.0f} %" for x in ratio]

gr.graficar_2barras (fco, capex_positivo, 
                     color1="#C296C4", color2="#BAC57D",
                     eje_x=años,
                     etiquetas=("Flujo de caja","Capex"),
                     eje_y="Valores")

ut.mostrar_tabla_4_listas(años,fco,capex_positivo,ratio_texto,"Flujo de caja","Capex", "% capex/fco")

#***********************************************FCF *****************

h3_especial("Free cash Flow")


fcf=ex.FCF(años,df_flujo,0)
gr.grafica_columnas(años,fcf,"Años","FCF","#628585")

ut.mostrar_dos_arrays_texto (años,fcf,"Free Cash Flow")



#***********************************************FCF - Dividendos  *****************

h3_especial("Free cash Flow - Dividendos")

fcf=fcf
dividendos=ex.dividendos(df_flujo)

dividendos = [-x for x in dividendos]

pay_out_fcf= ut.divide_listas (dividendos,fcf)
pay_out_fcf = [round(100*x) for x in pay_out_fcf]
pay_out_fcf_texto = [f"{x} %" for x in pay_out_fcf]


gr.graficar_2barras (fcf, dividendos, 
                     color1="#628585", color2="#F7A354",
                     eje_x=años,
                     etiquetas=("FCF","Dividendos"),
                     eje_y="Valores")


cagr=rt.calcular_cagr(fcf)
ut.mostrar_tabla_tres_celdas("CAGR", "FCF", cagr)
cagr=rt.calcular_cagr(dividendos)
ut.mostrar_tabla_tres_celdas("CAGR", "Dividendos", cagr)


ut.mostrar_tabla_4_listas(años,fcf,dividendos,pay_out_fcf_texto,"FCF","Dividendos", "Pay-out (FCF)%")

lim_sup=[85]*10
lim_inf=[30]*10

gr.graficar_tres_lineas(pay_out_fcf, lim_sup, lim_inf,"#762C79","#FC0000","#077703", eje_x=años, etiquetas=("pay out-fcf","lim sup","lim inf"), eje_y="ratio")




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

