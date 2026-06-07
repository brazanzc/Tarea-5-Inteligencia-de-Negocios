# Análisis Exploratorio de Datos — Dataset de ACV (Stroke)

Análisis exploratorio y limpieza de datos sobre el dataset público de accidentes cerebrovasculares (ACV), con generación de visualizaciones listas para reportes en LaTeX o similares.

---

## Requisitos

- Python 3.8+
- Las siguientes librerías:

```bash
pip install pandas matplotlib seaborn numpy
```

---

## Dataset

El script espera el archivo `healthcare-dataset-stroke-data.csv` en el mismo directorio de ejecución.

**Fuente recomendada:** [Kaggle — Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

### Columnas principales

| Columna | Descripción |
|---|---|
| `id` | Identificador único (se elimina en el preprocesamiento) |
| `age` | Edad del paciente |
| `avg_glucose_level` | Nivel promedio de glucosa en sangre |
| `bmi` | Índice de masa corporal |
| `stroke` | Variable objetivo: `1` = tuvo ACV, `0` = no tuvo ACV |

---

## Uso

```bash
python main.py
```

El script imprime en consola un resumen del dataset, los valores nulos por columna, el total de pacientes procesados y los casos positivos de ACV.

---

## Preprocesamiento

1. **Imputación de valores nulos:** los valores faltantes en la columna `bmi` se reemplazan con la mediana de la columna.
2. **Eliminación de columna irrelevante:** se elimina `id` por no aportar valor analítico.

---

## Visualizaciones generadas

El script guarda tres gráficos en el directorio de trabajo:

| Archivo | Descripción |
|---|---|
| `fig1_age_stroke.png` | Histograma apilado de distribución de edad según casos de ACV |
| `fig2_glucose_stroke.png` | Boxplot del nivel promedio de glucosa por grupo (ACV / No ACV) |
| `fig3_heatmap.png` | Mapa de calor de correlaciones entre variables numéricas |

---

## Estructura del proyecto

```
.
├── stroke_eda.py                      # Script principal
├── healthcare-dataset-stroke-data.csv # Dataset de entrada
├── fig1_age_stroke.png                # Gráfico generado
├── fig2_glucose_stroke.png            # Gráfico generado
├── fig3_heatmap.png                   # Gráfico generado
└── README.md
```

---

## Notas

- Los gráficos se guardan con `plt.savefig()` y se cierran con `plt.close()` para ser usados directamente en documentos LaTeX (`\includegraphics{}`).
- El análisis asume que la variable `stroke` es binaria (`0` / `1`).
