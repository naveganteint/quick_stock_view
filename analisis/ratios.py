
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

    if not lista or len(lista) < 2:
        return "N/A"

    valor_inicial = lista[0]
    valor_final = lista[-1]
    n = len(lista)

    if valor_inicial == 0:
        return "N/A"

    # 🔴 Casos especiales
    if valor_inicial < 0 and valor_final > 0:
        return "Calculo no posible, comienza en (neg) 📈"

    if valor_inicial > 0 and valor_final < 0:
        return "Calculo no posible, termina en (Neg) 📉"

    if valor_inicial < 0 and valor_final < 0:
        return "Calculo no posible, termina en (Neg) 📉"

    # 🟢 Caso normal
    cagr = (valor_final / valor_inicial) ** (1 / (n - 1)) - 1

    return f"{cagr*100:.2f} %"


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




#******* Calcular margenes % *************************************************************



def dividir_y_convertir_a_porcentaje(lista1, lista2):
    """
    Divide cada elemento de lista1 entre el correspondiente de lista2,
    multiplica el resultado por 100 y devuelve una nueva lista.
    
    Parámetros:
    - lista1: primera lista de números
    - lista2: segunda lista de números (debe tener la misma longitud que lista1)
    
    Retorna:
    - lista de resultados en porcentaje
    """
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud")

    resultados = []
    for a, b in zip(lista1, lista2):
        if b == 0:
            resultados.append(None)  # evitar división por cero
        else:
            resultados.append(round((a / b) * 100, 2))
    return resultados

