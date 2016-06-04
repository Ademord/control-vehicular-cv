import BD
import fecha
import cv2
import uuid

def save(ip, lugar, placa, miembro, image, mismatch):
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
		"miembro": miembro,
		"mismatch": mismatch
	}
	
	query = "INSERT INTO registro(camara, lugar, filename, mime, placa, miembro, mismatch, created_at, updated_at) VALUES ('{camara}', '{lugar}', '{filename}', '{mime}', '{placa}', '{miembro}', '{mismatch}','{fecha}', '{fecha}');".format(**reg)
	print("Query: insert registro")
	BD.execute(query)