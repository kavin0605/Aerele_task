from app import create_app, db
from app.models import Product, Location, ProductMovement

app = create_app()

with app.app_context():
    db.create_all()
    if not Product.query.first():
        products = [
            Product(id='P-A', name='Product A'),
            Product(id='P-B', name='Product B'),
            Product(id='P-C', name='Product C'),
            Product(id='P-D', name='Product D'),
        ]
        db.session.add_all(products)
    if not Location.query.first():
        locations = [
            Location(id='L-X', name='Location X'),
            Location(id='L-Y', name='Location Y'),
            Location(id='L-Z', name='Location Z'),
            Location(id='L-W', name='Location W'),
        ]
        db.session.add_all(locations)
    db.session.commit()

    # Sample movements (ensure idempotency by checking existence)
    if ProductMovement.query.count() < 5:
        moves = [
            ProductMovement(product_id='P-A', to_location_id='L-X', qty=10),  # add stock
            ProductMovement(product_id='P-B', to_location_id='L-X', qty=5),
            ProductMovement(product_id='P-A', from_location_id='L-X', to_location_id='L-Y', qty=3),  # transfer
            ProductMovement(product_id='P-A', to_location_id='L-X', qty=7),
            ProductMovement(product_id='P-B', from_location_id='L-X', qty=2),  # remove
        ]
        db.session.add_all(moves)
        db.session.commit()
    print('Seed complete.')
