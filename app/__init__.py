#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import web

from . import config


web.config.debug = web.config.DEBUG = config.DEBUG
web.config.debug_sql = web.config.DEBUG_SQL = config.DEBUG_SQL

web.config.DEV = config.DEV

web.config.LOGGER_NAME = config.LOGGER_NAME
web.config.LOG_ENABLE = config.LOG_ENABLE
web.config.LOG_FORMAT = config.LOG_FORMAT

web.config.DISABLE_HTTP_ACCEPT_CHECK = config.DISABLE_HTTP_ACCEPT_CHECK


def app_factory():
    """App factory."""
    import weblib.gettext
    import weblib.redis
    from weblib.app_processors import load_gettext
    from weblib.app_processors import load_logger
    from weblib.app_processors import load_path_url
    from weblib.app_processors import load_redis
    from weblib.app_processors import load_render
    from weblib.app_processors import load_session
    from weblib.session import RedisStore

    from app.urls import URLS

    redis = weblib.redis.create_redis()
    views = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'views')
    app = web.application(URLS, globals())
    session = web.session.Session(app, RedisStore(redis))
    gettext = weblib.gettext.create_gettext()

    app.add_processor(web.loadhook(load_logger))
    app.add_processor(web.loadhook(load_path_url))
    app.add_processor(web.loadhook(load_render(views)))
    app.add_processor(web.loadhook(load_session(session)))
    app.add_processor(web.loadhook(load_gettext(gettext)))
    app.add_processor(web.loadhook(load_redis(redis)))

    return app
