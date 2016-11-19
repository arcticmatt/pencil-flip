#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'arctictern'
SITENAME = u'pencil flip'
# Needed for Disqus URLS to work
# SITEURL = 'http://blog.pencilflip.com'
SITEURL = ''
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['tag_cloud']

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('spotify', 'https://open.spotify.com/user/1240806741'),
          ('bandcamp', 'https://bandcamp.com/mattlim'),
          ('goodreads', 'https://www.goodreads.com/user/show/41722131-matt-lim'),
          ('github', 'https://github.com/arcticmatt/'),
          ('linkedin', 'https://www.linkedin.com/pub/matt-lim/a6/1a5/b31'),)

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom URL
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/custom.css']
# Change path of custom.css to 'static/custom.css' in output dir
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
        'extra/custom.css': {'path': 'static/custom.css'},}

# Theme. I look good.
THEME = '../pelican-bootstrap3'
FAVICON = 'images/favicon.png'
SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 130
HIDE_SITENAME = True
PYGMENTS_STYLE = 'solarizedlight'

# Custom CSS
CUSTOM_CSS = 'static/custom.css'

# Disqus stuff
DISQUS_SITENAME = 'pencilflip'
DISQUS_SHORTNAME = 'pencilflip'
DISQUS_DISPLAY_COUNTS = True

# Exclude articles
#ARTICLE_EXCLUDES = ['Life-in-Haiku']
