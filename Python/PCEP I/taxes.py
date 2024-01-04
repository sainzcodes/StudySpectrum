income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

lowtaxland_tax = income * lowtaxland_rate
ripoffland_tax = income * ripoffland_rate
savings = ripoffland_tax - lowtaxland_tax

print('Your income is ' + str(income) + ' and you would pay ' + str(lowtaxland_tax) + ' income tax in Lowtaxland or ' + str(ripoffland_tax) + ' income tax in Ripoffland. \nYou would save ' + str(savings) + ' by paying taxes in Lowtaxland!')

