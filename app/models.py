#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from weblib.db import backref
from weblib.db import declarative_base
from weblib.db import relationship
from weblib.db import uuid
from weblib.db import Boolean
from weblib.db import Column
from weblib.db import DateTime
from weblib.db import Enum
from weblib.db import ForeignKey
from weblib.db import Integer
from weblib.db import String
from weblib.db import Text
from weblib.db import Time



Base = declarative_base()


class Session(Base):
    __tablename__ = 'session'

    session_id = Column(String, primary_key=True)
    atime = Column(Time, default=datetime.now)
    data = Column(Text)


class User(Base):
    __tablename__ = 'user'

    id = Column(String, default=uuid, primary_key=True)
    name = Column(String, nullable=False)
    avatar = Column(String, nullable=True)
    deleted = Column(Boolean, default=False, nullable=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    device = relationship('Device', uselist=False)
    driver = relationship('Driver', uselist=False,
                          backref=backref('user', lazy='joined',
                                          cascade='expunge'))
    passenger = relationship('Passenger', uselist=False,
                             backref=backref('user', lazy='joined',
                                             cascade='expunge'))

    def __repr__(self):
        return '<User id=%(id)s, name=%(name)s, '\
               'avatar=%(avatar)s>' % self.__dict__


class Device(Base):
    __tablename__ = 'device'

    id = Column(String, default=uuid, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    device_token = Column(String)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<Device id=%(id)s, user_id=%(id)s, '\
               'device_token=%(device_token)s>' % self.__dict__


class Token(Base):
    __tablename__ = 'token'

    id = Column(String, default=uuid, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<Token id=%(id)s, user_id=%(user_id)s>' % self.__dict__


class Account(Base):
    __tablename__ = 'account'

    id = Column(String, default=uuid, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    external_id = Column(String, nullable=False)
    type = Column(Enum('fake', 'facebook', name='account_type'), nullable=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<Account id=%(id)s, user_id=%(user_id)s, '\
               'external_id=%(external_id)s, type=%(type)s>' % self.__dict__


class Driver(Base):
    __tablename__ = 'driver'

    id = Column(String, default=uuid, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    license_plate = Column(String)
    telephone = Column(String)
    hidden = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<Driver id=%(id)s, user_id=%(user_id)s, '\
               'license_plate=%(license_plate)s, '\
               'telephone=%(telephone)s, hidden=%(hidden)s>' % self.__dict__


class Passenger(Base):
    __tablename__ = 'passenger'

    id = Column(String, default=uuid, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    origin = Column(Text)
    destination = Column(Text)
    active = Column(Boolean, default=True)
    seats = Column(Integer)

    def __repr__(self):
        return '<Passenger id=%(id)s, user_id=%(user_id)s, '\
               'origin=%(origin)s, destination=%(destination)s, '\
               'seats=%(seats)d, active=%(active)s>' % self.__dict__


class RideRequest(Base):
    __tablename__ = 'ride_request'

    id = Column(String, default=uuid, primary_key=True)
    driver_id = Column(String, ForeignKey('driver.id'))
    passenger_id = Column(String, ForeignKey('passenger.id'))
    accepted = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<RideRequest id=%(id)s, driver_id=%(driver_id)s, '\
               'passenger_id=%(passenger_id)s, '\
               'accepted=%(accepted)s>' % self.__dict__
