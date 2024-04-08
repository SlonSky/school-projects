import os
import unittest
import yaml

class AdApplicationTest(unittest.TestCase):

    def load_configs(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(root + '/config/config.yaml', 'r') as conf_file:
            conf = yaml.load(conf_file)

            mode = os.getenv('MODE')

            os.environ['DB_NAME'] = conf[mode]['database']
            os.environ['DB_USER'] = conf[mode]['user']
            os.environ['DB_PASSWORD'] = conf[mode]['password']
            os.environ['DB_HOST'] = conf[mode]['host']

    def setUp(self):
        self.load_configs()
        from AdApplication.domain.entity.Customer import DB, Customer
        DB.create_tables([Customer, ])

    def tearDown(self):
        from AdApplication.domain.entity.Customer import DB, Customer
        DB.drop_tables([Customer, ])

    def test_delete_customers_first_name_starts_with(self):
        from AdApplication.domain.repository.impls.CustomerRepositoryImpl import CustomerRepositoryImpl
        from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl

        repository = CustomerRepositoryImpl()

        customer1 = repository.create(1, 'John', 'Smith', 5)
        customer2 = repository.create(2, 'Vasco', 'Sullivan', 0)
        customer3 = repository.create(3, 'Adam', 'Kirk', 14)
        customer4 = repository.create(4, 'Jimm', 'Kevo', 5)

        service = CustomerServiceImpl(repository)

        start_char = 'J'
        expected = [customer2, customer3]

        service.delete_customers_first_name_starts_with(start_char)

        result = repository.find_all()

        self.assertListEqual(expected, result)

    def test_delete_customers_first_name_starts_with_empty(self):
        from AdApplication.domain.repository.impls.CustomerRepositoryImpl import CustomerRepositoryImpl
        from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl

        repository = CustomerRepositoryImpl()

        service = CustomerServiceImpl(repository)

        start_char = 'J'
        expected = []

        service.delete_customers_first_name_starts_with(start_char)

        result = repository.find_all()

        self.assertListEqual(expected, result)

    def test_delete_customers_first_name_starts_with_no_such_items(self):
        from AdApplication.domain.repository.impls.CustomerRepositoryImpl import CustomerRepositoryImpl
        from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl

        repository = CustomerRepositoryImpl()

        customer1 = repository.create(1, 'John', 'Smith', 5)
        customer2 = repository.create(2, 'Vasco', 'Sullivan', 0)
        customer3 = repository.create(3, 'Adam', 'Kirk', 14)
        customer4 = repository.create(4, 'Jimm', 'Kevo', 5)

        service = CustomerServiceImpl(repository)

        start_char = 'X'
        expected = [customer1, customer2, customer3, customer4]

        service.delete_customers_first_name_starts_with(start_char)

        result = repository.find_all()

        self.assertListEqual(expected, result)


    def test_delete_customers_id_non_fibonacci(self):
        from AdApplication.domain.repository.impls.CustomerRepositoryImpl import CustomerRepositoryImpl
        from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl

        repository = CustomerRepositoryImpl()

        customer1 = repository.create(1, 'John', 'Smith', 5)
        customer2 = repository.create(2, 'Vasco', 'Sullivan', 0)
        customer3 = repository.create(3, 'Adam', 'Kirk', 14)
        customer4 = repository.create(4, 'Jimm', 'Kevo', 5)

        service = CustomerServiceImpl(repository)

        expected = [customer1, customer2, customer3]

        service.delete_customers_id_non_fibonacci()

        result = repository.find_all()

        self.assertListEqual(expected, result)

    def test_delete_customers_id_non_fibonacci_empty(self):
        from AdApplication.domain.repository.impls.CustomerRepositoryImpl import CustomerRepositoryImpl
        from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl

        repository = CustomerRepositoryImpl()


        service = CustomerServiceImpl(repository)

        expected = []

        service.delete_customers_id_non_fibonacci()

        result = repository.find_all()

        self.assertListEqual(expected, result)

    def test_delete_customers_id_non_fibonacci_all_fibonacci(self):
        from AdApplication.domain.repository.impls.CustomerRepositoryImpl import CustomerRepositoryImpl
        from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl

        repository = CustomerRepositoryImpl()

        customer1 = repository.create(1, 'John', 'Smith', 5)
        customer2 = repository.create(2, 'Vasco', 'Sullivan', 0)
        customer3 = repository.create(3, 'Adam', 'Kirk', 14)
        customer4 = repository.create(5, 'Jimm', 'Kevo', 5)

        service = CustomerServiceImpl(repository)

        expected = [customer1, customer2, customer3, customer4]

        service.delete_customers_id_non_fibonacci()

        result = repository.find_all()

        self.assertListEqual(expected, result)


