import requests

operacoes = ['soma','subtrai','multiplica','divide']

for op in operacoes:
    api_op = 'http://ec2-3-133-82-159.us-east-2.compute.amazonaws.com:3000/calculadora/operacoes/{}/{}/{}'.format(op, 36, 2)
    response = requests.post(api_op)

    if response.status_code.real != 200:
        print('Erro ao acessar status = ', response.status_code)
        break

    resp = response.json()

    if resp['error'] == 'False':
        print('Erro ao calcular')
    else:
        print('Resultado da operação {} = {}'.format(op, resp['value']))