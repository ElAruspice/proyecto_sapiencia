#Trabajo final redes neuronales

"""El presente material hace parte de la ruta de formación del talento especializado de SAPIENCIA

Los documentos que utilizaremos en la presente y proximas clases son una mezcla del trabajo de muchos profesores y académicos.

En caso de utilizar el presente contenido favor citarlo y brindar los créditos respectivos.

Integrantes

Jhon Esteban Velásquez
Geiver Alberto Zabala 
Alberto Náder Galeano


Descripción trabajo final

  1. Analizar el código paso a paso y entenderlo y realizar una breve explicación de como funciona.
  2. Realizar módificaciones variando parámetros como la cantidad de neuronas, tipo de optimizador, funciones de activación, funciones de pérdida y tamaños de entrada de las imágenes.
  3. A partir del entendimiento del código en el punto 1 responda las siguientes preguntas: 

    ¿Cual es el objetivo de categorizar los targets o labels correspondientes a cada imagen?
    ¿En que me ayuda la normalización a la hora de entrenar los datos?
  
  4. Realice un informe detallando los resultados obtenidos en el punto 2. El informe debe responder las siguiente preguntas:
  
    ¿Cómo variaron los resultados con el aumento o disminución de las neuronas?
    ¿Cómo cambia la presición del modelo propuesto, al cambiar la función de activación, que se logra observar de los resultados?
    ¿Cuál sería a su criterio la función de activación que se adapta al presente análisis?
    ¿Cómo se comportaron los resultados de las funciones de perdida analizadas?
    ¿Mejoraron los resultados al reducir o aumentar el tamaño de entrada de la imagen?
    ¿Cuál fue la mejor solución que logró encontrar y por qué?

Nota: El informe debe llevar los valores que probaron en el modelo y para lo cuál como minimo se deben analizar 4 optimizadores,4 funciones de activación, 4 funciones de perdida, 4 opciones de neuronas y tamaños de entrada de la imagen.
  5. Concluir en que casos se debe utilizar los optimizadores, funciones de pérdida, funciones de activación y tener en cuenta que se debe presentar una gráfica representativa de cada función de activación describiendo los rangos de la función y su comportamiento.


##Porcentajes de calificación

1.   Punto 1 : 10%
2.   Punto 2 : 10%
3.   Punto 3 : 10%
4.   Punto 4 : 25%
5.   Punto 5 : 15%
6.   Sustentación : 30%

##Limitantes
Grupos máximo de 3 personas y mínimo de 2 personas

"""

#Para iniciar, se instalan las librerías requeridas para el ejercicio propuesto:
#Como segundo paso procedemos a importar las bibliotecas TensorFlow y Keras a Python, dado que son ampliamente utilizadas para el aprendizaje profundo. Mientras Tensorflow se encarga de ejecutar los gráficos de forma ágil, Keras facilita la creación de modelos de aprendizaje profundo en Python.

import tensorflow as ts
import numpy as np
from keras import layers, models
from keras.utils import to_categorical
from keras.datasets import mnist
import matplotlib.pyplot as plt
import pandas as pd

(train_data, train_labels), (test_data, test_labels) =mnist.load_data()
train_data
train_data.shape
train_data[0]
plt.imshow(train_data[0])
train_labels[0]
