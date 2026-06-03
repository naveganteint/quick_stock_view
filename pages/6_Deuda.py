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
    '<h1 style="text-align: center; color: #1b3865; margin-top: -40px;">Deuda</h1>',
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







#***********************************************Deuda neta- Ebitda *****************

h3_especial("Deuda neta - Ebitda")



deuda_neta= ex.deuda_neta(df_balance)


ebitda=ex.ebitda(df_resultado)


gr.graficar_2barras (deuda_neta, ebitda, 
                     color1="#B43838", color2="#52923E",
                     eje_x=años,
                     etiquetas=("deuda neta","ebitda"),
                     eje_y="Valores")



ratio=ut.divide_listas(deuda_neta,ebitda)


ut.mostrar_tabla_4_listas (años, deuda_neta, ebitda, ratio, "Deuda neta","Ebitda","Ratio Deuda neta/Ebitda")
gr.graficar_una_linea (ratio, "#B43838", eje_x=años, etiqueta="Ratio Deuda neta/Ebitda", eje_y="Ratio")



#***********************************************Deuda neta - cfo *****************

h3_especial("Deuda neta- Flujo de caja operativo")


fco=ex.FCO(df_flujo)
ratio=ut.divide_listas(deuda_neta,fco)


gr.graficar_2barras (deuda_neta, fco, 
                     color1="#B43838", color2="#C296C4",
                     eje_x=años,
                     etiquetas=("deuda","fco"),
                     eje_y="Valores")


ut.mostrar_tabla_4_listas (años, deuda_neta, fco, ratio, "Deuda neta","fco","Ratio Deuda neta/fco")
gr.graficar_una_linea (ratio, "#B43838", eje_x=años, etiqueta="Ratio Deuda/Ebitda", eje_y="Ratio")




#*********************************************** Deuda neta *****************

h3_especial("Deuda neta")

fila=ut.buscar_fila(df_balance, "Short-Term Debt")
try:
    current_debt=ut.fila_a_array (df_balance,fila+1)
except :
    current_debt= 10* [0]

current_debt=ut.limpiar_a_numeros(current_debt)



fila=ut.buscar_fila(df_balance, "Capital Leases (Current)")
try:
    current_lease=ut.fila_a_array (df_balance,fila+1)
except :   
    current_lease= 10* [0]

current_lease=ut.limpiar_a_numeros(current_lease)


fila=ut.buscar_fila(df_balance, "Long-Term Debt")
long_debt=ut.fila_a_array (df_balance,fila+1)
long_debt=ut.limpiar_a_numeros(long_debt)




long_lease=ex.long_lease(df_balance)



fila=ut.buscar_fila(df_balance, "Cash & Equivalents")
caja=ut.fila_a_array (df_balance,fila+1)
caja=ut.limpiar_a_numeros(caja)

cero = [0] * 10

#ut.mostrar_dos_arrays(años, current_debt)
#ut.mostrar_dos_arrays(años, current_lease)
#ut.mostrar_dos_arrays(años, long_debt)
#ut.mostrar_dos_arrays(años, long_lease)



deuda =ut.sumar_cinco_listas(current_debt, current_lease, long_debt, long_lease, cero)
deuda_neta = [
    (a if isinstance(a, (int, float)) else 0) -
    (b if isinstance(b, (int, float)) else 0)
    for a, b in zip(deuda, caja) ]



gr.graficar_tres_lineas(deuda, caja, deuda_neta,"pink","lightgreen","red", eje_x=años, etiquetas=("Deuda","Caja","Deuda_neta"), eje_y="Deuda neta")

ut.crear_tabla_4_listas(años, deuda, caja, deuda_neta, "Deuda","Caja","Deuda neta")

st.write("")


#*************************************************************************************************************
#***************************************************** Intereses / Ebit ************************************
#*************************************************************************************************************


h3_especial("Ratio de cobertura( ebit/ intereses)")

ebit=ex.beneficio_operativo(df_resultado)
intereses=ex.intereses(df_resultado)
intereses= [round(-x,2) if isinstance(x, (int, float)) else x for x in intereses]




gr.graficar_2barras (ebit, intereses, 
                     color1="#52923E", color2="#E6C302",
                     eje_x=años,
                     etiquetas=("ebit","intereses"),
                     eje_y="Valores")


ratio_intereses_ebit=ut.divide_listas(intereses, ebit)
#ratio_intereses_ebit= [ round(100*x,2) if isinstance(x, (int, float)) else x for x in ratio_intereses_ebit]





ut.mostrar_tres_arrays (años,ebit,intereses,"ebit","intereses")
años=años[1:]





ratio_intereses_ebit = [
    f"{x*100:.2f} %" if isinstance(x, (int, float)) and x is not None else "-"
    for x in ratio_intereses_ebit
]


ut.mostrar_dos_arrays_texto (años,ratio_intereses_ebit,"% intereses/ebit")


















#****************************************************** Coste de la deuda **********************************************
h3_especial(" Coste de la deuda")





try:
    coste_deuda= [
        round((a if isinstance(a, (int, float)) else 0) /
        (b if isinstance(b, (int, float)) else 0),4)
        for a, b in zip(intereses, deuda)
    ]
except:
    coste_deuda=10*[1]

coste_deuda = [round(100*x,2) if isinstance(x, (int, float)) else x for x in coste_deuda]

lim_sup= 10 * [6]
lim_inf= 10 * [4]
gr.graficar_tres_lineas(coste_deuda, lim_sup, lim_inf,"#3B3C42","coral","lightgreen", eje_x=años, etiquetas=("tipo interes medio deuda %","limite con riesgo","limite_sano"), eje_y="Coste de la deuda")

ut.crear_tabla_4_listas(años, intereses, deuda, coste_deuda, "Intereses","Deuda","Coste deuda %")
st.write("")



#*********************************************** caja *****************

h3_especial("caja")

fcf=ex.FCF(años,df_flujo,0)
deuda_neta=ex.deuda_neta(df_balance)
delta_deuda_neta=ut.variacion_absoluta (deuda_neta)
caja=ex.caja(df_balance)


caja_anterior=caja[:-1]
caja_anterior.insert(0,0)
variacion_caja= ut.resta_listas(caja,caja_anterior)
variacion_caja[0] = "-"
emision_deuda=ex.pago_deuda(df_flujo)

activos=ex.activos(df_balance)
por_activos=ut.divide_listas(caja,activos)
por_activos=[round (x*100,0) for x in por_activos]
por_activos=[f"{x:.0f} %" for x in por_activos]


gr.grafica_columnas(años,caja,"Años","Caja","#83F068")
cagr=rt.calcular_cagr(caja)
ut.mostrar_tres_arrays_texto(años,  caja ,por_activos,"Caja","Porcentaje de los activos")
ut.mostrar_dos_arrays_texto (años,variacion_caja,"variacion Caja")
ut.mostrar_tabla_tres_celdas("CAGR", "Caja", cagr)

st.write("")
st.write("")
st.write("")




titulo_con_ventana_informativa ("Relación deuda con caja", DEFINICIONES["relacion deuda-caja"])



delta_deuda_neta = [float(x) if x != "-" else 0 for x in delta_deuda_neta]

gr.grafica_columnas(años,deuda_neta,"Años","Deuda neta","#E95151")
cagr=rt.calcular_cagr(deuda_neta)

variacion_por=ut.variacion_porcentual(deuda_neta)

#ut.mostrar_dos_arrays_texto (años,delta_deuda_neta,"variacion deuda")
ut.mostrar_tres_arrays_texto(años,delta_deuda_neta,variacion_por,"Δ Deuda_neta","Δ Porcentual")

ut.mostrar_tabla_tres_celdas("CAGR", "Deuda_neta", cagr)




def analizar_deuda_vs_caja(delta_cash, net_debt_issuance, delta_net_debt=None):

    def safe_float(x):
        try:
            if x == "-" or x is None:
                return None
            return float(x)
        except:
            return None

    def direction(x):
        if x is None:
            return "→"
        if x > 0:
            return "↑"
        if x < 0:
            return "↓"
        return "→"

    resultados = []

    n = len(delta_cash)

    for i in range(n):

        # -----------------------
        # LIMPIEZA
        # -----------------------
        dc = safe_float(delta_cash[i])
        ndi = safe_float(net_debt_issuance[i])
        dnd = safe_float(delta_net_debt[i]) if delta_net_debt is not None else None

        if dc is None or ndi is None:
            resultados.append({
                "icono": "⚪",
                "explicacion": "Dato no disponible o inválido para este año",
                "Δ caja": "→",
                "Emision Deuda": "→",
                "Δ Deuda neta": "→"
            })
            continue

        gap = (dnd - ndi) if dnd is not None else None

        icono = "🟡"
        explicacion = "Sin clasificación"

        # -----------------------
        # DIRECCIONALIDAD
        # -----------------------
        delta_cash_dir = direction(dc)
        emission_debt_dir = direction(ndi)
        delta_net_debt_dir = direction(dnd)

        # =========================================================
        # CASO CON Δ DEUDA NETA
        # =========================================================
        if dnd is not None:

            if dnd < 0:

                if dc > 0:
                    icono = "🟢"
                    explicacion = "Reduce deuda y genera caja (autofinanciación fuerte)"

                elif dc < 0:
                    icono = "🟡"
                    explicacion = "Reduce deuda consumiendo caja"

                else:
                    icono = "🟡"
                    explicacion = "Reduce deuda sin efecto en caja"

            elif dnd > 0:

                if gap is not None and gap > 0:
                    icono = "🚨"
                    explicacion = "Crecimiento de deuda neta superior a emisión → presión de caja"

                else:

                    if dc > 0:
                        icono = "🟡"
                        explicacion = "Emite deuda y aumenta caja"

                    elif dc < 0:
                        icono = "🚨"
                        explicacion = "Se endeuda pero pierde caja"

                    else:
                        icono = "🟡"
                        explicacion = "Aumento de deuda sin impacto en caja"

            else:

                if dc > 0:
                    icono = "🟢"
                    explicacion = "Caja positiva sin cambio de deuda"

                elif dc < 0:
                    icono = "🟡"
                    explicacion = "Caja negativa sin cambio de deuda"

                else:
                    icono = "🟡"
                    explicacion = "Estabilidad total"

        # =========================================================
        # CASO SIN Δ DEUDA NETA
        # =========================================================
        else:

            if ndi > 0:

                if dc > 0:
                    icono = "🟢"
                    explicacion = "Emite deuda con mejora de caja"
                else:
                    icono = "🚨"
                    explicacion = "Emite deuda sin soporte en caja"

            elif ndi < 0:

                if dc >= 0:
                    icono = "🟢"
                    explicacion = "Reduce deuda con generación de caja"
                else:
                    icono = "🟡"
                    explicacion = "Reduce deuda consumiendo caja"

            else:

                if dc > 0:
                    icono = "🟢"
                    explicacion = "Caja positiva sin deuda"
                else:
                    icono = "🟡"
                    explicacion = "Neutral"

        resultados.append({
            "icono": icono,
            "explicacion": explicacion,
            "Δ caja": delta_cash_dir,
            "Emision Deuda": emission_debt_dir,
            "Δ Deuda neta": delta_net_debt_dir
        })

    return resultados





#delta_caja_neta=ut.variacion_absoluta (deuda_neta)


estudio_deuda=analizar_deuda_vs_caja(variacion_caja, emision_deuda, delta_deuda_neta)

variacion_caja_por=ut.variacion_porcentual(caja)
variacion_emitida=ut.variacion_porcentual(emision_deuda)

data=[]

for i in range(len(estudio_deuda)):

    icono = estudio_deuda[i]["icono"]
    exp = estudio_deuda[i]["explicacion"] 
    var_deuda= estudio_deuda [i]["Δ Deuda neta"] 
    var_caja= estudio_deuda [i]["Δ caja"] 
    emi_deuda= estudio_deuda [i]["Emision Deuda"] 
    var_deuda_por=variacion_por[i]
    var_caja_por=variacion_caja_por[i]
    var_emitida=variacion_emitida[i]




    data.append({
        "Año": años[i] if i < len(años) else i,
        
        "Deuda neta": var_deuda,
        "Δ Deuda neta %": var_deuda_por,
        "Estado": icono,
        "Explicación": exp,
        "Δ Caja": var_caja,
        "Δ Caja %": var_caja_por,

        "Δ Emision": emi_deuda,

        #"Δ Emision": var_emitida,
        })

df_deuda = pd.DataFrame(data)


 # Convertir DataFrame a HTML
html_table = df_deuda.to_html(index=False, header=True, table_id="tabla_estudio_wc", escape=False)

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


var_emision_deuda=ut.variacion_absoluta(emision_deuda)

var_emision_deuda = [float(x) for x in var_emision_deuda if x != "-"]

st.write("")
st.write("")
st.write("")

gr.graficar_2barras (variacion_caja[1:], var_emision_deuda, 
                     color1="#85EB9F", color2="#DB7979",
                     eje_x=años[1:],
                     etiquetas=( "Δ Caja","Δ Deuda Emitida"),
                     eje_y="Valores")

dif=ut.resta_listas(variacion_caja[1:],var_emision_deuda)

ut.mostrar_cuatro_arrays(años[1:],variacion_caja[1:],var_emision_deuda,dif,"Δ Caja","Δ Deuda Emitida","Diferencia")


dif2=ut.suma_listas(delta_deuda_neta[1:],dif)
ut.mostrar_tres_arrays_texto(años[1:],delta_deuda_neta[1:],dif2,"Δ Deuda_neta","comp con CyE")