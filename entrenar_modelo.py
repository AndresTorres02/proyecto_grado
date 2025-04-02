import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

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
    tf.keras.layers.Dense(2, activation='softmax')  # 2 clases: 'sana' y 'infectada'
])

# Compilar el modelo
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

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

# Entrenar el modelo
model.fit(train_dataset, validation_data=val_dataset, epochs=10)

# Guardar el modelo entrenado
model.save("modelo_entrenado/piña_modelo.h5")
print("Modelo guardado en 'modelo_entrenado/piña_modelo.h5'")
