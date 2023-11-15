import pytesseract
from PIL import Image

image_path = "/home/mike/Documents/python_staff/analize-de-rutina.png"
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)
print(extracted_text)