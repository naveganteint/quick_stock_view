import streamlit as st
import utils.funciones as ut
import modules.Valoracion_Gorka as vg

def app():

    # 🔴 1. ESTADO INICIAL
    if "view" not in st.session_state:
        st.session_state.view = "main"

    # 🔴 2. MENÚ SOLO SI NO ESTÁS EN GORKA
    if st.session_state.view != "gorka":
        estado = ut.menu_valoracion(prefix="val")

        if estado == "gorka":
            st.session_state.view = "gorka"
            st.rerun()

        if estado == "main":
            pass

    # 🔴 3. VISTAS CONTROLADAS
    if st.session_state.view == "gorka":
        vg.app()
        st.stop()

    # 🔴 4. CONTENIDO NORMAL
    st.write("Contenido del módulo de valoración")