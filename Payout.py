import sys
import requests


def program(currency, addr, payout):
    print('''
#######################################
#######################################
############   #(    /#   #   #########
############   #  (#  #   #  ##########
############   #  ##  #      ##########
############   #  #####     ###########
############   #  #####     ,##########
########   #   #  ##,,#   ,  ##########
########   #   #  ##  #   #  ##########
########      /#      #   #   #########
##########  .#####  ###///#///#########
#######################################''')
    print("As the time to payout increases, the inaccuracy increases.\n")
    # API calls
    hashrate = requests.get('https://api.nanopool.org/v1/{}/avghashrate/{}'.format(currency, addr)).json()
    calc = requests.get('https://api.nanopool.org/v1/{}/approximated_earnings/{}'.format(currency, hashrate['data']['h6'])).json()
    balance = requests.get('https://eth.nanopool.org/api/v1/balance_hashrate/{}'.format(addr)).json()
    rawTime = 0
    while balance['data']['balance'] < float(payout):
        rawTime += 1
        balance['data']['balance'] += calc['data']['hour']['coins']
    if rawTime == 24:
        print("It will take about 1 day to payout.")
    if rawTime > 24:
        days = rawTime/24
        hours = ((days%1)*24)
        print("It will take about {} days and {} hours to payout.".format(int(days), int(hours)))
    elif rawTime == 0:
        print("It will take less then 1 hour to payout.")
    elif rawTime < 24:
        print("It will take about {} hours to payout.".format(rawTime))


if __name__ == "__main__":
    try:
        currency = str(sys.argv[1])
        addr = sys.argv[2]
        payout = float(sys.argv[3])
        if sys.argv[1] in ("h", "-h", "--help"):
            raise ValueError
    except(IndexError, ValueError):
<<<<<<< HEAD
        print("Usage: Payout.py <currency (eth/etc/sia/zec/xmr/pasc)> <account address> <minimum payout>")
        sys.exit(1)
    program(currency, addr, payout)
=======
        print("Usage: payout.py <minimum payout> <current balance> <estimated per hour earnings>\nRemember: only use numbers.")
        sys.exit(1)
    program(arg1, arg2, arg3)
>>>>>>> origin/master
