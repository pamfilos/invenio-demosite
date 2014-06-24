# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""
    invenio_demosite.views
    -------------------------------

    Demosite interface.
"""
from invenio.base.i18n import _

from flask import Blueprint, render_template, redirect, url_for
from jinja2 import TemplateNotFound
from flask.ext.breadcrumbs import register_breadcrumb

blueprint = Blueprint('invenio_dphep', __name__, url_prefix='',
                      template_folder='templates', static_folder='static')


@blueprint.route('/')
@blueprint.route('/index')
def index():
	try:
		return render_template('index3.html')
		# return render_template('index.html')
	except TemplateNotFound:
		abort(404)

@blueprint.route('/about')
def about():
	title = _('About')
	try:
		return render_template('about.html', title=title)
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/workshops')
# @register_breadcrumb(blueprint, '.workshops', _('Workshops'))
def workshops():
	title = _("Workshops")
	try:
		return render_template('workshops2.html', title=title )
		# return render_template('workshops.html', title=title )
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/people')
def people():
	title = _('People')
	try:
		return render_template('people_byInstitute.html', title=title)
		# return render_template('people.html', title=title)
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/people/institutes')
def people_by_institutes():
	title = _('People')
	try:
		return render_template('people_byInstitute.html', title=title)
	except TemplateNotFound:
		redirect(url_for('.index'))


@blueprint.route('/press')
def press():
	try:
		return render_template('press2.html')
		# return render_template('press.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/find')
def find():
	try:
		return render_template('find2.html')
		# return render_template('find.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/submit')
def submit():
	try:
		return render_template('submit2.html')
		# return render_template('submit.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/learn')
def learn():
	try:
		return render_template('learn.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/contribute')
def fund():
	try:
		return render_template('fund.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/keynotes')
def keynote():
	try:
		return render_template('keynotes.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/news')
def news():
	try:
		return render_template('news.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/test/<page>')
# @register_breadcrumb(blueprint, '.news', _('Page'))
def test(page):
	try:
		return render_template('%s.html' % page)
	except TemplateNotFound:
			abort(404)
