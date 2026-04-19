import cv2
import os

# webcam 
camera = cv2.VideoCapture(0)

# output directory
output_folder = "./captured_images"
os.makedirs(output_folder, exist_ok=True)

# initialize counter
count = 1

while True:
    ret, frame = camera.read()  # Capture a frame

    if not ret:
        print("cannot read the frame.")
        break

    filename = f"{count:06d}.jpg"
    save_path = os.path.join(output_folder, filename)

    # save the image
    cv2.imwrite(save_path, frame)

    # display the image
    cv2.imshow("Webcam", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # increa the count
    count += 1

cap.release()                      # Release the camera
cv2.destroyAllWindows()
