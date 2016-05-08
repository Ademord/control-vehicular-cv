import time
import datetime
def getCurrentTimestamp():
	fecha = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	return fecha