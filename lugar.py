import BD
def find(id):
	print("Query: query lugares")
	lugar = BD.execute("SELECT nombre FROM lugar WHERE id = '{}';".format(id))
	lugar = lugar[0][0]
	return lugar