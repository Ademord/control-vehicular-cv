import BD
def findMiembroByPlate(plate):
	print("Query: query miembros")
	#OpenALPR
	#alt: reconocimiento erroneo
	query = """SELECT m.nombres, m.apellidos FROM miembro as m, placa as p WHERE p.miembro_id = m.id AND p.numero = '%s'""" % (plate)
	miembro = BD.execute(query)
	if miembro: 
		#print("-".join(miembro[0]))
		if len(miembro)>1:
			print("mas de un miembro tiene esta placa")
		miembro = "-".join(miembro[0])		
	else:
		miembro = "Miembro no registrado"
		# print(miembro)

	return miembro
	#Save
	#dilema: desnormalizacion de lugar
	#answer: if a camera changes over time, the data might change
	
	#dilema2: multcamarales filenames/fotos para un solo auto
	#answer: en algun **lugar** agrupar segun { x < fecha < y; placa = z }