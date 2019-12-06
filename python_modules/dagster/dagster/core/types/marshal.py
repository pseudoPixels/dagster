import pickle
from abc import ABCMeta, abstractmethod

import six

from dagster import check
from dagster.utils import PICKLE_PROTOCOL


class SerializationStrategy(six.with_metaclass(ABCMeta)):
    def __init__(self, name, write_mode='wb', read_mode='rb'):
        self._name = name
        self._write_mode = write_mode
        self._read_mode = read_mode

    @property
    def name(self):
        return self._name

    @property
    def read_mode(self):
        return self._read_mode

    @property
    def write_mode(self):
        return self._write_mode

    @abstractmethod
    def serialize(self, value, writable):
        '''Core Serialization Method'''

    @abstractmethod
    def deserialize(self, readable):
        '''Core Deserialization Method'''


class PickleFileBasedSerializationStrategy(SerializationStrategy):  # pylint: disable=no-init
    def __init__(self, name='pickle_file', **kwargs):
        super(PickleFileBasedSerializationStrategy, self).__init__(name, **kwargs)

    def serialize(self, value, writable):
        check.str_param(writable, 'writable')

        with open(writable, self.write_mode) as write_obj:
            pickle.dump(value, write_obj, PICKLE_PROTOCOL)

    def deserialize(self, readable):
        check.str_param(readable, 'readable')

        with open(readable, self.read_mode) as read_obj:
            return pickle.load(read_obj)


class PickleBufferBasedSerializationStrategy(SerializationStrategy):
    def __init__(self, name='pickle_stream', **kwargs):
        super(PickleBufferBasedSerializationStrategy, self).__init__(name, **kwargs)

    def serialize(self, value, writable):
        pickle.dump(value, writable, PICKLE_PROTOCOL)

    def deserialize(self, readable):
        return pickle.load(readable)
