from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer,ForeignKey,String, false





class InstagramImage(Base):
    __tablename__ = 'images'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    user = relationship("User",back_populates="images")
    Image = Column(String(),nullable=false)