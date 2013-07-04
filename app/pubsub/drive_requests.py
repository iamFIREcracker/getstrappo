#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.weblib.pubsub import Publisher


class ActiveDriveRequestsWithDriverIdGetter(Publisher):
    def perform(self, repository, driver_id):
        """Search for all the active drive requests associated with the given
        driver ID.

        When done, a 'drive_requests_found' message will be published,
        followed by the list of drive requests.
        """
        self.publish('drive_requests_found',
                     repository.get_all_active_by_driver(driver_id))


class DriveRequestCreator(Publisher):
    def perform(self, repository, driver_id, passenger_id):
        """Creates a ride request from driver identified by ``driver_id`` and
        passenger identified by ``passenger_id``.

        On success a 'drive_request_created' message will be published toghether
        with the created request.
        """
        request = repository.add(driver_id, passenger_id)
        self.publish('drive_request_created', request)


class DriveRequestAcceptor(Publisher):
    def perform(self, repository, driver_id, passenger_id):
        """Marks the ride request between driver identified by ``driver_id`` and
        the passenger identified by ``passenger_id`` as _accepted_.

        On success a 'drive_request_accepted' message with the accepted ride
        request object will be published;  on the other hand a
        'drive_request_not_found' message will be generated.
        """
        request = repository.accept(driver_id, passenger_id)
        if request is None:
            self.publish('drive_request_not_found', driver_id, passenger_id)
        else:
            self.publish('drive_request_accepted', request)


def serialize(request):
    if request is None:
        return None
    return dict(id=request.id, accepted=request.accepted)


def _serialize(request):
    from app.pubsub.drivers import serialize as serialize_driver
    from app.pubsub.passengers import serialize as serialize_passenger
    from app.pubsub.users import serialize as serialize_user
    d = serialize(request)
    d.update(passenger=serialize_passenger(request.passenger))
    d['passenger'].update(user=serialize_user(request.passenger.user))
    d.update(driver=serialize_driver(request.driver))
    d['driver'].update(user=serialize_user(request.driver.user))
    return d


class MultipleDriveRequestsSerializer(Publisher):
    def perform(self, requests):
        """Convert a list of drive requests into serializable dictionaries.

        At the end of the operation, the method will emit a
        'drive_requests_serialized' message containing serialized objects.
        """
        self.publish('drive_requests_serialized', 
                     [_serialize(r) for r in requests])
