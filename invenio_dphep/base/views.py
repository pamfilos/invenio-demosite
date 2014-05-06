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

from flask import Blueprint, render_template, redirect, url_for
from jinja2 import TemplateNotFound

blueprint = Blueprint('invenio_dphep', __name__, url_prefix='',
                      template_folder='templates', static_folder='static')


@blueprint.route('/')
@blueprint.route('/index')
def index():
	try:
		return render_template('index.html')
	except TemplateNotFound:
		abort(404)

@blueprint.route('/about')
def about():
	try:
		return render_template('index.html')
	except TemplateNotFound:
		abort(404)

@blueprint.route('/workshops')
def workshops():
	try:
		return render_template('workshops.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/people')
def people():
	try:
		return render_template('people.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/press')
def press():
	try:
		return render_template('press.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/find')
def search():
	try:
		return render_template('find.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/submit')
def submit():
	try:
		return render_template('submit.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/learn')
def learn():
	try:
		return render_template('learn.html')
	except TemplateNotFound:
		redirect(url_for('.index'))

@blueprint.route('/fund')
def fund():
	try:
		render_template('fund.html')
	except TemplateNotFound:
		redirect(url_for('.index'))