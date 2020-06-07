
import locale
import os
from pony import orm
import gettext
from unitils.init import make_locale_mo

root_path = os.getcwd()

default_locale  = locale.getdefaultlocale()[0]

first_mo_file_path =  os.path.join(
    'locale', 'en_US',
    'LC_MESSAGES','iru.mo')

db_path = os.path.join( root_path, 'data', 'iru.db' )

if default_locale not in  os.listdir('locale'): 
    default_locale = 'en_US'

if not os.path.exists( first_mo_file_path ):
    make_locale_mo()

_ = gettext.translation('iru', 'locale', [ default_locale ] )\
    .gettext


db  = orm.Database()
db.bind(
    provider='sqlite', 
    filename= db_path , 
    create_db=True)
