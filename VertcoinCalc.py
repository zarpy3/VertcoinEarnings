import coinmarketcap
import json
import time
from coinmarketcap import Market
import re

def currencyChoice():
    print('Please choose from the following options for your currency:')
    print('')
    print('1. GBP')
    print('2. USD')
    print('')
    global payoutCur
    payoutCur = int(input('Please choose your currency: '))
    print('')

def rejectedHashUnits():
    print('Please choose from the following options for rejected hashrate:')
    print('1. MH/s')
    print('2. KH/s')
    print('')
    global rejectUnits
    rejectUnits = int(input('Please choose your units: '))
    print('')

coinmarketcap = Market()
vtcJ = coinmarketcap.ticker('vertcoin', convert='GBP')
svtcJ = str(vtcJ)

#Almost definitely not the most efficient way of doing it but it works

def gbpCur():
    priceGBPPartMatch = str(re.findall(r'\'price_gbp\'\: \'[0-9]{1,}\.[0-9]{1,}', svtcJ))
    priceGBP = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', priceGBPPartMatch))
    intPriceGBP = priceGBP.replace("[", "")
    intPriceGBP = intPriceGBP.replace("'", "")
    global floatPriceGBP
    floatPriceGBP = float(intPriceGBP.replace("]", ""))

def usdCur():
    priceUSDPartMatch = str(re.findall(r'\'price_usd\'\: \'[0-9]{1,}\.[0-9]{1,}', svtcJ))
    priceUSD = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', priceUSDPartMatch))
    intPriceUSD = priceUSD.replace("[", "")
    intPriceUSD = intPriceUSD.replace("'", "")
    global floatPriceUSD
    floatPriceUSD = float(intPriceUSD.replace("]", ""))

def btcCur():
    priceBTCPartMatch = str(re.findall(r'\'price_btc\'\: \'[0-9]{1,}\.[0-9]{1,}', svtcJ))
    priceBTC = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', priceBTCPartMatch))
    intPriceBTC = priceBTC.replace("[", "")
    intPriceBTC = intPriceBTC.replace("'", "")
    global floatPriceBTC
    floatPriceBTC = float(intPriceBTC.replace("]", ""))

print('''
                                    :::::
                                :::::::::::::
                              ::::::::::::::::::
                            :::::::::::::::::::::
                           ::::::::::::::::::::
                          ::::::::::::::::::::      :
                         ::::::::::::::::::::      ::
                        ::::::::::::::::::::      :::
                        :::::::::::::::::::      :::::
                        ::::::::::::::::::      ::::::
                        ::::::                 :::::::
                         ::::::::             ::::::::
                          ::::::::           :::::::::
                          :::::::::         :::::::::
                           :::::::::       :::::::::
                            :::::::::     :::::::::
                             :::::::::   :::::::::
                               ::::::::.::::::::
                                  ::::::::::::
                                     ::::::

''')
print('Hello, Welcome to the VertCoin profit calculator.')
print('Please enter the following information:')
print('')

hashrate = float(input('Please enter your hashrate (MH/s): '))
H = hashrate
print('')

rejectedHashUnits()

rejectedHashrate = float(input('Please enter your rejected hashrate: '))
print('')

if rejectUnits == 1:
    RH = rejectedHashrate
elif rejectUnits == 2:
    RH = rejectedHashrate / 1000
else:
    print('')
    print('Please enter a valid option.')
    print('')
    rejectedHashUnits()



effectiveHashrate = H - RH
EH = effectiveHashrate

globalPoolHashrate = float(input('Please enter the global hashrate (GH/s): '))
GH = globalPoolHashrate * 1000
print('')

blockValue = float(input('Please enter the block value (VTC): '))
BV = blockValue
print('')

nodeFee = float(input('Please enter the node fee (%): '))
NF = nodeFee / 100
print('')

donationFee = float(input('Please enter the donation fee (%): '))
DF = donationFee / 100
print('')

payout = BV * (EH/GH*(1-(NF-DF)))

currencyChoice()

if payoutCur == 1:
    gbpCur()
    btcCur()
    VTC = floatPriceGBP * payout
    sign = '£'
    BTC = floatPriceBTC * payout
elif payoutCur == 2:
    usdCur()
    btcCur()
    VTC = floatPriceUSD * payout
    sign = '$'
    BTC = floatPriceBTC * payout
else:
    print('')
    print('Please choose a valid option.')
    print('')
    currencyChoice()

print('Your estimated payout is: ' + str(round(payout,6)) + ' VTC / ' + str(BTC) + ' BTC / ' + sign + str(round(VTC,4)))
