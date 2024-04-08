""" Contains interface for repository """
from abc import ABCMeta, abstractmethod


class CustomerRepository(object):

    """ Very abstract repository """

    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, id, first_name: str, last_name: str, ads_ordered_amt: int):
        """create customer"""

    @abstractmethod
    def find_all(self):
        """select all customers"""

    @abstractmethod
    def delete(self, id):
        """delete customer by id"""



