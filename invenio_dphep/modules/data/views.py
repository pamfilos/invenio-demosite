from flask import Blueprint, render_template
from jinja2 import TemplateNotFound


blueprint = Blueprint(
	'data', 
	__name__, 
	url_prefix='/data',
	template_folder='templates',
	static_folder='static',
	static_url_path=''
)

@blueprint.route('/', defaults={'data': 'index'}, methods=['GET', 'POST'])
def view(data):
	try:
		return render_template('data/%s.html' % data)
	except TemplateNotFound:
			abort(404)

@blueprint.route('/policy/<policy>', methods=['GET', 'POST'])
def policy(policy):
	## For now there is no usability of the Data module
	## so it will just render an example page of a policy
	try:
		return render_template('data/policy.html')
	except TemplateNotFound:
		abort(404)


@blueprint.route('/policy2/<policy>', methods=['GET', 'POST'])
def policy2(policy):
	## For now there is no usability of the Data module
	## so it will just render an example page of a policy
	try:
		return render_template('data/policy2.html')
	except TemplateNotFound:
		abort(404)



