from asyncio import AbstractEventLoop, get_event_loop

from aiohttp import ClientSession


class PaymeSubscribeReceipt:
    def __init__(self, paycom_id: str, secret_key: str, debug: bool = False, loop: AbstractEventLoop = None):
        # Asyncio loop instance
        if loop is None:
            loop = get_event_loop()
        self.loop = loop

        # URL's
        self.test_url: str = 'https://checkout.test.paycom.uz/api/'
        self.pro_url: str = 'https://checkout.paycom.uz/api/'
        self.__api_url: str = self.pro_url if debug else self.test_url

        self.__paycom_id: str = paycom_id
        self.__secret_key: str = secret_key

        self.__headers: dict = {
            "X-Auth": f"{self.__paycom_id}:{self.__secret_key}",
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

    async def receipt_create(self, amount: float, order_id: int) -> dict:
        """
        Yangi to'lov kvitansiyasini yaratish uchun funksiya.

        :param amount: To'lov miqdori.
        :param order_id: Buyurtma ID raqami
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/receipts.create
        """
        data: dict = {
            "method": "receipts.create",
            "params": {
                "amount": amount,
                "account": {
                    "order_id": order_id,
                }
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_create_p2p(self, token: str, amount: float, description: str = 'description') -> dict:
        """
        Yangi P2P tranzaksiyasini yaratish uchun funksiya.
        U sinov rejimida emas, faqat ishlab chiqarish rejimida ishlaydi.

        :param token: Karta faol tokeni.
        :param amount: Shaxsdan shaxsga o'tkaziladigan tranzaksiya summasi.
        :param description: Tavsifi
        :return: JSON
        """
        data: dict = {
            "method": "receipts.p2p",
            "params": {
                "token": token,
                "amount": amount,
                "description": description
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_pay(self, invoice_id: str, token: str, phone: str) -> dict:
        """
        Mavjud chekni to'lash uchun funksiya.

        :param invoice_id: Chek ID raqami.
        :param token: Karta faol tokeni.
        :param phone: To'lovchining telefon raqami.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/receipts.pay
        """
        data: dict = {
            "method": "receipts.pay",
            "params": {
                "id": invoice_id,
                "token": token,
                "payer": {
                    "phone": phone,
                }
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_send(self, invoice_id: str, phone: str) -> dict:
        """
        SMS xabarda to'lov kvitansiyasini yuborish uchun funksiya.

        :param invoice_id: Chek ID raqami.
        :param phone: To'lovchining telefon raqami.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/receipts.send
        """
        data: dict = {
            "method": "receipts.send",
            "params": {
                "id": invoice_id,
                "phone": phone
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_cancel(self, invoice_id: str) -> dict:
        """
        Navbatda turgan pullik chekni bekor qilish uchun funksiya.

        :param invoice_id: Chek ID raqami.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/receipts.cancel
        """
        data: dict = {
            "method": "receipts.cancel",
            "params": {
                "id": invoice_id
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_check(self, invoice_id: str) -> dict:
        """
        Chek mavjudligini tekshirish uchun funksiya.

        :param invoice_id: Chek ID raqami
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/receipts.check
        """
        data: dict = {
            "method": "receipts.check",
            "params": {
                "id": invoice_id
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_get(self, invoice_id: str) -> dict:
        """
        Mavjud chek holatini tekshirish uchun funksiya.

        :param invoice_id: Chek ID raqami
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/receipts.get
        """
        data: dict = {
            "method": "receipts.get",
            "params": {
                "id": invoice_id
            }
        }
        return await self.__requests(card_data=data)

    async def reciept_get_all(self, count: int, _from: str, to: str, offset: str) -> dict:
        """
        Barcha to'liq ma'lumotlarni oling,
        ma'lum bir davr uchun cheklar bo'yicha.

        :param count: Cheklar soni. Maksimal qiymati 50 ta.
        :param _from: Boshlanish sanasi.
        :param to: Tugash sanasi.
        :param offset: Keyingi o'tkazib yuborilgan cheklar soni.
        :return: JSON

        To'liq hujjat:
        https://developer.help.paycom.uz/uz/metody-subscribe-api/receipts.get_all
        """
        data: dict = {
            "method": "receipts.get_all",
            "params": {
                "count": count,
                "from": _from,
                "to": to,
                "offset": offset
            }
        }
        return await self.__requests(card_data=data)

    async def close(self):
        await self._session.close()
