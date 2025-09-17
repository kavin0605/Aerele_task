from flask import Blueprint, render_template, request, redirect, url_for, flash
from .. import db
from ..models import Location

bp = Blueprint('locations', __name__, url_prefix='/locations')


@bp.route('/')
def list_locations():
	locations = Location.query.order_by(Location.name).all()
	return render_template('locations/list.html', locations=locations)


@bp.route('/create', methods=['GET', 'POST'])
def create_location():
	if request.method == 'POST':
		lid = request.form['id'].strip()
		name = request.form['name'].strip()
		if not lid or not name:
			flash('ID and Name required')
		elif Location.query.get(lid):
			flash('Location ID exists')
		else:
			loc = Location(id=lid, name=name)
			db.session.add(loc)
			db.session.commit()
			flash('Location created')
			return redirect(url_for('locations.list_locations'))
	return render_template('locations/form.html', location=None)


@bp.route('/<lid>/edit', methods=['GET', 'POST'])
def edit_location(lid):
	location = Location.query.get_or_404(lid)
	if request.method == 'POST':
		location.name = request.form['name'].strip()
		db.session.commit()
		flash('Location updated')
		return redirect(url_for('locations.list_locations'))
	return render_template('locations/form.html', location=location)


@bp.route('/<lid>')
def view_location(lid):
	location = Location.query.get_or_404(lid)
	return render_template('locations/view.html', location=location)


@bp.route('/<lid>/delete', methods=['POST'])
def delete_location(lid):
	location = Location.query.get_or_404(lid)
	db.session.delete(location)
	db.session.commit()
	flash('Location deleted')
	return redirect(url_for('locations.list_locations'))

