import requests
import json

websiteURL = "bo-mtrwl.match-trade.com"
username = "tsadm330@gmail.com"
password = "Ya2t 159753"
partnerId = 115

# Mendapatkan access token
token_url = f"https://{websiteURL}/proxy/auth/oauth/token"
token_headers = {
    "Authorization": "Basic bGl2ZU10cjFDbGllbnQ6TU9USUI2ckRxbjNDenlNdDV2N2VHVmNhcWZqeDNlNWN1ZmlObG5uVFZHWVkzak5uRDJiWXJQS0JPTGRKMXVCRHpPWURTa1NVa1BObkxJdHd5bXRMZzlDUklLTmdIVW54MVlmdQ==",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "JSESSIONID=7029AE0C9AB3F5F730CDEA186A4A920A; JSESSIONID=CD912EF93AD198D9B12410F1CF09C886",
}
token_cookies = {"JSESSIONID": "430AA1648A1146D88531E00217CEB7A1"}
token_data = {
    "grant_type": "password",
    "username": f"{username}",
    "password": f"{password}"
}

token_response = requests.post(token_url, headers=token_headers, cookies=token_cookies, data=token_data)
token_response_data = json.loads(token_response.text)
accessToken = token_response_data['access_token']

# Mengatur nomor halaman yang ingin diambil
page_number = 5  # Ganti nomor halaman sesuai kebutuhan Anda

# Membuat permintaan untuk halaman yang ditentukan
url = f'https://mtco.match-trade.com/documentation/account/api/partner/{partnerId}/clients/view'
headers = {
    'Authorization': f'Bearer {accessToken}',
    'Content-Type': 'application/json'
}
params = {
    'from': '2020-01-01T00:00:00Z',
    'to': '2024-01-01T00:00:00Z'
}
# Menambahkan nomor halaman ke dalam parameter permintaan
params['page'] = page_number  

response = requests.get(url, headers=headers, params=params)
print(response.text)
