# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   os import environ

from decouple import config

class Config(object):

    basedir    = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = config('SECRET_KEY')

    # This will connect to the FTS db
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI', default='sqlite:///' + '/opt/FTSServer-UI.db')

    # certificates path
    certpath = config("CERT_DIR", default="/usr/local/lib/python3.8/dist-packages/FreeTAKServer/certs/").rstrip("/") + "/"

    # crt file path
    crtfilepath = config("CERT_PUB_KEY_PATH", default=f"{certpath}pubserver.pem")

    # key file path
    keyfilepath = config("CERT_PRIV_KEY_PATH", f"{certpath}pubserver.key.unencrypted")

    # this IP will be used to connect with the FTS API
    IP = config("FTS_HOST", default='127.0.0.1')

    # The URL the client uses
    IP_CLIENT = config("FTS_HOST_CLIENT", default="127.0.0.1")

    # Port the  UI uses to communicate with the API
    PORT = config("FTS_API_PORT", default='19023')

    # the public IP your server is exposing
    APPIP = config("BIND_IP", default="0.0.0.0")

    # webmap IP
    WEBMAPIP = config("WEB_MAP_HOST", default="127.0.0.1")

    # webmap port
    WEBMAPPORT = config("WEB_MAP_PORT", default=8000)

    # this port will be used to listen
    APPPort = config("BIND_PORT", default=5000)

    # the webSocket  key used by the UI to communicate with FTS.
    WEBSOCKETKEY = config("FTS_WEBSOCKET_KEY")

    # the API key used by the UI to comunicate with FTS. generate a new system user and then set it
    APIKEY = config("FTS_API_KEY", default='Bearer token')

    # For 'in memory' database, please use:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
            
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
