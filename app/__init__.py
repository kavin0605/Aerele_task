import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config: dict | None = None):
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///inventory.db')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
	if test_config:
		app.config.update(test_config)

	db.init_app(app)
	migrate.init_app(app, db)

	from . import models  # noqa: F401 ensure models are registered

	from .routes.products import bp as products_bp
	from .routes.locations import bp as locations_bp
	from .routes.movements import bp as movements_bp
	from .routes.reports import bp as reports_bp
	app.register_blueprint(products_bp)
	app.register_blueprint(locations_bp)
	app.register_blueprint(movements_bp)
	app.register_blueprint(reports_bp)

	@app.route('/')
	def index():
		from .models import Product, Location, ProductMovement
		
		# Get actual counts from database
		total_products = Product.query.count()
		total_locations = Location.query.count()
		total_movements = ProductMovement.query.count()
		
		# Calculate active inventory (non-zero balances) with error handling
		try:
			balance_data = ProductMovement.balance_query()
			active_inventory = len([item for item in balance_data if item.get('qty', 0) > 0])
		except Exception:
			active_inventory = 0
		
		# Get recent movements for activity feed
		recent_movements = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).limit(5).all()
		
		# Format recent movements with product and location names
		formatted_movements = []
		for movement in recent_movements:
			product = Product.query.get(movement.product_id)
			from_location = Location.query.get(movement.from_location_id) if movement.from_location_id else None
			to_location = Location.query.get(movement.to_location_id) if movement.to_location_id else None
			
			formatted_movements.append({
				'id': movement.id,
				'product_name': product.name if product else movement.product_id,
				'from_location_name': from_location.name if from_location else 'Stock Addition',
				'to_location_name': to_location.name if to_location else 'Stock Removal',
				'quantity': movement.qty,
				'timestamp': movement.timestamp
			})
		
		return render_template('index.html', 
							 total_products=total_products,
							 total_locations=total_locations, 
							 total_movements=total_movements,
							 active_inventory=active_inventory,
							 recent_movements=formatted_movements)

	return app

