import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Carga de datos
df = pd.read_csv('healthcare-dataset-stroke-data.csv')

# 2. Inspección preliminar
print("Información del dataset:")
print(df.info())
print("\nValores nulos por columna:")
print(df.isnull().sum())

# 3. Limpieza de datos (Data Cleaning)
# Imputar los valores nulos del IMC (bmi) con la mediana
df['bmi'] = df['bmi'].fillna(df['bmi'].median())

# Eliminar la columna 'id' ya que no aporta valor analítico
df = df.drop('id', axis=1)

# 4. Análisis Visual (EDA)
# Gráfico 1: Histograma de Edad vs ACV
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='age', hue='stroke', multiple='stack', bins=30, palette='Set1')
plt.title('Distribución de Edad según Casos de ACV')
plt.xlabel('Edad')
plt.ylabel('Cantidad de Pacientes')
plt.tight_layout()
plt.savefig('fig1_age_stroke.png') # Guardar para LaTeX
plt.close()

# Gráfico 2: Boxplot Glucosa vs ACV
plt.figure(figsize=(8, 5))
sns.boxplot(x='stroke', y='avg_glucose_level', data=df, palette='Set2')
plt.title('Nivel Promedio de Glucosa vs ACV')
plt.xlabel('ACV (0 = No, 1 = Sí)')
plt.ylabel('Nivel Promedio de Glucosa')
plt.tight_layout()
plt.savefig('fig2_glucose_stroke.png')
plt.close()

# Gráfico 3: Mapa de calor de correlaciones
plt.figure(figsize=(8, 6))
num_cols = df.select_dtypes(include=[np.number]).columns
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Mapa de Calor de Correlaciones Numéricas')
plt.tight_layout()
plt.savefig('fig3_heatmap.png')
plt.close()

print("\nTotal pacientes procesados:", len(df))
print("Total casos de ACV positivos:", df['stroke'].sum())