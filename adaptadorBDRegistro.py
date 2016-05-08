import BD
import fecha
import lugar

def save(camara, lugar_id, filename, mime, placa):
	
	
	reg = {
		"camara": camara,
		"lugar": lugar.find(lugar_id),
		"filename": filename,
		"mime": mime,
		"placa": placa,
		"fecha": fecha.getCurrentTimestamp()
	}
	
	query = "INSERT INTO registro(camara, lugar, filename, mime, placa, created_at, updated_at) VALUES ('{camara}', '{lugar}', '{filename}', '{mime}', '{placa}', '{fecha}', '{fecha}');".format(**reg)
	print("Query: insert registro")
	BD.execute(query)