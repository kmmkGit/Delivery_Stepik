from app import app, db, Dish, Category, Order, User
from sqlalchemy import func

with app.app_context():
    category_all = db.session.query(Category).all()
    """
    for category in category_all:
        print("Номер ", category.id, "Категория ", category.title)
        for item in category.dishes:
            print(item.title, end=", ")
        print()
    for category in category_all:
        print("Номер ", category.id, "Категория ", category.title)
"""
    sess_dish = [5, 7, 9]
    dish = db.session.query(Dish).filter(Dish.id.in_(sess_dish))
#    print([i.title for i in dish])
#    total1 = db.session.query(func.sum(Dish.price)).filter(Dish.id.in_(sess_dish)).scalar()
    total2 = func.sum(dish.price).scalar()
    print(total2)
