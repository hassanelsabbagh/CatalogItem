# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Categories, Base, Items, Users
import datetime

engine = create_engine('sqlite:///categories.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


cat1 = Categories(name="Soccer")
session.add(cat1)
session.commit()

cat2 = Categories(name="Basketball")
session.add(cat2)
session.commit()

cat3 = Categories(name="Baseball")
session.add(cat3)
session.commit()

cat4 = Categories(name="Frisbee")
session.add(cat4)
session.commit()

cat5 = Categories(name="Snowboarding")
session.add(cat5)
session.commit()

cat6 = Categories(name="Rock Climbing")
session.add(cat6)
session.commit()

cat7 = Categories(name="Foosball")
session.add(cat7)
session.commit()

cat8 = Categories(name="Skating")
session.add(cat8)
session.commit()

cat9 = Categories(name="Hockey")
session.add(cat9)
session.commit()

###############################
item1 = Items(name="Shinguards",
              description="""A shin guard is a thick piece of  material that
              you wear inside your socks to protect the shins""",
              categories=cat1,
              datee=datetime.datetime.now())
session.add(item1)
session.commit()


item1 = Items(name="Jersey", description="""A jersey is an item of knitted
              clothing, traditionally in wool or cotton, with sleeves,
              worn as a pullover""",
              categories=cat1, datee=datetime.datetime.now())
session.add(item1)
session.commit()

item1 = Items(name="Soccercleats", description="""Soccer shoes, soccer cleats,
              soccer boots whatever the name""",
              categories=cat1, datee=datetime.datetime.now())
session.add(item1)
session.commit()

########################################################
item2 = Items(name="Jersey", description="""A jersey is an item of knitted
              clothing, traditionally in wool or cotton""", categories=cat2,
              datee=datetime.datetime.now())
session.add(item2)
session.commit()

######################################################
item3 = Items(name="Bat", description="""A baseball bat is a smooth wooden or
              metal club used in the sport of baseball to hit the ball after
              it is thrown bythe pitcher.""",
              categories=cat3, datee=datetime.datetime.now())
session.add(item3)
session.commit()

#####################################################

item4 = Items(name="Frisbee", description="""A frisbee is a gliding toy or
sporting item that is generally plastic and roughly 20 to 25 centimetres
(8 to 10 in) in diameter with a lip""",
              categories=cat4, datee=datetime.datetime.now())
session.add(item4)
session.commit()

##################################################

item5 = Items(name="Goggles", description="""Glasses wore in snowboarding""",
              categories=cat5, datee=datetime.datetime.now())
session.add(item5)
session.commit()

item5 = Items(name="snowboarding", description="""Snowboarding is a
              recreational activity and Olympic involves descending standing
              on a snowboard""",
              categories=cat5, datee=datetime.datetime.now())
session.add(item5)
session.commit()


print"items added successfully"
