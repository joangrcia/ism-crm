import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imperium.settings")
import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker
from apps.trading_account_app.models import TradingAccount
from apps.partner_app.models import MibAccount, IbAccount, MibList, IbList
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.utils.timezone import now

fake = Faker()

def create_mib_account(user):
    mib_account = MibAccount.objects.create(user=user, is_confirm=True)
    print(f"Created MIB account for user: {user.username}")
    return mib_account

def create_ib_account(user):
    # Periksa apakah pengguna ada dalam MibAccount
    if MibAccount.objects.filter(user=user).exists():
        print(f"User {user.username} is already in MIB account, skipping IB account creation.")
        return None

    trading_account = TradingAccount.objects.order_by('?').first()
    ib_account = IbAccount.objects.create(user=user, name=fake.name(), account_number=trading_account)
    print(f"Created IB account for user: {user.username}")
    return ib_account


def create_mib_list():
    # Ambil semua MibAccount dalam urutan entri dalam basis data
    mib_accounts = MibAccount.objects.order_by('?').first()
    ib_account = IbAccount.objects.order_by('?').first()
    if MibList.objects.filter(ib_account=ib_account).exists():
        print(f"User {ib_account} is already in MIB account, skipping IB account creation.")
        return None
    mib_list = MibList.objects.create(mib=mib_accounts, ib_account=ib_account)
    print(f"Created MIB list for MIB: {mib_accounts}")
    return None

def create_ib_list(user):
    ib_account = IbAccount.objects.order_by('?').first()
    if IbList.objects.filter(client_account=user).exists():
        print(f"User {user.username} is already in MIB account, skipping IB account creation.")
        return None
    ib_list = IbList.objects.create(ib=ib_account, client_account=user)
    print(f"Created MIB list for IB: {ib_account}")
    return None

def generate_fake_data(num_entries=50):
    for _ in range(num_entries):
        try:
            user = User.objects.order_by('?').first()
            # create_mib_account(user)
            # create_mib_list()
            # create_ib_account(user)
            create_ib_list(user)
        except (ValidationError, IntegrityError):
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_entries = int(sys.argv[1])
        generate_fake_data(num_entries)
    else:
        generate_fake_data()

# create_dummy_users_and_details.py

# import os
# import sys  # Import modul sys untuk membaca argumen baris perintah
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imperium.settings")

# import django
# django.setup()

# from django.contrib.auth.models import User
# from faker import Faker
# from apps.user_app.models import PersonalDetail, BankDetail
# from apps.trading_account_app.models import TradingAccount, ProductTrading

# fake = Faker()

# def create_dummy_users_and_details(num_users=15, prefix="dummy_"):
#     for _ in range(num_users):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         randomnumver = fake.random_number(digits=3)
#         username = prefix + f'{first_name}_{last_name}'.lower()
#         email = f"{first_name}_{last_name}{randomnumver}@example.com".lower()
#         password = fake.password()
#         dm_group = ProductTrading.objects.order_by('?').first()

#         user = User.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#             password=password
#         )

#         print(f"User created: {first_name} {last_name} ({username}) - Email: {email}")

#         # Create Personal Detail
#         personal_detail = PersonalDetail.objects.create(
#             user=user,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             phone=fake.phone_number(),
#             id_type=fake.random_element(elements=('idcard', 'passport')),
#             id_number=fake.random_number(digits=9),
#             marital_status=fake.random_element(elements=('married', 'widowed', 'separated', 'divorced', 'single'))[:15],  # Mengurangi panjang nilai
#             country=fake.country()[:15],  # Mengurangi panjang nilai
#             state=fake.state()[:30],  # Mengurangi panjang nilai
#             city=fake.city()[:30],  # Mengurangi panjang nilai
#             postal=fake.postcode()[:10],  # Mengurangi panjang nilai
#             address=fake.address()[:50]  # Mengurangi panjang nilai
#         )

#         print("Personal detail created for user:", user.username)

#         # Create Bank Detail
#         bank_detail = BankDetail.objects.create(
#             user=personal_detail,
#             account_name=f"{first_name} {last_name}",
#             bank_account=fake.random_number(digits=12),
#             bank_address=fake.address(),
#             swift_code=fake.random_number(digits=9),
#             bank_name=fake.random_element(elements=('BCA', 'Mandiri', 'BRI', 'CIMB'))
#         )

#         print("Bank detail created for user:", user.username)

#         trading_account = TradingAccount.objects.create(
#             user=user,
#             account_number=fake.random_number(digits=7),
#             account_deposit=fake.random_number(digits=4),
#             dm_group=dm_group,
#         )

#         print("Trading account created for user:", user.username)

# if __name__ == "__main__":
#     if len(sys.argv) > 1:  # Periksa apakah ada argumen yang diberikan dari baris perintah
#         num_users = int(sys.argv[1])  # Ambil argumen pertama (indeks 0) sebagai jumlah pengguna
#         create_dummy_users_and_details(num_users)
#     else:
#         create_dummy_users_and_details()
