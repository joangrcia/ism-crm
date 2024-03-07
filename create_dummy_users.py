# create_dummy_users_and_details.py

import os
import sys  # Import modul sys untuk membaca argumen baris perintah
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imperium.settings")

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker
from apps.user_app.models import PersonalDetail, BankDetail
from apps.trading_account_app.models import TradingAccount, ProductTrading

fake = Faker()

def create_dummy_users_and_details(num_users=15, prefix="dummy_"):
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = prefix + f'{first_name}_{last_name}'.lower()
        email = f"{username}@example.com".lower()
        password = fake.password()
        dm_group = ProductTrading.objects.order_by('?').first()

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
            account_name=f"{first_name} {last_name}",
            bank_account=fake.random_number(digits=12),
            bank_address=fake.address(),
            swift_code=fake.random_number(digits=9),
            bank_name=fake.random_element(elements=('BCA', 'Mandiri', 'BRI', 'CIMB'))
        )

        print("Bank detail created for user:", user.username)

        trading_account = TradingAccount.objects.create(
            user=user,
            account_number=fake.random_number(digits=7),
            account_deposit=fake.random_number(digits=4),
            dm_group=dm_group,
        )

        print("Trading account created for user:", user.username)

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Periksa apakah ada argumen yang diberikan dari baris perintah
        num_users = int(sys.argv[1])  # Ambil argumen pertama (indeks 0) sebagai jumlah pengguna
        create_dummy_users_and_details(num_users)
    else:
        create_dummy_users_and_details()
