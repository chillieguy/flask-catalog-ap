from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Catalog, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Catalog Users
user1 = User(name="Chuck Underwood", email="chillieguy@gmail.com")
session.add(user1)
session.commit()


# Catalog catagories

cat1 = Catalog(category="Soccer", user_id=1)
session.add(cat1)
session.commit()

cat2 = Catalog(category="Basketball", user_id=1)
session.add(cat2)
session.commit()

cat3 = Catalog(category="Baseball", user_id=1)
session.add(cat3)
session.commit()

cat4 = Catalog(category="Frisbee", user_id=1)
session.add(cat4)
session.commit()

cat5 = Catalog(category="Snowboarding", user_id=1)
session.add(cat5)
session.commit()

cat6 = Catalog(category="Soccer", user_id=1)
session.add(cat6)
session.commit()

cat7 = Catalog(category="Skiing", user_id=1)
session.add(cat7)
session.commit()

cat8 = Catalog(category="Golf", user_id=1)
session.add(cat8)
session.commit()

cat9 = Catalog(category="Football", user_id=1)
session.add(cat9)
session.commit()

cat10 = Catalog(category="Lacrose", user_id=1)
session.add(cat10)
session.commit()

print("Added Catalog Catagories...")