import streamlit as st

import analisis.ratios as rt
import utils.funciones as ut
import utils.graficas as gr

import pandas as pd
import analisis.fuente as ex
from styles.style_utils import aplicar_estilos, h3_especial,titulo_con_ventana_informativa
from utils.definiciones import DEFINICIONES


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
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Calidad</h1>',
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

roe = [
    round(x * 100, 0) if x is not None else None
    for x in roe
]

roic = [
    round(x * 100, 0) if x is not None else None
    for x in roic
]

gr.graficar_tres_lineas(roe,roic,linea15,"#8287CE","#C7D31A","#F74444", eje_x=años, etiquetas=("Roe","Roic","15%"), eje_y="Rentabilidad")


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








#***************************************************** Cash conversion rate  **********************************************


titulo_con_ventana_informativa ("Cash conversion rate", DEFINICIONES["ccr"])

ebitda=ex.ebitda(df_resultado)
fco=ex.FCO(df_flujo)

gr.graficar_2barras (fco, ebitda, 
                     color1="#2C5834", color2="#CE9C30",
                     eje_x=años,
                     etiquetas=("FCO","Ebitda"),
                     eje_y="Valores")

cash_conversion_rate=ut.divide_listas (fco,ebitda)
cash_conversion_rate= [round (x*100,0) for x in cash_conversion_rate]
cash_conversion_rate = [f"{x:.0f} %" for x in cash_conversion_rate]



ut.mostrar_dos_arrays_texto_explicacion(años, cash_conversion_rate,"Cash conversion rate",DEFINICIONES["ccr"])





#***************************************************** ISGR + CALIDAD CRECIMIENTO **********************************************

titulo_con_ventana_informativa ("ISGR (Relación inventarios con ventas)", DEFINICIONES["ISGR"])

inventarios = ex.inventarios(df_balance)
gr.grafica_columnas(años, inventarios, "Años", "Inventarios", "#778FE0")
variacion1 = ut.variacion_porcentual(inventarios)
ut.mostrar_tres_arrays_texto(años, inventarios, variacion1, "Inventarios", "Variación Inventarios")

ventas = ex.ventas(df_resultado)
gr.grafica_columnas(años, ventas, "Años", "Ventas", "#61D7F5")
variacion2 = ut.variacion_porcentual(ventas)
ut.mostrar_tres_arrays_texto(años, ventas, variacion2, "Ventas", "Variación Ventas")


# -----------------------
# LIMPIEZA DATOS
# -----------------------
def limpiar_lista(lista):
    return [
        None if (x == "-" or x is None) else float(x.replace("%", "").strip())
        for x in lista
    ]

variacion1_clean = limpiar_lista(variacion1)
variacion2_clean = limpiar_lista(variacion2)


# -----------------------
# ISGR
# -----------------------
ratio_entre_variaciones = ut.divide_listas(variacion1_clean, variacion2_clean)


 # -----------------------
 # Funcion clasificar isgr, inventarios y ventas
 # -----------------------


def clasificar_empresa(delta_ventas, delta_inventarios, isgr):

    resultados = []

    for v, inv, g in zip(delta_ventas, delta_inventarios, isgr):

        # -----------------------
        # VALIDACIÓN
        # -----------------------
        if v is None or inv is None or g is None:
            resultados.append({
                "relacion": "⚪",
                "caso": "⚪",
                "tipo": "Sin datos",
                "explicacion": "Datos insuficientes"
            })
            continue

        # -----------------------
        # CASO 1: ↑ ventas / ↓ inventarios
        # -----------------------
        if v > 0 and inv < 0:
            relacion = "🟢 ↓↑"

            if g < 0:
                caso = "🔵"
                tipo = "Eficiencia extrema"
                exp = "Ultra eficiencia operativa"

            elif 0 <= g <= 1:
                caso = "🟢"
                tipo = "Eficiente"
                exp = "Crecimiento sano con eficiencia"

            else:
                caso = "🟡"
                tipo = "Infra-stock"
                exp = "Posible falta de inventario"

        # -----------------------
        # CASO 2: ↑ ventas / ↑ inventarios
        # -----------------------
        elif v > 0 and inv > 0:
            relacion = "🟡 ↑↑"

            if g < 1:
                caso = "🟢"
                tipo = "Crecimiento equilibrado"
                exp = "Crecimiento ordenado"

            elif 1 <= g <= 2:
                caso = "⚠️"
                tipo = "Tensión de crecimiento"
                exp = "Inventarios creciendo con ventas"

            else:
                caso = "🚨"
                tipo = "Sobreexpansión"
                exp = "Riesgo de acumulación"

        # -----------------------
        # CASO 3: ↓ ventas / ↑ inventarios
        # -----------------------
        elif v < 0 and inv > 0:
            relacion = "🔴 ↑↓"

            if g < 0:
                caso = "🚨"
                tipo = "Destrucción de demanda"
                exp = "Ventas caen + stock sube"

            elif 0 <= g <= 1:
                caso = "🔴"
                tipo = "Deterioro"
                exp = "Acumulación de stock con caída de ventas"

            else:
                caso = "💥"
                tipo = "Colapso operativo"
                exp = "Distorsión fuerte en el modelo"

        # -----------------------
        # CASO 4: ↓ ventas / ↓ inventarios
        # -----------------------
        elif v < 0 and inv < 0:
            relacion = "🟠 ↓↓"

            if g < 0:
                caso = "🟡"
                tipo = "Ajuste eficiente"
                exp = "Limpieza ordenada con caída de actividad"

            elif 0 <= g <= 1:
                caso = "🟠"
                tipo = "Contracción normal"
                exp = "Reducción controlada del negocio"

            else:
                caso = "🔴"
                tipo = "Contracción desordenada"
                exp = "Caída del negocio con tensión operativa"

        # -----------------------
        # CASO NEUTRO
        # -----------------------
        else:
            relacion = "⚪ 0"
            caso = "⚪"
            tipo = "Neutro"
            exp = "Combinación no estándar"

        resultados.append({
            "relacion": relacion,
            "caso": caso,
            "tipo": tipo,
            "explicacion": exp
        })

    return resultados




# -----------------------
# EJECUCIÓN
# -----------------------
resultado = clasificar_empresa(
    variacion2_clean,
    variacion1_clean,
    ratio_entre_variaciones
)


# -----------------------
# TABLA FINAL
# -----------------------
data = []

for i in range(len(años)):

    data.append({
        "Año": años[i],
        "Relacion I-V": resultado[i]["relacion"],
        "Δ Inventarios": variacion1[i],
        "Δ Ventas": variacion2[i],
        "Motivo": resultado[i]["tipo"],
        
        "ISGR": "-" if ratio_entre_variaciones[i] is None else round(ratio_entre_variaciones[i], 2),
        "caso": resultado[i]["caso"], 
        "Explicación": resultado[i]["explicacion"]

    })

df_isgr = pd.DataFrame(data)

html_table = df_isgr.to_html(index=False, escape=False, table_id="tabla_isgr")

css = """
<style>
table.dataframe#tabla_isgr {
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse;
}

table#tabla_isgr thead th {
    background-color: #D9E6E7;
    text-align: center;
    padding: 6px;
}

table#tabla_isgr td {
    border: 1px solid #ccc;
    padding: 6px;
    text-align: center;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)
st.markdown(html_table, unsafe_allow_html=True)



#*********************************************** crecimeinto estruturado *****************


titulo_con_ventana_informativa ("Crecimiento sostenible", DEFINICIONES["crecimiento"])

roe=roe
dividendos=ex.dividendos(df_flujo)
recompras=ex.recompras(df_flujo)

beneficio_neto_aux=ut.suma_listas(beneficio_neto,dividendos)
beneficio_neto_aux=ut.suma_listas(beneficio_neto_aux,recompras)
tasa_reinversion=ut.divide_listas(beneficio_neto_aux,beneficio_neto)

crecimiento= ut.multiplica_listas(roe,tasa_reinversion)



#ut.mostrar_cuatro_arrays(años,beneficio_neto,dividendos,recompras,"beneficio","dividendos","recompras")

tasa_reinversion = [round(x*100,2) for x in tasa_reinversion]
crecimiento= [round(x,2) for x in crecimiento]
ratio_crecimiento = [f"{x:.2f} %" for x in crecimiento]

st.write("")
ut.mostrar_tabla_4_listas(años,roe,tasa_reinversion,ratio_crecimiento,"Roe","tasa reinversion","Crecimiento estructurado")