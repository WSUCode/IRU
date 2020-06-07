
import locale
import os
from pony import orm
import gettext

default_locale  = locale.getdefaultlocale()[0]

if default_locale not in  os.listdir('locale'): default_locale = 'en_US'

_ = gettext.translation('iru', 'locale', [ default_locale ] )\
    .gettext

root_path = os.getcwd()

db  = orm.Database()
db.bind(
    provider='sqlite', 
    filename= os.path.join( root_path, 'data', 'iru.db' ) , 
    create_db=True)
