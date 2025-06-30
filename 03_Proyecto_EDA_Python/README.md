# Proyecto EDA con Python

## Descripción
Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre datos de campañas bancarias, combinando información de llamadas y detalle de clientes para extraer insights, limpiar y transformar datos, generar visualizaciones y ofrecer recomendaciones estratégicas.

## Requisitos
- Python 3.7 o superior  
- Librerías:  
  - pandas  
  - numpy  
  - matplotlib  
  - seaborn  
  - openpyxl  
- Jupyter Notebook o entorno compatible  
- Visual Studio Code (recomendado)

## Instalación
1. Clonar el repositorio  
2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

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

## Uso
1. Colocar los archivos de datos en `data/`.  
2. Abrir y ejecutar el notebook `notebooks/EDA_con_Python.ipynb`.  
3. Seguir los pasos de:
   - Transformación y limpieza de datos  
   - Análisis descriptivo  
   - Generación de visualizaciones  
   - Síntesis del informe y recomendaciones  

## Contribución
1. Hacer fork del proyecto  
2. Crear branch con nueva funcionalidad (`git checkout -b feature/nueva-idea`)  
3. Hacer commit de los cambios (`git commit -m "Añade nueva idea"`)  
4. Push al branch (`git push origin feature/nueva-idea`)  
5. Abrir Pull Request

## Autor
Pedro Polo – Estudiante de PL-300 de Power BI y Analisis de Datos en ThePower Business School.
Apasionado por el modelado de datos y la automatización de procesos.

