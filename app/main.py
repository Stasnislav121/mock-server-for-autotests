from typing import List, Dict, Union

from fastapi import FastAPI

app = FastAPI()

packs = [{
    "id": "799",
    "title": "Короб ХS",
    "image": "https://storage.img.net/mobile-app-images/packs/799.png?v=1",
    "length": 15,
    "width": 15,
    "height": 15,
    "parcelExample": "мобильный телефон, украшения, духи"
}]


@app.get('/packs')
async def get_packs() -> List[Dict[str, Union[str, int]]]:
    return packs
