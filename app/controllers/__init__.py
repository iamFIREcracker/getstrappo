#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from functools import partial

import web


class AppController(object):
    def GET(self):
        user_agent = web.ctx.environ.get('HTTP_USER_AGENT')
        if 'Android' in user_agent:
            raise web.seeother(web.config.ANDROID_DOWNLOAD_URL)
        if 'iPhone' in user_agent or 'iPad' in user_agent:
            raise web.seeother(web.config.ITUNES_DOWNLOAD_URL)
        raise web.seeother('/')


class IndexController(object):
    def GET(self):
        lang = web.ctx.environ.get('HTTP_ACCEPT_LANGUAGE')
        lang = lang.split(',')[0] if lang else 'en-US'
        lang = lang.split('-')[0]
        raise web.seeother(lang)


class IndexController(object):
    def GET(self, lang='en'):
        if lang not in ['en', 'it']:
            raise web.seeother('en')

        return web.ctx.render.\
            index(_=partial(web.ctx.gettext,
                            lang=lang),
                  android_download_url=web.config.ANDROID_DOWNLOAD_URL,
                  itunes_download_url=web.config.ITUNES_DOWNLOAD_URL,
                  year=datetime.now().year)


class IndexLangController(object):
    def GET(self, lang):
        if lang not in ['en', 'it']:
            raise web.seeother('en')

        return web.ctx.render.\
            index(_=partial(web.ctx.gettext,
                            lang=lang),
                  android_download_url=web.config.ANDROID_DOWNLOAD_URL,
                  itunes_download_url=web.config.ITUNES_DOWNLOAD_URL,
                  year=datetime.now().year)


class OldIndexController(object):
    def GET(self):
        return web.ctx.render.oldindex()


class TOSController(object):
    def GET(self):
        return web.ctx.render.tos()


class SitemapController(object):
    def GET(self):
        web.header('Content-Type', 'text/xml')
        return web.ctx.render.sitemap()
