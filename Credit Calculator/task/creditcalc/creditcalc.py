import math

menu = input("""What do you want to calculate?
type 'n' - for count of months,
type 'a' - for annuity monthly payment,
type 'p' - for monthly payment:
""")

if menu == "n":

    credit_principal = int(input("Enter credit principal:\n"))
    monthly_payment = float(input("Enter monthly payment:\n"))
    credit_interest = float(input("Enter credit principal:\n"))

    interest = (1/12) * (credit_interest / 100)
    months_count = math.log(monthly_payment / (monthly_payment - interest * credit_principal), 1 + interest)
    years = round(months_count / 12)

    if round(months_count / 12) == 0:
        print("you need {} months to repay this credit!".format(str(round(months_count % 12))))
    elif math.ceil(months_count) % 12 == 0:
        print("You need {} years to repay this credit!".format(str(math.ceil(months_count/12))))
    elif round(months_count % 12) > 1:
        print("You need {} years and {} months to repay this credit!".
              format(str(math.floor(months_count/12)), str(math.ceil(months_count % 12))))

elif menu == "a":

    credit_principal = int(input("Enter credit principal:\n"))
    periods_count = float(input("Enter count of periods:\n"))
    credit_interest = float(input("Enter credit principal:\n"))

    interest = (1/12) * (credit_interest / 100)
    a = (interest * math.pow(1 + interest, periods_count))/(math.pow(1 + interest, periods_count) - 1)
    annuity = credit_principal * a

    print("Your annuity payment = " + str(math.ceil(annuity)))

elif menu == "p":

    monthly_payment = float(input("Enter monthly payment:\n"))
    periods_count = float(input("Enter count of periods:\n"))
    credit_interest = float(input("Enter credit principal:\n"))

    interest = (1/12) * (credit_interest / 100)
    a = (interest * math.pow(1 + interest, periods_count)) / (math.pow(1 + interest, periods_count) - 1)
    principal = monthly_payment / a

    print("Your credit principal = " + str(round(principal)))
