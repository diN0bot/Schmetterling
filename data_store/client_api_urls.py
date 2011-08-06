from django.conf.urls.defaults import patterns, url

from django.contrib import admin
admin.autodiscover()

identifier_re = '(?P<identifier>[\w\d_-]+)'

urlpatterns = patterns('data_store.client_api',
    url(r'^boxes/?$', 'boxes', name='boxes'),
    url(r'^box/%s/?$' % identifier_re, 'box', name='box'),

    url(r'^leaves/?$', 'leaves', name='leaves'),
    url(r'^leaf/%s/?$' % identifier_re, 'leaf', name='leaf'),

    url(r'^nest/%s/in/%s/?$' % (identifier_re,
                                identifier_re), 'nest', name='nest'),
    url(r'^unnest/%s/?$' % identifier_re, 'unnest', name='unnest'),

    url(r'^merge_leaves/%s/and/%s/?$' % (identifier_re,
                                         identifier_re),
        'merge_leaves', name='merge_leaves'),
)
