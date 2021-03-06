from openalpr import Alpr
from argparse import ArgumentParser
import cv2
import threading
import adaptadorBDLugar
import adaptadorBDMiembro
import adaptadorBDRegistro
import re

class recognize(threading.Thread):
    def __init__(self, image, cam):
        threading.Thread.__init__(self)
        self.image = image
        self.cam = cam 
        self.plate = ""
        self.precision = 0
        self.miembro = ""
    def process(self, data):
        plate = ""
        confidence = ""
        parser = ArgumentParser(description='OpenALPR Python Test Program')

        parser.add_argument("-c", "--country", dest="country", action="store", default="bo",
                          help="License plate Country" )

        OpenALPR_path = "C:/Users/Franco/Documents/Github/control-vehicular-cv/openalpr_32bit/"

        parser.add_argument("--config", dest="config", action="store", default=OpenALPR_path+"openalpr.conf",
                          help="Path to openalpr.conf config file" )

        parser.add_argument("--runtime_data", dest="runtime_data", action="store", default=OpenALPR_path+"runtime_data",
                          help="Path to OpenALPR runtime_data directory" )

        #parser.add_argument('plate_image', help='License plate image file')

        options = parser.parse_args()

        # print(options.country, options.config, options.runtime_data)

        alpr = None
        try:
            alpr = Alpr(options.country.encode('ascii'), options.config.encode('ascii'), options.runtime_data.encode('ascii'))

            if not alpr.is_loaded():
                print("Error loading OpenALPR")
            else:
                # print("Using OpenALPR " + alpr.get_version().decode('ascii'))

                alpr.set_top_n(7)
                alpr.set_default_region(b"wa")
                alpr.set_detect_region(False)
                # jpeg_bytes = open(options.plate_image, "rb").read()
                # results = alpr.recognize_array(jpeg_bytes)
                jpeg_bytes = data
                results = alpr.recognize_array(bytes(bytearray(data)))
                
                # Uncomment to see the full results structure
                # import pprint
                # pprint.pprint(results)

                # print("Image size: %dx%d" %(results['img_width'], results['img_height']))
                print("OpenALPR " + alpr.get_version().decode('ascii') + " (" + options.country + ") " + "pt: %.2f" % results['processing_time_ms'])

                i = 0 
                if results['results']:
                    plate = results['results'][0]['plate']
                    confidence = results['results'][0]['confidence']
                    #print("%12s%12f" % (plate, confidence))

        finally:
            if alpr:
                alpr.unload()

        return plate, confidence
    def run(self):
        print("Entering sub-thread")
        ret, enc = cv2.imencode("*.bmp", self.image)
        self.plate, self.precision = self.process(enc)
        print("(" + self.plate + ", " + str(self.precision) + ", " + self.miembro + ")")
        if self.plate:
            self.miembro = adaptadorBDMiembro.findMiembroByPlate(self.plate)
            license_plate = re.compile(r"^\d{1,4}[A-Z]{3}$",re.I)
            ml = True
            if license_plate.search(self.plate): ml = False
            print(ml)
            adaptadorBDRegistro.save(self.cam.ip, adaptadorBDLugar.find(self.cam.lugar_id), self.plate, self.miembro, self.image, ml)

        # compare plate against template
        print("Exiting sub-thread")
        