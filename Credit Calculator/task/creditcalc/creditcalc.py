import math

print("Enter the credit principal: ")
principal = int(input())

print("""What do you want to calculate?
type 'm' - for count of months,
type 'p' - for monthly payment:""")

months_or_payment = input()

if months_or_payment == "m":
    print("Enter monthly payment:")
    monthly_payment = int(input())

    number_of_months = principal / monthly_payment

    if math.ceil(number_of_months) == 1:
        print("It takes {} month to repay the credit".format(str(math.ceil(number_of_months))))
    else:
        print("It takes {} months to repay the credit".format(str(math.ceil(number_of_months))))

elif months_or_payment == "p":
    print("Enter count of months:")
    number_of_months = int(input())

    monthly_payment = principal / number_of_months
    rounded_figure = math.ceil(monthly_payment)

    if monthly_payment == rounded_figure:
        print("Your monthly payment = " + str(rounded_figure))
    else:
        last_payment = principal - (number_of_months - 1) * rounded_figure
        print("Your monthly payment = {} with last month payment = {}.".format(str(rounded_figure), str(last_payment)))
