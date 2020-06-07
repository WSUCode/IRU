
import os
from pony import orm
from pony.orm.core import Json, Optional, PrimaryKey, Required

from pony import orm

root_path = os.getcwd()

data_dir_path = os.path.join( root_path, 'data' )
db_path = os.path.join( root_path, 'data', 'iru.db' )


def make_locale_mo():
    po_files = os.listdir( 
        os.path.join( root_path , 'locale', )
     )
    
    for f in po_files:
        f = f'{root_path}/locale/{f}/LC_MESSAGES/iru'
        os.system( f'msgfmt -o {f}.mo {f}.po' )

def create_db():
    if not os.path.exists( data_dir_path ):
        os.makedirs( data_dir_path )
    db  = orm.Database()
    db.bind(
        provider='sqlite', 
        filename= db_path , 
        create_db=True)


def init():
    if not os.path.exists('locale/en_US/LC_MESSAGES/iru.mo'):
        make_locale_mo()
    if not os.path.exists( db_path ):
        create_db()
