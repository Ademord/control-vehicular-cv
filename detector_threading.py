import cv2
import camara
import reconocedor
import threading
import adaptadorBDMiembro
import adaptadorBDRegistro
import adaptadorBDLugar



#cascPath = "haarcascade_frontalface_alt.xml"
cascPath = "haarcascade_russian_plate_number.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

class Detector(threading.Thread):
	def __init__(self, thread_id, name, cam):
		threading.Thread.__init__(self)
		self.name = name
		self.thread_id = thread_id
		self.cam =  camara.Camara() 
		# verificar si asi se desempaqueta un diccionario
		# self.cam =  Camara(**cam) 
		self.name = name + " " + self.cam.ip
		self.thread_lock = threading.Lock()

	def run(self):
		print("Starting " + self.name)
		window_name = self.name
		cv2.namedWindow(window_name)
		count = 0
		while True:
			if count%30 == 0:
				got_a_frame, image = self.cam.read()
				if not got_a_frame:  # error on video source or last frame finished
					print("Error getting the frame")
					break
				# cv2.imshow(window_name, image)
				plate, precision = reconocedor.plate_detect(image, self.thread_id)
				miembro = adaptadorBDMiembro.findMiembroByPlate(plate)
				print("(" + plate + ", " + precision + ", " + miembro + ")")
				# compare plate against template
				if plate:
					adaptadorBDRegistro.save(self.cam.ip, adaptadorBDLugar.find(self.cam.lugar_id), plate, miembro, image)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			count+=1

		cv2.destroyWindow(window_name)
		print(self.name + " Exiting")

	def run_rectangles(self):
		while(True):
			# Capture frame-by-frame
			ret, frame = self.cam.read() 
			# Display the resulting frame
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags=cv2.CASCADE_SCALE_IMAGE
			)
			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			# Display the resulting frame
			return frame
			# threading.Thread(None, cv2.imshow, None, (self.name, original_frame)).start()

		#dilema: multiples placas en una sola imagen
