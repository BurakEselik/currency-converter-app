import requests
import json

base_url = "https://api.exchangerate-api.com/v4/latest"
valid_currencies = ['TRY', 'USD', 'EUR']

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

def calc_currency(alınan: str, bozulan: str, miktar: str, rates: dict):
    print(f'{rates[bozulan]} {bozulan} = {rates[alınan]} {alınan}')
    print(f'{float(rates[bozulan])*float(miktar)} {bozulan} = {float(rates[alınan])*int(miktar)} {alınan}')


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
    bozulan = input('Bozulacak döviz türünü yazın: ')
    alınan =  input('Alınacak döviz türünü yazın: ')
    miktar = input(f'Ne kadar {bozulan} bozdurmak istiyorsunuz: ')
    return bozulan, alınan, miktar

def main():
    while True:
        welcomme = input('Döviz Uygulamasına Hoş Geldiniz'.center(70, '*'))
        if welcomme == 'q' or welcomme == 'Q':
            break
        else:
            bozulan, alınan, miktar = get_datas_from_user()
            result = get_currency_data(bozulan)
            result = convert_json(result)
            calc_currency(alınan, bozulan, miktar, result['rates'])

if __name__ == '__main__':
    main()