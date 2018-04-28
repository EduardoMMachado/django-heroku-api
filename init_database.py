import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PlanilhaDeContas.settings")
django.setup()

from contas.models import Transaction

def fill_data_base():
    for i in range(1000000):
        print('Transação ' + str(i))
        t = Transaction()
        t.register_name = 'Teste ' + str(i)
        t.amount = i%7 * 0.01
        t.save()

fill_data_base()
