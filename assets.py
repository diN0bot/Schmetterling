from django_assets import Bundle, register
js = Bundle('static/js/jquery.1.6.1.min.js', 'static/js/underscore-min.js', 'static/js/backbone-min.js', 'static/js/ICanHaz.min.js',
    filters = 'jsmin', output = 'static/js/packed.js')

register('js_lib', js)
