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

print(" ELECTRICITY BILL ESTIMATOR")
cents_per_hour = float(input(" Enter cents per Kilo watt hour: "))
daily_kwh_usage = float(input(" Enter the daily use of kilo watt hours your using: "))
billing_days = float(input(" Enter the number of Billing days: "))
bill_amount = (daily_kwh_usage*billing_days*cents_per_hour)/100


print("Total Bill estimate is ${}".format(bill_amount))