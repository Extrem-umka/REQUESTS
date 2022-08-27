from pprint import pprint

import requests

def superheroes_requests():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    # pprint(response.json())
    for new_response in response.json():
        # print(new_response['name'])
        # for new in new_response:
        # print(new_response['powerstats']['intelligence'])
        # intel = {'Hulk': int(new_response['powerstats']['intelligence']), 'Captain America': int(new_response['powerstats']['intelligence']), 'Thanos': int(new_response['powerstats']['intelligence'])}
        # print(intel)
        intel = {new_response['name']: int(new_response['powerstats']['intelligence'])}
        # print(intel)
        for k, v in intel.items():
            # print(f' {k} : {v}')
            if k == 'Hulk':
                print(f'У супергероя {k} уровень интеллекта = {v}')
            elif k == 'Captain America':
                print(f'У супергероя {k} уровень интеллекта = {v}')
            elif k == 'Thanos':
                print(f'У супергероя {k} уровень интеллекта = {v}')


if __name__ == '__main__':
    superheroes_requests()