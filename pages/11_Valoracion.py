import streamlit as st

import analisis.ratios as rt
import utils.funciones as ut
import utils.graficas as gr

import pandas as pd
import analisis.fuente as ex
from styles.style_utils import aplicar_estilos, h3_especial,tabla_2,tabla_22,tabla_222,h2_especial,tabla_2_1

import modules.Valoracion_Gorka as vg
import modules.Valoracion_Guillen as vgu
import modules.Valoracion_General as vgg






# 🔴 IMPORTANTE: inicializar siempre
if "view" not in st.session_state:
    st.session_state.view = "main"



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
st.write("")


#*************************************** menu valoracion *********************

# 🔴 1. Estado inicial
if "view" not in st.session_state:
    st.session_state.view = "main"


# 🔴 CSS botones
st.markdown("""
<style>
div.stButton > button {
    width: 150px;
    font-size: 16px;
    background-color: #F0E68C;   /* fondo */
    color: black;                /* texto */
    border: 2px solid #4CAF50;   /* borde */
    border-radius: 8px;          /* esquinas redondeadas */
    padding: 8px 10px;
    font-weight: bold;
        
}

/* 🔵 Hover (cuando pasas el ratón) */
div.stButton > button:hover {
    background-color: #C2DAC1;
    color: black;
    border: 2px solid #1b3865;
}
</style>
""", unsafe_allow_html=True)










# 🔴 2. MENÚ (siempre visible)
esp1,esp2,col3, col4, col5,col6,esp7,esp8 = st.columns(8)

if col4.button("General"):
    st.session_state.view = "general"

if col5.button("Gorka"):
    st.session_state.view = "gorka"

if col6.button("Guillen"):
    st.session_state.view = "guillen"

if col3.button("inicio"):
    st.session_state.view = "main"   




st.markdown('<hr style="border-top: 2px solid #4CAF50;">', unsafe_allow_html=True)


# 🔴 3. CONTENIDO (solo uno se muestra)
if st.session_state.view == "gorka":
    vg.app(df_resultado,df_balance,df_flujo,años)

elif st.session_state.view == "guillen":
    vgu.app()

elif st.session_state.view == "general":
    vgg.app(df_resultado,df_balance,df_flujo,años)


else:
 
    st.markdown(
        '<h3 style="text-align: center; color: #1b3865; margin-top: 10px;">¿Qué tipo de valoración quieres utilizar?</h3>',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
        """,
        unsafe_allow_html=True
        )

    st.write("")

    st.markdown(
        """
        <div style="text-align: center; margin: 5px;">
            <i class="bi bi-graph-up" style="font-size: 160px; color: #2E8B57;"></i>
        </div>
        """,
        unsafe_allow_html=True
    )



