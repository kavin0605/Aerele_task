from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .. import db
from ..models import ProductMovement, Product, Location

bp = Blueprint('movements', __name__, url_prefix='/movements')


@bp.route('/')
def list_movements():
	movements = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).limit(200).all()
	return render_template('movements/list.html', movements=movements)


@bp.route('/stock-info')
def stock_info():
	"""API endpoint to get current stock for a product at a location"""
	product_id = request.args.get('product_id')
	location_id = request.args.get('location_id')
	
	if not product_id or not location_id:
		return jsonify({'error': 'Missing product_id or location_id'}), 400
	
	stock = get_current_stock(product_id, location_id)
	return jsonify({'stock': stock})


@bp.route('/create', methods=['GET', 'POST'])
def create_movement():
	products = Product.query.order_by(Product.name).all()
	locations = Location.query.order_by(Location.name).all()
	if request.method == 'POST':
		product_id = request.form['product_id']
		from_location_id = request.form.get('from_location_id') or None
		to_location_id = request.form.get('to_location_id') or None
		qty = int(request.form['qty'])
		
		if not product_id or qty <= 0:
			flash('Product and positive quantity required', 'error')
		elif not from_location_id and not to_location_id:
			flash('Specify at least a from or to location', 'error')
		else:
			# Check if we have enough stock when moving FROM a location
			if from_location_id:
				current_stock = get_current_stock(product_id, from_location_id)
				if current_stock < qty:
					product = Product.query.get(product_id)
					location = Location.query.get(from_location_id)
					flash(f'Insufficient stock! Current stock of {product.name} at {location.name}: {current_stock} units. Cannot move {qty} units.', 'error')
					return render_template('movements/form.html', products=products, locations=locations, movement=None)
			
			mv = ProductMovement(product_id=product_id, from_location_id=from_location_id, to_location_id=to_location_id, qty=qty)
			db.session.add(mv)
			db.session.commit()
			flash('Movement recorded successfully', 'success')
			return redirect(url_for('movements.list_movements'))
	return render_template('movements/form.html', products=products, locations=locations, movement=None)


def get_current_stock(product_id, location_id):
	"""Get current stock for a product at a specific location"""
	balance_data = ProductMovement.balance_query()
	for item in balance_data:
		if item['product_id'] == product_id and item['location_id'] == location_id:
			return item['qty']
	return 0


@bp.route('/<int:mid>/delete', methods=['POST'])
def delete_movement(mid):
	mv = ProductMovement.query.get_or_404(mid)
	db.session.delete(mv)
	db.session.commit()
	flash('Movement deleted')
	return redirect(url_for('movements.list_movements'))

