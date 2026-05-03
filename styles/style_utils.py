import streamlit as st


def aplicar_estilos():
    st.markdown(
        """
        <style>

        /* Fondo sidebar */
        [data-testid="stSidebar"] {
            background-color: white;
        }

        /* Hacer que cada enlace ocupe toda la línea */
        [data-testid="stSidebarNav"] a {
            display: block;
            width: 100%;
            padding: 10px 12px;
            border-radius: 8px;
            transition: all 0.3s ease;
            background-color: #F0E68C;  /* color de fondo constante */
        }

        /* Texto del menú */
        [data-testid="stSidebarNav"] span {
            color: black !important;
            font-weight: bold;
            font-size: 18px;
            
        }

        /* Hover en TODA la línea */
        [data-testid="stSidebarNav"] a:hover {
            background-color: #C2DAC1 !important;
        }

        /* Cambiar color del texto en hover */
        [data-testid="stSidebarNav"] a:hover span {
            color: black !important;
        }

        /* Página seleccionada (activa) */
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background-color: #2E8B57 !important;
        }




        </style>
        """,
        unsafe_allow_html=True

    )




def h3_especial(texto):
    """
    Muestra un título h3 centrado, con texto color #1b3865
    y fondo de la mitad de la pantalla color #DABBED.
    """
    st.markdown(f"""
    <div style="
        width: 70%;                /* ancho del div */
        background-color: #C2DAC1;
        text-align: center;
        padding: 2px 0;            /* padding vertical mínimo */
        margin: 0 auto;             /* centra horizontalmente */
        border-radius: 4px;
    ">
        <span style="
            color: #1b3865;
            font-size: 24px;
            font-weight: bold;
        ">{texto}</span>
    </div>
    """, unsafe_allow_html=True)


def h2_especial(texto):
    """
    Muestra un título h2 centrado, con texto color #7FFF00
    y fondo de la mitad de la pantalla color #DABBED.
    """
    st.markdown(f"""
    <div style="
        width: 30%;                /* ancho del div */
        background-color: lightblue;
        text-align: center;
        padding: 2px 0;            /* padding vertical mínimo */
        margin: 0 auto;             /* centra horizontalmente */
        border-radius: 4px;
    ">
        <span style="
            color: #1b3865;               
            font-size: 16px;
            font-weight: bold;
        ">{texto}</span>
    </div>
    """, unsafe_allow_html=True) 


def texto_multiplo(texto1, texto2):

    st.markdown(f"""
    <div style="
        width: 70%;
        background-color: white;
        text-align: left;
        padding: 10px;
        margin: 0 auto;
        border-radius: 8px;
    ">
        <span style="font-size:16px; color:#1b3865;">
            {texto1}
        </span>
        <span style="font-size:28px; font-weight:bold; color:#1b3865;">
            {texto2}
        </span>
    </div>
    """, unsafe_allow_html=True)

#**********************************************************Tabla 2 ********************************************************


def tabla_2(cadena, numero):
    html = f"""
    <div style="width:300px; margin-left:350px;">
        <table style="border-collapse: collapse;">
            <tr>
                <td style="border:1px solid #DCDCDC; padding: 0px 0px 0px 15px;width:200px;color:gray;font-size: 12px;">{cadena} </td>
                <td style="border:1px solid #DCDCDC; padding: 0px 10px 0px 0px;width:100px;text-align: right;color: #1b3865;background:#DCDCDC;font-size: 14px;">{numero:.2f}</td>
            </tr>
        </table>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)




def tabla_22(cadena, numero):
    html = f"""
    <div style="width:300px; margin-left:400px;">
        <table style="border-collapse: collapse;">
            <tr>
                <td style="border:1px solid gray; padding: 0px 0px 0px 15px;width:200px;color:gray;">{cadena} </td>
                <td style="border:1px solid gray; padding: 0px 10px 0px 0px;width:100px;text-align: right;color: #1b3865;background:#E6E6FA; font-size: 16px;">{numero:.2f}</td>
            </tr>
        </table>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)




def tabla_222(cadena, numero):
    html = f"""
    <div style="width:300px; margin-left:450px;">
        <table style="border-collapse: collapse;">
            <tr>
                <td style="border:1px solid gray; padding: 0px 0px 0px 15px;width:200px;color:gray;font-size: 14px;">{cadena} </td>
                <td style="border:1px solid gray; padding: 0px 10px 0px 0px;width:100px;text-align: right;color: #1b3865;background:#B5CAF2; font-size: 18px;"><b>{numero:.2f}</b></td>
            </tr>
        </table>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)




def tabla_2_1(cadena, numero):
    html = f"""
    <div style="width:300px; margin: 0 auto;">
        <table style="border-collapse: collapse;">
            <tr>
                <td style="border:1px solid #DCDCDC; padding: 0px 0px 0px 15px;width:200px;color:black;font-size: 15px;"><b>{cadena}</b> </td>
                <td style="border:1px solid #DCDCDC; padding: 0px 10px 0px 0px;width:100px;text-align: right;color: #1b3865;background:lightblue;font-size: 14px;">{numero:.2f}</td>
            </tr>
        </table>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)



    