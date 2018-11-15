import cv2
class Cam:
  def startcam(self):
    video = cv2.VideoCapture(0)

    while True:
      ret, frame = video.read()
      cv2.imshow('frame', frame)
      
      if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break
    video.release()
    cv2.destroyAllWindows()
   
myObject = Cam()
myObject.startcam()
  
