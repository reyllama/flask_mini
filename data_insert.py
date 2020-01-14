from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)

session = DBsession()
first_restaurant = Restaurant(name="Pizza_Albolo", id=1)
session.add(first_restaurant)
cheesepizza = MenuItem(name="cheese pizza", description='Very chessy. Our signiture menu.',
                        course='Entree', price='12.99', restaurant=first_restaurant)
session.add(cheesepizza)
session.commit()
