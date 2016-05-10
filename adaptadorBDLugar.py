import BD
def find(id):
	print("Query: query lugares")
	lugar = BD.execute("SELECT nombre FROM lugar WHERE id = '{}';".format(id))
	if lugar:
		lugar = lugar[0][0]
	else:
		lugar = "S/N"
	return lugar