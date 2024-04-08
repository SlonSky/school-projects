""" Main model of the app """

import os

import peewee as pw

DB = pw.MySQLDatabase(
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=3306
)
DB.connect()


class Customer(pw.Model):

    """ Customer's model """

    class Meta:
        """ Define db connection"""
        database = DB

    first_name = pw.CharField(max_length=32)
    last_name = pw.CharField(max_length=32)
    ads_ordered_amt = pw.IntegerField(default=0)


DB.create_tables([Customer, ])
