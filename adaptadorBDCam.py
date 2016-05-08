import BD
def all():
	cams = BD.execute("""SELECT c.ip, c.lugar_id FROM camara c""")
	print("Query: all cams")
	return cams
