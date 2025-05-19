import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload video file
uploaded = files.upload()  # This will prompt you to upload a file

# Get the uploaded file name (assuming it's the first file in the upload)
video_file = list(uploaded.keys())[0]  # Get the uploaded file's name

# Load video or camera feed
cap = cv2.VideoCapture(video_file)  # Use the uploaded video file

# Predefined parking positions (list of top-left x, y coordinates)
parking_spots = [(60, 100), (160, 100), (260, 100), (360, 100)]
spot_width, spot_height = 80, 160

# Function to check if a parking spot is empty
def check_parking_spot(img, x, y, w, h):
    roi = img[y:y+h, x:x+w]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 25, 16)
    non_zero = cv2.countNonZero(thresh)
    return non_zero < 900  # Threshold for empty spot

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Loop through predefined parking spots and check for availability
    for pos in parking_spots:
        x, y = pos
        empty = check_parking_spot(frame, x, y, spot_width, spot_height)
        color = (0, 255, 0) if empty else (0, 0, 255)  # Green if empty, Red if occupied
        cv2.rectangle(frame, (x, y), (x+spot_width, y+spot_height), color, 2)
        status = "Empty" if empty else "Occupied"
        cv2.putText(frame, status, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Convert the frame to RGB (for correct display with matplotlib)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display using matplotlib
    plt.imshow(frame_rgb)
    plt.axis('off')  # Hide axes
    plt.show()

    # Optional: Exit after 1 iteration for testing, remove for continuous run
    break

cap.release()
