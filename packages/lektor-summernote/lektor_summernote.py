import email

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
 <script src="/javascripts/disablebuttonsnew.js"></script> 
  <script>
    (new MutationObserver(function() {
            [...document.getElementsByTagName('textarea')].forEach(e => {
            if (e.className === 'form-control') {
            e.id = "summernote";

            var editor = $(e).summernote({
                height: 150,   //set editable area's height
                callbacks: {
                onChange: function(contents, $editable) {
                    console.log('onChange:', contents, $editable);
                }
                }
                }).on('summernote.change', function(customEvent, contents, $editable) { 
         });
        var stuff = $('textarea#summernote.form-control').summernote('code');
          Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set.call(e, stuff);
            let ev = new Event('input', { bubbles: true });
            ev.simulated = true;
            e.dispatchEvent(ev);
    }; 
    });
    })).observe(
        document.getElementsByTagName('body')[0],
        {
            subtree: true,
            childList: true
        },
    );
  </script>
{% endblock %}
'''


def get_description(mod):
    distribution = pkg_resources.get_distribution(mod)
    if distribution.has_metadata('PKG-INFO'):
        meta = distribution.get_metadata('PKG-INFO')
    elif distribution.has_metadata('METADATA'):
        meta = distribution.get_metadata('METADATA')
    else:
        return None
    return email.message_from_string(meta).get('Summary', None)


def patched_endpoint(*args, **kwargs):
    return render_template_string(TEMPLATE)


class SummernotePlugin(Plugin):
    name = 'Summernote'
    description = get_description(__module__)

    def on_server_spawn(self, *args, **kwargs):
        # remove all rules except the first one which is edit redirect
        while len(dash.bp.deferred_functions) > 1:
            dash.bp.deferred_functions.pop()
        # ... and fill all the rules back with our wrapper template
        for path, endpoint in dash.endpoints:
            dash.bp.add_url_rule(path, endpoint, patched_endpoint)
