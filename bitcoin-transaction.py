from requests import get
from matplotlib import pyplot as plt
from datetime import datetime
import requests

def transaction_details(wallet_address):
    url = 'https://blockchain.info/rawaddr/'+wallet_address
    response = get(url)
    data = response.json()x
    return data

def bitcoin_price_in_usd():
    response = get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    rate = data["bpi"]["USD"]["rate"].replace(',','')
    return rate

BITCOIN_VALUE = 10 ** 8
wallet_address = input('Bitcoin address: ')

details = transaction_details(wallet_address)
no_of_transactions = details.get('n_tx')
total_bitcoin_received = details.get('total_received') / BITCOIN_VALUE
total_bitcoin_sent = details.get('total_sent') / BITCOIN_VALUE
total_bitcoin_in_wallet = details.get('final_balance') / BITCOIN_VALUE

bitcoin_rate_in_USD = float(bitcoin_price_in_usd())
bitcoin_received_USD = "%.0f" %(float(total_bitcoin_received) * bitcoin_rate_in_USD)
bitcoin_sent_USD = "%.0f" %(float(total_bitcoin_sent) * bitcoin_rate_in_USD)
final_balance_in_USD = "%.0f" %(float(total_bitcoin_in_wallet) * bitcoin_rate_in_USD)



BTC = f'''\nWallet Address: {wallet_address}\nNumber of Transactions: {no_of_transactions}\nTotal Bitcoin Received: {total_bitcoin_received} BTC\nTotal Bitcoin Sent: {total_bitcoin_sent} BTC\nTotal Bitcoin in Wallet: {total_bitcoin_in_wallet} BTC\n\nBitcoin Received in USD: ${bitcoin_received_USD}\nTotal Bitcoin Sent in USD: ${bitcoin_sent_USD}\nFinal Balance in USD: ${final_balance_in_USD}'''
print(BTC)
