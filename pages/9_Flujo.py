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
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Flujo de Efectivo</h1>',
    unsafe_allow_html=True
)

años=df_resultado.columns.tolist()
años=ut.procesar_array (años)




#****************************************************** Estudio capex mantenimiento **********************************************

h3_especial("Estudio capex mantenimiento")


capex= ex.capex(df_flujo)
capex_mantenimiento=ex.capex_mantenimiento(df_flujo)
depreciacion= ex.depreciacion(df_flujo)

capex_inversion=ut.resta_listas(capex,capex_mantenimiento)



capex_n = [-round(x,0) for x in capex]
capex_mantenimiento_n=[-round(x,0)  for x in capex_mantenimiento]
capex_inversion_n=[-round(x,0)  for x in capex_inversion]

capex_n2 = [f"{x:.0f}"  for x in capex_n]
capex_mantenimiento_n2=[f"{x:.0f}" for x in capex_mantenimiento_n]
capex_inversion_n2=[f"{x:.0f}" for x in capex_inversion_n]


listas=[capex_n,capex_mantenimiento_n,capex_inversion_n,depreciacion]
colores=["#D1B65F", "#5F8594","#1DA9E0", "#B48966"]

etiquetas=["Capex","Capex mantenimiento","Capex inversion","Depreciacion"]


############################## capex mantenimiento segund Depreciacion y ventas ***************
ventas=ex.ventas(df_resultado)
gr.graficar_2barras ( capex_n, ventas,
                      color1="#A4B885",color2="#7BD8DF",
                     eje_x=años,
                     etiquetas=("Capex","Ventas"),
                     eje_y="Valores")


ratio_ventas_capex= ut.divide_listas(capex_n,ventas)

ratio_ventas_capex = [round(x*100,2) for x in ratio_ventas_capex]
ratio_ventas_capex = [f"{x:.0f} %" for x in ratio_ventas_capex]





crecimiento_ventas=ut.variacion_porcentual(ventas)
crecimiento_capex=ut.variacion_porcentual(capex_n)
cereciiento_deprecacion=ut.variacion_porcentual(depreciacion)




años_aux=años[1:]
ut.mostrar_dos_arrays_texto(años,ratio_ventas_capex,"ratio capex/ventas")

ut.mostrar_dos_arrays_texto(años,crecimiento_ventas,"Crecimiento ventas")
ut.mostrar_dos_arrays_texto(años,crecimiento_capex,"Crecimiento capex")
ut.mostrar_dos_arrays_texto(años,cereciiento_deprecacion,"Crecimiento depreciacion")

                            


st.write("")
st.write("")

media_ventas = rt.promedio(ventas)

aux_venta_depreciacion = [v / media_ventas for v in depreciacion]
capex_mant_segun_ventas=ut.multiplica_listas(aux_venta_depreciacion,ventas)
capex_mant_segun_ventas=[round(x) for x in capex_mant_segun_ventas]

gr.graficar_2barras (capex_mant_segun_ventas, capex_mantenimiento_n, 
                     color1="#7064B8", color2="#6B9133",
                     eje_x=años,
                     etiquetas=("C. mant segun ventas","C. mant segun Depreciacion"),
                     eje_y="Valores")





###############**************************Fin capex mantenimiento segun ventas


gr.graficar_2barras (capex_n, depreciacion, 
                     color1="#D1B65F", color2="#B48966",
                     eje_x=años,
                     etiquetas=("Capex","Depreciacion"),
                     eje_y="Valores")

ratio=ut.divide_listas(capex_n,depreciacion)
ratio = [round(x*100,2) for x in ratio]
ratio_texto = [f"{x:.0f} %" for x in ratio]

ut.mostrar_tabla_4_listas(años,capex_n,depreciacion,ratio_texto,"Capex","Depreciacion", "% Capex/Depreciacion")







capex_inversion_ventas=ut.resta_listas(capex_n,capex_mant_segun_ventas)
capex_inversion_ventas=[round(x) for x in capex_inversion_ventas]

h3_especial(" capex mantenimiento")





gr.graficar_barra_y_apilada(capex_n, capex_mant_segun_ventas, capex_inversion_ventas,
                                    "#D1B65F","#F58544", "#1DA9E0",
                                    eje_x=años,
                                    etiquetas=("Capex","Capex_mantenimiento","Capex_inversion"),
                                    eje_y_izq="Millones",
                                   )


ut.crear_tabla_4_listas (años,capex_mant_segun_ventas, capex_inversion_ventas,capex_n,"Capex mantenimiento","Capex inversion","Capex")



fco=ex.FCO(df_flujo)
gr.graficar_2barras (fco, capex_n, 
                     color1="#C296C4", color2="#BAC57D",
                     eje_x=años,
                     etiquetas=("Flujo de caja","Capex"),
                     eje_y="Valores")




#ut.crear_tabla_4_listas (años,capex_mantenimiento_n2,capex_inversion_n2,capex_n2,"C. mantenimiento (metodo promedio Depreciacion)","Capex inversion","Capex")

#******************************************************************************************************************
#****************************************************** Calculo de CFO*********************************************
#******************************************************************************************************************

st.write("")
st.write("")
st.write("")


h3_especial("Calculo CFO")

# 📥 selector centrado
col1, col2, col3 = st.columns([1, 1, 4])



with col2:
        anio_seleccionado = st.selectbox(
            "Selecciona el año",
            años,
            index=len(años) - 1,
            key="selector_anio_1"
        )


# 🔑 índice normal
indice = años.index(anio_seleccionado)

# 🔥 índice invertido (lo que tú quieres)
indice_inv = indice - len(años)


beneficio=ex.beneficio(df_resultado)
depreciacion=depreciacion
variacion_WC=ex.variacion_wc(df_flujo)
cambio_impuestos=ex.change_defer_taxes(df_flujo)
other_cfo=ex.other_cfo(df_flujo)

Stock_base=ex.stock_base_compensation(df_flujo)
valores_cfo = [beneficio[indice_inv], depreciacion[indice_inv],  variacion_WC[indice_inv],cambio_impuestos[indice_inv],Stock_base[indice_inv],other_cfo[indice_inv],None]
etiquetas_cfo = ["Beneficio neto", "Depreciacion", "Variacion WC","Cambio impuestos diferidos","compensacion por stocks options","Otros","CFO"]

etiquetas_cfo = [f"<b>{e}</b>" for e in etiquetas_cfo]

gr.asignar_capital(valores_cfo, etiquetas_cfo,
                    color_total="#AC6509",
                    titulo="CFO")





#****************************************************** Asignacion de capital año ....*********************************************

h3_especial("Asignacion del capital del año")

# 📥 selector centrado
col1, col2, col3 = st.columns([1, 1, 4])



with col2:
        anio_seleccionado = st.selectbox(
            "Selecciona el año",
            años,
            index=len(años) - 1,
            key="selector_anio_2"
        )


# 🔑 índice normal
indice = años.index(anio_seleccionado)

# 🔥 índice invertido (lo que tú quieres)
indice_inv = indice - len(años)





fco=ex.FCO(df_flujo)
capex=ex.capex(df_flujo)

dividendos=ex.dividendos(df_flujo)
recompras=ex.recompras(df_flujo)
adquisiciones=ex.adquisiciones(df_flujo)
deuda_emitida=ex.pago_deuda(df_flujo)
variacion_cash=ex.variacion_en_caja(df_flujo)





#***** calculo working capital*****************
#activo_cp=ex.activo_cp(df_balance)
#pasivos_cp=ex.pasivos_cp(df_balance)

#working_capital=ut.resta_listas (activo_cp,pasivos_cp)
#delta_wc= ut.variacion_absoluta(working_capital)
#delta_wc= [0 if x == "-" else -int(float(x)) for x in delta_wc]

#***** Fin calculo working capital*****************



inversiones_varias=ex.inversiones_varias(df_flujo)

Otra_financiacion=ex.other_cash_financing(df_flujo)
cambio=ex.change(df_flujo)


valores = [fco[indice_inv], -capex_mant_segun_ventas[indice_inv],  -capex_inversion_ventas[indice_inv],adquisiciones[indice_inv],inversiones_varias[indice_inv],dividendos[indice_inv],recompras[indice_inv],deuda_emitida[indice_inv],Otra_financiacion[indice_inv],variacion_cash[indice_inv],cambio[indice_inv],None]

etiquetas = ["Flujo de caja operativo", "Capex Mantenimiento", "Capex Inversion","Adquisiciones","Inversiones Varias","Dividendos","Recompras","Emision Deuda","Otra financiacion","Variacion en caja","change effect","Total"]


etiquetas_tabla=etiquetas
valores_tabla=valores

etiquetas = [f"<b>{e}</b>" for e in etiquetas]


gr.asignar_capital(valores, etiquetas,
                    color_total="#F78C35",
                    titulo="Flujo de caja")






etiquetas_tabla.insert(2, "<b>**Free cash Flow</b>")
etiquetas_tabla.insert(6, "<b>**Cash from Investing</b>")
etiquetas_tabla.insert(11, "<b>**Cash from Financing</b> ")
etiquetas_tabla[-1]=("<b>**Resultado de caja</b>")




valores_tabla.insert(2, fco[indice_inv] - capex_mantenimiento_n[indice_inv])
valores_tabla.insert(6,  -capex_inversion_n[indice_inv]+adquisiciones[indice_inv]+inversiones_varias[indice_inv])
valores_tabla.insert(11, dividendos[indice_inv]+recompras[indice_inv]+deuda_emitida[indice_inv]+Otra_financiacion[indice_inv])
valores_tabla[-1]= valores_tabla[2]+valores_tabla[6]+valores_tabla[11]+valores_tabla[13]

remanente=[]
remanente.append(fco[indice_inv])
remanente.append(fco[indice_inv] - capex_mant_segun_ventas[indice_inv])





fcf_tabla= fco[indice_inv] - capex_mant_segun_ventas[indice_inv] 

remanente.append("<b>--</b>")
remanente.append(fcf_tabla+valores[3])
remanente.append(remanente[3]+valores[4])
remanente.append(remanente[4]+valores[5])
remanente.append("<b>--</b>")
remanente.append(remanente[5]+valores[7])
remanente.append(remanente[7]+valores[8])
remanente.append(remanente[8]+valores[9])
remanente.append(remanente[9]+valores[10])
remanente.append("<b>--</b>")
remanente.append("<b>--</b>")
remanente.append(remanente[10]+valores[13])




remanente.append(remanente[13]-valores[14])




df_asignacion = pd.DataFrame({
    "Concepto": etiquetas_tabla,
    "Importe": valores_tabla,  
    "Remanente":remanente 
})



df_asignacion["Importe"] = [
    "<b>--</b>" if x == "<b>--</b>" or pd.isna(x)
    else f"{float(x):.0f}"
    for x in df_asignacion["Importe"]
]

df_asignacion["Remanente"] = [
    "<b>--</b>" if x == "<b>--</b>" or pd.isna(x)
    else f"{float(x):.0f}"
    for x in df_asignacion["Remanente"]
]


 # Convertir DataFrame a HTML
html_table = df_asignacion.to_html(index=False, header=True, table_id="tabla_estudio_wc", escape=False)

# CSS para centrar celdas y encabezado
css = """
    <style>
    table.dataframe#tabla_estudio_wc {
        width: auto;
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto; /* centra la tabla */
    }

    table.dataframe#tabla_estudio_wc tbody tr{
        background-color: white;
        text-align: left;
        padding: 4px;
    }

    table#tabla_estudio_wc thead th {
        background-color: #D9E6E7;
        text-align: center;
        padding: 4px;
    }

    table.dataframe#tabla_estudio_wc td {
        border: 1px solid #ccc;
         text-align: center;   /* 👈 esto es lo clave */
    }
    </style>
    """

    # Mostrar CSS y tabla
st.markdown(css, unsafe_allow_html=True)
st.markdown(html_table, unsafe_allow_html=True)

st.write("")

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

gr.graficar_barra_y_apilada(fco, cash_from_finacing2, cash_from_inversion2,
                                    "#D099F0","#F15540", "#E2B25A",
                                    eje_x=años,
                                    etiquetas=("FCO","Cash from investing","Cash from financing"),
                                    eje_y_izq="Millones",
                                   )




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



#****************************************************** Evolucion Asignacion de capital **********************************************

h3_especial("Evolución Asignacion del capital")

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





#******************************************************Adquisiciones **********************************************

h3_especial("Adquisiciones")
adquisiciones=adquisiciones
gr.grafica_columnas(años,adquisiciones,"Años","Adquisiciones","#351D03")

#******************************************************Inversion **********************************************

h3_especial("Inversion")
inversion=inversiones_varias
gr.grafica_columnas(años,inversion,"Años","Inversiones","#C46807")

#******************************************************recompras **********************************************

h3_especial("Recompras")
recompras=recompras
gr.grafica_columnas(años,recompras,"Años","Recompras","#5D9414")

#******************************************************Dividendos **********************************************

h3_especial("Dividendos")
dividendos=dividendos
gr.grafica_columnas(años, dividendos, "Años","Dividendos","#E76C1A")





#******************************************************Financiacion varia **********************************************


h3_especial("Financiacion varia")



financiacion_varia=Otra_financiacion
gr.grafica_columnas(años, financiacion_varia, "Años","Financiacion varia","#476096")

#******************************************************Pago deuda **********************************************


h3_especial("Emision neta de deduda")

pago_deuda=deuda_emitida
gr.grafica_columnas(años, pago_deuda, "Años","Financiacion varia","#EE5A6E")








