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
        """
        Ma'lumotlarni yuborish uchun funksiya.

        :param card_data: Karta maʼlumotlari oʻz ichiga oladi.
        :return JSON:
        """
        async with self._session.post(url=self.__api_url, json=card_data, headers=self.__headers) as response:
            return await response.json()

    async def card_create(self, number: str, expire: str, save: bool) -> dict:
        """
        Yangi karta tokenini yaratish uchun funksiya.

        :param number: Karta raqami.
        :param expire: Amal qilish muddati.
        :param save: Agar True bo'lsa, token keyingi to'lovlar uchun ishlatilishi mumkin;
        agar False bo'lsa, token faqat bir marta ishlatilishi mumkin. To'lovdan so'ng bir martalik token o'chiriladi.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/cards.create
        """
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
        """
        Tasdiqlash kodini olish uchun funksiya.

        :param token: Karta tokeni.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/cards.get_verify_code
        """
        data: dict = {
            "method": "cards.get_verify_code",
            "params": {
                "token": token,
            }
        }
        return await self.__requests(card_data=data)

    async def card_verify(self, verify_code: int, token: str) -> dict:
        """
        SMS orqali yuborilgan kod yordamida kartani tekshirish.

        :param verify_code: Tekshirish uchun kod.
        :param token: Karta tokeni.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/cards.verify
        """
        data: dict = {
            "method": "cards.verify",
            "params": {
                "token": token,
                "code": verify_code
            }
        }
        return await self.__requests(card_data=data)

    async def card_check(self, token: str) -> dict:
        """
        Karta tokeni faol yoki faol emasligini tekshirish.

        :param token: Karta tokeni.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/cards.check
        """
        data: dict = {
            "method": "cards.check",
            "params": {
                "token": token,
            }
        }
        return await self.__requests(card_data=data)

    async def card_remove(self, token: str) -> dict:
        """
        Karta tokenini o'chirish.

        :param token: O'chiriladigan karta tokeni.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/cards.remove
        """
        data: dict = {
            "method": "cards.remove",
            "params": {
                "token": token,
            }
        }
        return await self.__requests(card_data=data)

    async def close(self):
        await self._session.close()
