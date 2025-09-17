from datetime import datetime
from . import db


class Product(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.String(40), primary_key=True)  # product_id
	name = db.Column(db.String(120), nullable=False, unique=True)
	description = db.Column(db.Text, nullable=True)
	movements = db.relationship('ProductMovement', back_populates='product', cascade='all, delete-orphan')

	def __repr__(self):
		return f'<Product {self.id} {self.name}>'


class Location(db.Model):
	__tablename__ = 'locations'
	id = db.Column(db.String(40), primary_key=True)  # location_id
	name = db.Column(db.String(120), nullable=False, unique=True)
	movements_from = db.relationship('ProductMovement', foreign_keys='ProductMovement.from_location_id', back_populates='from_location')
	movements_to = db.relationship('ProductMovement', foreign_keys='ProductMovement.to_location_id', back_populates='to_location')

	def __repr__(self):
		return f'<Location {self.id} {self.name}>'


class ProductMovement(db.Model):
	__tablename__ = 'product_movements'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # movement_id
	timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	from_location_id = db.Column(db.String(40), db.ForeignKey('locations.id'), nullable=True)
	to_location_id = db.Column(db.String(40), db.ForeignKey('locations.id'), nullable=True)
	product_id = db.Column(db.String(40), db.ForeignKey('products.id'), nullable=False)
	qty = db.Column(db.Integer, nullable=False)

	product = db.relationship('Product', back_populates='movements')
	from_location = db.relationship('Location', foreign_keys=[from_location_id], back_populates='movements_from')
	to_location = db.relationship('Location', foreign_keys=[to_location_id], back_populates='movements_to')

	def __repr__(self):
		return f'<Movement {self.id} P:{self.product_id} {self.from_location_id}->{self.to_location_id} qty={self.qty}>'

	@staticmethod
	def balance_query():
		"""Return list of dicts with product_id, location_id, qty balance.
		Handles transfers by subtracting from source and adding to destination.
		"""
		from sqlalchemy import func
		incoming = (db.session.query(
			ProductMovement.product_id.label('product_id'),
			ProductMovement.to_location_id.label('location_id'),
			ProductMovement.qty.label('delta'))
			.filter(ProductMovement.to_location_id.isnot(None)))
		outgoing = (db.session.query(
			ProductMovement.product_id.label('product_id'),
			ProductMovement.from_location_id.label('location_id'),
			(-ProductMovement.qty).label('delta'))
			.filter(ProductMovement.from_location_id.isnot(None)))
		union_sub = incoming.union_all(outgoing).subquery()
		query = (db.session.query(
			union_sub.c.product_id,
			union_sub.c.location_id,
			func.sum(union_sub.c.delta).label('qty'))
			.group_by(union_sub.c.product_id, union_sub.c.location_id))
		return [
			{'product_id': r.product_id, 'location_id': r.location_id, 'qty': r.qty}
			for r in query if r.qty != 0
		]

