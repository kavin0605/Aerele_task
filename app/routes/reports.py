from flask import Blueprint, render_template, jsonify
from collections import defaultdict
from ..models import ProductMovement, Product, Location
from sqlalchemy import func

bp = Blueprint('reports', __name__, url_prefix='/reports')


@bp.route('/balance')
def balance_report():
	# Compute balance per product+location
	rows = []
	for rec in ProductMovement.balance_query():
		product = Product.query.get(rec['product_id'])
		location = Location.query.get(rec['location_id']) if rec['location_id'] else None
		rows.append({
			'product': product.name if product else rec['product_id'],
			'product_id': rec['product_id'],
			'location': location.name if location else 'N/A',
			'location_id': rec['location_id'],
			'qty': rec['qty']
		})
	rows.sort(key=lambda x: (x['product'], x['location']))
	
	# Prepare chart data
	chart_data = prepare_chart_data(rows)
	
	return render_template('reports/balance.html', rows=rows, chart_data=chart_data)


@bp.route('/charts')
def charts_report():
	# Get all balance data
	balance_data = []
	for rec in ProductMovement.balance_query():
		product = Product.query.get(rec['product_id'])
		location = Location.query.get(rec['location_id']) if rec['location_id'] else None
		balance_data.append({
			'product': product.name if product else rec['product_id'],
			'product_id': rec['product_id'],
			'location': location.name if location else 'N/A',
			'location_id': rec['location_id'],
			'qty': rec['qty']
		})
	
	# Get movement trends
	movement_trends = get_movement_trends()
	
	# Prepare comprehensive chart data
	chart_data = prepare_comprehensive_chart_data(balance_data, movement_trends)
	
	return render_template('reports/charts.html', chart_data=chart_data)


@bp.route('/api/chart-data')
def api_chart_data():
	"""API endpoint for dynamic chart data"""
	balance_data = []
	for rec in ProductMovement.balance_query():
		product = Product.query.get(rec['product_id'])
		location = Location.query.get(rec['location_id']) if rec['location_id'] else None
		balance_data.append({
			'product': product.name if product else rec['product_id'],
			'product_id': rec['product_id'],
			'location': location.name if location else 'N/A',
			'location_id': rec['location_id'],
			'qty': rec['qty']
		})
	
	movement_trends = get_movement_trends()
	chart_data = prepare_comprehensive_chart_data(balance_data, movement_trends)
	
	return jsonify(chart_data)


def prepare_chart_data(rows):
	"""Prepare basic chart data for balance report"""
	# Product totals
	product_totals = defaultdict(int)
	for row in rows:
		product_totals[row['product']] += row['qty']
	
	# Location totals
	location_totals = defaultdict(int)
	for row in rows:
		if row['location'] != 'N/A':
			location_totals[row['location']] += row['qty']
	
	return {
		'product_labels': list(product_totals.keys()),
		'product_data': list(product_totals.values()),
		'location_labels': list(location_totals.keys()),
		'location_data': list(location_totals.values())
	}


def prepare_comprehensive_chart_data(balance_data, movement_trends):
	"""Prepare comprehensive chart data for charts report"""
	# Product totals
	product_totals = defaultdict(int)
	for row in balance_data:
		product_totals[row['product']] += row['qty']
	
	# Location totals
	location_totals = defaultdict(int)
	for row in balance_data:
		if row['location'] != 'N/A':
			location_totals[row['location']] += row['qty']
	
	# Stock status distribution
	well_stocked = len([r for r in balance_data if r['qty'] > 10])
	low_stock = len([r for r in balance_data if 0 < r['qty'] <= 10])
	out_of_stock = len([r for r in balance_data if r['qty'] <= 0])
	
	return {
		'product_labels': list(product_totals.keys()),
		'product_data': list(product_totals.values()),
		'location_labels': list(location_totals.keys()),
		'location_data': list(location_totals.values()),
		'stock_status_labels': ['Well Stocked', 'Low Stock', 'Out of Stock'],
		'stock_status_data': [well_stocked, low_stock, out_of_stock],
		'movement_trends': movement_trends
	}


def get_movement_trends():
	"""Get movement trends over time"""
	from datetime import datetime, timedelta
	from .. import db
	
	# Get movements from last 30 days grouped by date
	thirty_days_ago = datetime.utcnow() - timedelta(days=30)
	
	movements = db.session.query(
		func.date(ProductMovement.timestamp).label('date'),
		func.count(ProductMovement.id).label('count'),
		func.sum(ProductMovement.qty).label('total_qty')
	).filter(
		ProductMovement.timestamp >= thirty_days_ago
	).group_by(
		func.date(ProductMovement.timestamp)
	).order_by('date').all()
	
	dates = []
	counts = []
	quantities = []
	
	for movement in movements:
		# Handle both date and string objects
		if hasattr(movement.date, 'strftime'):
			dates.append(movement.date.strftime('%Y-%m-%d'))
		else:
			dates.append(str(movement.date))
		counts.append(movement.count)
		quantities.append(movement.total_qty)
	
	return {
		'dates': dates,
		'movement_counts': counts,
		'total_quantities': quantities
	}

