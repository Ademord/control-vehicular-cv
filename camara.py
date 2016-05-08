import cv2
class Camara():
	def __init__(self, ip = "", lugar = 0 , subtype = 1, URL = 0):
		self.ip = ip
		self.subtype = subtype # 1: low res
		if ip != "":
			URL = "rtsp://admin:admin@{0}:554/cam/realmonitor?channel=1&subtype={1}&unicast=true&proto=Onvif".format(self.ip, self.subtype)
		self.capture = cv2.VideoCapture(URL)
	def __del__(self):
		self.capture.release()

	def read(self):
		return self.capture.read()

