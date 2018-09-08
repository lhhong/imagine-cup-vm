from PIL import Image
from io import BytesIO
import base64
from flask import Flask, request, jsonify
from predict import predict_vector_from_url, predict_vector

app = Flask("Predictor")

@app.route('/', methods = ['POST'])
def predict():
    img = request.form['image']
    im = Image.open(BytesIO(base64.b64decode(img)))
    fill_color = '#fff'  # your background
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1])
        im = background
    im.save( 'query_image.jpg', 'JPEG' )
    return jsonify({'vector': predict_vector()})

if __name__ == '__main__':
    app.run()


