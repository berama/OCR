import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def OCR(file, processed_name):
    #uploading the image
    image = cv2.imread(file)

    #converting to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #adding tresh
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	
    #saving the image
    cv2.imwrite(processed_name, gray)