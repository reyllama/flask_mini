from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)

session = DBsession()

# veggies = session.query(MenuItem).filter_by(name='Veggie Burger')

veggie_burgers = session.query(MenuItem).filter_by(name='Veggie Burger')
print('-'*30)
print("Initial Price")
print('-'*30)
for burger in veggie_burgers:
    print(burger.name)
    print(burger.price)
    print()
print('modification ON')
for burger in veggie_burgers:
    burger.price = 1.99
    session.add(burger)
    session.commit()
print("modification complete")
print()
print('-'*30)
print("New Price")
print('-'*30)
for burger in veggie_burgers:
    print(burger.name)
    print(burger.price)
    print()
