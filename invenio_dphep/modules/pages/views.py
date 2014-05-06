from flask import Blueprint, render_template
from jinja2 import TemplateNotFound


blueprint = Blueprint(
	'pages', 
	__name__, 
	url_prefix='/pages',
	template_folder='templates',
	static_folder='static',
	static_url_path=''
)

@blueprint.route('/', defaults={'page': 'index'}, methods=['GET', 'POST'])
@blueprint.route('/<page>')
def view(page):
	try:
		return render_template('pages/%s.html' % page)
	except TemplateNotFound:
			abort(404)


