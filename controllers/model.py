from sqlalchemy import *
from sqlalchemy import event
from sqlalchemy.orm import *

# Logging / uncomment the lines below to enable
#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)
#logging.getLogger('sqlalchemy.orm.unitofwork').setLevel(logging.DEBUG)

# Create a db engine
db_engine = create_engine('sqlite:///store.db', pool_recycle=3600)

# show the SQL operations
db_engine.echo = True

# create metadata and bind to the db_engine
metadata = MetaData()
metadata.bind = db_engine

# Define tables and classes
# User table 
user = Table('user', metadata,
    Column('user_id', Integer, primary_key = True),
    Column('user_name', String(16), nullable = False),
    Column('email_address', String(60), nullable = False),
    Column('hash', String(60), nullable = False),
    Column('password', String(20), nullable = False)
)

'''
# Example of table and relationship / foreign key.
user_prefs = Table('user_prefs', metadata,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)
'''

metadata.create_all(db_engine, checkfirst=True)

class User(object):
	pass

mapper(User, user)