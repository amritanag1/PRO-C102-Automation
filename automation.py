import cv2
import random
import time

startTime = time.time()

def TakeImage(): 
    number = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "NewPicture" + str(number) + ".jpg"
        print(img_name)
        cv2.imwrite(img_name,frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()



while(True):
    if((time.time()-startTime) >= 600):
        TakeImage()



