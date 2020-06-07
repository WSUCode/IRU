
from pony import orm
from setting import db
from pony.orm.core import Json, Optional, PrimaryKey, Required

class IruPersonGender( Enum ):
    male = 0 
    female = 1
    unknown = 2

class IruPerson( db.Entity ):
    id = PrimaryKey(int, auto=True)
    name = Required( str )
    age = Optional( int )
    gender = Optional( int )
    school = Optional( str )
    enrolling_date = Optional( str )
    schooling_length = Optional( int )
    face_encodings = Required( Json )

db.generate_mapping(create_tables=True)