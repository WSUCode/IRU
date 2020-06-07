
import os
from pony import orm
from pony.orm.core import Json, Optional, PrimaryKey, Required
from setting import db

root_path = os.getcwd()

db_path = os.path.join( root_path, 'data', 'iru.db' )


def make_locale_mo():
    po_files = os.listdir( 
        os.path.join( root_path , 'locale', )
     )
    
    for f in po_files:
        f = f'{root_path}/locale/{f}/LC_MESSAGES/iru'
        os.system( f'msgfmt -o {f}.mo {f}.po' )

def init():
    if not os.path.exists('locale/en_US/LC_MESSAGES/iru.mo'):
        make_locale_mo()