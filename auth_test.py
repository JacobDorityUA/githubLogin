import requests
import passwords

url = "http://localhost:8080/basic-auth/jacob/dority"

username = passwords.USERNAME
password = passwords.PASSWORD

response = requests.get(url, auth=(username,password))

print(response.text)
