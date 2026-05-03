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



#***********************************************cfo - capex *****************

h3_especial("Flujo de caja operativo - capex")

fco=ex.FCO(df_flujo)
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



#*********************************************** Varacion caja *****************

h3_especial("Variacion de caja")

fcf_dividendos=ut.resta_listas (fcf,dividendos)

deuda_neta=ex.deuda_neta(df_balance)
deuda_neta_anterior=deuda_neta[:-1]
deuda_neta_anterior.insert(0,0)
variacion_deuda_neta= ut.resta_listas(deuda_neta,deuda_neta_anterior)
variacion_deuda_neta[0] = "-"






caja=ex.caja(df_balance)
recompras=ex.recompras(df_flujo)
adquisiciones=ex.adquisiciones(df_flujo)


suma_com_ad=ut.suma_listas(recompras,adquisiciones)





suma_fcf_div_suma=ut.suma_listas(suma_com_ad,fcf_dividendos)



caja_anterior=caja[:-1]
caja_anterior.insert(0,0)
variacion_caja= ut.resta_listas(caja,caja_anterior)
variacion_caja[0] = "-"






suma_asignacion=ut.suma_listas (variacion_deuda_neta,suma_fcf_div_suma)

comparacion=ut.resta_listas(suma_asignacion,variacion_caja)

#ut.mostrar_tres_arrays_texto(años, fcf_dividendos, variacion_deuda_neta ,"FCF menos dividendos","Variacion deuda neta")
#ut.mostrar_tabla_4_listas(años,recompras,adquisiciones,suma_com_ad,"Recompras","Adquisiciones","Suma")
#ut.mostrar_dos_arrays_texto (años,caja,"Caja")
#ut.mostrar_tres_arrays_texto(años, variacion_caja, suma_fcf_div_suma ,"variacion caja","FCF menos div, recompras y adquisiciones")
#ut.mostrar_dos_arrays_texto (años,suma_asignacion,"suma asignacion flujo con variacion deuda")
#ut.mostrar_dos_arrays_texto (años,comparacion,"comparacion variacion caja con asignacion de capitals")



pago_deuda=ex.pago_deuda(df_flujo)

st.markdown(
    "<h5 style='text-align: center;'>Δ deuda neta > deuda emitida → están consumiendo caja</h5>",
    unsafe_allow_html=True
)

dif_var_deuda=ut.resta_listas(pago_deuda,variacion_deuda_neta)
ut.mostrar_tabla_4_listas(años,pago_deuda,variacion_deuda_neta,dif_var_deuda,"Emision deuda","Variacion Deuda neta","Diferencia")
#ut.mostrar_tres_arrays_texto(años,  variacion_deuda_neta ,pago_deuda,"variacion deuda neta","Deuda emitida")

ut.mostrar_dos_arrays_texto (años,variacion_caja,"variacion Caja")


gr.grafica_columnas(años,caja,"Años","Caja","#83F068")
cagr=rt.calcular_cagr(caja)
ut.mostrar_tabla_tres_celdas("CAGR", "Caja", cagr)


activos=ex.activos(df_balance)
por_activos=ut.divide_listas(caja,activos)
por_activos=[round (x*100,0) for x in por_activos]
por_activos=[f"{x:.0f} %" for x in por_activos]


ut.mostrar_tres_arrays_texto(años,  caja ,por_activos,"Caja","Porcentaje de los activos")