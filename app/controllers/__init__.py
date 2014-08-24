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
        lang = lang.split('-')[0]
        raise web.seeother(lang)

class IndexENController(object):
    def GET(self):
        return web.ctx.render.index(gettext=partial(web.ctx.gettext,
                                                    lang='en'))


class IndexITController(object):
    def GET(self):
        return web.ctx.render.index(gettext=partial(web.ctx.gettext,
                                                    lang='it'))


class OldIndexController(object):
    def GET(self):
        return web.ctx.render.oldindex()

class TOSController(object):
    def GET(self):
        return web.ctx.render.tos()
