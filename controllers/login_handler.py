import crypt
import pdb
import util

class Login:

	username = ""
	password = ""
	
	def __init__(self, username = None, password = None):
		# initialize login model
		self.username = username
		self.password = password
	
	def verify(self):
		#verify login
		dbstransaction = model.Session()
		user_record_query = dbstransaction.query(model.User).filter(model.User.user_name == self.user_name)
		try:
			result = user_record_query.one()
			if(result and util.decrypt(result.Hash,result.Password) == self.password):
				return True
			else:
				return False
		except: 
			return False
		
class TestLogin(Login):
	
	def verify(self):
		# test login 
		return True if (self.user_name == "username" and self.password == "password") else False