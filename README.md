# [Southxchange](www.southxchange.com/)

<img src='https://www.cryptunit.com/exchangeicons/38.png' width="300" height="300">

[Buy me a coffee ☕︎](https://paywall.link/to/donate)

Southxchange is a cryptocurrency broker that does not require KYC trading is accepted with Lightning, with this library you can interact with the platform.

#### Market
 - [x] List Orders
 - [x] Place Order
 - [x] Cancel Order
 - [x] Cancel Orders

#### Wallets
 - [x] Generate Address
 - [x] Withdraw
 - [x] Balances
 - [x] Transactions List

#### Markets
- [x] List Markets
- [x] Price
- [x] Prices
- [x] Book
- [x] Trades
- [x] History

## Instalation

##### (Southxchange)  requires [ Python ](https://www.python.org) v3.8

```sh
$ pip install Southxchange
```

#### Getting Started

```python
Python 3.8.3 (default, Jun 16 2020, 19:00:28)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import Southxchange
>>>
>>> Southxchange.Southxchange('Private', 'Secret') # Entering credentials.
```

#### Market

```python
>>> Market = Southxchange.Market()
```

- Places an order in a given market.

```python
>>> Market.placeorder('DOGE', 'BTC', amount=1, type='BUY', limitprice='0.00000001') # Place Order.
{'error' : False, 'message' : 'Created order.', 'orderid' : 123456}
```

- Cancels a given order.

```python
>>> Market.cancelorder(123456) # Cancel Order.
{'error' : False, 'message' : 'Cancel order.', 'orderid' : 123456}
```

- Cancels a given order.

```python
>>> Market.cancelorders('BTC', 'DOGE') # Cancel Orders
{'error' : False, 'message' : 'Cancel orders.'}
```

- Lists all pending orders.

```python
>>> Market.listorders() # List Orders.
[{'Code': '132541', 'Type': 'buy', 'Amount': 1.0, 'OriginalAmount': 1.0, 'LimitPrice': 1e-08, 'ListingCurrency': 'DOGE', 'ReferenceCurrency': 'BTC'}]
```

#### Wallets

```python
>>> Wallets = Southxchange.Wallets()
```

- Generates a new address for a given cryptocurrency.

```python
>>> Wallets.newaddress('BTC') # New Address.
{'error': False, 'message': 'New address generated.', 'address': '3G983JSIM ...'}
```

- Lists balances for all currencies.

```python
>>> Wallets.balances() # List Balances.
[{"Currency":"BTC","Deposited": 1 ,"Available": 1, "Unconfirmed": 5}]
```

- List all transactions.

```python
>>> Wallets.transactions('BTC', type='transactions', pageindex=1, pagesize=50) # List History Transactions.
{'TotalElements': 50, 'Result': [{...} ...] ...}
```

- Withdraws to a given address. 

```python
>>> Wallets.withdraw('BBP', 'BPHoq ...', amount='2') # Withdraw
{'error': False, 'message': '', ...}
```

#### Markets

```python
>>> Markets = Southxchange.Markets()
```

- Lists all markets

```python
>>> Markets.listmarkets()
[['DASH', 'BTC'] ...]
```

- Gets price of a given market

```python
>>> Markets.price('ltc', 'btc')
{'Bid': 0.00454897, 'Ask': 0.004590561, 'Last': 0.004599999, 'Variation24Hr': 0.27, 'Volume24Hr': 34.04216098}
```

- Lists prices of all markets

```python
>>> Markets.prices()
[{'Market': 'DASH/BTC', 'Bid': 0.007663185, 'Ask': 0.007716761, 'Last': 0.007727174, 'Variation24Hr': 3.73, 'Volume24Hr': 32.97202091} ...]
```

- Lists order book of a given market


```python
>>> Markets.book('ltc', 'btc')
{'BuyOrders': [{'Index': 0, 'Amount': 8.0, 'Price': 0.004562066} ... ]}
```

- Lists latest trades in a given market

```python
>>> Markets.trades('ltc','btc')
[{'At': 1592996087, 'Amount': 0.00149447, 'Price': 0.004599999, 'Type': 'buy'} ...]
```

- List market history between two dates

```python
>>> Markets.history('ltc', 'btc', 1514775600000, 1517367600000, periods=100)
[{'At': 1592996087, 'Amount': 0.00149447, 'Price': 0.004599999, 'Type': 'buy'} ... ]
```


| Field           | Description     |
| :-------------: | :-------------: |
| start           | Start date in milliseconds from January 1, 1970 |
| end             | End date in milliseconds from January 1, 1970 |
| periods         | Number of periods to get (Optional: defaults to 100) |


