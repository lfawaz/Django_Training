import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
# Import settings
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=10):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):


        # Create Fake Data for entry
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()


        # Create new Webpage Entry
        user = User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
