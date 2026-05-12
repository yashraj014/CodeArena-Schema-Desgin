from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import Mapped,mapped_column, DeclarativeBase,relationship,sessionmaker
from typing import List
db_url="sqlite:///memory.db"
engine=create_engine(db_url)

Session=sessionmaker(bind=engine)
session=Session()

class Base(DeclarativeBase):
    pass

contest_registration= Table(
    "contest_register",
    Base.metadata,
    Column("coder_id",ForeignKey("coders.id"),primary_key=True),
    Column("contest_id",ForeignKey("contests.id"),primary_key=True),
      
)
    

class Coder(Base):
    __tablename__='coders'
    
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(nullable=False,unique=True)
    password:Mapped[str]=mapped_column(nullable=False)
    
    profile:Mapped["CoderProfile"]=relationship(back_populates="coder",single_parent=True)
    contests: Mapped[List["Contest"]] = relationship(
        secondary=contest_registration, back_populates="coders"
    )

class CoderProfile(Base):
    __tablename__="profiles"
    
    id:Mapped[int]=mapped_column(primary_key=True)
    current_rating:Mapped[int]=mapped_column(nullable=True)
    global_rank:Mapped[int]=mapped_column(nullable=True)
    favourite_language:Mapped[str]=mapped_column(nullable=True)
    coder_id:Mapped[int]= mapped_column(ForeignKey("coders.id"),unique=True)
    
    coder:Mapped["Coder"]=relationship(back_populates="profile")
    
class Contest(Base):
    __tablename__="contests"
    
    id:Mapped[int]= mapped_column(primary_key=True)
    name:Mapped[str]
    
    problems:Mapped[List["Problem"]]=relationship(back_populates="contest")
    coders: Mapped[List["Coder"]] = relationship(
        secondary=contest_registration, back_populates="contests"
    )
    
class Problem(Base):
    __tablename__="problems"
    
    id:Mapped[int]= mapped_column(primary_key=True)
    title:Mapped[str]
    
    contest_id:Mapped[int]=mapped_column(ForeignKey("contests.id"))
    
    contest:Mapped["Contest"]=relationship(back_populates="problems")
    
    


Base.metadata.create_all(engine)