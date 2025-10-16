# Reconocimiento de Gestos en Tablet con KNN y PCA

Este proyecto tiene como objetivo **clasificar gestos realizados en un tablet** utilizando aprendizaje supervisado. Cada gesto se registra como un conjunto de mediciones temporales de posición y presión del dedo, y el modelo utiliza técnicas de **preprocesamiento, reducción de dimensionalidad y KNN** para realizar la clasificación.

---

## Estructura de Datos

Los datos están organizados en carpetas por usuario:
```
gestures/
    user_01/
        gesture_01_sample_01.csv
        gesture_01_sample_02.csv
        ...
    user_02/
        ...
```
Cada CSV contiene las columnas:

- `temporal_point` – índice temporal del punto de la muestra  
- `x` – coordenada X del dedo  
- `y` – coordenada Y del dedo  
- `height` – altura del área de contacto  
- `width` – ancho del área de contacto  
- `finger_pressure` – presión del dedo sobre la pantalla  

---

## Preprocesamiento

1. **Carga de datos**: Se combinan todas las muestras en un único `DataFrame` con columnas adicionales: `user`, `gesture` y `sample`.  
2. **Eliminación de duplicados y puntos temporales inválidos**: Se filtran gestos repetidos y `temporal_point = 0`.  
3. **Vectorización de muestras**: Cada gesto se convierte en un vector de características aplanando los valores de las columnas relevantes (`x`, `y`, `height`, `width`, `finger_pressure`).  
4. **Padding**: Las muestras con diferente número de puntos se rellenan para mantener un tamaño uniforme.  
5. **Escalado**: Se aplica `StandardScaler` para normalizar las características.  
6. **Reducción de dimensionalidad**: Se utiliza PCA para mantener el 95% de la varianza, reduciendo la dimensionalidad y mejorando la eficiencia.

---

## Modelo

- **Algoritmo**: K-Nearest Neighbors (KNN)  
- **Selección de k**: Se evalúan múltiples valores de `k` mediante validación cruzada, eligiendo el que maximiza la precisión.  
- **Validación**: Se realiza separación en entrenamiento y prueba respetando grupos de usuario para evitar filtrado de muestras del mismo usuario.  

---

## Resultados

Ejemplo de métricas obtenidas:
```
Precisión en entrenamiento: 0.954
Precisión en test: 0.935
```
- Las precisiones indican que el modelo **generaliza bien** sin sobreajustarse a los datos de entrenamiento.  
- También se realizaron validaciones cruzadas con `GroupKFold` para evaluar estabilidad por usuario.

---

## Uso

```python
from load_gestures import load_gestures
import numpy as np

# Cargar datos
df = load_gestures("gestures/")

# Preprocesamiento, PCA y KNN (como en el notebook principal)
# ...
```

---

## Dependencias
- Python 3.10+
- pandas
- numpy
- scikit-learn
- matplotlib

---

## Notas
- Se pueden generar imágenes para cada gesto usando `images.py`, que las genera por usuario y muestra.
- El módulo `load_gestures.py` permite cargar los datos desde cualquier ruta.
- KNN es sensible al ruido; PCA ayuda a mejorar la robustez y eficiencia.