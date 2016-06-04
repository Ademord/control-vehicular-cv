#python 3.4
import detector_threading as dt
import adaptadorBDCam

def main():
	print("1")
	cams = adaptadorBDCam.all()
	print(cams)
	for cam in cams:
		#self.camaras.extend((camara.Camara(cam[0],cam[1]),))
		print("2")

		thread1 = dt.Detector(1, "Thread 1", cam)
		# donde cam es una tupla (ip,lugar)
		# thread1 = MyThread(1, "Thread 1", cam, thread_lock)
		print("3")
		thread1.start()
	print("Exiting Main Thread")

if __name__ == '__main__':
    main()	