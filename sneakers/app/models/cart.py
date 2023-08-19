from .db import db, environment, SCHEMA, add_prefix_for_prod

class Cart(db.Model): # Singlular Capital
    __tablename__ = 'carts' # lowercase plural

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    cart_products_relationship = db.relationship('Product', back_populates='product_carts_relationship')
    cart_users_relationship = db.relationship('User', back_populates='user_carts_relationship')

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'user_id': self.user_id
        }

    def to_dict_no_item(self):
        return {
            'id': self.id,
        }
