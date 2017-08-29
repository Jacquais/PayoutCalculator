import sys
def program(arg1, arg2, arg3):
    raw = 0
    if sys.argv[1] in ("h", "-h", "--help"):
        print("Usage: payout.py <minimum payout> <current balance> <estimated per hour earnings>")
    while arg2 < arg1:
        raw += 1
        arg2 += arg3
    if raw >= 24:
        days = raw/24
        hours = ((days%1)*24)
        print("It will take about {} days and {} hours to payout.".format(int(days), int(hours)))
if __name__ == "__main__":
    try:
        arg1 = float(sys.argv[1])
        arg2 = float(sys.argv[2])
        arg3 = float(sys.argv[3])
    except(IndexError, ValueError):
        print("Usage: payout.py <minimum payout> <current balance> <estimated per hour earnings>\nRemember: only use numbers.")
        sys.exit(1)
    program(arg1, arg2, arg3)
