import cv2



# ================= CONFIGURATION =================
# Replace this with your image filename
IMAGE_PATH = "Edited.png"
SECONDARY_IMAGE_PATH = "OriginalImage.png"


# =================================================

def click_event(event, x, y, flags, param):
    """
    This function is called every time a mouse event happens.
    We check if the event was a Left Button Click.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # 1. Print coordinates to the console
        print(f"📍 Coordinates: x={x}, y={y}")

        # 2. visual feedback: Draw a small red circle where you clicked
        # (Image, Center, Radius, Color(BGR), Thickness)
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        
        # 3. Visual feedback: Write the text coordinates next to the dot
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"{x},{y}"
        cv2.putText(img, text, (x + 10, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        
        # 4. Refresh the image window to show the drawing
        cv2.imshow("Image Viewer", img)
        with open("game_data.txt", "r") as f:
            content = f.read()
        parts = content.split(",")
        xCircle = int(parts[0])
        yCircle = int(parts[1])
        circle_r = int(parts[2])
        if (x - xCircle + 100 <= 200 and x - xCircle + 100 >= 0) and (y - yCircle + 100 <= 200 and y - yCircle + 100 >= 0):
            print("✅ Correct! You clicked inside the circle.")
        else:
            print("❌ Incorrect. Try again!")
  
# Load the image  
img = cv2.imread(IMAGE_PATH)
img_circle = cv2.imread(SECONDARY_IMAGE_PATH)

# Check if image exists
if img is None:
    print(f"❌ Error: Could not load image '{IMAGE_PATH}'. Check the filename.")
else:
    
    print("✅ Image loaded successfully.")
    print("👉 Click anywhere on the image to get coordinates.")

    print("👉 Press any key on your keyboard to exit.")

    # Create the window and attach the mouse callback function
    cv2.imshow("Image Viewer", img)
    cv2.imshow("Circle Viewer", img_circle)

    cv2.setMouseCallback("Image Viewer", click_event)

    # Keep the window open until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  