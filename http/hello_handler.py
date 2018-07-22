#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

class HelloHandler(RequestHandler):

    def get(self):
        self.write('Hello World!')


