import cv2
import numpy as np
import camara
import reconocedor

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
		while(True):
			# Capture frame-by-frame
			temp = []
			for a in self.camaras:
				ret, frame = a.read() 
				temp.extend((frame,))
			#print(temp)
			both = np.hstack(temp)
			# Display the resulting frame
			cv2.imshow(self.name, both)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			# Save to image file on trigger
			if cv2.waitKey(1) & 0xFF == ord('s'):
				filename = r'C:\Users\Franco\Homestead\Projects\control-vehicular\storage\app\mat.png'
				mime = "image/png"
				cv2.imwrite(filename, both);
				#se deberia pasar a traves de hilos
				print("camara de llamada:", )
				filename = 'mat.png'
				reconocedor.process(self.camaras[0].ip, self.camaras[0].lugar, filename, mime)
				
		cv2.destroyAllWindows()