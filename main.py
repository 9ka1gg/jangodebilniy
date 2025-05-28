import os

import django
from django.db import models

from dotenv import load_dotenv
load_dotenv()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    all_passcards = Passcard.objects.all()
    one_passcard = all_passcards[1]
    print(all_passcards)
    print('\n', one_passcard.owner_name, one_passcard.passcode, one_passcard.created_at, one_passcard.is_active)
    active_passcards = Passcard.objects.filter(is_active=True)
    print(len(active_passcards))
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
