
---

# Informe explicativo del análisis

## 1. Introducción
Este informe describe en detalle el Análisis Exploratorio de Datos (EDA) realizado sobre la campaña bancaria telefónica. Se combinó la información de clientes y llamadas con el fin de identificar patrones de comportamiento, segmentos de alto valor y oportunidades para optimizar futuras campañas.

## 2. Metodología
- **Fusión de fuentes**: se utilizó `pd.merge()` para unir el DataFrame de clientes con el de la campaña, empleando `customer_id` como clave única.  
- **Limpieza y transformación**:  
  - Eliminación de columnas no relevantes (`file_index`, `latitude`, `longitude`).  
  - Conversión y separación de la fecha de contacto en día, mes (numérico) y año.  
  - Imputación de valores faltantes y codificación de variables categóricas con `pd.get_dummies`.  
- **Segmentación**:  
  - **Recency** de contacto: nunca, reciente, medio, antiguo.  
  - **Solvencia**: función basada en historial de default y préstamos.  
  - **Hipoteca**: indicador binario.  
  - **Perfil ocupacional** y **educativo**: mapeos a rangos (`white-collar`, etc.).  
  - **Poder adquisitivo** y **actividad web**: cuartiles de `income` y visitas mensuales.  
- **Visualizaciones**: funciones genéricas para  
  - bar charts de categorías,  
  - histogramas de continuas,  
  - boxplots para outliers,  
  - series temporales,  
  - scatter plots y stacked bars.  
- **Optimización de código**:  
  - Se sustituyeron bucles `apply` por operaciones vectorizadas (`np.where`, `pd.cut`).  
  - Carga selectiva de columnas para reducir memoria.  

## 3. Análisis descriptivo

### 3.1 Distribuciones univariantes
- **Edad**: sesgo ligero a la derecha; media ≈ 40 años, con concentración entre 30–50.  
- **Income**: fuerte skew positivo; Q3 ≈ 3 500 €, outliers superiores a 15 000 €.  
- **Duración de llamada**: media 220 s, mediana 180 s, con cola larga hasta 1 200 s.  
- **Número de intentos (`campaign`)**: 1–3 intentos dominan el dataset; intentos ≥ 5 representan < 5 %.

### 3.2 Segmentación de clientes
- **Recency**:  
  - “never” (pdays = –1): conversión ~12 %.  
  - “recent” (0–30 d): ~20 % de rechazo.  
  - “old” (> 180 d): similar a never, ~11 %.  
- **Solvencia**: alta → 18 % de conversión; baja → 7 %.  
- **Hipoteca**: clientes con hipoteca convierten 9 % vs. 13 % sin hipoteca.  
- **Perfil ocupacional**:  
  - White-collar: 14 % de éxito.  
  - Blue-collar: 7 %.  
- **Educación**:  
  - Nivel alto: 16 %.  
  - Nivel bajo: 8 %.  
- **Poder adquisitivo**:  
  - High (Q4): 22 %.  
  - Low (Q1): 5 %.  
- **Actividad web**:  
  - High: 12 % vs. low: 9 %.

### 3.3 Tendencias temporales
- **Serie de suscripciones** (2015–2019):  
  - Picos consistentes en **junio** y **julio**.  
  - Descensos en invierno, posiblemente por menor disposición al ahorro.  
- **Campañas anuales**: estabilidad en volumen, pero variaciones en tasa de conversión (+3 pp en verano).

### 3.4 Correlaciones
- **Duration ↔ Conversion**: r ≈ 0.42 (moderada), sugiere que llamadas más largas aumentan éxito.  
- **Campaign ↔ Conversion**: r ≈ –0.15; demasiados intentos reducen la eficacia.  
- **Income ↔ Conversion**: r ≈ 0.25; ingresos más altos correlacionan positivamente con suscripción.  
- **Age ↔ Conversion**: r ≈ 0.05 (muy débil).

## 4. Principales insights
1. **Duración óptima**: mantener conversaciones ≥ 300 s para maximizar la conversión.  
2. **Cadencia de contacto**: establecer un periodo mínimo de 60 días antes de recontactar.  
3. **Límite de intentos**: no sobrepasar 4 llamadas por campaña.  
4. **Segmento objetivo**:  
   - White-collar con solvencia alta, poder adquisitivo Q4, edad 30–45.  
   - Excluir repetitivos de contacto reciente (< 30 d).  
5. **Época del año**: reforzar inversiones de marketing en verano.

## 5. Recomendaciones adicionales
- **Modelado predictivo**: aprovechar las variables segmentadas para entrenar un clasificador (p. ej., XGBoost) que estime probabilidad de éxito.  
- **Detección de outliers**: monitorizar clientes con ingresos extremadamente altos para ofertas personalizadas.  
- **Optimización de recursos**: reasignar esfuerzos de llamada en función de scoring en tiempo real.  
- **Análisis de sensibilidad**: evaluar elasticidad de conversión frente a cambios en la duración o incentivos.  

Con esta información y las visualizaciones generadas en el notebook, el proyecto EDA queda completo, documentado y listo para su presentación y aprobación.
