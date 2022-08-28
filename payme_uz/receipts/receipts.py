from asyncio import AbstractEventLoop

from payme_uz.requests import Requests


class PaymeSubscribeReceipt(Requests):
    def __init__(self, paycom_id: str, secret_key: str, debug: bool = False, loop: AbstractEventLoop = None):
        super().__init__(paycom_id, debug, loop)
        self._headers['X-Auth'] += f':{secret_key}'

    async def create(self, amount: float, order_id: int) -> dict:
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
        return await self._requests(card_data=data)

    async def create_p2p(self, token: str, amount: float, description: str = 'description') -> dict:
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
        return await self._requests(card_data=data)

    async def pay(self, invoice_id: str, token: str, phone: str) -> dict:
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
        return await self._requests(card_data=data)

    async def send(self, invoice_id: str, phone: str) -> dict:
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
        return await self._requests(card_data=data)

    async def cancel(self, invoice_id: str) -> dict:
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
        return await self._requests(card_data=data)

    async def check(self, invoice_id: str) -> dict:
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
        return await self._requests(card_data=data)

    async def get(self, invoice_id: str) -> dict:
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
        return await self._requests(card_data=data)

    async def get_all(self, count: int, _from: str, to: str, offset: str) -> dict:
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
        return await self._requests(card_data=data)
