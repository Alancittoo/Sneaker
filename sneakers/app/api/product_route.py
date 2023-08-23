from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import User, db, Product
from app.forms.product_form import ProductForm

product_routes = Blueprint('product', __name__)

#Read
@product_routes.route('/allProducts')
@login_required
def all_products():
    res = Product.query.all()
    return {'Product': [product.to_dict() for product in res]}


@product_routes.route('/<int:product_id>')
@login_required
def single_product(product_id):
    res = Product.query.get(product_id)

    return {'Product': res.to_dict()}

#create
@product_routes.route('/newProduct', methods=['POST'])
@login_required
def create_product():
    user = current_user

    form['csrf_token'].data = request.cookies['csrf_token']
    form = ProductForm()

    if form.validate_on_submit():
        product = Product(
            name = form.data['name'],
            # image
            description = form.data['description'],
            type = form.data['type'],
            status = form.data['status'],
            price = form.data['price']
        )
        db.session.add(product)
        db.session.commit()
        return product.to_dict()
    return {'errors': form.errors}, 400
