from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    status = Column(String)
    dob = Column(Date)

    courses = relationship("Course", back_populates="instructor")

class Instructor(User):
    __tablename__ = "instructors"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    courses = relationship("Course", back_populates="instructor")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, index=True)
    status = Column(String)
    description = Column(String)
    instructor_id = Column(Integer, ForeignKey("instructors.id"))

    instructor = relationship("Instructor", back_populates="courses")
