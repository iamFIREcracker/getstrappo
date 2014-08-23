#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
import web

from app.weblib.controllers import AbstractCookieAuthorizableController
from app.weblib.controllers import AbstractParamAuthorizableController


class IndexController(object):
    def GET(self):
        lang = web.ctx.environ.get('HTTP_ACCEPT_LANGUAGE')
        lang = lang.split(',')[0] if lang else 'en-US'
        return web.ctx.render.index(gettext=partial(web.ctx.gettext,
                                                    lang=lang))

class OldIndexController(object):
    def GET(self):
        return web.ctx.render.oldindex()

class TOSController(object):
    def GET(self):
        return web.ctx.render.tos()
