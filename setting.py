
import locale
import os
from pony import orm
import gettext
from unitils.init import make_locale_mo

default_locale  = locale.getdefaultlocale()[0]

if default_locale not in  os.listdir('locale'): default_locale = 'en_US'

if not os.path.exists( 'locale/en_US/LC_MESSAGES/iru.mo' ):
    make_locale_mo()

_ = gettext.translation('iru', 'locale', [ default_locale ] )\
    .gettext

root_path = os.getcwd()

db  = orm.Database()
db.bind(
    provider='sqlite', 
    filename= os.path.join( root_path, 'data', 'iru.db' ) , 
    create_db=True)
