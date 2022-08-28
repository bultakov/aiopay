from asyncio import get_event_loop, AbstractEventLoop

from aiohttp import ClientSession


class Requests:
    def __init__(self, paycom_id: str, debug: bool = False, loop: AbstractEventLoop = None):
        # Asyncio loop instance
        if loop is None:
            loop = get_event_loop()
        self.loop = loop

        self._headers: dict = {
            "X-Auth": paycom_id,
        }

        # URL's
        self.test_url: str = 'https://checkout.test.paycom.uz/api/'
        self.pro_url: str = 'https://checkout.paycom.uz/api/'

        self.__api_url: str = self.test_url if debug else self.pro_url

        self._session = ClientSession(loop=self.loop)

    async def _requests(self, card_data: dict) -> dict:
        """
        Ma'lumotlarni yuborish uchun funksiya.

        :param card_data: Karta maʼlumotlari oʻz ichiga oladi.
        :return JSON:
        """
        async with self._session.post(url=self.__api_url, json=card_data, headers=self._headers) as response:
            return await response.json()

    async def close(self):
        await self._session.close()
