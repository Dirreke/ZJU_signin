""" 
Filename: cc98_signin.py
Author: Dirreck
Created: 2025-05-23
Version: 1.0
"""
import sys
import requests

# get token
def login(username, password):
    url = 'https://openid.cc98.org/connect/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'client_id': '9a1fd200-8687-44b1-4c20-08d50a96e5cd',
        'client_secret': '8b53f727-08e2-4509-8857-e34bf92b27f2',
        'scope': 'cc98-api openid offline_access',
    }
    proxies = {
        'http': None,
        'https': None
    }
    response = requests.post(url, data=data, headers=headers, proxies=proxies)
    if response.status_code == 200:
        print("Login successful")
        token = response.json()['access_token']
        return token
    else:
        print("Login failed")
        exit(1)

# sign in
def signin(token):
    url = 'https://api.cc98.org/me/signin'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    proxies = {
        'http': None,
        'https': None
    }
    response = requests.post(url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        print("Sign in successful")
    elif response.status_code == 400:
        print("Already signed in")
    else:
        print("Sign in failed")
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        USERNAME = input("请输入用户名：")
        PASSWORD = input("请输入密码：")
    elif len(sys.argv) == 3:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]
    else:
        print("参数错误")
        print("用法：python a.py [username] [password]")
        print("如果不提供参数，将会提示输入用户名和密码")
        exit(1)
    # login
    token = login(USERNAME, PASSWORD)
    # sign in
    signin(token)