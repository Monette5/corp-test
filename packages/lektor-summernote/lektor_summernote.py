# -*- coding: utf-8 -*-

import pkg_resources
from flask import Blueprint, render_template_string
from lektor.admin.modules import dash
from lektor.pluginsystem import Plugin

TEMPLATE = '''
{% extends "dash.html" %}
{% block scripts %}
  {{ super() }}
<script type="text/javascript" src="/static/jquery.js"></script>
<link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css" />
<link href="/static/bootstrap.min.css" media="all" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="/static/bootstrap.min.js"></script>
<link rel="stylesheet" href="/static/summernote.css" rel="stylesheet">
<script type="text/javascript" src="/static/summernote.js"></script>
<script type="text/javascript" src="/static/summernoteCall.js"></script>

                
{% endblock %}
'''
   

def patched_endpoint(*args, **kwargs):
    return render_template_string(TEMPLATE)


class SummernotePlugin(Plugin):
    name = 'lektor-summernote'
    description = u'Add your description here.'

    def on_server_spawn(self, *args, **kwargs):
        # remove all rules except the first one which is edit redirect
        while len(dash.bp.deferred_functions) > 1:
            dash.bp.deferred_functions.pop()
        # ... and fill all the rules back with our wrapper template
        for path, endpoint in dash.endpoints:
            dash.bp.add_url_rule(path, endpoint, patched_endpoint)
