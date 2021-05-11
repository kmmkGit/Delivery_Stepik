import csv
from app import app, db, Dish, Category


with app.app_context():
    with open("delivery_categories.csv", encoding='utf-8') as r_file:
        csv_categories = csv.reader(r_file, delimiter=',')
        for csv_line in list(csv_categories)[1:]:
            category = Category(csv_id=int(csv_line[0]), title=csv_line[1])
            print(category.csv_id, type(category.csv_id), category.title, len(category.title))
            db.session.add(category)

    with open("delivery_items.csv", encoding='utf-8') as r_file:
        csv_items = csv.reader(r_file, delimiter=',')
        for csv_line in list(csv_items)[1:]:
            db.session.add(Dish(
                title=csv_line[1],
                price=float(csv_line[2]),
                description=csv_line[3],
                picture=csv_line[4],
                category=db.session.query(Category).filter(Category.csv_id == csv_line[5]).scalar(),
            ))
    db.session.commit()
