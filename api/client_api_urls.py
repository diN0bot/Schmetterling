from django.conf.urls.defaults import patterns, url

from django.contrib import admin
admin.autodiscover()

# this is all wrong. should be an API with settings for the Version One and Git Hub interactions

identifier_re = '[\w\d_-]+'
for var in ['identifier',
            'outter_box',
            'inner_box',
            'leaf1',
            'leaf2']:
    locals()[var] = '(?P<%s>%s)' % (var, identifier_re)

urlpatterns = patterns('data_store.client_api',
    url(r'^boxes/$', 'boxes', name='boxes'),
    url(r'^box/%s/$' % identifier, 'box', name='box'),

    url(r'^leaves/$', 'leaves', name='leaves'),
    url(r'^leaf/%s/$' % identifier, 'leaf', name='leaf'),

    url(r'^nest/%s/in/%s/$' % (outter_box, inner_box), 'nest', name='nest'),
    url(r'^unnest/%s/$' % identifier, 'unnest', name='unnest'),

    url(r'^merge_leaves/%s/and/%s/$' % (leaf1,
                                         leaf2),
        'merge_leaves', name='merge_leaves'),
)
