import BD
import fecha
import cv2
import uuid

def save(ip, lugar, placa, miembro, image):
	print("Query: query registro")
	filename = str(uuid.uuid4()) + ".png"
	path = r'C:/Users/Franco/Homestead/Projects/control-vehicular/storage/app/' + filename
	cv2.imwrite(path, image);
	mime = "image/png"
	reg = {
		"camara": ip,
		"lugar": lugar,
		"filename": filename,
		"mime": mime,
		"placa": placa,
		"fecha": fecha.getCurrentTimestamp(),
		"miembro": miembro
	}
	
	query = "INSERT INTO registro(camara, lugar, filename, mime, placa, miembro, created_at, updated_at) VALUES ('{camara}', '{lugar}', '{filename}', '{mime}', '{placa}', '{miembro}', '{fecha}', '{fecha}');".format(**reg)
	print("Query: insert registro")
	BD.execute(query)