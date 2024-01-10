import os
import datetime

from cryptochaos import logistic
from dotenv import load_dotenv

import application.salary as salary
from application.db.people import get_employees


def current_date():
    date_ = datetime.datetime.now().strftime('%d.%m.%Yг.')
    print('Текущая дата:', date_)


def encrypted():
    load_dotenv()
    encrypted_text = os.getenv('TEXT')
    r = float(os.getenv('FLOAT_N'))
    encrypted_text = logistic.logistic_encrypt(encrypted_text, r)
    print('зашифрованный текст:', encrypted_text)
    decrypted(encrypted_text, r)


def decrypted(encrypted_text, r):
    decrypted_text = logistic.logistic_decrypt(encrypted_text, r)
    print('расшифрованный текст:', decrypted_text)


if __name__ == "__main__":
    print('**** задание-2 *****')
    salary.calculate_salary()
    get_employees()
    print('**** задание-3 *****')
    current_date()
    print('**** задание-4 *****')
    encrypted()
