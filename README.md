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
>>> 
```

#### Market

```python
>>> Market = Southxchange.Market()
>>> 
>>> Market.placeorder('DOGE', 'BTC', amount=1, type='BUY', limitprice='0.00000001') # Place Order.
{'error' : False, 'message' : 'Created order.', 'orderid' : 123456}
>>> 
>>> Market.cancelorder(123456) # Cancel Order.
{'error' : False, 'message' : 'Cancel order.', 'orderid' : 123456}
>>>
>>> Market.cancelorders('BTC', 'DOGE') # Cancel Orders
{'error' : False, 'message' : 'Cancel orders.'}
>>>
>>> Market.listorders() # List Orders.
[{'Code': '132541', 'Type': 'buy', 'Amount': 1.0, 'OriginalAmount': 1.0, 'LimitPrice': 1e-08, 'ListingCurrency': 'DOGE', 'ReferenceCurrency': 'BTC'}]
>>>
```

#### Wallets

```python
>>> Wallets = Southxchange.Wallets()
>>>
>>> Wallets.newaddress('BTC') # New Address.
{'error': False, 'message': 'New address generated.', 'address': '3G983JSIM ...'}
>>>
>>> Wallets.balances() # List Balances.
[{"Currency":"BTC","Deposited": 1 ,"Available": 1, "Unconfirmed": 5}]
>>>
>>> Wallets.transactions('BTC', type='transactions', pageindex=1, pagesize=50) # List History Transactions.
{'TotalElements': 50, 'Result': [{...} ...] ...}
>>>
>>> Wallets.withdraw('BBP', 'BPHoq ...', amount='2') # Withdraw
{'error': False, 'message': '', ...}
>>>
```
