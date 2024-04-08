import os
import unittest
from unittest.mock import patch, MagicMock

import yaml

from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl


class AdApplicationTest(unittest.TestCase):

    def test_delete_customers_first_name_starts_with(self):

        repository = MagicMock()

        customer1 = type('', (object,), {'id': 1, 'first_name': 'John', 'last_name': 'Smith', 'ad_orders_amt': 5})
        customer2 = type('', (object,), {'id': 2, 'first_name': 'Vasco', 'last_name': 'Sullivan', 'ad_orders_amt': 0})
        customer3 = type('', (object,), {'id': 3, 'first_name': 'Adam', 'last_name': 'Kirk', 'ad_orders_amt': 14})
        customer4 = type('', (object,), {'id': 4, 'first_name': 'Jimm', 'last_name': 'Kevo', 'ad_orders_amt': 5})

        repository.find_all.return_value = [
            customer1, customer2, customer3, customer4
        ]

        repository.delete.return_value = True

        start_char = 'J'
        service = CustomerServiceImpl(repository)


        service.delete_customers_first_name_starts_with(start_char)

        self.assertTrue(repository.find_all.called)
        self.assertTrue(repository.find_all.called_with(customer1))
        self.assertTrue(repository.find_all.called_with(customer3))

    def test_delete_customers_first_name_starts_with_empty(self):

        repository = MagicMock()
        repository.find_all.return_value = []
        repository.delete.return_value = True

        service = CustomerServiceImpl(repository)

        start_char = 'J'

        service.delete_customers_first_name_starts_with(start_char)

        self.assertTrue(repository.find_all.called)
        self.assertFalse(repository.delete.called)

    def test_delete_customers_first_name_starts_with_no_such_items(self):
        repository = MagicMock()

        customer1 = type('', (object,), {'id': 1, 'first_name': 'John', 'last_name': 'Smith', 'ad_orders_amt': 5})
        customer2 = type('', (object,), {'id': 2, 'first_name': 'Vasco', 'last_name': 'Sullivan', 'ad_orders_amt': 0})
        customer3 = type('', (object,), {'id': 3, 'first_name': 'Adam', 'last_name': 'Kirk', 'ad_orders_amt': 14})
        customer4 = type('', (object,), {'id': 4, 'first_name': 'Jimm', 'last_name': 'Kevo', 'ad_orders_amt': 5})

        repository.find_all.return_value = [
            customer1, customer2, customer3, customer4
        ]

        repository.delete.return_value = True

        start_char = 'X'

        service = CustomerServiceImpl(repository)
        service.delete_customers_first_name_starts_with(start_char)

        self.assertTrue(repository.find_all.called)
        self.assertFalse(repository.delete.called)


    def test_delete_customers_id_non_fibonacci(self):
        repository = MagicMock()

        customer1 = type('', (object,), {'id': 1, 'first_name': 'John', 'last_name': 'Smith', 'ad_orders_amt': 5})
        customer2 = type('', (object,), {'id': 2, 'first_name': 'Vasco', 'last_name': 'Sullivan', 'ad_orders_amt': 0})
        customer3 = type('', (object,), {'id': 3, 'first_name': 'Adam', 'last_name': 'Kirk', 'ad_orders_amt': 14})
        customer4 = type('', (object,), {'id': 4, 'first_name': 'Jimm', 'last_name': 'Kevo', 'ad_orders_amt': 5})

        repository.find_all.return_value = [
            customer1, customer2, customer3, customer4
        ]

        repository.delete.return_value = True

        service = CustomerServiceImpl(repository)
        service.delete_customers_id_non_fibonacci()

        self.assertTrue(repository.find_all.called)

        self.assertTrue(repository.delete.called_with(customer2))
        self.assertTrue(repository.delete.called_with(customer1))
        self.assertTrue(repository.delete.called_with(customer3))



    def test_delete_customers_id_non_fibonacci_empty(self):

        repository = MagicMock()
        repository.find_all.return_value = []
        repository.delete.return_value = True

        service = CustomerServiceImpl(repository)
        service.delete_customers_id_non_fibonacci()

        self.assertTrue(repository.find_all.called)
        self.assertFalse(repository.delete.called)

    def test_delete_customers_id_non_fibonacci_all_fibonacci(self):
        repository = MagicMock()

        customer1 = type('', (object,), {'id': 1, 'first_name': 'John', 'last_name': 'Smith', 'ad_orders_amt': 5})
        customer2 = type('', (object,), {'id': 3, 'first_name': 'Vasco', 'last_name': 'Sullivan', 'ad_orders_amt': 0})
        customer3 = type('', (object,), {'id': 2, 'first_name': 'Adam', 'last_name': 'Kirk', 'ad_orders_amt': 14})
        customer4 = type('', (object,), {'id': 5, 'first_name': 'Jimm', 'last_name': 'Kevo', 'ad_orders_amt': 5})

        repository.find_all.return_value = [
            customer1, customer2, customer3, customer4
        ]

        repository.delete.return_value = True

        service = CustomerServiceImpl(repository)

        service.delete_customers_id_non_fibonacci()


        self.assertTrue(repository.delete.called_with(customer2))
        self.assertTrue(repository.delete.called_with(customer1))
        self.assertTrue(repository.delete.called_with(customer3))
        self.assertTrue(repository.delete.called_with(customer4))


