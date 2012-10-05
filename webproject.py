from bottle import *

# bussiness logic located in controllers
# check __init__ for the list of controllers loaded.
import controllers

# middleware for session management
from beaker.middleware import SessionMiddleware

session_opts = { 
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './session_data',
    'session.auto': True
}

thisapp = SessionMiddleware(controllers.server.webApp, session_opts)

# Start the Bottle webapp 
run(app=thisapp, host='0.0.0.0', port=8080, server=CherryPyServer) 

