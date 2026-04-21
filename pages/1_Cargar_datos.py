import streamlit as st
import pandas as pd
import numpy as np
from styles.style_utils import aplicar_estilos


aplicar_estilos()


st.markdown("<h1 style='color:#2E8B57;'>Cargar archivo excel</h1>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Selecciona tu archivo Excel", type=["xlsx"])

if uploaded_file:
    xls = pd.ExcelFile(uploaded_file)
    st.session_state.hojas = {}

    nombres_fijos = ["resultado", "balance", "flujo"]

    for i, sheet_name in enumerate(xls.sheet_names):
        if i < len(nombres_fijos):

            df = xls.parse(sheet_name)

            # limpieza
            df.columns = df.columns.map(str)
            df = df.replace('—', np.nan)
            df = df.infer_objects()

            st.session_state.hojas[nombres_fijos[i]] = df

    st.success(f"Se cargaron {len(st.session_state.hojas)} hojas: resultado, balance, flujo")