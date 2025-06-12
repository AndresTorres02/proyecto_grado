import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import os

# Crear directorio si no existe
model_dir = "modelo_entrenado"
os.makedirs(model_dir, exist_ok=True)

# Cargar dataset
dataset_path = "dataset"  # Carpeta donde están las imágenes de piña
img_size = (224, 224)
batch_size = 32  

train_dataset = image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

val_dataset = image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

class_names = train_dataset.class_names
num_classes = len(class_names)

# Cargar MobileNetV3 sin la última capa
base_model = tf.keras.applications.MobileNetV3Large(
    weights="imagenet", include_top=False, input_shape=(224, 224, 3)
)
base_model.trainable = False  # Congelar capas base

# Construir el modelo
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(num_classes, activation='softmax')  # número de clases dinámico
])

# Compilar el modelo
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# Entrenar el modelo
model.fit(train_dataset, validation_data=val_dataset, epochs=10)

# Guardar el modelo entrenado en el directorio 'modelo_entrenado/pina_modelo'
model.save(os.path.join(model_dir, "pina_modelo.keras"))
print(f"Modelo guardado en '{os.path.join(model_dir, 'pina_modelo')}'")
