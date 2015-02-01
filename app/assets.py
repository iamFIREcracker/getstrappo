#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from webassets import Bundle
from webassets import Environment


env = Environment('./static', '/static')
env.debug = web.config.debug

env.register('css_all',
             Bundle('css/bootstrap.min.css',
                    'css/owl.theme.css',
                    'css/owl.theme.css',
                    'css/owl.carousel.css',
                    'css/nivo-lightbox.css',
                    'css/nivo_themes/default/default.css',
                    'css/animate.min.css',
                    'css/styles.css',
                    'css/colors/strappo-blue.css',
                    'css/responsive.css',
                    filters='cssmin',
                    output='css/all.%(version)s.css'))

env.register('js_custom',
             Bundle('js/custom.js',
                    filters='rjsmin',
                    output="js/custom.%(version)s.js"))
