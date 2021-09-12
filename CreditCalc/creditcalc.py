import math
import sys


def start():
    parse_parameters = parsing_parameters()
    if validate_parameters(parse_parameters) is None:
        if 'diff' in parse_parameters.values():
            calc_diff_payment(parse_parameters)
        elif 'annuity' in parse_parameters.values() and 'payment' not in parse_parameters.keys():
            calc_annuity_payment(parse_parameters)
        elif 'annuity' in parse_parameters.values() and 'periods' not in parse_parameters.keys():
            calc_count_of_months(parse_parameters)
        elif 'annuity' in parse_parameters.values() and 'principal' not in parse_parameters.keys():
            calc_principal(parse_parameters)
    else:
        print(validate_parameters(parse_parameters))


def parsing_parameters():
    input_parametrs = {}
    for parameter in sys.argv[1:]:
        input_parametrs.update({parameter.split("=")[0][2:]: parameter.split("=")[1]})
    return input_parametrs


def validate_parameters(parameters: dict):
    if len(sys.argv) < 5:
        return "Incorrect parameters"
    elif "type" not in parameters.keys() or "interest" not in parameters.keys():
        return "Incorrect parameters"
    elif "diff" in parameters.values() and "payment" in parameters.keys():
        return "Incorrect parameters"
    for key, value in parameters.items():
        if key == "type":
            continue
        else:
            if float(value) < 0:
                return "Incorrect parameters"


def calc_count_of_months(parameters: dict):
    principal = int(parameters['principal'])
    payment = float(parameters['payment'])
    percent = (float(parameters['interest']) * 0.01) / (12 * 1)
    count_time = math.ceil(math.log(payment / (payment - percent * principal), 1 + percent))
    if count_time == 1:
        print(f"You need {count_time} month to repay this credit!")
        print(f"\nOverpayment = {math.ceil((count_time * payment) - principal)}")
    elif count_time < 12:
        print(f"You need {count_time} months to repay this credit!")
        print(f"\nOverpayment = {math.ceil((count_time * payment) - principal)}")
    elif count_time == 12:
        print(f"You need {count_time} year to repay this credit!")
        print(f"\nOverpayment = {math.ceil((count_time * payment) - principal)}")
    elif count_time > 12 and count_time % 12 != 0:
        print(f"You need {count_time // 12} years and {count_time % 12} months to repay this credit!")
        print(f"\nOverpayment = {math.ceil((count_time * payment) - principal)}")
    elif count_time > 12 and count_time % 12 == 0:
        print(f"You need {count_time // 12} years to repay this credit!")
        print(f"\nOverpayment = {math.ceil((count_time * payment) - principal)}")


def calc_annuity_payment(parameters: dict):
    principal = int(parameters['principal'])
    periods = int(parameters['periods'])
    percent = (float(parameters['interest']) * 0.01) / (12 * 1)
    annuity_pay = math.ceil(principal * ((percent * ((1 + percent) ** periods)) / (((1 + percent) ** periods) - 1)))
    print(f"Your annuity payment = {annuity_pay}!")
    print(f"\nOverpayment = {(annuity_pay * periods) - principal}")


def calc_principal(parameters: dict):
    payment = int(parameters['payment'])
    periods = int(parameters['periods'])
    percent = (float(parameters['interest']) * 0.01) / (12 * 1)
    principal = math.floor(payment / ((percent * ((1 + percent) ** periods)) / (((1 + percent) ** periods) - 1)))
    print(f"Your credit principal = {principal}!")
    print(f"\nOverpayment = {(payment * periods) - principal}")


def calc_diff_payment(parameters: dict):
    principal = int(parameters['principal'])
    periods = int(parameters['periods'])
    interest = (float(parameters['interest']) * 0.01) / (12 * 1)
    all_payments = []
    for month in range(1, periods + 1):
        #print(interest * (principal - ((principal * (month - 1)) / interest)))
        diff_payment = (principal / periods) + (interest * (principal - ((principal * (month - 1)) / periods)))
        all_payments.append(math.ceil(diff_payment))
        print(f"Month {month}: paid out {math.ceil(diff_payment)}")
    print(f"\nOverpayment = {sum(all_payments) - principal}")


start()