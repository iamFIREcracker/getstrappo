#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.controllers import IndexController
from app.controllers import TOSController


URLS = (
    '/', IndexController,
    '/tos', TOSController,
)
