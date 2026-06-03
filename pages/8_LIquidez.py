import streamlit as st

import analisis.ratios as rt
import utils.funciones as ut
import utils.graficas as gr

import pandas as pd
import analisis.fuente as ex
from styles.style_utils import aplicar_estilos, h3_especial, titulo_con_ventana_informativa,titulo_con_ventana_informativa2
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




#***************************************************** Working capital **********************************************

titulo_con_ventana_informativa ("Working Capital (fondo de maniobra)", DEFINICIONES["wc"])


working_capital=ut.resta_listas (activo_cp,pasivos_cp)

delta_wc= ut.variacion_absoluta(working_capital)
delta_wc = [
    f"{float(x):.0f}" if x != "-" else "-"
    for x in delta_wc
]

gr.grafica_columnas(años,working_capital,"Años","Working capital (fondo de maniobra)","#CA92F0")
ut.mostrar_tres_arrays_texto(años, working_capital,delta_wc,"Working capital","Δ working capital")



caja=ex.caja(df_balance)
delta_caja= ut.variacion_absoluta(caja)
delta_caja = [
    f"{float(x):.0f}" if x != "-" else "-" for x in delta_caja]




gr.grafica_columnas(años,caja,"Años","caja","#9FF18E")
ut.mostrar_tres_arrays_texto(años, caja,delta_caja,"caja","Δ caja")


delta_caja=ut.limpiar_lista_numerica(delta_caja)
delta_wc=ut.limpiar_lista_numerica(delta_wc)

años1=años[1:]

gr.graficar_2barras (delta_caja[1:], delta_wc[1:], 
                     color1="#9FF18E", color2="#CA92F0",
                     eje_x=años1,
                     etiquetas=("Δ caja","Δ working capital"),
                     eje_y="Valores")


impacto_caja_wc=ut.suma_listas(delta_caja,delta_wc)
ut.mostrar_cuatro_arrays(años,delta_caja, delta_wc, impacto_caja_wc,"Δ caja","Δ working capital","Caja resto negocio")






########################################### funcion estudio caja -  workin capital ########################
def analyze_cash_quality(delta_cash, delta_wc):
    results = []

    for i in range(len(delta_cash)):
        dc = delta_cash[i]
        dwc = delta_wc[i]

        if i == 0 or dc is None or dwc is None:
            results.append({"type": "N/A"})
            continue

        # impacto del WC en caja
        wc_impact = -dwc  

        # caja que NO viene del WC (“si resto el efecto del working capital, me queda lo que viene del resto del negocio”)
        non_wc_cash = dc - wc_impact  

        # clasificación
        if dc > 0:
            if wc_impact > 0 and non_wc_cash > 0:
                quality = "🟢 Strong (operativo + WC)"
            elif wc_impact > 0 and non_wc_cash <= 0:
                quality = "🟡 WC-driven (potencial maquillaje)"
            elif wc_impact <= 0 and non_wc_cash > 0:
                quality = "🟢 Operativo puro"
            else:
                quality = "🔴 Inconsistente"
        else:
            if wc_impact < 0 and non_wc_cash < 0:
                quality = "🔴 Doble presión (operativo + WC)"
            elif wc_impact > 0 and non_wc_cash < 0:
                quality = "🔴 Negocio débil (WC no compensa)"
            elif wc_impact < 0 and non_wc_cash > 0:
                quality = "🟡 WC enmascara debilidad"
            else:
                quality = "🔴 Débil"

        results.append({
            "Δ_cash": dc,
            "Δ_wc": dwc,
            "Impacto en caja wc": wc_impact,
            "Caja resto negocio": non_wc_cash,
            "quality": quality
        })

    return results



estudio= analyze_cash_quality(delta_caja, delta_wc)
años_dicc=años[1:]


tabla = []

for i in range(1, len(estudio)):
    tabla.append({
        "Año": años_dicc[i],
        "Relacion Working Capital - Caja": estudio[i].get("quality", "-")
    })

df_estudio_wc = pd.DataFrame(tabla)



titulo_con_ventana_informativa2 ("Estudio WC", DEFINICIONES["relacion wc-caja"],"white")



 # Convertir DataFrame a HTML
html_table = df_estudio_wc.to_html(index=False, header=True, table_id="tabla_estudio_wc", escape=False)

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
    }
    </style>
    """

    # Mostrar CSS y tabla
st.markdown(css, unsafe_allow_html=True)
st.markdown(html_table, unsafe_allow_html=True)






###########*************************************fin estudio




inventarios=ex.inventarios(df_balance)
clientes=ex.clientes(df_balance)
proveedores=ex.proveedores(df_balance)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
años=años[1:]
gr.graficar_tres_lineas(inventarios, clientes, proveedores,"#F18F8F","#ECC060","#664158", eje_x=años, etiquetas=("inventarios","clientes","proveedores"), eje_y="factores working capital")

