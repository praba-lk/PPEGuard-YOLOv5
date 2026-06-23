from ultralytics import YOLO
import cv2

# Load trained YOLOv8 model
model = YOLO(r"C:\Users\DELL\Desktop\Sample_Project\best.pt")  # Adjust path as needed

# Open webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret: 
        break

    # Run YOLOv8 inference on the frame (BGR image)
    results = model(frame, verbose=False)

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
