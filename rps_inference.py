def neural(path):
    import pathlib

    import matplotlib.pyplot as plt
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

    class_names=['бумага','камень','ножницы']
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


    model.load_weights("rps_model").expect_partial()


    loss,acc =model.evaluate(train_ds, verbose=2)
    print("Restored model, accuracy: {:5.2f}%".format(100*acc))


    img=keras.utils.load_img(path, target_size=rzmer)
    img_array = tf.keras.utils.img_to_array(img)
    img_array=tf.expand_dims(img_array, 0)

    # make predictions
    predictions=model.predict(img_array)
    score=tf.nn.softmax(predictions[0])

    # print inference result
    return "На изображении скорее всего {} ({}% вероятность)".format(class_names[np.argmax(score)],
                                                                        100 * np.max(score))