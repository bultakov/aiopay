![alt text](https://i.imgur.com/XDz8NNJ_d.webp?maxwidth=760&fidelity=grand)

# Payme API uchun Asinxron kutubxona!!!

<hr>

## Boshlash

* O'rnatish:

```
$ pip install -U aiopay
```

* Example:

```python
from asyncio import get_event_loop

from payme_uz.cards import PaymeSubscribeCard


async def main():
    card_api = PaymeSubscribeCard(
        paycom_id='paycom_id',
        debug=True
    )  # debug: True - sinov rejimi, False - ishlab chiqarish rejimi
    data = await card_api.card_create(number='8600069195406311', expire='0399', save=True)
    print(data)
    await card_api.close()


if __name__ == '__main__':
    get_event_loop().run_until_complete(main())


```

* Result:

```json5
{
  "jsonrpc": "2.0",
  "result": {
    "card": {
      "number": "860006******6311",
      "expire": "03/99",
      "token": "6308******5xUj",
      "recurrent": true,
      "verify": false,
      "type": "22618"
    }
  }
}
```