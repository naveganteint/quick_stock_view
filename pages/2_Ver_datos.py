import streamlit as st
import numpy as np
from styles.style_utils import aplicar_estilos


aplicar_estilos()



st.markdown("<h1 style='color:#2E8B57;'>Ver datos</h1>", unsafe_allow_html=True)

if "hojas" in st.session_state and st.session_state.hojas:

    for nombre_hoja, df in st.session_state.hojas.items():
        st.markdown(
            f'<h3 style="color: #2E8B57; background-color: #C2DAC1; padding: 5px; border-radius: 5px;">Tabla: {nombre_hoja}</h3>',
            unsafe_allow_html=True
        )

        df_limpio = df.copy()

        df_limpio.columns = df_limpio.columns.map(str)

        df_limpio.replace('—', np.nan, inplace=True)
        df_limpio = df_limpio.infer_objects()

        df_mostrar = df_limpio.astype(str).replace("nan", "-")

        st.table(df_mostrar)

else:
    st.info("Primero carga un archivo en 'Cargar Excel'")

