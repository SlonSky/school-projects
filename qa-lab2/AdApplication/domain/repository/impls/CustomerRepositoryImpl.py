""" Implements repository with mysql db """
import os
import peewee as pw

from AdApplication.domain.entity.Customer import Customer
from AdApplication.domain.repository.CustomerRepository import CustomerRepository


class CustomerRepositoryImpl(CustomerRepository):

    def create(self, id, first_name: str, last_name: str, ads_ordered_amt: int):
        return Customer.create(
            id=id,
            first_name=first_name,
            last_name=last_name,
            ads_ordered_amt=ads_ordered_amt
        )

    def find_all(self):
        return list(Customer.select())

    def delete(self, id):
        Customer.delete_by_id(id)



