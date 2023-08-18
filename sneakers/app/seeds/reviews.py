from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():
    review1 = Review(
        comment = 'This shoe fits really nice and look great! ',
        stars = 5,
        product_id = 1,
        user_id = 1
    )
    review2 = Review(
        comment = 'This shoe is trash',
        stars =1,
        product_id = 2,
        user_id =2
    )
    review3 = Review(
        comment = 'Im so drippy',
        stars = 4,
        product_id = 3,
        user_id = 3
    )
    review4 = Review(
        comment = 'Filler',
        stars = 4,
        product_id = 4,
        user_id = 1
    )
    review5 = Review(
        comment = 'Filler',
        stars = 3,
        product_id =5,
        user_id = 2
    )
    review6 = Review(
        comment = 'Filler',
        stars = 4,
        product_id = 6,
        user_id = 3
    )
    review7 = Review(
        comment = 'Filler',
        stars = 5,
        product_id = 7,
        user_id = 1
    )
    review8 = Review(
        comment = 'Filler',
        stars = 1,
        product_id = 8,
        user_id = 2
    )
    review9 = Review(
        comment = 'Filler',
        stars = 2,
        product_id = 9,
        user_id = 3
    )
    review10 = Review(
        comment = 'Filler',
        stars = 4,
        product_id = 10,
        user_id = 3
    )
    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.add(review9)
    db.session.add(review10)
    db.session.commit()

    def undo_reviews():
        if environment == "production":
            db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
        else:
            db.session.execute(text("DELETE FROM products"))

        db.session.commit()
