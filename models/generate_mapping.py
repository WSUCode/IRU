
from pony import orm
from iru import db
import os
from iru import root_path

db  = orm.Database()
db.bind(
    provider='sqlite', 
    filename= os.path.join( root_path, 'data', 'iru.db' ) , 
    create_db=True)

if __name__ == "__main__":
    db.generate_mapping(create_tables=True)
    pass