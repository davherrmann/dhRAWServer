'''
Created on 21 May 2013

@author: dherrmann
'''

import json
import cherrypy
from util_exif import extract_exifs_from_folder as extract_exifs

imageSourceFolder = "./imageSource"

class ImageInfoJSON(object):
    @cherrypy.expose
    def index(self):
        return json.dumps(extract_exifs(imageSourceFolder)).replace(", ", ",<br>")

cherrypy.config.update({'server.socket_host': '0.0.0.0'} )   
cherrypy.quickstart(ImageInfoJSON())