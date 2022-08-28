from payme_uz.requests import Requests


class PaymeSubscribeCard(Requests):
    async def create(self, number: str, expire: str, save: bool) -> dict:
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
        return await self._requests(card_data=data)

    async def get_verify_code(self, token: str) -> dict:
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
        return await self._requests(card_data=data)

    async def verify(self, verify_code: int, token: str) -> dict:
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
        return await self._requests(card_data=data)

    async def check(self, token: str) -> dict:
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
        return await self._requests(card_data=data)

    async def remove(self, token: str) -> dict:
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
        return await self._requests(card_data=data)
