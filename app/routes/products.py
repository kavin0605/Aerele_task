from flask import Blueprint, render_template, request, redirect, url_for, flash
from .. import db
from ..models import Product

bp = Blueprint('products', __name__, url_prefix='/products')


@bp.route('/')
def list_products():
	products = Product.query.order_by(Product.name).all()
	return render_template('products/list.html', products=products)


@bp.route('/create', methods=['GET', 'POST'])
def create_product():
	if request.method == 'POST':
		pid = request.form['id'].strip()
		name = request.form['name'].strip()
		desc = request.form.get('description', '').strip()
		initial_stock = request.form.get('initial_stock', '0').strip()
		initial_location = request.form.get('initial_location', '').strip()
		
		if not pid or not name:
			flash('ID and Name required', 'error')
		elif Product.query.get(pid):
			flash('Product ID already exists', 'error')
		else:
			try:
				initial_stock = int(initial_stock) if initial_stock else 0
			except ValueError:
				flash('Initial stock must be a valid number', 'error')
				return render_template('products/form.html', product=None)
			
			# Create the product
			p = Product(id=pid, name=name, description=desc)
			db.session.add(p)
			
			# Add initial stock if specified
			if initial_stock > 0 and initial_location:
				from ..models import ProductMovement
				# Create an initial stock movement (incoming to location)
				mv = ProductMovement(
					product_id=pid,
					from_location_id=None,  # No source location (initial stock)
					to_location_id=initial_location,
					qty=initial_stock
				)
				db.session.add(mv)
				flash_msg = f'Product created with {initial_stock} units added to initial location'
			else:
				flash_msg = 'Product created successfully'
			
			db.session.commit()
			flash(flash_msg, 'success')
			return redirect(url_for('products.list_products'))
	
	# Get locations for the form
	from ..models import Location
	locations = Location.query.order_by(Location.name).all()
	return render_template('products/form.html', product=None, locations=locations)


@bp.route('/<pid>/edit', methods=['GET', 'POST'])
def edit_product(pid):
	from ..models import Location, ProductMovement
	product = Product.query.get_or_404(pid)
	locations = Location.query.order_by(Location.name).all()
	
	# Get current stock information for this product
	balance_data = ProductMovement.balance_query()
	current_stock = []
	for item in balance_data:
		if item['product_id'] == pid:
			location = Location.query.get(item['location_id']) if item['location_id'] else None
			current_stock.append({
				'location_id': item['location_id'],
				'location_name': location.name if location else 'Unknown',
				'quantity': item['qty']
			})
	
	if request.method == 'POST':
		product.name = request.form['name'].strip()
		product.description = request.form.get('description', '').strip()
		
		# Handle stock adjustment if provided
		stock_action = request.form.get('stock_action')
		if stock_action and stock_action in ['add', 'remove', 'transfer']:
			stock_quantity = request.form.get('stock_quantity')
			stock_location = request.form.get('stock_location')
			transfer_to_location = request.form.get('transfer_to_location')
			
			try:
				stock_quantity = int(stock_quantity) if stock_quantity else 0
				
				if stock_quantity > 0 and stock_location:
					if stock_action == 'add':
						# Add stock (incoming movement)
						mv = ProductMovement(
							product_id=pid,
							from_location_id=None,
							to_location_id=stock_location,
							qty=stock_quantity
						)
						db.session.add(mv)
						flash(f'Added {stock_quantity} units to inventory', 'success')
						
					elif stock_action == 'remove':
						# Remove stock (outgoing movement)
						mv = ProductMovement(
							product_id=pid,
							from_location_id=stock_location,
							to_location_id=None,
							qty=stock_quantity
						)
						db.session.add(mv)
						flash(f'Removed {stock_quantity} units from inventory', 'success')
						
					elif stock_action == 'transfer' and transfer_to_location:
						# Transfer stock between locations
						mv = ProductMovement(
							product_id=pid,
							from_location_id=stock_location,
							to_location_id=transfer_to_location,
							qty=stock_quantity
						)
						db.session.add(mv)
						flash(f'Transferred {stock_quantity} units from {stock_location} to {transfer_to_location}', 'success')
			except ValueError:
				flash('Invalid stock quantity', 'error')
		
		db.session.commit()
		flash('Product updated successfully', 'success')
		return redirect(url_for('products.list_products'))
		
	return render_template('products/form.html', product=product, locations=locations, current_stock=current_stock)


@bp.route('/<pid>')
def view_product(pid):
	product = Product.query.get_or_404(pid)
	return render_template('products/view.html', product=product)


@bp.route('/<pid>/delete', methods=['POST'])
def delete_product(pid):
	try:
		product = Product.query.get_or_404(pid)
		# The cascade='all, delete-orphan' in the model will automatically delete related movements
		db.session.delete(product)
		db.session.commit()
		flash('Product and all related movements deleted successfully', 'success')
	except Exception as e:
		db.session.rollback()
		flash(f'Error deleting product: {str(e)}', 'error')
	return redirect(url_for('products.list_products'))

