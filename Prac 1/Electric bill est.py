'''
cp1404 practical 1
electric bill estimator
Author Corey Burns
'''

print(" ELECTRICITY BILL ESTIMATOR")
cents_per_hour = float(input(" Enter cents per Kilo watt hour: "))
daily_kwh_usage = float(input(" Enter the daily use of kilo watt hours your using: "))
billing_days = float(input(" Enter the number of Billing days: "))
bill_amount = (daily_kwh_usage*billing_days*cents_per_hour)/100


print("Total Bill estimate is ${}".format(bill_amount))
print

print(" ELECTRICITY BILL ESTIMATOR")
MENU = """TARIFF_11 = 0.244618
TARIFF_31 = 0.136928"""
tariff_11 = 0.244618
tariff_31 = 0.136928
cents_per_hour = float(input(" Please Enter Tariff Number- 11 or 31 : "))
daily_kwh_usage = float(input(" Enter the daily use of kilo watt hours your using: "))
billing_days = float(input(" Enter the number of Billing days: "))
if cents_per_hour == 11:
    cents_per_hour = tariff_11
elif cents_per_hour == 31:
    cents_per_hour = tariff_31
else:
    print(" ***invalid entry ***")
    cents_per_hour = float(input(" Please Enter Tariff Number- 11 or 31 : "))

bill_amount = cents_per_hour * daily_kwh_usage * billing_days


print("Total Bill estimate is ${:.2f}".format(bill_amount))