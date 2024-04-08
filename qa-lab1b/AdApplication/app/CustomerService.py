from abc import ABCMeta, abstractmethod

from AdApplication.domain.repository.CustomerRepository import CustomerRepository


class CustomerService(object):
    __metaclass__ = ABCMeta

    repository: CustomerRepository

    @abstractmethod
    def delete_customers_first_name_starts_with(self, char):
        "Delete customers which first name start with given char"

    @abstractmethod
    def delete_customers_id_non_fibonacci(self):
        "Delete customers which id does not belong to fibonnaci sequence"
