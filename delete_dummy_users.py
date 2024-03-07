# delete_dummy_users.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imperium.settings")

import django
django.setup()

from django.contrib.auth.models import User
def delete_dummy_users():
    dummy_users = User.objects.filter(username__startswith='dummy_')
    dummy_users.delete()
    print("Dummy users deleted successfully.")


if __name__ == "__main__":
    delete_dummy_users()
