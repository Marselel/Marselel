def vegetables(path): 
    import pathlib

    import matplotlib.pyplot as plt
    import numpy as np
    import PIL
    import tensorflow as tf

    from tensorflow import keras
    from keras import layers
    from keras.models import Sequential


    dataset_dir=pathlib.Path(r"C:\Golang\vegetables\train")
    val_dir=pathlib.Path(r'C:\Golang\vegetables\validation')
    print(len(list(dataset_dir.glob('*/*.jpg'))))

    batch_size= 32
    img_width=180
    img_height=180

    train_ds=tf.keras.utils.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height,img_width),
        batch_size=batch_size
    )

    val_ds=tf.keras.utils.image_dataset_from_directory(
        val_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height,img_width),
        batch_size=batch_size
    )


    class_names = train_ds.class_names
    print(f'Class names: {class_names}')

    # cache
    AUTOTUNE=tf.data.AUTOTUNE
    train_ds=train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds=val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # create models

    num_classes=len(class_names)
    model=Sequential([
        layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),


        # Аугументация
        layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical", input_shape=(img_height, img_width, 3)),
        layers.experimental.preprocessing.RandomRotation(0.1),
        layers.experimental.preprocessing.RandomZoom(0.1),
        # layers.experimental.preprocessing.RandomRotation(0.2),
        # layers.experimental.preprocessing.RandomZoom(0.2),
        layers.experimental.preprocessing.RandomContrast(0.2),


        # дальше везде одинаково
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),

        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),

        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        
        # регуляризация
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
    model.load_weights('animals_model').expect_partial()


    loss,acc =model.evaluate(train_ds, verbose=2)
    print("Restored model, accuracy: {:5.2f}%".format(100*acc))

    img=keras.utils.load_img(path, target_size=(180,180,3))
    img_array = tf.keras.utils.img_to_array(img)
    img_array=tf.expand_dims(img_array, 0)

        # make predictions
    predictions=model.predict(img_array)
    score=tf.nn.softmax(predictions[0])

    # print inference result
    return  "На изображении скорее всего {} ({}% вероятность)".format(class_names[np.argmax(score)],
                                                                            100 * np.max(score))
print(vegetables('images/goroh.jpg'))