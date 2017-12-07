import coinmarketcap
import json
import time
from coinmarketcap import Market
import re

coinmarketcap = Market()
vtcGBPJ = coinmarketcap.ticker('vertcoin', convert='GBP')
#print(vtcGBPJ)
svtcGBPJ = str(vtcGBPJ)
priceGBPPartMatch = str(re.findall(r'\'price_gbp\'\: \'[0-9]{1,}\.[0-9]{1,}', svtcGBPJ))
priceGBP = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', priceGBPPartMatch))
intPriceGBP = priceGBP.replace("[", "")
intPriceGBP = intPriceGBP.replace("'", "")
floatPriceGBP = float(intPriceGBP.replace("]", ""))




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

VTC = floatPriceGBP * payout

print('Your estimated payout is: ' + str(round(payout,6)) + ' VTC. Which is £' + str(round(VTC,4)))
