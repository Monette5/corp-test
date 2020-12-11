# -*- coding: utf-8 -*-

import pkg_resources
from flask import Blueprint, render_template_string
from lektor.admin.modules import dash
from lektor.pluginsystem import Plugin

TEMPLATE = '''
{% extends "dash.html" %}
{% block scripts %}
  {{ super() }}
 <script src="https://code.jquery.com/jquery-3.5.1.min.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.js"></script>

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
