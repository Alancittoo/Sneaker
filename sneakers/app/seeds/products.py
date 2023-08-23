from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text


def seed_products():
    product1 = Product(
        name = 'Jordan 1',
        image = 'url1',
        description = 'Rock out in these new shoes for the school year1',
        type = 'Jordans',
        status = True,
        price = 100
    )
    product2 = Product(
        name = 'Jordan 2',
        image = 'url2',
        description = 'Rock out in these new shoes for the school year2',
        type = 'Jordans',
        status = True,
        price = 100

    )
    product3 = Product(
        name = 'Jordan 3',
        image = 'url3',
        description = 'Rock out in these new shoes for the school year3',
        type = 'Jordans',
        status = True,
        price = 100

    )
    product4 = Product(
        name = 'Jordan 4',
        image = 'url4',
        description = 'Rock out in these new shoes for the school year4',
        type = 'Jordans',
        status = True,
        price = 100

    )
    product5 = Product(
        name = 'Jordan 5',
        image = 'url5',
        description = 'Rock out in these new shoes for the school year5',
        type = 'Jordans',
        status = False,
        price = 100

    )
    product6 = Product(
        name = 'Jordan 6',
        image = 'url6',
        description = 'Rock out in these new shoes for the school year6',
        type = 'Jordans',
        status = True,
        price = 100

    )
    product7 = Product(
        name = 'Jordan 7',
        image = 'url7',
        description = 'Rock out in these new shoes for the school year7',
        type = 'Jordans',
        status = True,
        price = 100

    )
    product8 = Product(
        name = 'Jordan 8',
        image = 'url8',
        description = 'Rock out in these new shoes for the school year8',
        type = 'Jordans',
        status = False,
        price = 100

    )
    product9 = Product(
        name = 'Jordan 9',
        image = 'url9',
        description = 'Rock out in these new shoes for the school year9',
        type = 'Jordans',
        status = True,
        price = 100

    )
    product10 = Product(
        name = 'Jordan 10',
        image = 'url10',
        description = 'Rock out in these new shoes for the school year11',
        type = 'Jordans',
        status = False,
        price = 100
        
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
