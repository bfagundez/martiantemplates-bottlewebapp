from bottle import *
from server import *

@webApp.get('/resource/<id>')
def get_resource(id):
	return None
	
@webApp.post('/resource/<id>')
def save_resource(id):
	return None

@webApp.put('/resource/<id>')
def update_resource(id):
	return None

@webApp.delete('/resource/<id>')
def delete_resource(id):
	return None