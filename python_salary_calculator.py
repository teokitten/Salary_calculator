gross = input("What's your gross salary?")
print "- Social Insurance: {}".format(gross * 0.065)
print "- Health Insurance: {}".format(gross * 0.045)
print "- Income Tax: {}".format(gross * 1.34 * 0.15)
print "+ Tax bonus from government: 2070"
print "Your Netto salary is: {}".format(gross - (gross * 0.065) - (gross * 0.045) - (gross * 1.34 * 0.15) + 2070)
