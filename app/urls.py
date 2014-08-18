#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.controllers import IndexController
from app.controllers import OldIndexController
from app.controllers import TOSController


URLS = (
    '/', IndexController,
    '/old', OldIndexController,
    '/tos', TOSController,
)
