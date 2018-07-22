#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urls import handlers
import tornado.web
import tornado.wsgi
import gevent.wsgi
from datetime import datetime

def get_tornado_application():
    application = tornado.web.Application(handlers, debug=True)
    return application

def get_wsgi_application():
    app = get_tornado_application()
    return tornado.wsgi.WSGIAdapter(app)


app = get_wsgi_application()

def run():
    server = gevent.wsgi.WSGIServer(('', 8000), app)
    print (datetime.now().strftime("[%Y-%m-%d %H:%m:%S] ") +
           'Server is running at http://127.0.0.1:8000 | Debug: ' + str(True) + '\n' +
           'Quit this server whit CTRL + C')
    server.serve_forever()



run()