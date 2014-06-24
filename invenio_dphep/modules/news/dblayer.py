from time import localtime, mktime
from datetime import datetime

from invenio.ext.sqlalchemy import db
from invenio_dphep.modules.models import NwsStory, NwsTOOLTIP, NwsTAG

def get_latest_created_story_id():
	"""Returns the id of the latest created news story available."""

	return NwsStory.all().order_by(NwsStory.created_date).limit(1)

def get_latest_updated_story_id():
	"""Returns the id of the latest updated news story available."""

	return NwsStory.all().order_by(NwsStory.updated_date).limit(1)

def get_story_tooltips(story_id):
	"""Returns all the available tooltips for given story ID"""

	return NwsTOOLTIP.query(NwsTOOLTIP.id, NwsTOOLTIP.body,\
		NwsTOOLTIP.target_element, NwsTOOLTIP.target_page\
		).filter( NwsTOOLTIP.id_story = story_id)


def get_story_tags(story_id):
	"""Returns all TAGs for a given story ID"""

	return NwsTAG.query()