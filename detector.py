import cv2
import numpy as np
import camara
import reconocedor
import sys
import adaptadorBDMiembro
import threading
import adaptadorBDRegistro


#cascPath = "haarcascade_frontalface_alt.xml"
cascPath = "haarcascade_russian_plate_number.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

class Detector():
	def __init__(self, camaras, name = "Camaras"):
		self.name = name
		self.camaras = []
		#Set Cameras & Connect
		for cam in camaras:
			self.camaras.extend((camara.Camara(),))
			#self.camaras.extend((camara.Camara(cam[0],cam[1]),))
		print(self.camaras)
	def __del__(self):
		cv2.destroyAllWindows()

	def run(self):
		_cam = self.camaras[0]
		while(True):
			# Capture frame-by-frame
			ret, frame = _cam.read() 

			# Display the resulting frame
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags=cv2.CASCADE_SCALE_IMAGE
			)
			original_frame = frame.copy()

			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

			# Display the resulting frame
			cv2.imshow(self.name, original_frame)
			plate = ""
			if cv2.waitKey(1) & 0xFF == ord('r'):
				ret, enc = cv2.imencode("*.bmp", original_frame)
				plate, confidence = reconocedor.process(enc)

			# if cv2.waitKey(1) & 0xFF == ord('s'):
			if plate:
				filename = r'C:\Users\Franco\Homestead\Projects\control-vehicular\storage\app\mat.png'
				#cv2.imwrite(filename, original_frame);
				# se deberia pasar a traves de hilos
				camara = self.camaras[0].ip
				print(plate)
				# lugar = self.camaras[0].lugar_id
				filename = 'mat.png'
				mime = "image/png"
				miembro = adaptadorBDMiembro.findMiembroByPlate(plate)
				if miembro: 
					print("-".join(miembro[0]))
				else:
					print("Miembro no registrado") 
				# adaptadorBDRegistro.save(camara, lugar, filename, mime, plate)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		cv2.destroyAllWindows()

		#dilema: multiples placas en una sola imagen
