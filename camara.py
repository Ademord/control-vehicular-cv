import cv2
class Camara():
	def __init__(self, ip = "111.222.0.1", lugar_id = 0 , subtype = 0, URL = 0):
		self.ip = ip
		self.lugar_id = lugar_id
		self.subtype = subtype # 1: low res
		self.URL = URL
		if ip != "":
			self.URL = "rtsp://admin:admin@{0}:554/cam/realmonitor?channel=1&subtype={1}&unicast=true&proto=Onvif".format(self.ip, self.subtype)
		self.capture = cv2.VideoCapture(self.URL)
	def __del__(self):
		self.capture.release()

	def read(self):
		return self.capture.read()

