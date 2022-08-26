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
        async with self._session.post(url=self.__api_url, json=card_data, headers=self.__headers) as response:
            return await response.json()

    async def receipt_create(self, amount: float, order_id: int) -> dict:
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

    async def receipt_create_p2p(self, token: str, amount: float, p2p_description: str = 'description') -> dict:
        data: dict = {
            "method": "receipts.p2p",
            "params": {
                "token": token,
                "amount": amount,
                "description": p2p_description
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_pay(self, invoice_id: str, token: str, phone: str) -> dict:
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
        data: dict = {
            "method": "receipts.send",
            "params": {
                "id": invoice_id,
                "phone": phone
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_cancel(self, invoice_id: str) -> dict:
        data: dict = {
            "method": "receipts.cancel",
            "params": {
                "id": invoice_id
            }
        }
        return await self.__requests(card_data=data)

    async def receipt_check(self, invoice_id: str) -> dict:
        data: dict = {
            "method": "receipts.check",
            "params": {
                "id": invoice_id
            }
        }
        return await self.__requests(card_data=data)

    async def reciept_get(self, invoice_id: str) -> dict:
        data: dict = {
            "method": "receipts.get",
            "params": {
                "id": invoice_id
            }
        }
        return await self.__requests(card_data=data)

    async def reciept_get_all(self, count: int, _from: str, to: str, offset: str) -> dict:
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
