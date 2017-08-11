import unzip_requirements
import json
import datetime
import urllib, cStringIO, io
import base64
from PIL import Image

URL = 'https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png'

def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }
    keypairs = {'style': 'kanagawa', 'token': 'hahaNONE'}

    #Worker gets token and image URL from queue.
    with io.BytesIO() as input_buffer, io.BytesIO() as output_buffer:
      #Worker carries out style transfer on the image URL.
      #transfer(input_buffer, output_buffer, keypairs['style']) 
      input_buffer = io.BytesIO(urllib.urlopen(URL).read())
      img = Image.open(input_buffer)
    
      img.save(output_buffer, format="JPEG")
      encoded = base64.b64encode(output_buffer.getvalue())

    headers = {
      'Access-Control-Allow-Origin': '*'
    }
    response = {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(encoded) #json.dumps(body)
    }

    #When transfer is completed, worker places get on queue - EB HANDLES
    return response

if __name__ == "__main__":
  endpoint(None, None)
