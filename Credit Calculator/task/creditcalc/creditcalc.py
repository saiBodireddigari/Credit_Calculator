import math
import argparse


def main():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("--type", type=str)
    my_parser.add_argument("--principal", type=int)
    my_parser.add_argument("--payment", type=float)
    my_parser.add_argument("--periods", type=int)
    my_parser.add_argument("--interest", type=float)

    my_args = my_parser.parse_args()
    dict_args = {key: val for key, val in vars(my_args).items() if val is not None}

    calc_type = my_args.type
    principal = my_args.principal
    payment = my_args.payment
    periods = my_args.periods
    interest = my_args.interest
    if interest is not None:
        nominal_interest = (1 / 12) * (interest / 100)

    payment_with_diff = (calc_type == "diff") and (payment is not None)

    if (calc_type is None) or payment_with_diff or (interest is None) or len(dict_args) < 4:
        print("Incorrect parameters")
    else:
        if (calc_type == "diff") and payment is None:
            if principal > 0 and periods > 0 and interest > 0:
                diff_pay(principal, periods, nominal_interest)
            else:
                print("Incorrect parameters")
        elif calc_type == "annuity":
            if payment is None:
                if principal > 0 and periods > 0 and interest > 0:
                    annuity_payment(principal, periods, nominal_interest)
                else:
                    print("Incorrect parameters")
            elif principal is None:
                if payment > 0 and periods > 0 and interest > 0:
                    credit_principal(payment, periods, nominal_interest)
                else:
                    print("Incorrect parameters")
            elif periods is None:
                if principal > 0 and payment > 0 and interest > 0:
                    number_of_months(principal, payment, nominal_interest)
                else:
                    print("Incorrect parameters")


def number_of_months(principal, payment, interest):

    months_count = math.log(payment / (payment - interest * principal), 1 + interest)

    if round(months_count / 12) == 0:
        print("you need {} months to repay this credit!".format(str(round(months_count % 12))))
    elif math.ceil(months_count) % 12 == 0:
        print("You need {} years to repay this credit!".format(str(math.ceil(months_count / 12))))
    elif round(months_count % 12) > 1:
        print("You need {} years and {} months to repay this credit!".
              format(str(math.floor(months_count / 12)), str(math.ceil(months_count % 12))))

    over_payment = int(payment * math.ceil(months_count) - principal)
    print(over_payment)
    print("Overpayment = {}".format(over_payment))


def credit_principal(payment, periods, interest):
    a = (interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1)
    principal = payment / a

    print("Your credit principal = {}!".format(str(math.floor(principal))))
    over_payment = int(payment * periods - principal)
    print("Overpayment = {}".format(over_payment))


def annuity_payment(principal, periods, interest):

    diff_list = differentiated_payments(principal, periods, interest)
    a = (interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1)
    annuity = principal * a

    print("Your annuity payment = {}!".format(str(math.ceil(annuity))))
    over_payment = int(math.ceil(annuity) * periods - principal)
    print("Overpayment = {}".format(over_payment))


def diff_pay(principal, periods, interest):
    diff_list = differentiated_payments(principal, periods, interest)
    m = 1
    payment = 0
    for pay in diff_list:
        print("Month {}: paid out {}".format(str(m), pay))
        m += 1
        payment += pay
    print()
    print("Overpayment = {}".format(str(payment - principal)))


def differentiated_payments(principal, periods, interest):
    diff_list = []
    for i in range(1, periods + 1):
        dm = math.ceil((principal / periods) + interest * (principal - (principal * (i - 1)) / periods))
        diff_list.append(dm)
    return diff_list


if __name__ == '__main__':
    main()
