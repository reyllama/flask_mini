from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)

session = DBsession()

# restaurant = session.query(Restaurant).filter_by(id=3)
# items = session.query(MenuItem).filter_by(restaurant_id=1)
# for item in items:
#     print(item.name)
#     print(item.price)
#     print(item.description)


restaurants = session.query(Restaurant).filter_by(id=6).first()
# menus = session.query(MenuItem).filter_by(restaurant_id = 6)
# for item in menus:
#     print(item.name)
#     print(item.price)
#     print(item.description[:10])
#     print()
print(restaurants.id)
