from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker


Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    secondname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self) -> str:
        return f"({self.ssn}) {self.firstname} {self.lastname} {self.gender} {self.age})"

class Thing(Base):
    __tablename__ = "things"
    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner) -> None:
        self.tid = tid
        self.description = description
        self.owner = owner


    def __repr__(self) -> str:
        return f"({self.tid} {self.description} owned by {self.owner})"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
person = Person(123123, "Mike", "Smith", "m", 35)
session.add(person)
session.commit()

p1 = Person(12313, "Mike", "Smith", "m", 35)
p2 = Person(12323, "Mike", "Smith", "m", 35)
p3 = Person(13123, "Mike", "Smith", "m", 35)
p4 = Person(23123, "Mike", "Smith", "m", 35)


session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.commit()

results = session.query(Person).filter(Person.firstname == "Blue")
print(results)
t1 = Thing(1, "Car", p1.ssn);
session.add(t1)
session.commit()
