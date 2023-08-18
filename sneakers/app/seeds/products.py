from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text


def seed_products():
    product1 = Product(
        name = 'Jordan 1',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = True,
    )
    product2 = Product(
        name = 'Jordan 2',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = True,
    )
    product3 = Product(
        name = 'Jordan 3',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = True,
    )
    product4 = Product(
        name = 'Jordan 4',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = True,
    )
    product5 = Product(
        name = 'Jordan 5',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = False,
    )
    product6 = Product(
        name = 'Jordan 6',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = True,
    )
    product7 = Product(
        name = 'Jordan 7',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = True,
    )
    product8 = Product(
        name = 'Jordan 8',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = False,
    )
    product9 = Product(
        name = 'Jordan 9',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = True,
    )
    product10 = Product(
        name = 'Jordan 10',
        image = 'url',
        description = 'Rock out in these new shoes for the school year',
        type = 'Jordans',
        status = False,
    )


    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.add(product7)
    db.session.add(product8)
    db.session.add(product9)
    db.session.add(product10)
    db.session.commit()


    def undo_products():
        if environment == "production":
            db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
        else:
            db.session.execute(text("DELETE FROM products"))

        db.session.commit()
