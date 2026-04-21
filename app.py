import streamlit as st

from styles.style_utils import aplicar_estilos


aplicar_estilos()
st.set_page_config(
    page_title="Quick stock view",
    layout="wide"
)




# Inicializar session_state global
if "hojas" not in st.session_state:
    st.session_state.hojas = {}





st.markdown('<h1 style="text-align: center;color: #2E8B57;">Quick Stock View </h1>', unsafe_allow_html=True)


st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <div style="text-align: center; margin: 20px;">
        <i class="bi bi-clipboard2-data" style="font-size: 200px; color: #2E8B57;"></i>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

st.markdown(
    """
    <div style="
        background-color: white;
        color: #2E8B57;
        padding: 15px;
        font-size: 20px;
        text-align: center;
    ">
        Pagina inicial de la aplicacion de analisis de las cuentas de la empresas
    </div>
    """,
    unsafe_allow_html=True
)


