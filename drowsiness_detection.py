import torch
import numpy as np
import winsound

model =  torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt', force_reload=True)
count = 0

def check_drowsy(frame):
    results = model(frame)
    global count
    output = [str(i) for i in results.pandas().xyxy[0]['name']]
    if('close' in output or 'yawn' in output):
        count = count+1
        if(count>5):                 # if more than 5 frame have closed eyes then start alert
            winsound.Beep(1000,100)
    else:
        count = 0
    return np.squeeze(results.render())