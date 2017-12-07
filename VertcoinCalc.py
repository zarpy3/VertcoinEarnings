import coinmarketcap
import json
import time
from coinmarketcap import Market
import re
import urllib

def startOption():
    print('Choose from the following options:')
    print('1. Enter p2pool link.')
    print('2. Enter your details manualy.')
    print('')
    global link
    link = int(input('Please choose an option: '))
    print('')

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

def myHashrate():
    localStats = urllib.request.urlopen(p2pool + '/local_stats')
    localStatsPage = localStats.read()
    hashratesString = str(localStatsPage)
    regexHashrates = str(re.findall(r'miner_hash_rates\"\: \{[A-Za-z0-9\{\"\,:\. ]{1,}', hashratesString))
    regexMyLocalStatsHashWallet = str(re.findall(r'\"' + vertcoinWallet + '\": [0-9]{1,}\.[0-9]{1,}', regexHashrates))
    regexMyLocalStatsHash = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', regexMyLocalStatsHashWallet))
    regexMyLocalStatsHash = regexMyLocalStatsHash.replace("[", "")
    regexMyLocalStatsHash = regexMyLocalStatsHash.replace("'", "")
    global myHashrate
    myHashrate = float(regexMyLocalStatsHash.replace("]", ""))
    myHashrate = myHashrate / 1000000 #gets it in MH/s

def myRejectedHashrate():
    localStats = urllib.request.urlopen(p2pool + '/local_stats')
    localStatsPage = localStats.read()
    rejectedHashratesString = str(localStatsPage)
    regexRejectedHashrates = str(re.findall(r'miner_dead_hash_rates\"\: \{[A-Za-z0-9\{\"\,:\. ]{1,}', rejectedHashratesString))
    regexMyLocalStatsRejectedHashWallet = str(re.findall(r'\"' + vertcoinWallet + '\": [0-9]{1,}\.[0-9]{1,}', regexRejectedHashrates))
    regexMyLocalStatsRejectedHash = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', regexMyLocalStatsRejectedHashWallet))
    regexMyLocalStatsRejectedHash = regexMyLocalStatsRejectedHash.replace("[", "")
    regexMyLocalStatsRejectedHash = regexMyLocalStatsRejectedHash.replace("'", "")
    global myRejectedHashrate
    myRejectedHashrate = float(regexMyLocalStatsRejectedHash.replace("]", ""))
    myRejectedHashrate = myRejectedHashrate / 1000000 #gets value in MH/s

def myBlockValue():
    localStats = urllib.request.urlopen(p2pool + '/local_stats')
    localStatsPage = localStats.read()
    blockValueString = str(localStatsPage)
    regexBlockValue = str(re.findall(r'block_value\"\: [0-9]{1,}\.[0-9]{1,}\,', blockValueString))
    regexBlockValue = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', regexBlockValue))
    regexBlockValue = regexBlockValue.replace("[", "")
    regexBlockValue = regexBlockValue.replace("'", "")
    global myBlockValue
    myBlockValue = float(regexBlockValue.replace("]", ""))

def myFee():
    localStats = urllib.request.urlopen(p2pool + '/local_stats')
    localStatsPage = localStats.read()
    feeString = str(localStatsPage)
    regexFee = str(re.findall(r'fee\"\: [0-9]{1,}\.{0,}[0-9]{0,}\,', feeString))
    regexFee = str(re.findall(r'[0-9]{1,}\.{0,}[0-9]{0,}', regexFee))
    regexFee = regexFee.replace("[", "")
    regexFee = regexFee.replace("'", "")
    global myFee
    myFee = float(regexFee.replace("]", ""))

def myDonation():
    localStats = urllib.request.urlopen(p2pool + '/local_stats')
    localStatsPage = localStats.read()
    donationString = str(localStatsPage)
    regexDonation = str(re.findall(r'donation_proportion\"\: [0-9]{1,}\.{0,}[0-9]{0,}\,', donationString))
    regexDonation = str(re.findall(r'[0-9]{1,}\.{0,}[0-9]{0,}', regexDonation))
    regexDonation = regexDonation.replace("[", "")
    regexDonation = regexDonation.replace("'", "")
    global myDonation
    myDonation = float(regexDonation.replace("]", ""))

def myGlobalHashrate():
    globalStats = urllib.request.urlopen(p2pool + '/global_stats')
    globalStatsPage = globalStats.read()
    globalHashString = str(globalStatsPage)
    regexGlobalHash = str(re.findall(r'pool_hash_rate\"\: [0-9]{1,}\.[0-9]{1,}\,', globalHashString))
    regexGlobalHash = str(re.findall(r'[0-9]{1,}\.[0-9]{1,}', regexGlobalHash))
    regexGlobalHash = regexGlobalHash.replace("[", "")
    regexGlobalHash = regexGlobalHash.replace("'", "")
    global myGlobalHash
    myGlobalHash = float(regexGlobalHash.replace("]", ""))
    myGlobalHash = myGlobalHash / 1000000


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

def manual():
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

    global payout
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

def dataInput():
    if config == 0:
        global p2pool
        p2pool = input('Please input the p2pool\'s address: ')
        p2pool = p2pool.replace('/static/', '')
        global vertcoinWallet
        vertcoinWallet = input('Please input your vertcoin wallet address: ')
        print('')
    else:
        p2pool = p2pool
        p2pool = p2pool.replace('/static/', '')
        vertcoinWallet = vertcoinWallet

def automatic():
    dataInput()
    myHashrate()
    print('Your hashrate is ' + str(myHashrate) + ' MH/s.')
    myRejectedHashrate()
    print('Your rejected hashrate is: ' + str(myRejectedHashrate) + ' MH/s.')
    EH = myHashrate - myRejectedHashrate
    myGlobalHashrate()
    GH = myGlobalHash
    print('The global hashrate is: ' + str(myGlobalHash) + ' MH/s')
    myBlockValue()
    BV = myBlockValue
    print('The block value is: ' + str(myBlockValue) + '.')
    myFee()
    NF = myFee
    print('The node fee is: ' + str(myFee) + '%')
    myDonation()
    DF = myDonation
    print('The donation fee is: ' + str(myDonation) + '%')
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

config = 'config.txt'
configOpen = open(config)
configFile = configOpen.read()
configRegex = str(re.findall(r'\"replace this text between the quotes\"', configFile))
if configRegex == '[\'\"replace this text between the quotes\"\']':
    print('Please enter the following information:')
    print('')
    config = 0
    startOption()

    if link == 1:
        automatic()
    elif link == 2:
        manual()
    else:
        print('Please choose a valid option.')
        print('')
        startOption()
else:
    print('Do you want to load from config.txt?:')
    configQuestion = int(input('Enter 1 to load from config.txt, enter 2 for more options: '))
    print('')
    if configQuestion == 1:
        config = 1
        p2poolRegex = str(re.findall(r'p2pool: \"http://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{1,}/static[/]{0,}', configFile))
        p2poolRegex = p2poolRegex.replace('[', '')
        p2poolRegex = p2poolRegex.replace(']', '')
        p2poolRegex = p2poolRegex.replace("'", '')
        p2poolRegex = p2poolRegex.replace('"', '')
        p2pool = p2poolRegex.replace('p2pool: ', '')

        walletRegex = str(re.findall(r'wallet: \"[0-9A-Za-z]{1,}\"', configFile))
        walletRegex = walletRegex.replace('[', '')
        walletRegex = walletRegex.replace(']', '')
        walletRegex = walletRegex.replace("'", '')
        walletRegex = walletRegex.replace('"', '')
        vertcoinWallet = walletRegex.replace('wallet: ', '')
        automatic()
    else:
        config = 0
        automatic()
