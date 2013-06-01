#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue


class Future(object):
    """Extremely simplified implementation of a future (just a wrapper of
    a standard blocking queue).
    """
    def __init__(self):
        self._queue = Queue.Queue()

    def set(self, value):
        """Sets the object returned by the future."""
        self._queue.put(value)

    def get(self):
        """Gets the object contained by the future."""
        return self._queue.get()


class Publisher(object):
    """Defines a simple message publisher.

    A publisher is an object with two methods:  the first is needed to register
    'listeners' to the publisher, so that they can be notified when a new
    message is required to be published;  the second is the 'publish' method.

    >>> class WorldHelloer:
    ...   def hello(self):
    ...     print 'Hello, world!'
    >>> class NameHelloer:
    ...   def __init__(self, name):
    ...     self.name = name
    ...   def hello(self):
    ...     print 'Hello, %(name)s!' % dict(name=self.name)

    >>> p = Publisher()
    >>> p.publish('hello')

    >>> p = Publisher()
    >>> p.add_subscriber(WorldHelloer())
    >>> p.publish('hello')
    Hello, world!

    >>> p = Publisher()
    >>> p.add_subscriber(NameHelloer('Foo'), NameHelloer('Bar'))
    >>> p.publish('hello')
    Hello, Foo!
    Hello, Bar!
    """

    def __init__(self):
        """Constructor.

        Initialize the list of subscribers."""
        self.subscribers = []

    def add_subscriber(self, subscriber, *moresubscribers):
        """Adds a new subscriber to the list of publisher subscribers."""
        self.subscribers += [subscriber] + list(moresubscribers)

    def publish(self, message, *args, **kwargs):
        """Publishes ``message`` to all the registered subscribers having
        a method with the name equal to the message.

        For example, if ``message`` is 'hello_world', only those subscribers
        with a method named 'hello_wordld' will be notified of this message."""
        for subscriber in self.subscribers:
            if hasattr(subscriber, message):
                getattr(subscriber, message)(*args, **kwargs)


class LoggingSubscriber(object):
    """A generic subscriber in charge of logging each received event.

    >>> from collections import namedtuple
    >>> Logger = namedtuple('Logger', 'info'.split())
    >>> def info(message):
    ...   print message
    >>> logger = Logger(info)
    >>> this = LoggingSubscriber(logger)

    >>> this.on_button_clicked('Button1')
    Received event='on_button_clicked' args=('Button1',)

    >>> this.on_validation_error('Invalid format')
    Received event='on_validation_error' args=('Invalid format',)
    """
    def __init__(self, logger):
        self.logger = logger

    def __getattr__(self, name):
        def callable(*args):
            msg = 'Received event=%(event)r args=%(args)r'
            msg = msg % dict(event=name, args=args)
            self.logger.info(msg)
        return callable
