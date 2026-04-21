
import streamlit as st
import pandas as pd
import numpy as np



#***************************** Calcular EPS y formula similares

def dividir_listas(beneficios, acciones):
    """
    Calcula el beneficio por acción (EPS).

    Parámetros:
    - beneficios: lista de beneficios netos
    - acciones: lista de número de acciones

    Retorna:
    - lista con el EPS para cada elemento
    """

    if len(beneficios) != len(acciones):
        raise ValueError("Las listas deben tener la misma longitud")

    eps = []

    for b, a in zip(beneficios, acciones):
        if a == 0:
            eps.append(None)  # evitar división por cero
        else:
            eps.append(round(float(b / a), 4))

   
    return eps



#*********************** promedio lista ***********************************************

def promedio(lista):
    valores = []

    for x in lista:
        try:
            valores.append(float(x))
        except:
            continue

    return sum(valores) / len(valores) if valores else None


#*********************** calcular cagr ***********************************************



def calcular_cagr(lista):
    """
    Calcula el CAGR (tasa de crecimiento anual compuesto)
    entre el primer y último valor de una lista.
    """

    # Validaciones
    if not lista or len(lista) < 2:
        raise ValueError("La lista debe tener al menos 2 valores")

    valor_inicial = lista[0]
    valor_final = lista[-1]
    n = len(lista)

    if valor_inicial == 0:
        valor_inicial=0.01

    # Fórmula CAGR
    cagr = (valor_final / valor_inicial) ** (1 / (n - 1)) - 1

    cagr = f"{cagr*100:.2f} %"


    return cagr


#********************************************tax ratio **********************************


def calculo_tasa(beneficios_a_i, impuesto):
    """
    Calcula el tax rate (tasa de impuesto)

   
    """

    if len(beneficios_a_i) != len(impuesto):
        raise ValueError("Las listas deben tener la misma longitud")

    tax_rate = []

    for a, b in zip(beneficios_a_i, impuesto):
        if a == 0:
            tax_rate.append(None)  # evitar división por cero
        else:
            if a > 0:
                if b > 0:
                    tax_rate.append(round(b/a, 2))
                else:
                    tax_rate.append(round(0.25, 2))                   
            else:
                    tax_rate.append(round(0, 2))     
                 
   
    return tax_rate




#**************************************** Calcular nopat *******************************
def calcular_nopat(lista1, lista2):
    """

    """

    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud")

    resultado = []

    for b, a in zip(lista1, lista2):
            resultado.append(round(b * (1-a) , 2))

   
    return resultado




#************************** convertir a numero B o M ************************************************************


def convertir_a_numero(lista):
    """
    Convierte valores tipo '1.7B', '500M', etc. a números reales.
    B = miles de millones
    M = millones
    """
    
    resultado = []

    for x in lista:
        if isinstance(x, str):

            if x.endswith("B"):
                valor = float(x[:-1]) * 1_000

            elif x.endswith("M"):
                valor = float(x[:-1]) * 1

            else:
                valor = float(x)

        else:
            valor = x

        resultado.append(valor)

    return resultado

