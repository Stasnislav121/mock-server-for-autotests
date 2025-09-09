from typing import List, Dict, Union

from fastapi import FastAPI

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
