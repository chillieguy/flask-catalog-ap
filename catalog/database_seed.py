from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Catagory, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Catalog Users
user1 = User(name="Chuck Underwood", email="chillieguy@gmail.com")
session.add(user1)
session.commit()

print("Added User...")

# Catalog catagories

cat1 = Catagory(name="Soccer", user_id=1)
session.add(cat1)
session.commit()

cat2 = Catagory(name="Basketball", user_id=1)
session.add(cat2)
session.commit()

cat3 = Catagory(name="Baseball", user_id=1)
session.add(cat3)
session.commit()

cat4 = Catagory(name="Frisbee", user_id=1)
session.add(cat4)
session.commit()

cat5 = Catagory(name="Snowboarding", user_id=1)
session.add(cat5)
session.commit()

cat6 = Catagory(name="Soccer", user_id=1)
session.add(cat6)
session.commit()

cat7 = Catagory(name="Skiing", user_id=1)
session.add(cat7)
session.commit()

cat8 = Catagory(name="Golf", user_id=1)
session.add(cat8)
session.commit()

cat9 = Catagory(name="Football", user_id=1)
session.add(cat9)
session.commit()

cat10 = Catagory(name="Lacrose", user_id=1)
session.add(cat10)
session.commit()

print("Added Catalog Catagories...")

item1 = Item(name="Soccer Ball", description="This is my soccer ball..", catagory_id=1 ,user_id=1)
session.add(item1)
session.commit()

item2 = Item(name="Kids Soccer Ball", description="A ball that is just right for your kids...", catagory_id=1 ,user_id=1)
session.add(item2)
session.commit()

item3 = Item(name="Mega Putter", description="This putter is guaranteed to sink your ball...", catagory_id=8 ,user_id=1)
session.add(item3)
session.commit()

print("Added Item items...")