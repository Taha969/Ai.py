Text Recognition and Highlighting using EasyOCR and OpenCV

This project is a simple demonstration of how to use the EasyOCR and OpenCV (cv2) libraries to detect and read text from an image, then highlight the detected text by drawing bounding boxes and writing the recognized text back onto the image.

✨ Features

  .Text Detection and Reading: Uses EasyOCR to accurately read text from images.

  .Text Highlighting: Draws green rectangles around each piece of detected text.

  .Labeling: Overlays the recognized text (label) on the image next to the bounding box.

  .Image Display: Shows the final annotated image in a separate window.

⚙️ Prerequisites

You need to have both the OpenCV and EasyOCR libraries installed. You can install them easily using pip:
Bash

pip install opencv-python easyocr

📝 How to Use

  1.Save the Code: Save the provided code into a Python file (e.g., ocr_highlight.py).

  2.Provide an Image: Place an image named AI.py.png in the same directory as your Python script.

        Note: You can change the image file name by modifying the line img = cv2.imread('AI.py.png') to match your image file.

  3.Run the Script: Execute the file using your Python interpreter:
    Bash

    python ocr_highlight.py

  A window will pop up showing the image with the detected and highlighted text. Press any key to close the window.

🔍 Code Breakdown

Line ->	Description
import cv2 ->	Imports the OpenCV library for image operations (reading, displaying, drawing).
import easyocr ->	Imports the EasyOCR library for text detection and recognition.
img = cv2.imread('AI.py.png') ->	Reads the source image file.
reader = easyocr.Reader(['en'] , gpu=False) ->	Initializes the EasyOCR reader for the English language ('en'), running on the CPU (gpu=False).
result = reader.readtext(img) ->	Performs the Optical Character Recognition (OCR) on the image.
for text in result: ->	Iterates through every piece of text detected in the image.
cv2.rectangle(...) ->	Draws a green bounding box around the coordinates of the detected text.
cv2.putText(...) ->	Writes the detected text (detctedText) onto the image.
cv2.imshow('Image', img) =>	Displays the final annotated image.
cv2.waitKey(0) ->	Waits indefinitely for a key press to keep the display window open.

🌐 Supported Languages

The reader is currently set up for English: reader = easyocr.Reader(['en'] , gpu=False).

To change the language, replace 'en' with the corresponding language code (e.g., 'ar' for Arabic). You can also use multiple languages simultaneously (e.g., ['en', 'ar']).
