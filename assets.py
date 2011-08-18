from django_assets import Bundle, register
js = Bundle('static/js/jquery-1.6.2.min.js', 'static/js/jquery-ui-1.8.15.custom.min.js', 'static/js/underscore-min.js', 'static/js/backbone-min.js', 'static/js/ICanHaz.min.js',
    filters = 'jsmin', output = 'static/js/packed.js')

backbone = Bundle('static/js/backbone/app.js', 'static/js/backbone/models.js', 'static/js/backbone/collections.js', 'static/js/backbone/routers.js', 'static/js/backbone/views.js',
    filters = 'jsmin', output = 'static/js/backbone.js')

css = Bundle('static/css/style.css', 'static/css/smoothness/jquery-ui-1.8.15.custom.css', 'static/css/grid.css',
    filters = 'cssutils', output = 'static/css/packed.css')

register('js_lib', js)
register('backbone', backbone)
register('css', css)
