from app import app, db, Dish, Category, Order, User


with app.app_context():
    category_all = db.session.query(Category).all()
    for category in category_all:
        print("Номер ", category.id, "Категория ", category.title)
        for item in category.dishes:
            print(item.title, end=", ")
        print()
    for category in category_all:
        print("Номер ", category.id, "Категория ", category.title)
