# create_dummy_users.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imperium.settings")

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

def create_dummy_users(num_users=99, prefix="dummy_"):
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = prefix + fake.user_name()
        email = fake.email()
        password = fake.password()

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

        print(f"User created: {first_name} {last_name} ({username}) - Email: {email}")

if __name__ == "__main__":
    create_dummy_users()
