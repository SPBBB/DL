import tensorflow  # TensorFlow is required for Keras to work
import cv2  # opencv-python is required
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model("./model_4_c200_m200/keras_model.h5", compile=False)

# Load the labels
class_names = open("./model_4_c200_m200/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image_ = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image_, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Show the image in a window
    image_    = cv2.putText(image_, class_name[:-2], (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    image_    = cv2.putText(image_, str(np.round(confidence_score * 100))[:-2]+"%", (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    cv2.imshow("Webcam Image", image_)

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
