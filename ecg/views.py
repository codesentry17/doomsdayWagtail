from PIL import Image
from io import BytesIO
import base64
import numpy as np
from keras.models import load_model


# Load your trained model
model = load_model('ECG_MODEL.h5')  # Replace with the path to your trained model

# Define the class labels
class_labels = ['F', 'M', 'N', 'Q', 'S', 'V']


def predictionFunction(mypic1):
    """function for ECG processing/prediction"""

    image = Image.open(mypic1)
    image = image.resize((256, 256)).convert('L')
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make predictions using your model
    predicted_probs = model.predict(image_array)
    predicted_label_index = np.argmax(predicted_probs)
    predicted_label = class_labels[predicted_label_index]

    return predicted_label





