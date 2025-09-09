from typing import List
from pydantic import BaseModel

from fastapi import FastAPI, status, Response

app = FastAPI()


packs = {
    "data": {
        "boxes": [{
            "id": "799",
            "title": "Короб ХS",
            "image": "https://storage.img.net/mobile-app-images/packs/799.png?v=1",
            "length": 15,
            "width": 15,
            "height": 15,
            "parcelExample": "мобильный телефон, украшения, духи"
        }]
    },
    "success": True,
    "name": "Список доступной упаковки",
    "message": "Данные успешно загружены",
    "time": "2023-10-25T14:30:00Z"
}


@app.get('/packs')
async def get_packs() -> dict:
    return packs


class PriceRequest(BaseModel):
    value: float
    code: str


class DeliveryRequest(BaseModel):
    senderCityCode: str
    receiverCityCode: str
    deliveryId: str
    declaredPrice: PriceRequest
    package: str
    paidByReceiver: bool
    additionalServices: List[str]


@app.post('/parcels/calc', status_code=status.HTTP_201_CREATED)
async def get_calc(request: DeliveryRequest, response: Response) -> dict:
    delivery_types = {'officeToOffice': 'Доставка от отделения до отделения',
                      'officeToDoor': 'Доставка от отделения до двери',
                      'doorToOffice': 'Доставка от двери до отделения',
                      'doorToDoor': 'Доставка от двери до двери'}

    request_delivery = request.deliveryId
    try:
        delivery_title = delivery_types[request_delivery]
    except KeyError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "data": {
                "errors": [
                    {
                        "field": "deliveryId",
                        "description": "Выбран неверный способ доставки"
                    }
                ]
            },
            "success": False,
            "name": "Неверные данные отправлений",
            "message": "Указаны неверные входные параметры для отправлений",
            "time": "2023-09-09T17:47:21+0300"
        }

    return {
        "data": {
            "delivery": {
                "id": request_delivery,
                "title": delivery_title,
                "description": "Доставка 1 рабочий день",
                "price": {
                    "value": 324.67,
                    "code": "RUB"
                }
            },
            "deliveryServices": [
                {
                    "id": 1324,
                    "title": "Доставка отправления между адресатами",
                    "price": {
                        "value": 0,
                        "code": "RUB"
                    }
                }
            ],
            "discount": None,
            "finalPrice": {
                "value": 349.67,
                "code": "RUB"
            }
        },
        "success": True,
        "name": "",
        "message": "",
        "time": "2023-09-09T17:47:21+0300"
    }
