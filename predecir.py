import tensorflow as tf
print(tf.__version__)
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

    print(f"La imagen '{img_path}' fue clasificada como: {predicted_class} ({confidence:.2f}% de confianza)")

# Prueba con una imagen de piña
img_path = "C:\\Users\\FELIPE\\Desktop\\Uceva\\Semestre X\\Proyecto\\dataset\\sana1.jpg"  # Cambia esto por la imagen a probar
predecir_imagen(img_path)
