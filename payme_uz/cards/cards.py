from asyncio import AbstractEventLoop, get_event_loop

from aiohttp import ClientSession


class PaymeSubscribeCard:
    def __init__(self, paycom_id: str, debug: bool = False, loop: AbstractEventLoop = None):
        # Asyncio loop instance
        if loop is None:
            loop = get_event_loop()
        self.loop = loop

        # URL's
        self.test_url: str = 'https://checkout.test.paycom.uz/api/'
        self.pro_url: str = 'https://checkout.paycom.uz/api/'
        self.__api_url: str = self.test_url if debug else self.pro_url

        self.__paycom_id: str = paycom_id

        self.__headers: dict = {
            "X-Auth": self.__paycom_id,
        }

        self._session = ClientSession(loop=self.loop)

    async def __requests(self, card_data: dict) -> dict:
        async with self._session.post(url=self.__api_url, json=card_data, headers=self.__headers) as response:
            return await response.json()

    async def card_create(self, number: str, expire: str, save: bool) -> dict:
        data: dict = {
            "method": "cards.create",
            "params": {
                "card": {
                    "number": number,
                    "expire": expire,
                },
                "save": save,
            }
        }
        return await self.__requests(card_data=data)

    async def card_get_verify_code(self, token: str) -> dict:
        data: dict = {
            "method": "cards.get_verify_code",
            "params": {
                "token": token,
            }
        }
        return await self.__requests(card_data=data)

    async def card_verify(self, verify_code: int, token: str) -> dict:
        data: dict = {
            "method": "cards.verify",
            "params": {
                "token": token,
                "code": verify_code
            }
        }
        return await self.__requests(card_data=data)

    async def card_check(self, token: str) -> dict:
        data: dict = {
            "method": "cards.check",
            "params": {
                "token": token,
            }
        }
        return await self.__requests(card_data=data)

    async def card_remove(self, token: str) -> dict:
        data: dict = {
            "method": "cards.remove",
            "params": {
                "token": token,
            }
        }
        return await self.__requests(card_data=data)

    async def close(self):
        await self._session.close()
