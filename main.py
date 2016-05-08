#python 3.4
import detector as dt
import adaptadorBDCam
#Get Cameras
cams = adaptadorBDCam.all()
#Set Streams & Detection
detector = dt.Detector(cams)
detector.run()

