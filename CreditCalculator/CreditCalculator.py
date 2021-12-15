import math
import argparse


print("""
Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!
""")

par = argparse.ArgumentParser()
par.add_argument("--principal", type=int)
par.add_argument("--payment", type=int)
par.add_argument("--interest", type=float)
par.add_argument("--periods", type=int)
par.add_argument("--annuity", type=float)
par.add_argument("--type", type=str)
arg = par.parse_args()


def a1(princ, pay, inter):
    i = (inter * 0.01 / 12)
    fr = (pay / (pay - i * princ))
    res = math.ceil(math.log(fr, i + 1))
    a = res / 12
    b = (a - math.floor(a)) * 12
    if math.floor(b) != 0:
        print(f"It will take {math.floor(a)} years and {math.ceil(b)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(a)} years to repay this loan!\n")
    print(f"Overpayment {int(princ * (1 + inter * 0.01 / 0.75) - princ)}")


def a2(prin, per, inter):
    i = (inter * 0.01 / 12)
    n = pow(1 + i, per)
    res1 = prin * ((i * n) / (n - 1))
    print(f"Your monthly payment = {math.ceil(res1)}!/n")
    print(f"Overpayment {math.ceil(res1) * per - prin}")


def a3(pay, per, inter):
    i = (inter * 0.01 / 12)
    n = pow(1 + i, per)
    res2 = math.floor(float(pay / ((i * n) / (n - 1))))
    print(f"Your loan principal = {res2}!\n")
    print(f"Overpayment {pay * per - res2}")


def diff(principial, periods, interest):
    i = interest * 0.001 / 12
    month = 0
    result = 0
    st = list(reversed(range(2, periods + 2)))
    for monthly in st:
        monthly -= 1
        e = math.ceil(principial / periods)  + i *((principial * monthly) / periods)
        result += e
        month += 1
        print(f"Month {month}: payment is {math.ceil(e)}")
    print(f"Overpayment {math.ceil(result - principial)}")

try:
    if arg.type == "annuity":
        if arg.payment is not None and arg.principal is not None:
            if arg.principial > 0 and arg.payment > 0 and arg.interest > 0:
                a1(arg.principal, arg.periods, arg.interest)
            else:
                print("Incorrect parameters")
        elif arg.princspal is not None and arg.periods is not None:
            if arg.principal > 0 and arg.periods > 0 and arg.interest > 0:
                a2(arg.principal, arg.periods, arg.interest)
            else:
                print("Incorrect parameters")
        elif arg.payment is not None:
            if arg.payment > 0 and arg.periods > 0 and arg.interest > 0:
                a3(arg.principal, arg.periods, float(arg.interest))
            else:
                print("Incorrect parameters")
    elif arg.type == "diff":
        if arg.principal > 0 and arg.periods > 0 and arg.interest > 0:
            diff(arg.principal, arg.periods, arg.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
except TypeError:
    print("Incorrect parameters")
