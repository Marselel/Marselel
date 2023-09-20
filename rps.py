import pathlib

from matplotlib import pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential


dataset_dir=pathlib.Path('rps_dataset/')

# image_count=len(list(dataset_dir.glob('*/*.png')))
# print(image_count)

batch_size=32

rzmer=(180,180)

train_ds=tf.keras.utils.image_dataset_from_directory(
    dataset_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=rzmer,
    batch_size=batch_size
)
val_ds=tf.keras.utils.image_dataset_from_directory(
    dataset_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=rzmer,
    batch_size=batch_size
)

class_names=train_ds.class_names
print(f'Названия классов: {class_names}')

# cache
AUTOTUNE=tf.data.AUTOTUNE
train_ds=train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds=val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# create model

num_classes=len(class_names)
model=Sequential([
    layers.experimental.preprocessing.Rescaling(1./255,input_shape=(180,180,3)),


    # АУГУМЕНТАЦИЯ
    layers.experimental.preprocessing.RandomFlip("horizontal",input_shape=(180,180,3)),
    layers.experimental.preprocessing.RandomRotation(0.1),
    layers.experimental.preprocessing.RandomZoom(0.1),
    layers.experimental.preprocessing.RandomContrast(0.2),

    # 
    layers.Conv2D(16,3, activation='relu',padding='same'),
    layers.MaxPooling2D(),

    layers.Conv2D(32,3, activation='relu',padding='same'),
    layers.MaxPooling2D(),

    layers.Conv2D(64,3, activation='relu',padding='same'),
    layers.MaxPooling2D(),


    layers.Dropout(0.2),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)

])




model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)
model.summary()


# train model
epochs=30
history=model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)


# vizualize
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()


# сохранение модели


model.save_weights('rps_model')
print('Model saved!')

