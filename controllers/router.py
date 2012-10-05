from bottle import *
from server import *
import model

# importing static files.
@webApp.get('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@webApp.route('/')
@webApp.route('/home')
def home():
    return template('views/home', get_url = webApp.get_url )

@webApp.route('/admin')
def admin_section():
    
    dbtransaction = model.Session()
    users = dbtransaction.query(model.user).all()
    dbtransaction.close()
    
    return template('views/admin/userlist', get_url = webApp.get_url, users=users )

@webApp.route('/admin/user/edit/<user_id>')
def edit_user(user_id):
    
    dbtransaction = model.Session()
    user_data = dbtransaction.query(model.user).get(user_id)
    dbtransaction.close()
    
    return template('views/admin/user_form', get_url = webApp.get_url, user_data=user_data )

    
