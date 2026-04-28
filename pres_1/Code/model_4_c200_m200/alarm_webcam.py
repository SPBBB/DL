import cv2
import numpy as np
import tensorflow
import pygame
import threading
import time
import sys

pygame.mixer.init()
pygame.mixer.music.load('audio.mp3')

# -------------------------------
# 1. user input function
# -------------------------------
def get_user_settings():
    try:
        threshold = int(input("Enter drowsiness threshold (recommended 7~15): "))
    except:
        print("Invalid input. Using default value 10.")
        threshold = 10
    return threshold

# -------------------------------1
# 2. state predicting function 
# -------------------------------
def predict_state(frame, model, class_names):
    image = cv2.resize(frame, (224, 224))
    image = np.asarray(image, dtype=np.float32)
    image = (image / 127.5) - 1
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()

    return class_name

# -------------------------------
# 3. alarm function
# -------------------------------
alarm_playing = False

def play_alarm():
    global alarm_playing
    if not alarm_playing:
        alarm_playing = True
        
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue
        
        alarm_playing = False

def trigger_alert(frame):
    cv2.putText(frame, "WAKE UP!", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    threading.Thread(target=play_alarm).start()

# -------------------------------
# 4. main function
# -------------------------------
def main():
    try:
        
        threshold = get_user_settings() # user input

        
        model = tensorflow.keras.models.load_model("keras_model.h5", compile=False) # road model
        class_names = open("labels.txt", "r").readlines()

        camera = cv2.VideoCapture(0)

        
        recent_states = [] # save recent states

        while True:
            ret, frame = camera.read()
            if not ret:
                print("Camera error")
                break

            # predict state
            state = predict_state(frame, model, class_names)

            # save a current state in the list
            recent_states.append(state)

            # at most 15 states
            if len(recent_states) > 16:
                recent_states.pop(0)

            # -------------------------------
            # LOOP 2: for loop 
            # -------------------------------
            drowsy_count = 0
            for s in recent_states:
                if "Drowsy" in s:
                    drowsy_count += 1
            

            # -------------------------------
            # DECISION
            # -------------------------------
            if drowsy_count > threshold:
                trigger_alert(frame)
            else:
                pygame.mixer.music.stop()

                # save log
                with open("log.txt", "a") as f:
                    f.write(f"Drowsy at {time.time()}\n")

            # print screen
            cv2.putText(frame, state, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            cv2.imshow("Drowsiness Detection", frame)


            # break code
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        camera.release()
        cv2.destroyAllWindows()
        pygame.mixer.music.stop()
        sys.exit()


    except Exception as e:
        print("Error occurred:", e)

# exeute
main()
