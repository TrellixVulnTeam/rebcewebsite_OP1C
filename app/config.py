import os
class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')

####This config is for production but also local tests on remote google CloudSQL
class ProductionConfig(Configuration):
    DEBUG = True
    PROJECT_ID = 'rebcewebsite-176915' # Can be found at: https://console.developers.google.com
