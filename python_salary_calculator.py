gross_salary = input("What's your gross salary?")
print "- Social Insurance: {}".format(gross_salary * 0.065)
print "- Health Insurance: {}".format(gross_salary * 0.045)
print "- Income Tax: {}".format(gross_salary * 1.34 * 0.15)
print "+ Tax bonus from government: 2070"
print "Your Netto salary is: {}".format(gross_salary - (gross_salary * 0.065) - (gross_salary * 0.045) - (gross_salary * 1.34 * 0.15) + 2070)
