import requests
import json

status = 'available'

# GET
res_get = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'available'},
                       headers={'accept': 'application/json'})

if 'application/json' in res_get.headers['Content-Type']:
    res_get.json()
else:
    res_get.text

print(f'Статус ответа на GET запрос (вывод всех питомцев со статусом available): {res_get.status_code}')
print(type(res_get.json()))

# POST
info_pet = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

header1 = {'accept': 'application/json', 'Content-Type': 'application/json'}
res_post_addNewPet = requests.post(f'https://petstore.swagger.io/v2/pet', data=json.dumps(info_pet, ensure_ascii=False),
                                   headers=header1)

print(f'Статус ответа на POST запрос (добавление нового питомца): {res_post_addNewPet.status_code}')
print('Карточка питомца:')
print(res_post_addNewPet.json())
print(type(res_post_addNewPet.json()))

# PUT
info_new = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Bim"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

header1 = {'accept': 'application/json', 'Content-Type': 'application/json'}
res_put_UpdatedUser = requests.put(f'https://petstore.swagger.io/v2/pet', data=json.dumps(info_new, ensure_ascii=False),
                                   headers=header1)
print(f'Статус ответа на PUT запрос (изменение питомца): {res_put_UpdatedUser.status_code}')
print('Карточка питомца:')
print(res_put_UpdatedUser.json())
print(type(res_put_UpdatedUser.json()))

info_new_pet2 = res_put_UpdatedUser.json()
id_pet = info_new_pet2.get("id")

# DEL
"""Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении"""

header3 = {'accept': 'application/json'}
res_del_DelNewPet = requests.delete(f'https://petstore.swagger.io/v2/pet/{id_pet}', headers=header3)

print(f'Статус ответа на DEL запрос (удаление питомца): {res_del_DelNewPet.status_code}')
print(type(res_del_DelNewPet.json()))
