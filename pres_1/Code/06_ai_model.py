import tensorflow as tf  # TensorFlow is required for Keras to work
import cv2  # opencv-python is required
import numpy 

# Disable scientific notation for clarity
numpy.set_printoptions(suppress=True) # 뭐지 

# Load the model
model = tf.keras.models.load_model("./model_4_c200_m200/keras_model.h5", compile=False)

# Load the labels
class_names = open("./model_4_c200_m200/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image_ = camera.read() # ret, image_ = camera.read() -> use of ret? 

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image_, (224, 224), interpolation=cv2.INTER_AREA) #  interpolation=cv2.INTER_AREA

    # Make the image a numpy array and reshape it to the models input shape.
    image = numpy.asarray(image, dtype=numpy.float32).reshape(1, 224, 224, 3) # numpyarray 구조 

    # Normalize the image array
    image = (image / 127.5) - 1 #Normalize?

    # Predicts the model
    prediction = model.predict(image)
    index = numpy.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index] # numpyarray 구조 

    # Show the image in a window
    image_    = cv2.putText(image_, class_name[:-2], (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2) # 텍스트 뒷부분 (좌표)
    image_    = cv2.putText(image_, str(numpy.round(confidence_score * 100))[:-2]+"%", (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2) # (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2

    cv2.imshow("Webcam Image", image_)

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")  # class_name[2:0] 왜 :-2 와 가탸
    print("Confidence Score:", str(numpy.round(confidence_score * 100))[:-2], "%") # str(numpy.round(confidence_score * 100))[:-2]

    # Listen to the keyboard for presses.
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'): # 잡
        break

camera.release() # cv2.VdeoCaptrue.release() method 머지
cv2.destroyAllWindows()

import time

""" 

import time 

def Timer(n) : 
    for i in range(1, n+1) : 
        t1 = time.time()
        while True : 
            t2 = time.Time()
            image_    = cv2.putText(image_, str(i), (122, 122), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2) 
            cv2.imshow("Webcam Image", image_)
            if t2-t1 == delta : 
                break
    image_    = cv2.putText(image_, "", (122, 122), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

def 설문() : # 웹캠 찍기 전에 한 번, 웹캠 찍은 후에 한 번 
claim = input("How are you now?(감정1/2/3/4): " )
return claim 

def 대답list(claim1,prediction, claim2, . .) :

    if claim1 == "감정1" & prediction == "감정2" & claim2 == "감정3" : 
        print(" . . ")
    
    if . .
    
    .
    .


근데 이제 뭐함? -> flowchart 짜고 데모비디오 찍고 데이터 콜렉션 -> AI 학습 사이트 가서 데이터 넣어서 학습시키기 -> 파일 export 해서 안의 keras`~, label~ file 덮어쓰기하면 댐
"""