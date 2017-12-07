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

print('Please choose from the following options for rejected hashrate:')
print('1. MH/s')
print('2. KH/s')
print('')
rejectUnits = int(input('Please choose your units: '))
print('')

rejectedHashrate = float(input('Please enter your rejected hashrate: '))
print('')
if rejectUnits == 1:
    RH = rejectedHashrate
elif rejectUnits == 2:
    RH = rejectedHashrate / 1000

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
    VTC = floatPriceGBP * payout
    sign = '£'
elif payoutCur == 2:
    usdCur()
    VTC = floatPriceUSD * payout
    sign = '$'
else:
    print('')
    print('Please choose a valid option.')
    currencyChoice()

print('Your estimated payout is: ' + str(round(payout,6)) + ' VTC. Which is '+ sign + str(round(VTC,4)))
