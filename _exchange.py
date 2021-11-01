import requests
import json

base_url = "https://api.exchangerate-api.com/v4/latest"
valid_currencies = ['TRY', 'USD', 'EUR']

@property
def version():
    return 1.0

def get_currency_data(currency: str) -> str:
    if currency in valid_currencies:
        url = '/'.join([base_url, currency])
        responce = requests.get(url)
    else:
        return None
    return responce.text

def convert_json(x: str):
    if isinstance(x, str):
        y = json.loads(x)
        return y
    else:
        raise TypeError

def calc_currency(received: str, exchanged: str, quantity: str, rates: dict):
    print(f'{rates[exchanged]} {exchanged} = {rates[received]} {received}')
    print(f'{float(rates[exchanged])*float(quantity)} {exchanged} = {float(rates[received])*int(quantity)} {received}')


def edit_datas(func):
    def inner(*args, **kwargs):
        datas = func(*args, **kwargs)
        new_datas = []
        for i in datas:
            i = i.strip().upper()
            new_datas.append(i)
        return new_datas
    return inner

@edit_datas
def get_datas_from_user():
    exchanged = input('Write the type of currency to be exchanged : ')
    received =  input('Type the type of currency to be received : ')
    quantity = input(f'How much {exchanged} do you want to exchange? : ')
    return exchanged, received, quantity

def main():
    print('Döviz Uygulamasına Hoş Geldiniz'.center(70, '*'))
    while True:
        welcomme = input('\nçıkmak için (q), devam etmek için herhangi bir tuşa basın:  ')
        if welcomme == 'q' or welcomme == 'Q':
            print('Thank you for choosing us :) by by!')
            break
        else:
            exchanged, received, quantity = get_datas_from_user()
            result = get_currency_data(exchanged)
            result = convert_json(result)
            calc_currency(received, exchanged, quantity, result['rates'])

if __name__ == '__main__':
    main()