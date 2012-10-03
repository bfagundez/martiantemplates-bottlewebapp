from bottle import *
from server import *

# importing static files.
@webApp.get('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@webApp.route('/')
@webApp.route('/home')
def home():
    return template('views/home', get_url = webApp.get_url )