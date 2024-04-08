import yaml

import os


def load_configs():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(root + '/config/config.yaml', 'r') as conf_file:
        conf = yaml.load(conf_file)

        mode = os.getenv('MODE')

        os.environ['DB_NAME'] = conf[mode]['database']
        os.environ['DB_USER'] = conf[mode]['user']
        os.environ['DB_PASSWORD'] = conf[mode]['password']
        os.environ['DB_HOST'] = conf[mode]['host']


def main():

    load_configs()


    from AdApplication.app.impls.CustomerServiceImpl import CustomerServiceImpl
    from AdApplication.domain.repository.impls.CustomerRepositoryImpl import CustomerRepositoryImpl

    repository = CustomerRepositoryImpl()
    service = CustomerServiceImpl(repository)

    print(repository.find_all())

    service.delete_customers_id_non_fibonacci()

    print(repository.find_all())

if __name__ == '__main__':
    main()
