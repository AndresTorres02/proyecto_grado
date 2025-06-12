import tensorflow as tf
import numpy as np

# Cargar el modelo entrenado
model = tf.keras.models.load_model("modelo_entrenado/pina_modelo.keras")

# Definir clases
class_names = ['sana', 'fusariosis', 'fitóftora', 'antracnosis',
                'mancha_de_la_hoja', 'pudricion_de_la_raiz', 'pudricion_del_corazon']

# Función para hacer predicciones
def predecir_imagen(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.mobilenet_v3.preprocess_input(x)

    preds = model.predict(x)
    predicted_class = class_names[np.argmax(preds)]
    confidence = np.max(preds) * 100

    return predicted_class, confidence
