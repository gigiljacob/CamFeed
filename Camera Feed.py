#Code to read video feed from your webcam
#importing necessary packages
import cv2

class Cam:
  def startcam(self):
    #VideoCapture capture your video from source (here 0 is webcam). To take a video file specify filename in quotes 'example.mp4'
    video = cv2.VideoCapture(0)

    while True:
      #reading each frame of the Video obtained from source
      ret, frame = video.read()
      
      #displaying captured frame using imshow function
      cv2.imshow('frame', frame)
      
      #to exit the code
      if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break
    video.release()
    cv2.destroyAllWindows()
   
myObject = Cam()
myObject.startcam()
  
