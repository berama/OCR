from flask import Flask, render_template, request
from OCR import OCR
import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


#defining the routing for the main page
@app.route("/")
def index():
	return render_template("upload.html")

@app.route("/upload", methods=["GET","POST"])
def upload():
	target_path = os.path.join(APP_ROOT, 'static/images/')

	if not os.path.isdir(target_path):
		os.mkdir(target_path)

	file = request.files.getlist("file")[0]
	filename = file.filename
	final_path = "".join([target_path, filename])
	file.save(final_path)

	imagepath = "./static/images/" + filename
	save_to_file = filename.split(".")
	save_to_file = "./static/images/" + save_to_file[0] + "_processed." + save_to_file[1]
	OCR(imagepath, save_to_file)
	#converting the image to text
	text = pytesseract.image_to_string(Image.open(save_to_file), lang = 'pol')
	#loading the second page
	return render_template("processed.html", image_unprocessed=imagepath, display=text)

if __name__ == "__main__":
	app.run(debug=True)