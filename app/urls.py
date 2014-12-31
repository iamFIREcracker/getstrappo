#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.controllers import IndexController
from app.controllers import IndexLangController
from app.controllers import OldIndexController
from app.controllers import TOSController
from app.controllers import SitemapController


URLS = (
    '/old', OldIndexController,
    '/tos', TOSController,
    '/sitemap.xml', SitemapController,

    '/', IndexController,
    '/(.+)', IndexLangController,
)
