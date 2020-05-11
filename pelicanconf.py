#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

MAIN_MENU = True

AUTHOR = 'Renato Lelis'
SITEURL = 'https://rjlelis.github.io/'
SITENAME = "Renato Lelis"
SITETITLE = "Renato Lelis"
SITESUBTITLE = "Desenvolvedor | Inspirante a musico"
SITEDESCRIPTION = "Um blog onde vou escrever artigos técnicos e outras coisas que eu quiser"
SITELOGO = SITEURL + "images/profile.jpg"

COPYRIGHT_NAME = 'Renato Lelis'
COPYRIGHT_YEAR = datetime.today().year
FAVICON = SITEURL + "/images/favicon.png"

# Theme related
THEME = 'Flex'

PATH = 'content'

TIMEZONE = 'America/Fortaleza'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# LINKS = (
#     ("Portfolio", "#"),
# )

SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/renato-lelis"),
    ("github", "https://github.com/rjLelis"),
    ("twitter", "https://twitter.com/renato_lelis"),
    ("medium", "https://medium.com/@renatojlelis")
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
