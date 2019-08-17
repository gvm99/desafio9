from flask import Flask, render_template, request, json, jsonify
import os
import json
import numpy as np
import io
from PIL import Image
import wiotp.sdk.application
import base64

app = Flask(__name__)
app.config.from_object(__name__)
port = int(os.getenv('PORT', 8080))

@app.route("/", methods=['GET'])
def hello():
    error=None
    return render_template('index.html', error=error)

def myEventCallback(event):
    str = "%s event '%s' received from device [%s]: %s"
    print(event.data)
    #fahrenheit = 9.0/5.0 * event.data['data']['temperatura'] + 32
    #Umidade = volume de água / volume total

@app.route("/iot", methods=['GET'])
def result():
    myConfig = { 
        "auth":{
            "key": "a-y76ylb-ckj29x2v6b",
            "token": "IoZc5eC_lxrtJdmi4O",
            
        }
    }
    client = wiotp.sdk.application.ApplicationClient(config=myConfig)
    client.connect()
    device = {"typeId": "maratona", "deviceId": "d9"}
    client.subscribeToDeviceEvents(typeId="maratona", deviceId="d9", eventId="sensor",msgFormat="json")
    lastEvent = client.lec.get(device, "sensor")
    event = json.loads((base64.b64decode(lastEvent.payload).decode('utf-8')))
    print(event)
    #ITU = T - 0.55 ( 1 - UR )( T - 14 )
    itu = (event['data']['temperatura'] - 0.55)*( 1 - event['data']['umidade_ar'] )*( event['data']['temperatura'] - 14 )
    # Implemente sua lógica aqui e insira as respostas na variável 'resposta'
    resposta = {
        "iotData": {
            "timestamp": event['data']['timestamp'],
              "temperatura": event['data']['temperatura'],
              "umidade_ar": event['data']['umidade_ar'], 
              "umidade_solo": event['data']['umidade_solo']
        },
        "itu": itu,
        "volumeAgua": event['data']['umidade_solo'],
        "fahrenheit": 9.0/5.0 * event['data']['temperatura'] + 32
    }
    response = app.response_class(
        response=json.dumps(resposta),
        status=200,
        mimetype='application/json'
    )
    return response

def prepare_image(image):
    image = image.resize(size=(96,96))
    image = np.array(image, dtype="float") / 255.0
    image = np.expand_dims(image,axis=0)
    image = image.tolist()
    return image

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    image = request.files["image"].read()
    image = Image.open(io.BytesIO(image))
    image = prepare_image(image)

    # Faça uma requisição para o serviço Watson Machine Learning aqui e retorne a classe detectada na variável 'resposta'
    
    resposta = {
        "class": "data"
    }
    return resposta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)