""" Implementation of CustomerServie for command line usage """
from AdApplication.app.CustomerService import CustomerService


class CustomerServiceImpl(CustomerService):

    """ Implements full behaviour of interface"""

    def __init__(self, repository):
        CustomerServiceImpl.repository = repository

    def delete_customers_first_name_starts_with(self, char):
        customers = CustomerServiceImpl.repository.find_all()

        for i in customers:
            if i.first_name.startswith(char):
                CustomerServiceImpl.repository.delete(i.id)

    def delete_customers_id_non_fibonacci(self):
        customers = CustomerServiceImpl.repository.find_all()

        for i in customers:
            if not self.__is_fibonacci(i.id):
                CustomerServiceImpl.repository.delete(i.id)

    def __is_fibonacci(self, num):
        a = 1
        b = 1

        while True:

            if a == num:
                return True

            if a > num:
                return False

            a, b = b, a + b
