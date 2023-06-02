import requests

api_url = " http://ec2-3-133-82-159.us-east-2.compute.amazonaws.com:3000/calculadora/operacoes"
response = requests.get(api_url)
print(response.json())