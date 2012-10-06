from bottle import *
from server import *
import model
import pdb
import util

'''
    =================================================================
    General routes
    =================================================================
'''

# importing static files.
@webApp.get('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

# Public home.
@webApp.route('/')
@webApp.route('/home')
def home():
    return template('views/home', get_url = webApp.get_url )

'''
    =================================================================
    Admin area routes
    =================================================================
'''

@webApp.route('/admin')
def admin_section():
    
    dbtransaction = model.Session()
    users = dbtransaction.query(model.user).all()
    dbtransaction.close()
    
    return template('views/admin/userlist', get_url = webApp.get_url, users=users )


'''
    =================================================================
    Admin area login flow 
    =================================================================
'''

@webApp.post('/admin/login')
def login_post():
  """Login form posts and is processed"""
  login = login_handler.Login()
  login.username = request.forms.get('username')
  login.password = request.forms.get('password')
  url_redirection = request.forms.get('urlredirect')
  if login.verify():
    sess = request.environ.get('beaker.session')
    sess['username'] = login.username
    sess['auth'] = True
    sess.save() 
    redirect(url_redirection)
  else:
    return template('views/admin/login',get_url=webApp.get_url,error="Invalid login, please try again")
    #return template('login', result = "Invalid login, please try again")

@webApp.route('/admin/logout')
def login_logout():
  """Remove authenticated session"""
  sess = request.environ.get('beaker.session')
  sess.delete()
  #return template('login/logout')
  return template('views/logout',get_url=webApp.get_url)

def require_auth():
  """Check session for username"""
  sess = request.environ.get('beaker.session')
  
  if not sess.get('auth', False):
    abort(403)
  else:
    return True


'''
    =================================================================
    User administration area
    =================================================================
'''

@webApp.route('/admin/user/<user_id>')
def edit_user(user_id):
    
    dbtransaction = model.Session()
    user_data = dbtransaction.query(model.User).get(user_id)
    dbtransaction.close()
    
    return template('views/admin/user_form', get_url = webApp.get_url, user=user_data )

@webApp.route('/admin/user/delete/<user_id>')
def edit_user(user_id):
    
    dbtransaction = model.Session()
    user_data = dbtransaction.query(model.User).get(user_id)
    dbtransaction.delete(user_data)
    dbtransaction.commit()
    dbtransaction.close()
    
    return redirect('/admin')

@webApp.route('/admin/user/new')
@webApp.route('/admin/user/new/')
def new_user():
    return template('views/admin/user_form', get_url = webApp.get_url, user=None )

@webApp.post('/admin/user/save')
def save_user():
    dbtransaction = model.Session()
    user_record = model.User()
    
    # edit user
    if request.POST.get('user_id') is not None:
        user_record = dbtransaction.query(model.User).get(request.POST.get('user_id'))
    
    user_record.user_name = request.POST.get('user_name')
    user_record.email_address = request.POST.get('email_address')
    user_record.hash = util.generateHash()
    user_record.password = util.encrypt(user_record.hash,request.POST.get('password'))
    
    dbtransaction.add(user_record)
    dbtransaction.commit()
    
    return redirect('/admin')

