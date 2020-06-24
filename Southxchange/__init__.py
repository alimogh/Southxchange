#!/usr/bin/python3.8

import requests
import hashlib
import hmac
import json
import time

logged = [{'status' : False}]

def Southxchange(private, secret):

    global logged

    logged[0] = {'status' : True, 'private' : private, 'secret' : secret}

def Push(path, method='POST', json=None, headers=None):

    url = 'https://www.southxchange.com/api' + path

    if method == 'GET':
        return requests.get(url, json=json, headers=headers)

    if method == 'POST':
        return requests.post(url, json=json, headers=headers)

def Nonce():

    return int(time.time())

def Sign(data):

    if logged[0]['status'] == False:
        raise ValueError('You have not entered your keys in Southxchange(secret, private)')

    return hmac.new(logged[0]['secret'].encode(), json.dumps(data).encode(), hashlib.sha512).hexdigest()

class Market:

    def __init__(self):

        if logged[0]['status'] == False:
            raise ValueError('You have not entered your keys in Southxchange(secret, private)')

    def placeorder(self, x, y, amount=None, type=None, limitprice=None):

        if isinstance(x, str) == False or isinstance(y, str) == False:
            raise ValueError('(x, y) is not a string.')

        x, y = x.upper(), y.upper()

        type = str(type).upper()

        if not type in ['BUY', 'SELL']:
            raise ValueError('The value in (type={0}) is not within (BUY, SELL)'.format(type))

        if str(amount).replace('.', '', 1).isdigit() == False:
            raise ValueError('Amount is not a number.')

        data = {
            'nonce' : Nonce(), 'key' : logged[0]['private'],
            'listingCurrency' : x, 'referenceCurrency' : y,
            'type' : type, 'amount' : amount, 'limitPrice' : limitprice
        }

        request = Push('/placeOrder', json=data, headers={'Hash' : Sign(data)})

        if request.status_code != 200:
            return {'error' : True, 'message' : eval(request.text)}

        if request.status_code == 200:
            return {'error' : False, 'message' : 'Created order.', 'orderid' : int(eval(request.text))}

    def cancelorder(self, ordercode):

        ordercode = str(ordercode)

        if ordercode.isnumeric() == True:

            data = {'nonce' : Nonce(), 'key' : logged[0]['private'], 'orderCode' : ordercode}

            request = Push('/cancelOrder', json=data, headers={'Hash' : Sign(data)})

            if request.status_code == 204:
                return {'error' : False, 'message' : 'Cancel order.', 'orderid' : int(ordercode)}

    def cancelorders(self, x, y):

        if isinstance(x, str) == True and isinstance(y, str) == True:

            x, y = x.upper(), y.upper()

            data = {
                'nonce' : Nonce(), 'key' : logged[0]['private'],
                'listingCurrency' : x, 'referenceCurrency' : y
            }

            request = Push('/cancelMarketOrders', json=data, headers={'Hash' : Sign(data)})

            if request.status_code == 204:
                return {'error' : False, 'message' : 'Cancel orders.'}

    def listorders(self):

        data = {'nonce' : Nonce(), 'key' : logged[0]['private']}

        return Push('/listOrders', json=data, headers={'Hash' : Sign(data)}).json()

class Wallets:

    def __init__(self):

        if logged[0]['status'] == False:
            raise ValueError('You have not entered your keys in Southxchange(secret, private)')

    def newaddress(self, currency):

        if isinstance(currency, str) == False:
            raise ValueError('(currency) is not a string.')

        currency = str(currency).upper()

        data = {'nonce' : Nonce(), 'key' : logged[0]['private'], 'currency' : currency}

        request = Push('/generatenewaddress', json=data, headers={'Hash' : Sign(data)})

        if request.status_code == 400:
            return {'error' : True, 'message' : eval(request.text)}

        if request.status_code == 200:

            address = eval(request.text)
            address = address.replace('"', '')

            return {'error' : False, 'message' : 'New address generated.', 'address' : address}

    def withdraw(self, currency, address, amount=None):

        if isinstance(currency, str) == False or isinstance(address, str) == False:
            raise ValueError('(currency, address) is not a string.')

        if isinstance(currency, int) == True or isinstance(amount, str) == True:

            if str(amount).replace('.', '', 1).isdigit() == False:
                raise ValueError('(amount) it is not a number.')

            data = {'nonce' : Nonce(), 'key' : logged[0]['private'], 'currency' : currency, 'address' : address, 'amount' : amount}

            request = Push('/withdraw', json=data, headers={'Hash' : Sign(data)})

            if request.status_code == 400:
                return {'error' : True, 'message' : eval(request.text)}

            result = request.json()
            result.update({
                'error' : False, 'message' : '', 'status' : request['Status'],
                'max' : request['Max'],
                'maxdaily' : request['MaxDaily'],
                'movementid' : request['MovementId']
            })

            return result

    def balances(self):

        data = {'nonce' : Nonce(), 'key': logged[0]['private']}

        return Push('/listBalances', json=data, headers={'Hash' : Sign(data)}).text

    def transactions(self, currency, type='transactions', pageindex=1, pagesize=50):

        if isinstance(currency, str) == True:

            currency = str(currency).upper()

            if isinstance(pageindex, int) == True and isinstance(pagesize, int) == True:

                type = str(type).lower()

                if type in ['transactions', 'deposits', 'withdrawals']:

                    data = {
                        'nonce' : Nonce(), 'key' : logged[0]['private'],
                        'Currency': currency, 'TransactionType' : type,
                        'PageIndex' : pageindex, 'PageSize' : pagesize
                    }

                    return Push('/listTransactions', json=data, headers={'Hash' : Sign(data)}).json()

class Markets:

    def listmarkets(self):

        return Push('/markets', method='GET').json()

    def price(self, x, y):

        x, y = str(x).upper(), str(y).upper()

        request = Push('/price/{0}/{1}'.format(x, y), method='GET')

        if not type(eval(request.text)) in [dict, list]:
            raise ValueError('Market does not exist.')

        return request.json()

    def prices(self):

        return Push('/prices', method='GET').json()

    def book(self, x, y):

        x, y = str(x).upper(), str(y).upper()

        request = Push('/book/{0}/{1}'.format(x, y), method='GET')

        if not type(eval(request.text)) in [dict, list]:
            raise ValueError('Market does not exist.')

        return request.json()

    def trades(self, x, y):

        x, y = str(x).upper(), str(y).upper()

        request = Push('/trades/{0}/{1}'.format(x, y), method='GET')

        if not type(eval(request.text)) in [dict, list]:
            raise ValueError('Market does not exist.')

        return request.json()

    def history(self, x, y, start, end, periods=100):

        x, y = str(x).upper(), str(y).upper()

        if str(start).isnumeric() == False or str(end).isnumeric() == False:
            raise ValueError('(Start or End) are not an integer.')

        query = '/history/{0}/{1}/{2}/{3}/{4}'.format(x, y, start, end, periods)

        request = Push(query, method='GET')

        if not type(eval(request.text)) in [dict, list]:
            raise ValueError('Market does not exist.')

        return request.json()
