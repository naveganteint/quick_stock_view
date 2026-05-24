# definiciones.py
DEFINICIONES = {
    "ccr": """
Cash Conversion Rate (CCR)<BR>
Mide qué porcentaje del beneficio (normalmente EBITDA o beneficio neto) se convierte en flujo de caja real.<BR>
Indica la eficiencia con la que la empresa transforma sus ganancias contables en dinero disponible.<BR><BR>
💡 En general, cuanto más cercano o superior al 100%, mejor es la capacidad de generar caja,<BR> >90% → excelente,<BR> 70–90% → buena,<BR> 50–70% → media,<BR> <50% → baja calidad<BR><BR>
✅Un CCR alto sugiere buena calidad del beneficio y buena gestión del circulante.<BR>
⚠️ La diferencia entre EBITDA y FCO suele venir del capital circulante (clientes, inventarios y proveedores), gastos en
 inversiones y de los impuestos, que ajustan el beneficio contable hasta convertirlo en caja real, es decir, un CCR bajo puede indicar problemas de cobro, exceso de inventarios o fuertes inversiones (capex) que consumen efectivo y reducen la conversión de beneficios en liquidez.
<BR><BR>Un CCR bajo no siempre es malo: puede ser estacional (ej. retail), o por crecimiento (más inventario = más ventas futuras), o por inversión puntual.
Un CCR bajo solo es preocupante si es persistente y no está justificado por crecimiento o ciclo del negocio. En muchos casos, puede ser simplemente una fase normal de expansión o estacionalidad.
""",


    "wc": """
Es el dinero que la empresa necesita para operar en el corto plazo.<BR>
<BR>
Se calcula como:<BR>
Working Capital= Activo corriente −  Pasivo corriente<BR>
<BR>
🔍Incluye:<BR>
	🟢 Activo corriente, Inventarios (stock), Clientes (dinero que te deben), caja (a veces se excluye en análisis operativo)<BR>
	🔴 Pasivo corriente, Proveedores (a quién debes), Deudas a corto plazo, Otros pagos pendientes <BR>
<BR>
Cómo afecta a la caja<BR>
El working capital es un uso o liberación de caja:<BR>
🔹 Si aumenta el working capital<BR>
👉 consumes caja ❌, Ejemplos: más inventario, clientes pagan más tarde<BR>
🔹 Si disminuye el working capital<BR>
👉 liberas caja ✅, Ejemplos: reduces stock, cobras antes, pagas más tarde a proveedores<BR>
<BR>
Relación con el FCO<BR>
FCO=Beneficio+Ajustes-ΔWorkingCapital<BR>
👉 Es decir: si el WC sube → resta caja, si baja → suma caja <BR>

<BR>
Factores que afectan el working capital:<BR>
El capital de trabajo de una empresa no es estático, sino que varía con el tiempo en función de distintos factores, como:<BR>
	Gestión del inventario: Un exceso de stock inmoviliza capital, mientras que un inventario demasiado ajustado puede afectar la capacidad de venta.<BR>
	Plazos de cobro y pago: Si la empresa tarda demasiado en cobrar a sus clientes pero debe pagar a proveedores en plazos muy cortos, el working capital se verá afectado.
	<BR>Crecimiento del negocio: A medida que una empresa crece, sus necesidades de capital circulante aumentan, por lo que es fundamental gestionar bien los recursos.
	<BR>Condiciones del mercado: Factores como la inflación, cambios en la demanda o crisis económicas pueden afectar la liquidez de una empresa y, por ende, su capital de trabajo.
""",





"relacion wc-caja":
"""
➕➕➕ CAJA CRECE (Δcaja > 0)<BR>
La empresa está generando caja, pero lo importante es: ¿de dónde viene?<BR>

<BR><BR>🟢CASO 1: “Strong (operativo + WC)”
 •Δ WC < 0 → el WC genera caja 
 •Resto negocio > 0 → el negocio también genera caja
✔Es el mejor escenario posible, crecimiento sano y alta calidad de caja

<BR><BR>🟡CASO 2: “WC-driven (potencial maquillaje)”
•	Δ WC < 0 → el WC genera caja 
•	Resto negocio ≤ 0 → el negocio NO genera caja 

La caja viene del working capital, no del negocio. Esto es clave: puede ser temporal, pero no es sostenible. La empresa “parece líquida”, pero el negocio no funciona bien

<BR><BR>🟢CASO 3: “Operativo puro”
•	Δ WC > 0 → el WC no ayuda (incluso consume) 
•	Resto de negocio > 0 → el negocio genera caja 

El negocio es fuerte y genera caja por sí mismo. Muy buena señal:
•	no depende del balance 
•	caja de alta calidad 

<BR><BR>🔴CASO 4: “Inconsistente”
•	combinaciones raras, Interpretación: Los datos no cuadran bien o hay efectos externos fuertes (deuda, extraordinarios, etc.)

<BR><BR>➖➖➖CAJA CAE (Δcaja < 0)

<BR><BR>🔴CASO 5: “Doble presión (operativo + WC)”
•	Δ WC > 0 → el WC consume caja 
•	Resto del negocio < 0 → el negocio también consume

Todo va mal a la vez.  Muy peligroso el negocio quema caja  y además el circulante empeora. ➡ riesgo real de liquidez


<BR><BR>🔴CASO 6: “Negocio débil (WC no compensa)”
•	Δ WC < 0 →  el WC ayuda generando caja
•	Resto del negocio < 0 → el negocio destruye caja 

El negocio es malo y ni siquiera el WC lo salva, Señal clara: modelo débil y problemas estructurales 


<BR><BR>🟡CASO 7: “WC enmascara debilidad”
•	Δ WC > 0 → el WC consume caja 
•	non_wc_cash > 0 → el negocio genera caja 

PERO la caja total cae,  Interpretación: El negocio funciona bien pero el working capital se lo “come”. (crecimiento mal gestionado, aumento de inventarios, empeoramiento en cobros). Riesgo operativo, no estructural

<BR><BR>🔴CASO 8: “Débil”
Caso residual, Interpretación: pérdida de caja sin drivers claros o mezcla de problemas



""",


"ISGR":
"""

ISGR = ΔInventario  / ΔVentas   (Inventory-to-Sales Growth Ratio)<BR>

La relación entre ventas e inventarios generan 4 escenarios básicos:

<BR><BR>🟢 CASO 1 — VENTAS ↑ + INVENTARIOS ↓ --> “EFICIENCIA OPERATIVA”
<BR>Qué está pasando: La empresa vende más y reduce stock.
<BR>Interpretación económica: alta rotación de inventarios, demanda fuerte o gestión muy eficiente no hay acumulación de productos
<BR>🌱 Sub-árbol ISGR:
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔵 ISGR < 0, 👉 eficiencia extrema, 👉 se vende muy rápido el stock
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟢 ISGR entre 0 y 1, 👉 crecimiento sano y equilibrado
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟡 ISGR > 1, 👉 posible infra-stock, 👉 riesgo de quedarse sin producto

<BR><BR>🟡 CASO 2 — VENTAS ↑ + INVENTARIOS ↑ --> 👉 “CRECIMIENTO CON ACUMULACIÓN”
<BR>Qué está pasando: La empresa crece, pero acumula inventario.
<BR>Interpretación económica: expansión del negocio, producción anticipada, posible exceso de optimismo
<BR>🌱 Sub-árbol ISGR:
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟢 ISGR < 1, 👉 crecimiento equilibrado
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ ISGR 1–2, 👉 tensión de crecimiento, 👉 inventarios empiezan a presionar
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🚨 ISGR > 2, 👉 sobreexpansión, 👉 riesgo de exceso de stock

<BR><BR>🔴 CASO 3 — VENTAS ↓ + INVENTARIOS ↑ --> 👉 “DETERIORO OPERATIVO”
<BR>Qué está pasando: La empresa vende menos pero acumula más stock.
<BR>Interpretación económica: caída de demanda, mala previsión, productos que no rotan
<BR>🌱 Sub-árbol ISGR:
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🚨 ISGR < 0, 👉 destrucción de demanda, 👉 deterioro fuerte
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔴 ISGR 0–1, 👉 deterioro progresivo, 👉 stock atrapado
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;💥 ISGR > 1, 👉 colapso operativo, 👉 grave desalineación negocio-mercado

<BR><BR>🟠 CASO 4 — VENTAS ↓ + INVENTARIOS ↓ --> 👉 “CONTRACCIÓN DEL NEGOCIO”
<BR>Qué está pasando: La empresa reduce ventas y reduce inventario al mismo tiempo.
<BR>Interpretación económica: ajuste de tamaño, reducción de actividad, fase de contracción del ciclo empresarial
<BR>🌱 Sub-árbol ISGR:
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟡 ISGR < 0, 👉 ajuste eficiente, 👉 limpieza ordenada del negocio
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟠 ISGR 0–1, 👉 contracción normal,👉 reducción controlada
	<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔴 ISGR > 1, 👉 contracción desordenada, 👉 caída con tensión operativa

""",

"relacion deuda-caja":

"""
Este análisis muestra la relación entre la variación de la caja y la emision de deuda neta .

<BR>El objetivo es entender si la deuda está realmente generando liquidez o si se está utilizando sin reflejarse en caja.

<BR>Se comparan tres variables:
<BR>- Δ Caja: variación real de la liquidez de la empresa
<BR>- Net Issuance of Debt: entrada o salida neta de financiación mediante deuda
<BR>- Δ Deuda neta: cambio total del endeudamiento

<BR>A partir de estas variables se evalúa la calidad del uso de la deuda:

<BR><BR>🟢 ESCENARIO SANO
<BR>La emisión de deuda se traduce en un aumento proporcional de caja.
<BR>La financiación se convierte en liquidez real y controlada.

<BR><BR>🟡 ESCENARIO INTERMEDIO
<BR>La empresa emite deuda pero la caja aumenta de forma limitada.
<BR>Esto indica que parte de la financiación se está utilizando en inversión o en la operativa del negocio.

<BR><BR>🔴 ESCENARIO PELIGROSO
<BR>La empresa se endeuda pero la caja disminuye.
<BR>Esto sugiere que la deuda no está generando liquidez, sino que se está utilizando para cubrir necesidades operativas o pérdidas.

<BR><BR>🚨 ESCENARIO CRÍTICO
<BR>La deuda neta crece más rápido que la emisión de deuda.
<BR>Esto indica presión financiera: la caja se está reduciendo más de lo que la deuda explica, señal de deterioro de liquidez.

<BR><BR>En conjunto, este análisis permite evaluar si la deuda está fortaleciendo la posición de liquidez o si está siendo absorbida sin generar caja.

"""








}