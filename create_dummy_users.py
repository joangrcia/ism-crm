# create_dummy_users_and_details.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imperium.settings")

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker
from apps.user_app.models import PersonalDetail, BankDetail
from apps.trading_account_app.models import TradingAccount

fake = Faker()

def create_dummy_users_and_details(num_users=15, prefix="dummy_"):
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = prefix + fake.user_name()
        email = fake.email()
        password = fake.password()

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

        print(f"User created: {first_name} {last_name} ({username}) - Email: {email}")

        # Create Personal Detail
        personal_detail = PersonalDetail.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=fake.phone_number(),
            id_type=fake.random_element(elements=('idcard', 'passport')),
            id_number=fake.random_number(digits=9),
            marital_status=fake.random_element(elements=('married', 'widowed', 'separated', 'divorced', 'single'))[:15],  # Mengurangi panjang nilai
            country=fake.country()[:15],  # Mengurangi panjang nilai
            state=fake.state()[:30],  # Mengurangi panjang nilai
            city=fake.city()[:30],  # Mengurangi panjang nilai
            postal=fake.postcode()[:10],  # Mengurangi panjang nilai
            address=fake.address()[:50]  # Mengurangi panjang nilai
        )


        print("Personal detail created for user:", user.username)

        # Create Bank Detail
        bank_detail = BankDetail.objects.create(
            user=personal_detail,
            account_name=fake.name(),
            bank_account=fake.random_number(digits=12),
            bank_address=fake.address(),
            swift_code=fake.random_number(digits=9),
            bank_name=fake.company()
        )

        print("Bank detail created for user:", user.username)

        trading_account = TradingAccount.objects.create(
            user=user,
            account_number=fake.random_number(digits=7),
            account_deposit=fake.random_number(digits=4),
            client_group=fake.random_element(elements=('Standard', 'VIP')),
        )

        print("Trading account created for user:", user.username)

if __name__ == "__main__":
    create_dummy_users_and_details()
