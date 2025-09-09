from fastapi import FastAPI


app = FastAPI()


@app.get('/packs')
async def get_packs():
    return {
                    "id": "799",
                    "title": "Короб ХS",
                    "image": "https://storage.img.net/mobile-app-images/packs/799.png?v=1",
                    "length": 15,
                    "width": 15,
                    "height": 15,
                    "parcelExample": "мобильный телефон, украшения, духи"
        }
