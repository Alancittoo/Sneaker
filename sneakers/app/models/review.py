from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .product import Product

class Review(db.Model): # Singlular Capital
    __tablename__ = 'reviews' # lowercase plural

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(255), nullable = False)
    stars = db.Column(db.Integer, nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    review_products_relationship = db.relationship('Product', back_populates='product_reviews_relationship')
    # review_products_relationship = db.relationship('Product', back_populates='product_reviews', foreign_keys=[product_id], remote_side=[product_id])
    review_users_relationship = db.relationship('User', back_populates='user_reviews_relationship')

    def to_dict(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'stars': self.stars,
            'product_id': self.product_id,
            'user_id': self.user_id
        }

    def to_dict_no_items(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'stars': self.stars
        }
