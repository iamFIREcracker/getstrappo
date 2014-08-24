#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.controllers import IndexController
from app.controllers import IndexENController
from app.controllers import IndexITController
from app.controllers import OldIndexController
from app.controllers import TOSController


URLS = (
    '/', IndexController,
    '/en', IndexENController,
    '/it', IndexITController,
    '/old', OldIndexController,
    '/tos', TOSController,
)
