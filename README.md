![alt text](https://i.imgur.com/XDz8NNJ_d.webp?maxwidth=760&fidelity=grand)

# Payme API uchun Asinxron kutubxona!!!

<hr>

## Boshlash

* O'rnatish:

```
$ pip install -U aiopay
```

* Ishlatish:

```python
from asyncio import get_event_loop

from payme_uz.cards import PaymeSubscribeCard


async def main():
    cards_api = PaymeSubscribeCard(paycom_id='paycom_id', debug=True)  # debug: True - sinov rejimi, False - ishlab chiqarish rejimi
    await cards_api.card_create(number='8600069195406311', expire='0399', save=True)


if __name__ == '__main__':
    get_event_loop().run_until_complete(main())

```