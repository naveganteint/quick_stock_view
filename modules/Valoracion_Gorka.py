import streamlit as st
import analisis.ratios as rt
import utils.funciones as ut
import utils.graficas as gr
import analisis.fuente as ex
from styles.style_utils import aplicar_estilos, h3_especial,h2_especial
import pandas as pd

def app(df_resultado,df_balance,df_flujo,años):
    st.header("📊 Valoración Gorka")
    st.write("Aquí va el análisis de Gorka")


        
    #***************************************************** acciones*********************************************


    fila=ut.buscar_fila(df_resultado, "Shares (Diluted)")
    num_acciones=ut.fila_a_array (df_resultado,fila+1)
    num_acciones_num=rt.convertir_a_numero(num_acciones)


    valor_num_acciones=num_acciones_num[-1]


    #*******************************************************************************************************




    h2_especial("Historial de crecimiento de datos económicos")



    beneficio=ex.beneficio(df_resultado)
    patrimonio=ex.patrimonio(df_balance)
    ventas=ex.ventas(df_resultado)

    dividendo=ex.dividendos(df_flujo)
    bpa=ut.divide_listas(beneficio,num_acciones_num)
    patrimonio=patrimonio
    retained=ex.retained(df_balance)
    activos=ex.activos(df_balance)


    encabezado= ["Ventas","Beneficio","BPA","Patrimonio","Retained","Activos"]
    cagrs = [rt.calcular_cagr(lista) for lista in [ventas, beneficio, bpa, patrimonio,retained, activos]]





    df = pd.DataFrame({
        "Ventas": ventas,
        "Beneficio": beneficio,
        "BPA": bpa,
        "Patrimonio": patrimonio,
        "Retained": retained,
        "Activos": activos
    },


    )



    df.index = años
    df.loc["CAGR"] = cagrs

    # Convertir DataFrame a HTML
    html_table = df.to_html(index=True, header=True, table_id="tabla_4listas", escape=False)

    # CSS para centrar celdas y encabezado
    css = """
        <style>
        table.dataframe#tabla_4listas {
            width: auto;
            border-collapse: collapse;
            margin-left: auto;
            margin-right: auto; /* centra la tabla */
        }

        table.dataframe#tabla_4listas tbody tr{
            background-color: white;
            text-align: center;
            padding: 4px;
        }

        table#tabla_4listas thead th {
            background-color: #D9E6E7;
            text-align: center;
            padding: 4px;
        }

        table.dataframe#tabla_4listas td {
            border: 1px solid #ccc;
        }

        table.dataframe#tabla_4listas tbody tr:last-child td,table.dataframe#tabla_4listas tbody tr:last-child th {
            background-color: #E7D6FC !important;
            font-weight: bold;
        }

            
        </style>
        """

    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)







    h3_especial("Parametros Valoracion")


    st.markdown("""
    <style>
    div[data-testid="stNumberInput"] {
        max-width: 300px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)


    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Inputs base")
            precio_accion = st.number_input("Precio", value=50.0)
            crecimiento = st.number_input("Crecimiento (%)", value=5.00)
            yield_dividendo = st.number_input("Dividendo (%)", value=2.00)

        with col2:
            st.markdown("### Escenarios")
            multiplo_neg = st.number_input("Negativo", value=10)
            multiplo = st.number_input("Normal", value=15)
            multiplo_pos = st.number_input("Positivo", value=20)

    st.write("")

    #*******************************************************valoracion- crecimiento

    h3_especial("Tabla Revalorizacion a 10 años segun escenario")
    st.write("")
    h2_especial("Crecimiento estimado BPA % anual")
    crecimiento_menos = crecimiento - 1.5
    crecimiento_mas = crecimiento + 1.5


    df_crecimiento = pd.DataFrame({
        "Negativo": f"{crecimiento_menos:.2f} %",
        "Esperado": f"{crecimiento:.2f} %",
        "Positivo": f"{crecimiento_mas:.2f} %",
    }, index=["Crecimiento"])
    # Convertir DataFrame a HTML
    html_table = df_crecimiento.to_html(index=True, header=True, table_id="tabla_4listas", escape=False)

    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)




    h2_especial("Beneficio proyectado 10 años")

    bpa_neg= bpa[-1] * ((1+crecimiento_menos/100) ** 10)
    bpa_esperado = bpa[-1] * ((1+crecimiento/100) ** 10)
    bpa_positivo= bpa[-1]* ((1+crecimiento_mas/100) ** 10)



    bpas=[bpa_neg,bpa_esperado,bpa_positivo]

    multiplos=[multiplo_neg,multiplo,multiplo_pos]



    df_bpa = pd.DataFrame({
        "BPA negativo": round(bpa_neg,2),
        "BPA normal": round(bpa_esperado,2),
        "BPA positivo": round(bpa_positivo,2),
    }, index=["BPA"])
    # Convertir DataFrame a HTML
    html_table = df_bpa.to_html(index=True, header=True, table_id="tabla_4listas", escape=False)

    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)


    precios = [round(a * b,2) for a in multiplos for b in bpas]



    def revalorizacion_anual(valor_inicial, lista, años=10):
        resultado = []

        for valor_final in lista:
            if isinstance(valor_final, (int, float)) and valor_inicial != 0:
                
                tasa = (valor_final / valor_inicial) ** (1 / años)-1
            
                resultado.append(tasa)
            else:
                resultado.append(None)

        return resultado


    revalorizacion= revalorizacion_anual(precio_accion,precios)

    revalorizacion_texto= [f"{x*100:.2f} %" if x is not None else "-" for x in revalorizacion]


    yield_lista=10*[yield_dividendo]
    yield_lista=[x/100 for x in yield_lista]
    revalorizacion_div = ut.suma_listas(revalorizacion,yield_lista)
    revalorizacion_div=[x*100 for x in revalorizacion_div]


    revalorizacion_div_texto= [f"{x:.2f} %" if x is not None else "-" for x in revalorizacion_div]

    columna_crecimiento= [crecimiento_menos,crecimiento,crecimiento_mas,crecimiento_menos,crecimiento,crecimiento_mas,crecimiento_menos,crecimiento,crecimiento_mas]
    columana_escenario=[multiplo_neg,multiplo_neg,multiplo_neg,multiplo,multiplo,multiplo,multiplo_pos,multiplo_pos,multiplo_pos]


    df_revalorizacion = pd.DataFrame({
        "Escenario":columana_escenario,
        "Crecimiento":columna_crecimiento,
        "Precio Revalorizado": precios,
        "Rev. anual": revalorizacion_texto,
        "Rev. con dividendos": revalorizacion_div_texto,
    })
    # Convertir DataFrame a HTML
    html_table = df_revalorizacion.to_html(index=False, header=True, table_id="tabla_rev", escape=False)


    css = """
        <style>
        table.dataframe#tabla_rev {
            width: auto;
            border-collapse: collapse;
            margin-left: auto;
            margin-right: auto; /* centra la tabla */
        }

        table.dataframe#tabla_rev tbody tr{
            background-color: white;
            text-align: center;
            padding: 4px;
        }

        table#tabla_rev thead th {
            background-color: #D9E6E7;
            text-align: center;
            padding: 4px;
        }

        table.dataframe#tabla_rev td {
            border: 1px solid #ccc;
        }

        table.dataframe#tabla_rev tbody tr:last-child th {
            background-color: #E7D6FC !important;
            font-weight: bold;
        }

        table.dataframe#tabla_rev tbody tr:nth-child(5) td {
        background-color: #E7D6FC;
    }


            
        </style>
        """




    # Mostrar CSS y tabla
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)









