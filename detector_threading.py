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

class Detector(threading.Thread):
	def __init__(self, thread_id, name, video_url, thread_lock):
		self.name = name
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.name = name
		self.video_url = video_url
		self.thread_lock = thread_lock

	def run(self):
		print "Starting " + self.name
		window_name = self.name
		cv2.namedWindow(window_name)
		video = cv2.VideoCapture(self.video_url)
		while True:
			got_a_frame, image = video.read()
			if not got_a_frame:  # error on video source or last frame finished
				break
			cv2.imshow(window_name, image)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

			if cv2.waitKey(1) & 0xFF == ord('r'):
				ret, enc = cv2.imencode("*.bmp", image)
				from multiprocessing.pool import ThreadPool
				pool = ThreadPool(processes=1)
				async_result = pool.apply_async(reconocedor.process, (enc)) # tuple of args for foo
				# do some other stuff in the main process
				plate = async_result.get()  # get the return value from your function.
				print(plate)
			# if cv2.waitKey(1) & 0xFF == ord('s'):
			if False:
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

		cv2.destroyWindow(window_name)
		print self.name + " Exiting"

	def run2(self):
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
			# threading.Thread(None, cv2.imshow, None, (self.name, original_frame)).start()
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

		#dilema: multiples placas en una sola imagen
