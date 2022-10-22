import os
import requests
from dotenv import load_dotenv
import argparse


def shorten_link(token, url):
    bitly_response = requests.post(
        'https://api-ssl.bitly.com/v4/bitlinks',
        json={"long_url": url},
        headers={"Authorization": f"Bearer {token}"}
    )
    bitly_response.raise_for_status()
    bitlink = bitly_response.json()['id']
    return bitlink


def count_clicks(token, bitlink):
    bitly_response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary', 
        headers={"Authorization": f"Bearer {token}"}
    )
    bitly_response.raise_for_status()
    clicks_count = bitly_response.json()['total_clicks']
    return clicks_count


def is_bitlink(token, url):
    bitly_response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url}', 
        headers={"Authorization": f"Bearer {token}"}
    )
    return bitly_response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(
        description='Программа делает Bitly ссылки \
        и показывает количество их использования'
    )
    parser.add_argument('users_url', help='Ваша ссылка')
    args = parser.parse_args()
    users_url = args.users_url
  
    
    if is_bitlink(token, users_url):
        try:
            clicks_count = count_clicks(token, users_url)
        except requests.exceptions.HTTPError:
            print('Введена некорректная ссылка')
        else:
            print(f'Количество переходов по ссылке битли: {clicks_count}')
    else:
        try:
            bitlink = shorten_link(token, users_url)
        except requests.exceptions.HTTPError:
            print('Введена некорректная ссылка')
        else:
            print('Битлинк', bitlink)