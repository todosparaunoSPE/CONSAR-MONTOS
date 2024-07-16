# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 08:24:41 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd

# Cargar el archivo Excel
file_path = 'saldos-copia.xlsx'
xls = pd.ExcelFile(file_path)

# Cargar datos de las hojas
df_recibidos = pd.read_excel(xls, sheet_name='montos recibidos')
df_cedidos = pd.read_excel(xls, sheet_name='montos cedidos')

# Listar fechas únicas de cada hoja
fechas_recibidos = df_recibidos['Fecha-Texto'].unique()
fechas_cedidos = df_cedidos['Fecha-Texto'].unique()

# Título de la aplicación
st.title("CONSAR: Comparación de Montos Recibidos y Cedidos")

# Sección de ayuda
st.sidebar.title("Ayuda")
st.sidebar.write("""
Esta aplicación permite comparar montos recibidos y cedidos en diferentes fechas. Sigue estos pasos:
1. Selecciona una fecha de la lista de 'montos recibidos'.
2. Selecciona una fecha de la lista de 'montos cedidos'.
3. Observa los datos completos de cada categoría.
4. Visualiza los datos filtrados según las fechas seleccionadas.
5. Compara los montos recibidos y cedidos por 'Descripción del Concepto'.
6. Observa la diferencia entre los montos recibidos y cedidos.

Las columnas mostradas en el resultado final son:
- Descripción del Concepto: El concepto del monto.
- Fecha-Texto_recibido: La fecha seleccionada de montos recibidos.
- Fecha-Texto_cedido: La fecha seleccionada de montos cedidos.
- Diferencia: La diferencia entre los montos recibidos y cedidos.
""")

# Mostrar dataframes de los datos completos
st.write("Datos completos de 'montos recibidos':")
st.dataframe(df_recibidos)

st.write("Datos completos de 'montos cedidos':")
st.dataframe(df_cedidos)

# Selección de fechas
fecha_recibido = st.selectbox("Selecciona una Fecha-Texto de 'montos recibidos'", fechas_recibidos)
fecha_cedido = st.selectbox("Selecciona una Fecha-Texto de 'montos cedidos'", fechas_cedidos)

# Filtrar datos según la fecha seleccionada
df_recibidos_filtrado = df_recibidos[df_recibidos['Fecha-Texto'] == fecha_recibido]
df_cedidos_filtrado = df_cedidos[df_cedidos['Fecha-Texto'] == fecha_cedido]

# Mostrar dataframes de los datos filtrados
st.write(f"Datos filtrados de 'montos recibidos' para {fecha_recibido}:")
st.dataframe(df_recibidos_filtrado)

st.write(f"Datos filtrados de 'montos cedidos' para {fecha_cedido}:")
st.dataframe(df_cedidos_filtrado)

# Combinar dataframes por "Descripción del Concepto"
df_combinado = pd.merge(df_recibidos_filtrado, df_cedidos_filtrado, on='Descripción del Concepto', suffixes=('_recibido', '_cedido'))

# Calcular la diferencia de montos
df_combinado['Diferencia'] = df_combinado['Datos_recibido'] - df_combinado['Datos_cedido']

# Seleccionar columnas relevantes
df_resultado = df_combinado[['Descripción del Concepto', 'Fecha-Texto_recibido', 'Fecha-Texto_cedido', 'Diferencia']]

# Mostrar el dataframe resultante
st.write("Resultado de la Comparación:")
st.dataframe(df_resultado)

# Aviso de copyright
st.sidebar.write("\n\n© 2024 todos los derechos reservados. Creado por jahoperi")
