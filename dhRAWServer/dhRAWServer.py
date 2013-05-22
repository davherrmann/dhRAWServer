'''
Created on 21 May 2013

@author: dherrmann
'''

import util_xml
import cherrypy
from util_exif import extract_exifs_from_folder as extract_exifs

imageSourceFolder = "./imageSource"

class ImageInfoXML(object):
    @cherrypy.expose
    def index(self):
        return util_xml.to_xml(extract_exifs(imageSourceFolder))

cherrypy.config.update({'server.socket_host': '0.0.0.0'} )   
cherrypy.quickstart(ImageInfoXML(), "/", "dhRAWServer.config")