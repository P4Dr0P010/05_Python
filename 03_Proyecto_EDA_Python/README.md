# Proyecto EDA con Python – Campaña Bancaria

## Descripción
Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre una campaña bancaria telefónica. El objetivo es combinar información de clientes y de llamadas para:
- Limpieza y transformación de datos.
- Generación de nuevas variables de segmentación.
- Análisis descriptivo y visualización.
- Extracción de insights y recomendaciones estratégicas.

## Flujo de trabajo
1. **Carga de datos**
   - Lectura de `bank-additional.csv` (detalle de la campaña) y de `customer-details.xlsx` (datos de clientes).  
2. **Fusión de datasets**
   - Unión con `pd.merge()` usando `customer_id` como clave para enriquecer cada registro de llamada con atributos demográficos y financieros.  
3. **Limpieza y transformación**
   - Eliminación de columnas irrelevantes (`file_index`, `latitude`, `longitude`).  
   - Corrección de tipos y formatos (p. ej., conversión de fecha).  
   - Mapeo de meses de texto a valores numéricos.  
4. **Generación de variables derivadas**
   - **Recency** (`contact_recency`) a partir de `pdays`.  
   - **Solvencia** (`solvency`) según historial de préstamos y default.  
   - **Hipoteca** (`has_mortgage`) binaria.  
   - **Segmento ocupacional** (`job_segment`) (white-collar vs. blue-collar, etc.).  
   - **Segmento educativo** (`education_segment`).  
   - **Poder adquisitivo** (`purchasing_power`) según cuartiles de ingreso.  
   - **Actividad web** (`web_activity`) según cuartiles de visitas en el sitio.  
5. **Análisis descriptivo y visualización**
   - Histogramas de variables continuas (`age`, `duration`, `campaign`, `income`).  
   - Gráficos de barras para variables categóricas y tasas de conversión por segmento.  
   - Boxplots para detectar outliers y comparar distribuciones.  
   - Gráficos de series temporales (suscripciones por mes/año).  
   - Scatter plots y stacked bars (poutcome vs. éxito).  
6. **Insights & recomendaciones**
   - Interpretación de cada visualización.  
   - Conclusiones accionables para optimizar futuras campañas.

## Estructura del proyecto
```
├── data/
│   ├── bank-additional.csv
│   └── customer-details.xlsx
├── notebooks/
│   └── EDA_con_Python.ipynb
├── figures/
│   └── (gráficos generados)
├── requirements.txt
└── README.md
```

## Instalación y ejecución
```bash
git clone https://github.com/P4Dr0P010/05_Python.git
cd 05_Python/03_Proyecto_EDA_Python

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt

# Iniciar Jupyter Notebook
jupyter notebook notebooks/EDA_con_Python.ipynb
```

## Metodología de limpieza y transformación
1. **Depuración inicial**
   - Eliminación de columnas vacías o no requeridas.  
   - Ajuste de índices y eliminación de duplicados.  
2. **Tratamiento de fechas**
   - Conversión de la columna `date` en tres campos: día, mes (numérico) y año.  
3. **Codificación de variables**
   - One-hot (`pd.get_dummies`) para `marital`, `education`, `contact`.  
   - Mapeo personalizado para segmentos ocupacionales y educativos.  
4. **Creación de variables derivadas**
   - Funciones vectorizadas (evitando `apply` lineal) para clasificar `pdays`, solvencia e hipoteca.  
   - Cálculo de cuartiles para ingresos y visitas web.

## Segmentaciones generadas
- **Recency**: never (–1), recent (0–30 d), mid (31–180 d), old (> 180 d)  
- **Solvencia**: baja, media, alta  
- **Hipoteca**: yes/no  
- **Job segment**: white-collar, blue-collar, services, student/retired  
- **Education segment**: bajo, medio, alto  
- **Poder adquisitivo**: low (Q1), medium (Q2–Q3), high (Q4)  
- **Actividad web**: low (Q1), medium (Q2–Q3), high (Q4)

## Visualizaciones clave
1. **Histograma de edad** y boxplot por `web_activity`.  
2. **Duración de llamada vs. tasa de éxito**: llamadas > 300 s duplican conversión.  
3. **Número de intentos (`campaign`)**: pico de conversión en 2–3 llamadas, fatiga tras la 4.  
4. **Serie temporal de suscripciones** por mes/año (2015–2019): picos en verano.  
5. **Conversion rate por segmento**: job_segment, education_segment, purchasing_power.  
6. **Scatter plot** de tasa de conversión vs. purchasing_power.  
7. **Stacked bar** de `poutcome` vs. `y` (success/failure/no contact).  
8. **Mapa de calor de correlaciones** entre variables numéricas.

## Principales insights
- **Duración media**: 360 s en llamadas exitosas vs. 180 s en fallidas.  
- **Cadencia óptima**: esperar ≥ 60 d antes de nuevo contacto; máximo 4 intentos.  
- **Segmentación premium**: white-collar con saldo €1 000–€5 000 y edad 30–45 años.  
- **Poder adquisitivo** alto presenta hasta un 22 % de conversión.  
- **Temporada estival** (junio-julio) aumenta receptividad (+5 pp).

## Recomendaciones
1. **Formación en llamadas**: guión estructurado de al menos 5 min.  
2. **Periodo de “enfriamiento”**: ≥ 60 d antes de recontactar.  
3. **Límite de intentos**: máximo 4 para evitar desgaste.  
4. **Campañas estacionales**: focalizar en verano.  
5. **Incentivos segmentados**: ofertas especiales a clientes con solvencia alta y actividad web elevada.

## Autor y licencia
Pedro Polo – AI900, Master en IA e Innovación, estudiante PL-300 Power BI  
MIT License
