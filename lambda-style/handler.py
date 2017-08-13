#import unzip_requirements
import json
import datetime
import base64
import time
import io
import cStringIO
import os
import re
import chainer
import random
import logging
import urllib

from PIL import Image, ImageFilter
import numpy as np
from chainer import Variable, serializers

from net import *

networks = {}
style = 'kanagawa'
networks[style] = FastStyleNet()
serializers.load_npz('models/'+style+'.model', networks[style])

def endpoint(event, context):
    print event['body']
    print json.loads(event['body'])['image']
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }
    keypairs = {'style': 'kanagawa', 'token': 'hahaNONE'}

    #Worker gets token and image URL from queue.
    with io.BytesIO() as input_buffer, io.BytesIO() as output_buffer:
      #Worker carries out style transfer on the image URL.
      #transfer(input_buffer, output_buffer, keypairs['style']) 
      ascii_image = json.loads(event['body'])['image'].encode('ascii', 'ignore')
      print ascii_image
      input_buffer = cStringIO.StringIO(re.sub('^data:image/.+;base64,', '', ascii_image).decode('base64'))
      #img = Image.open(cStringIO.StringIO(image_data))
    
      #Worker carries out style transfer on the image URL.
      transfer(input_buffer, output_buffer, keypairs['style']) 
      #img.save(output_buffer, format="JPEG")

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

def transfer(input_buffer, output_buffer, style='kanagawa', gpu=-1, median_filter=3, padding=50):
  start = time.time()
  times = []
  if style not in networks:
    networks[style] = FastStyleNet()
    serializers.load_npz('models/'+style+'.model', networks[style])
  network = networks[style]
  if gpu >= 0:
    cuda.get_device(0).use()
    network.to_gpu()
  xp = np if gpu < 0 else cuda.cupy
  
  times.append(time.time() - start - sum(times))
  image = np.asarray(Image.open(input_buffer).convert('RGB'), dtype=np.float32).transpose(2, 0, 1)
  image = image.reshape((1,) + image.shape)
  if padding > 0:
    image = np.pad(image, [[0, 0], [0, 0], [padding, padding], [padding, padding]], 'symmetric')
  image = xp.asarray(image)
  x = Variable(image)
  times.append(time.time() - start - sum(times))
  with chainer.no_backprop_mode():
    y = network(x)
  times.append(time.time() - start - sum(times))
  result = y.data #cuda.to_cpu(y.data)
  if padding > 0:
    result = result[:, :, padding:-padding, padding:-padding]
  result = np.uint8(result[0].transpose((1, 2, 0)))
  #med = Image.fromarray(result)
  #if median_filter > 0:
  #  med = med.filter(ImageFilter.MedianFilter(median_filter))
  Image.fromarray(result).save(output_buffer, 'JPEG')
  times.append(time.time() - start - sum(times))
  str_times = ['{:.3f}'.format(x) for x in times]
  print(str_times)

if __name__ == "__main__":
  postBody = '{"image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAkElEQVRoQ+2SwQkAMAyEkv2X7g6CUIL9nxDtzpG3R+6YDvmtZEUqIhnoa0liMbYiWJ00rIgkFmMrgtVJw4pIYjG2IlidNKyIJBZjK4LVScOKSGIxtiJYnTSsiCQWYyuC1UnDikhiMbYiWJ00rIgkFmMrgtVJw4pIYjG2IlidNKyIJBZjK4LVScOKSGIx9kyRBxCRADOd5J92AAAAAElFTkSuQmCC"}'
  event = {'body': postBody}
  endpoint(event, None)
