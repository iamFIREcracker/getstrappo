#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.weblib.controllers import AbstractCookieAuthorizableController
from app.weblib.controllers import AbstractParamAuthorizableController


class IndexController(object):
    def GET(self):
        return web.ctx.render.index()

class OldIndexController(object):
    def GET(self):
        return web.ctx.render.oldindex()

class TOSController(object):
    def GET(self):
        return web.ctx.render.tos()
