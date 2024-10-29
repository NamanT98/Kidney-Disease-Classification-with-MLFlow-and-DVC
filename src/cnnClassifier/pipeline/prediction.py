import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename: str):
        self.filename = filename

    def predict(self):
        model = load_model("artifacts\\training\\model.h5")
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]
