from .db import db, environment, SCHEMA, add_prefix_for_prod

class Product(db.Model): # Singlular Capital
    __tablename__ = 'products' # lowercase plural

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    image = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String(40), nullable=False)
    status = db.Column(db.Boolean)
    review_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('reviews.id')), nullable=False)

    product_reviews_relationship = db.relationship('Review', back_populates='review_products_relationship')
    product_carts_relationship = db.relationship('Cart', back_populates='cart_products_relationship')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description': self.description,
            'type': self.type,
            'status': self.status,
            'review_id': self.review_id
        }


    def to_dict_no_items(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description': self.description,
            'type': self.type,
            'status': self.status
        }
