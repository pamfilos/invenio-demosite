"""WebNews database model"""

# General imports
from invenio.ext.sqlalchemy import db
import datetime


# Many-to-Many relationship table
story_tag_association = db.Table('nwsSTORY_nwsTAG',
	db.Column('story_id', db.Integer(11), db.ForeignKey('nwsTAG.id'))
	db.Column('tag_id', db.Integer(11), db.ForeignKey('nswSTORY.id'))
)

class NwsSTORY(bd.Model):
	"""Represents a NwsSTORY record"""

	__tablename__ = 'nwsSTORY'
	id = db.Column( db.Integer(11, unsigned = True), 
		nullable = False, primary_key=True ,
		autoincrement = True)
	title = db.Column( db.String(256), nullable = False )
	body = db.Column(db.Text, nullable=True)
    created_date = db.Column(db.DateTime, nullable=False,
        default= db.func.now())
    updated_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class NwsTOOLTIP(db.Model):
	"""Represents a NwsTOOLTIP record"""
		
	__tablename__ = 'nwsTOOLTIP'
	id = db.Column( db.Integer(11, unsigned = True),
		nullable = False, primary_key=True, 
		autoincrement=True)
	id_story = db.Column( db.Integer(11, unsigned=True),
		nullable = False, db.ForeignKey(NwsSTORY.id))
	body = db.Column(db.Text, nullable=True)
	target_element = db.Column(db.Text, nullable=True)
	target_page = db.Column(db.Text, nullable=True)

class NwsTAG(db.Model):
 	"""Represents a NwsTAG model"""

 	__tablename__ = 'nwsTAG'
 	id = db.Column( db.Integer(11, unsigned = True),
 		nullable = False, 
 		primary_key = True,
 		autoincrement = True)
 	tag = db.Column (db.String(64), nullable=False)


